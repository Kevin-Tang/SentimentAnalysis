# Python2.7

import html2text
import urllib
from senticnet.senticnet import Senticnet
from nltk.sentiment.util import demo_liu_hu_lexicon
from nltk.sentiment.vader import SentimentIntensityAnalyzer

page = urllib.urlopen("example.html").read()
page = unicode(page, "utf-8")  # returns HTML file as Unicode

def preparePage(html):
    h = html2text.HTML2Text()
    h.ignore_links = True  # ignores links in the HTML
    h.ignore_images = True  # ignores images in the HTML
    h.body_width = 0  # no text-wrap
    h.hide_strikethough = True  # hides strike-through text
    sentence = h.handle(html)  # returns all text as 1 long string
    return sentence

def doVaderSentiment(sentence):
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(sentence)
    for sentiment in ss:
        print("The text has a " + sentiment + " of: " + str(ss[sentiment]))

    return True  # change to return ss

def doLiuHuLexicon(sentence):
    demo = demo_liu_hu_lexicon(sentence, plot=True)
    print(demo)

    return True


def doSenticNet(sentence):
    sn = Senticnet()
    words = sentence.split()
    pScores = {}
    averagePolarity = 0
    count = 0
    for word in words:
        try:
            conceptInfo = sn.concept(word)
            polarity = sn.polarity(word)
            pScores[word] = polarity
            averagePolarity += polarity
            count += 1
        except KeyError:
            pass
    print(pScores)
    print("Average polartiy of this sentence is " + str(averagePolarity / count) + ".")
    return True


def main(html):
    sentence = preparePage(html)
    # doVaderSentimenton(sentence)
    # doLiuHuLexicon(sentence)
    doSenticNet(sentence)

if __name__ == '__main__':
    main(page)