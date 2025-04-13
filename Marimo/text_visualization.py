import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # Text Visualization
        ---
        **Textbook is available @ [https://www.github.com/a-mhamdi/nlp](https://www.github.com/a-mhamdi/nlp)**
        """
    )
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    from collections import Counter
    return Counter, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md("""## Word Frequency""")
    return


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
    dummy_text_1 = "This is a test. This test is only a test. In the event of an actual emergency, this would be followed by instructions."

    plot_word_frequency(dummy_text_1, top_n=5)
    return (dummy_text_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""## Visualization with Seaborn""")
    return


@app.cell
def _():
    import pandas as pd
    import seaborn as sns
    return pd, sns


@app.cell
def _(Counter, pd, plt, sns):
    def plot_word_distribution(text, top_n=10):
        # Create word frequency distribution
        words = text.lower().split()
        word_freq = Counter(words)

        # Convert to DataFrame for Seaborn
        df = pd.DataFrame(word_freq.most_common(top_n),
                          columns=['Word', 'Frequency'])

        # Create plot
        plt.figure(figsize=(12, 6))
        sns.barplot(data=df, x='Word', y='Frequency')
        plt.xticks(rotation=45, ha='right')
        plt.title('Word Frequency Distribution')
        plt.tight_layout()
        plt.show()
    return (plot_word_distribution,)


@app.cell
def _(plot_word_distribution):
    dummy_text_2 = """
    The quick brown fox jumps over the lazy dog. The fox was quick and brown, while the dog was lazy and sleepy. Every day the fox would jump and run, while the dog would sleep and rest. The forest animals watched the fox and the dog with great interest, wondering why the fox was always so quick and the dog was always so lazy.
    """

    plot_word_distribution(dummy_text_2, top_n=5)
    return (dummy_text_2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""## Generate WordCloud""")
    return


@app.cell
def _():
    from wordcloud import WordCloud
    return (WordCloud,)


@app.cell
def _(WordCloud, plt):
    def generate_wordcloud(text):
        wordcloud = WordCloud(
            width=800, height=400,
            background_color='white',
            max_words=100
        ).generate(text)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
    return (generate_wordcloud,)


@app.cell
def _(generate_wordcloud):
    dummy_text_3 = """
    Artificial intelligence is rapidly transforming our world. Machine learning algorithms power recommendation systems we use daily on streaming platforms and e-commerce sites. Deep learning has revolutionized computer vision and natural language processing, enabling advances in autonomous vehicles and voice assistants. 

    Data science combines statistics, programming, and domain expertise to extract insights from massive datasets. Python has become the dominant programming language for data analysis and machine learning projects. Libraries like TensorFlow, PyTorch, and scikit-learn make implementing complex algorithms accessible to more developers.

    Cloud computing provides the infrastructure needed for processing big data. Companies leverage cloud services to scale their machine learning operations without maintaining expensive hardware. The cloud has democratized access to computational resources, allowing startups to compete with established enterprises.

    Cybersecurity concerns grow as AI systems become more integrated into critical infrastructure. Privacy advocates warn about the data collection required for training sophisticated models. Ethical AI development focuses on fairness, transparency, and accountability.

    Natural language processing enables computers to understand and generate human language. Text analytics helps organizations derive value from unstructured data sources like social media, customer reviews, and support tickets. Sentiment analysis gauges public opinion about products, services, and current events.

    The future of work will be shaped by automation and augmentation technologies. Some jobs will be replaced, while others will evolve to incorporate AI tools. New roles will emerge requiring skills in data interpretation and algorithmic thinking.

    Machine learning models continue to grow in size and complexity. Transformer architectures have set new benchmarks in language understanding. Computer vision systems can now identify objects and patterns with superhuman accuracy.
    """

    generate_wordcloud(dummy_text_3)
    return (dummy_text_3,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
