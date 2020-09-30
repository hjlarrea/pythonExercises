#Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: 
# http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
#
#The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can 
# read the full article without having to click any buttons.
#
#(Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through the solution of the 
# exercise posted here.)
#
#This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise we 
# will learn how to write this text to a .txt file.

def printArticle(uri):
    # Orchestrates getting the links for each page, the content for each page and returns the article
    pages = [uri] + findPages(uri,[])
    article = ''
    for i in range(0,len(pages)):
        article+=getPageContent(pages[i],i+1)
    return article

def findPages(uri,uris):
    # Finds recursively the lings to each page
    import requests
    from bs4 import BeautifulSoup
    link = BeautifulSoup(requests.get(uri).text,'html.parser').find('a',text='Next')
    if link != None:
        uris.append('https://www.washingtonpost.com'+link.get('href'))
        findPages('https://www.washingtonpost.com'+link.get('href'),uris)
        return uris
    else:
        return []

def getPageContent(uri,pageNumber):
    import requests
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(requests.get(uri).text,'html.parser')
    if pageNumber == 1:
        article = soup.title.text
        article += soup.p.text
    else:
        article = soup.p.text
    return article

if __name__ == "__main__":
    uri = 'https://www.washingtonpost.com/wp-dyn/articles/A2623-2005Mar26.html'
    print(printArticle(uri))