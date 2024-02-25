from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class TestOauth(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {
                "message": "You see this message from api TestOAuth. That mean you had Access Token."
            },
            status=status.HTTP_200_OK,
        )
