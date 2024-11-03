from rest_framework import serializers
from ..models import Result
from ..services import perform_analyze, clean_text
from .keywords import KeywordSerializer

class ResultSerializer(serializers.ModelSerializer):
    """Result serializer."""

    input_text = serializers.CharField(
        write_only=True,
    )
    type = serializers.CharField(
        read_only=True,
    )
    score = serializers.FloatField(
        read_only=True,
    )
    keywords = KeywordSerializer(
        many=True,
        read_only=True,
    )
    class Meta:
        model = Result
        fields = (
            "input_text",
            "type",
            "score",
            "keywords",
        )

    def save(self, **kwargs):
        """Perform prediction on the input text."""
        input_text = self.validated_data.get("input_text")
        text = clean_text(input_text)
        self.instance = perform_analyze(text)
        serializer = ResultSerializer(self.instance)
        return serializer.data
