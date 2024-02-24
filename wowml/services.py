import wowml_pb2, wowml_pb2_grpc


class WowMlService(wowml_pb2_grpc.WowControllerServicer):
    def setupMl(self, request, context):
        return "Message returned from setupMl"
