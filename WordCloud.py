from os import path
import requests
from collections import Counter
import wordcloud
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from wordcloud import WordCloud

def wordCloud():
    tags = open("C:/Users/ebin1/Desktop/tagss.txt", "r").read().split("\n")
    dataset = pd.read_csv("C:/Users/ebin1/Desktop/Tags1.csv")
    print(pd.Series(np.concatenate([x.split() for x in dataset.Tag])).value_counts())

    tagFreq = Counter()
    for word in tags:
        tagFreq[word] += 1
    mask=np.array(Image.open(path.join("C:/Users/ebin1/Desktop/masks-wordclouds", "comment.png")))
   #mask = np.array(Image.open(requests.get('http://www.clker.com/cliparts/O/i/x/Y/q/P/yellow-house-hi.png', stream=True).raw))
    wordcloud = WordCloud(width=1000, height=900, background_color='white',relative_scaling=.8,mask=mask).generate_from_frequencies(tagFreq)
    wordcloud.to_file("skills-cloud.png")
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

wordCloud()