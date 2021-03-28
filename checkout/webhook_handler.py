from django.http import HttpResponse


class Stripe_Webhook_Handler:
    # Stripe Webhooks

    # '__init__' is a setup method called each time an instance of a class
    # is created. Used to a assign the request as an attribute of the class
    def __init__(self, request):
        self.request = request

    # Generic, unknown and unexpected wh
    def handle_event(self, event):

        # Takes the event stripe is sending us and returns an HTTP response
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    # Payment_intent.succeeded wh
    def handle_payment_intent_succeeded(self, event):

        # Print out 'PaymentIntent' from stripe
        intent = event.data.object
        print(intent)

        # Takes the event stripe is sending us and returns an HTTP response
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    # Payment_intent.payment_failed wh
    def handle_payment_intent_payment_failed(self, event):

        # Takes the event stripe is sending us and returns an HTTP response
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)