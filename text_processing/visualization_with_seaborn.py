from collections import Counter
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


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


if __name__ == "__main__":
    dummy_text = """
    The quick brown fox jumps over the lazy dog. The fox was quick and brown, while the dog was lazy and sleepy. Every day the fox would jump and run, while the dog would sleep and rest. The forest animals watched the fox and the dog with great interest, wondering why the fox was always so quick and the dog was always so lazy.
    """
    plot_word_distribution(dummy_text, top_n=5)
