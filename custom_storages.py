from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

#   New class, inheriting from S3Boto3Storage for storing static files
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


#   New class, inheriting from S3Boto3Storage for storing media files
class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION