from django.db import models
from django_extensions.db.models import TimeStampedModel
from ml_api.constants import SentimentType

class Keyword(TimeStampedModel):
    """Represent for keyword model."""
    word = models.CharField(max_length=255, unique=True)
    type = models.CharField(
        max_length=255,
        choices=SentimentType.choices,
    )
    # Anything below a score of -0.05 we tag as negative and anything
    # above 0.05 we tag as positive. Anything in between inclusively,
    # we tag as neutral.
    score = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.word} - {self.score}"
