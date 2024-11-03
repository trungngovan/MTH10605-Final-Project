import nltk

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
from textblob import TextBlob
from ..constants import SentimentType, POSITIVE_THRESHOLD, NEGATIVE_THRESHOLD
from ..models import Keyword, Result


def perform_analyze(text):
    """Analyze the sentiment of a text."""
    blob = TextBlob(text)
    total_sentiment = round(blob.sentiment.polarity, 3)
    if total_sentiment == 0:
        return Result.objects.create(
            score=total_sentiment,
            type=SentimentType.NEUTRAL
        )
    keyword_ids = []
    for sentence in blob.sentences:
        for word in sentence.words:
            polarity_score = TextBlob(word).sentiment.polarity
            if polarity_score == 0:
                continue
            word_instance, created = Keyword.objects.update_or_create(
                word=word,
                defaults={
                    "score": round(polarity_score, 3),
                    "type": (
                        SentimentType.POSITIVE
                        if polarity_score >= POSITIVE_THRESHOLD else
                        SentimentType.NEGATIVE
                        if polarity_score <= NEGATIVE_THRESHOLD else
                        SentimentType.NEUTRAL
                    )
                }
            )
            keyword_ids.append(word_instance.id)
    result = Result.objects.create(
        score=total_sentiment,
        type=(
            SentimentType.POSITIVE if blob.sentiment.polarity > POSITIVE_THRESHOLD else
            SentimentType.NEGATIVE if blob.sentiment.polarity < NEGATIVE_THRESHOLD else
            SentimentType.NEUTRAL
        )
    )
    result.keywords.add(*keyword_ids)

    return result