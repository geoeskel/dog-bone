from django.http import HttpResponse


class Stripe_Webhook:
    # Stripe Webhooks

    # '__init__' is a setup method called each time an instance of a class is createrd
    # Used here to a assign the request as an attribute of the class
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):

        # Webhook events

        # Takes the event stripe is sending us and returns an HTTP response
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)