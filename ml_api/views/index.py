from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class IndexView(APIView):
    def get(self, request):
        return Response(
            data={
                "message": "Welcome to the Machine Learning API",
                "status": "Running",
                "endpoints": {
                    "Predict": "/api/v1/predict/",
                    "OpenAPI (Swagger)": "/api/v1/open-api/ui/",
                }
            },
            status=status.HTTP_200_OK
        )
