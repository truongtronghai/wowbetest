from django.contrib import admin
from django.urls import include, path

import wowml_pb2_grpc
from wowml.services import WowMlService

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("api.urls"), name="rest_api"),
    path("oauth/", include("oauth2_provider.urls", namespace="oauth2_provider")),
]


# gRPC endpoints
def grpc_handlers(server):
    wowml_pb2_grpc.add_WowControllerServicer_to_server(WowMlService, server)
