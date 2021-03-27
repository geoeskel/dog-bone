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
	for the current amount of the shopping bag
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
                <i class="fas fa-times"></i>
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
3.  Execute the 'confirmCardPayment' method
4.  Call the 'confirmCardPayment' method
5.  Provide the card to Stripe
6.  Execute the 'function(result)'
7.  If 'errorDiv', show it in card div and allow user to resubmit card
8.  If status is success, submit the form */
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    /* Trigger the overlay, fade out the form when submit clicked */
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            /* Trigger the overlay, fade out the form when submit clicked */
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
});