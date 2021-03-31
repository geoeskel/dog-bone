/*  Getting 'public_key' and 'client_secret' from the template using jquery 
    We're slicing first and last character as they will be quotation marks
    JS from: https://stripe.com/docs/payments/accept-a-payment */
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
// CSS from : https://stripe.com/docs/stripe-js
var style = {
    base: {
        color: '#000',
        fontFamily: '"Blinker", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
//  Mounting the card to the 'card-element' in checkout.html
card.mount('#card-element');

/*  Listener on 'card-elements' for change event checking for errors
    and displaying them in 'errorDiv' */

    /* Stripe works payment intents.
1. 	User hits the checkout page
2. 	The checkout view will call out to stripe and create a payment intent
	for the current amount of the shopping basket
3. 	Stripe will create it and attach a secret key for identification
4. 	Secret key will be returned to us and we'll send it to the template
	as the 'client_secret' variable.
5. 	Using the 'client_secret' key we call the 'confirmCardPayment()'
    method from stripe JS to verify the card number */
    
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-user-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

/*  Handling the submit function (listener)
1.  Prevent default action (POST)
2.  Disable card update to prevent multiple submissions
3.  Create vars to capture form data
4.  Post the captured data to 'cache_checkout_data' view
5.  The view updates the 'PaymentIntent' and returns 200 respoonse 
6.  Execute the 'confirmCardPayment' method from Stripe
7.  Call the 'confirmCardPayment' method from Stripe
8.  Provide the card to Stripe
9.  Execute the 'function(result)'
10. If 'errorDiv', show it in card div and allow user to resubmit card
11. If status is success, submit the form 
12. If anything goes wrong posting the data to the view, reload the page
    and display the error without charging the user */

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    // Trigger the overlay, fade out the form when submit clicked
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                // Client's billing information. We take it from the form and trimm the whitespace
                billing_details: {
                        name: $.trim(form.full_name.value),
                        phone: $.trim(form.phone_number.value),
                        email: $.trim(form.email.value),
                        address:{
                            line1: $.trim(form.street_address1.value),
                            line2: $.trim(form.street_address2.value),
                            city: $.trim(form.town_or_city.value),
                            country: $.trim(form.country.value),
                            state: $.trim(form.county.value),
                        }
                }
            },
            // Client's shipping information. We take it from the form and trimm the whitespace 
            shipping: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        postal_code: $.trim(form.postcode.value),
                        state: $.trim(form.county.value),
                    }
                },
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-user-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                // Trigger the overlay, fade out the form when submit clicked 
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);            
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // Page reload
        location.reload();
    })
});