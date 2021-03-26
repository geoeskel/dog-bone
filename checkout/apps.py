from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    # Overrites the ready method and imports the signals module
    def ready(self):
        import checkout.signals
