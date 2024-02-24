from django.contrib import admin
from django.urls import path

import wowml_pb2_grpc
from wowml.services import WowMlService

urlpatterns = [
    path("admin/", admin.site.urls),
]


# gRPC endpoints
def grpc_handlers(server):
    wowml_pb2_grpc.add_WowControllerServicer_to_server(WowMlService, server)
