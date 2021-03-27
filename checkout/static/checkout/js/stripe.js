/*  Getting 'public_key' and 'client_secret' from the template using jquery 
    We're slicing first and last character as they will be quotation marks
    JS from: https://stripe.com/docs/payments/accept-a-payment */
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
/* CSS from : https://stripe.com/docs/stripe-js */
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
/* Mounting the card to the 'card-element' in checkout.html */
card.mount('#card-element');