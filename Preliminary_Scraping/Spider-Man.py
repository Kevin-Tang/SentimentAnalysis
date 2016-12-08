import urllib
import requests
from AI_Team import doVaderSentimentonHTMLRequests
from lxml import html



def main():
	while True:
	    response = raw_input("\nPlease enter one of the following or 'end' to quit: \nYahoo! News, Google News, HuffintonPost, \nCNN, New York Times, Fox News, \nNBC News, Mail Online, Washington Post, \nThe Guardian, WSJ, ABCNews, \nBBC News, USA Today, LA Times\n")

	    if response.lower() == "yahoo! news":
	    	page = requests.get("https://www.yahoo.com/news/clinton-camp-trumps-jail-debate-quip-sounded-like-banana-republic-dictator-045453273.html")
	    	tree = html.fromstring(page.content)
	    	bodyParagraph = tree.xpath('//p@[@class="canvas-text Mb(1.0em) Mb(0)--sm Mt(0.8em)--sm canvas-atom"]/text()')
	    	return doVaderSentimentonHTMLRequests(bodyParagraph)
	    elif response.lower() == "google news":
	    	page = requests.get("http://www.cnn.com/2016/10/06/politics/obama-approval-rating-new-high/index.html")
	    	tree = html.fromstring(page.content)
	    	bodyParagraph = tree.xpath('//div[@class="zn-body__paragraph"]/text()')
	    elif response.lower() == "huffintonpost":
	    	page = requests.get("http://www.cnn.com/2016/10/06/politics/obama-approval-rating-new-high/index.html")
	    	tree = html.fromstring(page.content)
	    	bodyParagraph = tree.xpath('//div[@class="zn-body__paragraph"]/text()')
	    elif response.lower() == "cnn":
	    	page = requests.get("http://www.cnn.com/2016/10/06/politics/obama-approval-rating-new-high/index.html")
	    	tree = html.fromstring(page.content)
	    	bodyParagraph = tree.xpath('//div[@class="zn-body__paragraph"]/text()')
	    	return doVaderSentimentonHTMLRequests(bodyParagraph)
	    elif response.lower() == "new york times":
	    	page = requests.get("http://www.cnn.com/2016/10/06/politics/obama-approval-rating-new-high/index.html")
	    	tree = html.fromstring(page.content)
	    	bodyParagraph = tree.xpath('//div[@class="zn-body__paragraph"]/text()')
	    elif response.lower() == "fox news":
	    	page = requests.get("http://www.cnn.com/2016/10/06/politics/obama-approval-rating-new-high/index.html")
	    	tree = html.fromstring(page.content)
	    	bodyParagraph = tree.xpath('//div[@class="zn-body__paragraph"]/text()')
	    elif response.lower() == "nbc news":
	    	page = requests.get("http://www.cnn.com/2016/10/06/politics/obama-approval-rating-new-high/index.html")
	    	tree = html.fromstring(page.content)
	    	bodyParagraph = tree.xpath('//div[@class="zn-body__paragraph"]/text()')
	    elif response.lower() == "mail online":
	    	page = requests.get("http://www.cnn.com/2016/10/06/politics/obama-approval-rating-new-high/index.html")
	    	tree = html.fromstring(page.content)
	    	bodyParagraph = tree.xpath('//div[@class="zn-body__paragraph"]/text()')
	    elif response.lower() == "washington post":
	    	page = requests.get("http://www.cnn.com/2016/10/06/politics/obama-approval-rating-new-high/index.html")
	    	tree = html.fromstring(page.content)
	    	bodyParagraph = tree.xpath('//div[@class="zn-body__paragraph"]/text()')
	    elif response.lower() == "the guardian":
	    	page = requests.get("http://www.cnn.com/2016/10/06/politics/obama-approval-rating-new-high/index.html")
	    	tree = html.fromstring(page.content)
	    	bodyParagraph = tree.xpath('//div[@class="zn-body__paragraph"]/text()')
	    elif  response.lower() == "wsj":
	    	page = requests.get("http://www.cnn.com/2016/10/06/politics/obama-approval-rating-new-high/index.html")
	    	tree = html.fromstring(page.content)
	    	bodyParagraph = tree.xpath('//div[@class="zn-body__paragraph"]/text()')
	    elif response.lower() == "abcnews":
	    	page = requests.get("http://www.cnn.com/2016/10/06/politics/obama-approval-rating-new-high/index.html")
	    	tree = html.fromstring(page.content)
	    	bodyParagraph = tree.xpath('//div[@class="zn-body__paragraph"]/text()')
	    elif response.lower() == "bbc news":
	    	page = requests.get("http://www.cnn.com/2016/10/06/politics/obama-approval-rating-new-high/index.html")
	    	tree = html.fromstring(page.content)
	    	bodyParagraph = tree.xpath('//div[@class="zn-body__paragraph"]/text()')
	    elif response.lower() == "usa today":
	    	page = requests.get("http://www.cnn.com/2016/10/06/politics/obama-approval-rating-new-high/index.html")
	    	tree = html.fromstring(page.content)
	    	bodyParagraph = tree.xpath('//div[@class="zn-body__paragraph"]/text()')
	    elif response.lower() == "la times":
	    	page = requests.get("http://www.cnn.com/2016/10/06/politics/obama-approval-rating-new-high/index.html")
	    	tree = html.fromstring(page.content)
	    	bodyParagraph = tree.xpath('//div[@class="zn-body__paragraph"]/text()')
	    elif response.lower() == "end":
	    	return True
	    else:
	    	print "Invalid Input\nType 'end' to end program\n"

if __name__ == "__main__":
    main()
			