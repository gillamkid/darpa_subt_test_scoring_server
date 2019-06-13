from rest_framework import authentication
from django.db import models
from django.conf import settings

from . import models as dcm


class BearerAuthentication(authentication.TokenAuthentication):
    keyword = "Bearer"
    model=dcm.Token    
