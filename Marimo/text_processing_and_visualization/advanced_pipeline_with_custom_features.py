import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # Advanced Pipeline with Custom Features
        ---
        **Textbook is available @ [https://www.github.com/a-mhamdi/nlp](https://www.github.com/a-mhamdi/nlp)**
        """
    )
    return


@app.cell
def _():
    import re
    from LOCAL.text_preprocessor import TextPreprocessor
    return TextPreprocessor, re


@app.cell
def _(TextPreprocessor, re):
    class AdvancedTextPreprocessor(TextPreprocessor):
        def __init__(self, language='english', custom_stopwords=None):
            super().__init__(language)

            # Add custom stopwords if provided
            if custom_stopwords:
                self.stop_words.update(custom_stopwords)

        def remove_short_words(self, tokens, min_length=3):
            """Remove words shorter than min_length"""
            return [token for token in tokens if len(token) >= min_length]

        def normalize_elongated_words(self, text):
            """Normalize elongated words (e.g., 'hellooo' -> 'hello')"""
            pattern = re.compile(r'(.)\1{2,}')
            return pattern.sub(r'\1\1', text)

        def process(self, text, use_stemming=False, min_word_length=3):
            # Normalize elongated words
            text = self.normalize_elongated_words(text)

            # Get tokens from parent class
            tokens = super().process(text, use_stemming)

            # Remove short words
            tokens = self.remove_short_words(tokens, min_word_length)

            return tokens
    return (AdvancedTextPreprocessor,)


@app.cell
def _(AdvancedTextPreprocessor):
    if __name__ == '__main__':
        preprocessor = AdvancedTextPreprocessor()
        text = "The cats are running quickly through the forest!"
        processed_tokens = preprocessor.process(text, use_stemming=True)
        print("Processed tokens:", processed_tokens)
    return preprocessor, processed_tokens, text


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
