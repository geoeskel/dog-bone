from django.db import models


#   Category model (inherit from models.Model)
class Breeds(models.Model):
    name = models.CharField(max_length=254)
    #   friendly name is optional (null and blank = True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    #   string name definition
    def __str__(self):
        return self.name

    #   returns friendly name if exists
    def get_friendly_name(self):
        return self.friendly_name
