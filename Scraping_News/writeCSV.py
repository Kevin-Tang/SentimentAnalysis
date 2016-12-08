import csv
import traceback
import newspaper
from newspaper import Article


def buildNewspaper(url):
    """
    Takes in a URL to build through the newspaper module
    :param url:
    :return: list containing article website, article title, and article text
    """
    writeOut = []
    s_count = 0
    f_count = 0
    paper = newspaper.build(url, memoize_articles=False)
    print("Newspaper size " + str(paper.size()))  # Number of Articles in the build
    for article in paper.articles:
        try:
            art = []
            ar = Article(article.url)
            ar.download()
            ar.parse()
            art.append(paper.brand)
            art.append(ar.title)
            art.append(ar.text)
            writeOut.append(art)
            s_count += 1
            print("Number of Articles succeeded: " + str(s_count))
        except Exception as e:
            print(e)
            traceback.print_exc()
            f_count += 1
            print("Number of Articles failed: " + str(f_count))  # ParseError (Article html is set up weird)
    return writeOut

def main():
    news = buildNewspaper('http://foxnews.com')  # CHANGE news website HERE

    resultFile = open("FOXNEWS.csv", 'w')  # CHANGE name of .csv file to match content
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerow(["News Site", "Article Title", "Article Text"])
    wr.writerows(news)

if __name__ == '__main__':
    main()