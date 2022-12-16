from .base import *
from decouple import config

SECRET_KEY = config('PROD_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wishes_postgres_db',
        'USER': config('PROD_SECRET_KEY'),
        'PASSWORD': config('PROD_SECRET_KEY'),
        'HOST': config('PROD_SECRET_KEY'),
    }
}

# S3 BUCKETS
AWS_ACCESS_KEY_ID = config('PROD_SECRET_KEY')
AWS_SECRET_ACCESS_KEY = config('PROD_SECRET_KEY')
AWS_STORAGE_BUCKET_NAME = 'wishes-bucket'


AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_REGION_NAME = 'us-east-1'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'