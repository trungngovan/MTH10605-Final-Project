from .baseview import ReadOnlyViewSet
from ..models import Keyword
from ..serialzers import KeywordSerializer


class KeywordViewSet(ReadOnlyViewSet):
    """Keyword viewset."""

    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    search_fields = (
        "type",
        "word",
    )
    ordering_fields = (
        "score",
    )
