import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # Plot Word Frequency
        ---
        **Textbook is available @ [https://www.github.com/a-mhamdi/nlp](https://www.github.com/a-mhamdi/nlp)**
        """
    )
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    from collections import Counter
    import seaborn as sns
    return Counter, plt, sns


@app.cell
def _(Counter, plt):
    def plot_word_frequency(text, top_n=10):
        """
        Plot a bar chart of the top N most frequently occurring words in a given text.

        Parameters
        ----------
        text : str
            The text to be analyzed.
        top_n : int
            The number of top words to be included in the plot. Defaults to 10.

        Returns
        -------
        None
        """
        words = text.lower().split()
        word_freq = Counter(words)

        # Get top N words
        top_words = dict(word_freq.most_common(top_n))

        # Create bar plot
        plt.figure(figsize=(12, 6))
        plt.bar(top_words.keys(), top_words.values())
        plt.xticks(rotation=45, ha='right')
        plt.title('Top Word Frequencies')
        plt.xlabel('Words')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()
    return (plot_word_frequency,)


@app.cell
def _(plot_word_frequency):
    if __name__ == '__main__':
        dummy_text = "This is a test. This test is only a test. In the event of an actual emergency, this would be followed by instructions."
        plot_word_frequency(dummy_text, top_n=5)
    return (dummy_text,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
