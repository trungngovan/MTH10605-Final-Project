from django.db.models import TextChoices

class SentimentType(TextChoices):
    POSITIVE = ("positive", "Positive")
    NEGATIVE = ("negative", "Negative")
    NEUTRAL = ("neutral", "Neutral")


POSITIVE_THRESHOLD = 0.05
NEGATIVE_THRESHOLD = -0.05
