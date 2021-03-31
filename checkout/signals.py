"""
Built-in django feature. Signals are sent by Django to the
application after model instance is saved and after it's deleted

"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Updates the grand total on 'lineitem' updated or created
    'sender' is 'OrderLineItem', 'instance' is the actual model
     instance that sent it, 'created' is a boolean checking
     if it is a new instance or updated one,
    '*kwargs' are the keyword arguments
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Updates the grand total on 'lineitem' deleted
    'sender' is 'OrderLineItem', 'instance' is the actual model instance
    that sent it, 'created' is a boolean checking if it is
    a new instance or updated one, '*kwargs' are the keyword arguments
    """
    instance.order.update_total()
