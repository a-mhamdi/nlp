import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    from collections import Counter
    import pandas as pd
    import seaborn as sns
    from matplotlib import pyplot as plt
    return Counter, pd, plt, sns


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
    if __name__ == "__main__":
        dummy_text = """
        The quick brown fox jumps over the lazy dog. The fox was quick and brown, while the dog was lazy and sleepy. Every day the fox would jump and run, while the dog would sleep and rest. The forest animals watched the fox and the dog with great interest, wondering why the fox was always so quick and the dog was always so lazy.
        """
        plot_word_distribution(dummy_text, top_n=5)
    return (dummy_text,)


if __name__ == "__main__":
    app.run()
