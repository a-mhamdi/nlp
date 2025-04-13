import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # Text Processing
        ---
        **Textbook is available @ [https://www.github.com/a-mhamdi/nlp](https://www.github.com/a-mhamdi/nlp)**
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""## Create BoW""")
    return


@app.cell
def _():
    from sklearn.feature_extraction.text import CountVectorizer
    return (CountVectorizer,)


@app.cell
def _(CountVectorizer):
    def create_bow(documents):
        # Initialize vectorizer
        vectorizer = CountVectorizer()
        # Create BOW representation
        X = vectorizer.fit_transform(documents)
        # Get feature names (vocabulary)
        feature_names = vectorizer.get_feature_names_out()
        # Convert to array
        bow_array = X.toarray()

        return bow_array, feature_names, vectorizer
    return (create_bow,)


@app.cell
def _(create_bow):
    def test_bow():
        documents = [
            "The cat sat on the mat",
            "The dog ran in the park",
            "The cat and dog played"
        ]

        bow_array, features, vectorizer = create_bow(documents)
        print("Features:", features)
        print("BOW Matrix:\n", bow_array)

    test_bow()
    return (test_bow,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""## Create TF-IDF""")
    return


@app.cell
def _():
    from sklearn.feature_extraction.text import TfidfVectorizer
    return (TfidfVectorizer,)


@app.cell
def _(TfidfVectorizer):
    def create_tfidf(documents):
        # Initialize TF-IDF vectorizer
        tfidf = TfidfVectorizer()
        # Create TF-IDF matrix
        X = tfidf.fit_transform(documents)
        # Get feature names
        feature_names = tfidf.get_feature_names_out()

        return tfidf, feature_names, X.toarray()
    return (create_tfidf,)


@app.cell
def _(create_tfidf):
    # Example usage
    def test_tfidf():
        documents = [
            "The cat sat on the mat",
            "The dog ran in the park",
            "The cat and dog played"
        ]

        _, features, X = create_tfidf(documents)
        print("Features:", features)
        print("TF-IDF Matrix:\n", X)

    test_tfidf()
    return (test_tfidf,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""## Preprocess Text""")
    return


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
def _(nltk):
    # Download required NLTK data
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    return


@app.cell
def _(PorterStemmer, WordNetLemmatizer, re, stopwords, word_tokenize):
    class TextPreprocessor:
        def __init__(self, language='english'):
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
def _(TextPreprocessor, create_bow):
    def pipeline():
        preprocessor = TextPreprocessor()
        text = """
        Natural language processing (NLP) is a subfield of linguistics, computer science, 
        and artificial intelligence concerned with the interactions between computers and 
        human language, in particular how to program computers to process and analyze large 
        amounts of natural language data.
        """
        processed_tokens = preprocessor.process(text, use_stemming=True)

        # Create BOW representation
        bow_array, features, _ = create_bow([' '.join(processed_tokens)])

        print("Processed tokens:", processed_tokens)
        print("\nBag of Words representation:")
        print("Features:", features)
        print("BOW array:", bow_array)

    pipeline()
    return (pipeline,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
