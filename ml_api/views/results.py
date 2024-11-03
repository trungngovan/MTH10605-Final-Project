from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from .baseview import ReadOnlyViewSet
from ..models import Result
from ..serialzers import ResultSerializer


class ResultViewSet(ReadOnlyViewSet):
    """Sentence viewset."""

    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    search_fields = (
        "type",
    )
    ordering_fields = (
        "score",
    )

class PredictAPIView(CreateAPIView):
    """Predict view."""

    serializer_class = ResultSerializer

    def create(self, request, *args, **kwargs):
        """Predict the type of a sentence."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        return Response(result, status=status.HTTP_200_OK)