from django.urls import path
from api.views import TestOauth


urlpatterns = [
    path("", TestOauth.as_view(), name="get_message"),
]
