from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


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

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)