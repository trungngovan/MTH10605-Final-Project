from rest_framework import serializers
from ..models import Keyword

class KeywordSerializer(serializers.ModelSerializer):
    """Keyword serializer."""
    class Meta:
        model = Keyword
        fields = (
            "word",
            "type",
            "score",
        )
