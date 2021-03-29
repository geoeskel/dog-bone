from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

def profile(request):
    #   User profile
    profile = get_object_or_404(UserProfile, user=request.user)
    # If the request method is 'POST', create a new instance of
    # the user profile form using the post data.
    # The instance we're updating is the profile we've just retrieved
    # If the form is valid, save it and add a success message
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your profile!')
        else:
            messages.error(request, 'Failed to update your profile. Invalid form details?')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'Confirmation for order number {order_number}. '
        'We will send you a confirmation email on the past order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        # Check in the template if the user got there
        # via the order history view
        'from_profile': True,
    }

    return render(request, template, context)
