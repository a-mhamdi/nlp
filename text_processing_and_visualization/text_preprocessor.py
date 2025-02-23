import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import re
    import nltk
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
    from nltk.stem.porter import PorterStemmer
    return PorterStemmer, WordNetLemmatizer, nltk, re, stopwords, word_tokenize


@app.cell
def _(PorterStemmer, WordNetLemmatizer, nltk, re, stopwords, word_tokenize):
    class TextPreprocessor:
        def __init__(self, language='english'):
            # Download required NLTK data
            nltk.download('punkt')
            nltk.download('stopwords')
            nltk.download('wordnet')

            self.language = language
            self.stop_words = set(stopwords.words(language))
            self.lemmatizer = WordNetLemmatizer()
            self.stemmer = PorterStemmer()

        def clean_text(self, text):
            """Basic text cleaning"""
            # Convert to lowercase
            text = text.lower()

            # Remove special characters and digits
            text = re.sub(r'[^a-zA-Z\s]', '', text)

            # Remove extra whitespace
            text = re.sub(r'\s+', ' ', text).strip()

            return text

        def tokenize(self, text):
            """Tokenize text"""
            return word_tokenize(text)

        def remove_stopwords(self, tokens):
            """Remove stop words"""
            return [token for token in tokens if token not in self.stop_words]

        def lemmatize(self, tokens):
            """Lemmatize tokens"""
            return [self.lemmatizer.lemmatize(token) for token in tokens]

        def stem(self, tokens):
            """Stem tokens"""
            return [self.stemmer.stem(token) for token in tokens]

        def process(self, text, use_stemming=False):
            """Complete preprocessing pipeline"""
            # Clean text
            cleaned_text = self.clean_text(text)

            # Tokenize
            tokens = self.tokenize(cleaned_text)

            # Remove stopwords
            tokens = self.remove_stopwords(tokens)

            # Lemmatize or stem
            if use_stemming:
                tokens = self.stem(tokens)
            else:
                tokens = self.lemmatize(tokens)

            return tokens
    return (TextPreprocessor,)


@app.cell
def _(TextPreprocessor):
    if __name__ == "__main__":
        preprocessor = TextPreprocessor()
        text = "The cats are running quickly through the forest!"
        processed_tokens = preprocessor.process(text, use_stemming=True)
        print("Processed tokens:", processed_tokens)
    return preprocessor, processed_tokens, text


if __name__ == "__main__":
    app.run()
