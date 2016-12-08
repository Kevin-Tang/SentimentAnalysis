import html2text
import urllib
import nltk.sentiment.util
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import movie_reviews
from nltk.util import ngrams


def doVaderSentimentonLocalHTML(html):
	"""
	This function uses a local HTML file as its input. 
	Since html2text parses HTML text all into a giant string, 
	it's tough to do sentiment analysis on large body of sentences.
	This function will instead parse a whole page overall's sentiment.
	"""

	h = html2text.HTML2Text()
	h.ignore_links = True #ignores links in the HTML
	h.ignore_images = True #ignores images in the HTML
	h.body_width = 0 #no text-wrap
	h.hide_strikethough = True #hides strike-through text

	sentence = h.handle(html) #returns all text as 1 long string
	print(sentence)

	sid = SentimentIntensityAnalyzer()
	ss = sid.polarity_scores(sentence)

	for sentiment in ss:
		print ("The text has a " + sentiment + " of: " + str(ss[sentiment]))

	return True #change to return ss

def doVaderSentimentonHTMLRequests(html):
	"""
	This function uses an HTML input gathered from using the Requests library.
	It'll print a sentiment analysis for each sentence from the web page.
	"""

	sid = SentimentIntensityAnalyzer()

	for sentence in html:
		print sentence #1sentence in html
		print "1st: Compound, 2nd: Negative, 3rd: Neutral, 4th: Positive"
		ss = sid.polarity_scores(sentence)
		#print type(ss)
		for k in sorted(ss):
			print str(ss[k])
		print "\n"

	return True #change to return ss

def doNgrams(html):
	"""
	This function takes in a Local html file and runs NGrams analysis
	"""
	h = html2text.HTML2Text()
	h.ignore_links = True #ignores links in the HTML
	h.ignore_images = True #ignores images in the HTML
	h.body_width = 0 #no text-wrap
	h.hide_strikethough = True #hides strike-through text

	sentence = h.handle(html) #returns all text as 1 long string

	n = 2
	nGrams = ngrams(sentence.split(), n)
	#for grams in nGrams:
	#	print grams

	print nGrams
	return True


#doVaderSentiment(bodyParagraph)

#This is for doVaderSentiment()

#anyPage = requests.get("http://www.cnn.com/2016/10/06/politics/obama-approval-rating-new-high/index.html")
#pageTree = html.fromstring(anyPage.content)

#bodyParagraph = pageTree.xpath('//div[@class="zn-body__paragraph"]/text()') #CNN tags their body text with 'zn-body__paragraph'. Different websites use different tagging systmes.
#bodyParagraph = pageTree.xpath('//p/text()') #Wikipedia has all their body text in 'p'

page = urllib.urlopen("Mac.html").read()
page = unicode(page, "utf-8") #returns HTML file as Unicode

doVaderSentimentonLocalHTML(page)
