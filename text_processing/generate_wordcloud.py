from wordcloud import WordCloud
from matplotlib import pyplot as plt


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


if __name__ == '__main__':
    pass
