import re
import nltk
import contractions
from nltk.corpus import stopwords
from spellchecker import SpellChecker
import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Configure NLTK resources
nltk.data.path.append("ml_api/nltk_data")
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

stop_words = set(stopwords.words("english"))
lemmatizer = nltk.WordNetLemmatizer()
spell = SpellChecker()


def preprocess_text(sentence):
    """Preprocess the text data for sentiment analysis."""
    # Convert to lowercase and expand contractions
    sentence = contractions.fix(sentence.lower())

    # Remove digits
    sentence = re.sub(r"\d+", "", sentence)

    # Remove special characters except for apostrophes
    sentence = re.sub(r"[^\w\s'`’]", "", sentence)

    # Remove excess whitespace
    sentence = " ".join(sentence.split())
    return sentence


def perform_lemmatization(tokens):
    """Perform lemmatization on the tokens."""
    return [lemmatizer.lemmatize(token) for token in tokens]


def spell_check(tokens):
    """Perform spell checking on the tokens."""
    corrected_tokens = []
    for token in tokens:
        if len(token) > 2 and token not in spell and token not in stop_words:
            corrected_tokens.append(spell.correction(token))
        else:
            corrected_tokens.append(token)
    return corrected_tokens


def remove_names(text):
    """Remove names from the text using Named Entity Recognition (NER)."""
    doc = nlp(text)
    tokens_without_names = [
        token.text for token in doc if token.ent_type_ != "PERSON"
    ]
    return " ".join(tokens_without_names)


def clean_text(text):
    """Clean the text data."""
    text = remove_names(text)
    sentences = nltk.sent_tokenize(text)
    cleaned_sentences = []

    for sentence in sentences:
        sentence = preprocess_text(sentence)
        tokens = nltk.word_tokenize(sentence, preserve_line=True)
        tokens = spell_check(tokens)
        tokens = [token for token in tokens if token not in stop_words]
        lemmatized_tokens = perform_lemmatization(tokens)

        cleaned_sentences.append(" ".join(lemmatized_tokens))

    return ". ".join(cleaned_sentences)