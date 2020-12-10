import requests
from bs4 import BeautifulSoup
import re
import time

def scrape_article(article="https://en.wikipedia.org/wiki/Special:Random", file="wiki_data.txt"):
    """Scrape a single Wikipedia article for hyperlinks in to other Wikipedia articles. Outputs the
    scraped data to a file, one line per article. The format of a single line is:
    Article Name(type)/link1/link2/...
    Note: There are 4 possible types: Person, Place, Wildlife, and Misc.

    Parameters:
        article (string): The url of the article to scrape.
        file (string): The name of the file to write the scraped data to.
    """
    #Open the article and create a BeautifulSoup object.
    response = requests.get(url=article)
    soup = BeautifulSoup(response.content, 'html.parser')

    #Get the article title.
    title_tag = soup.find(id="firstHeading")
    title = title_tag.string

    #End the function if getting the title failed.
    if title is not None:
        #Get the article type by parsing the infobox class if it exists.
        type_tag = soup.find('table', {"class": re.compile(r"^infobox")})
        type = "Error0"
        try:
            type = type_tag.get("class")
            if "biography" in type:
                type = "Person"
            elif "geography" in type:
                type = "Place"
            elif "biota" in type:
                type = "Wildlife"
            else:
                type = "Misc"
        except AttributeError:
            type = "None"
        except:
            type = "Error"

        # Get all the links in the article.
        wikiLinks = soup.find(id="bodyContent").find_all('a', {"href": re.compile(r"^/wiki/(?!Category:|Help:|Portal:|Template:|Wikipedia:|File:|Special:|Book:|Template_talk:|Talk:)"), "class": False})

        #Write the scraped data to the file.
        with open(file, 'a') as fout:
            header = title + "(" + type + ")"
            fout.write(header)
            for link in wikiLinks:
                fout.write("/")
                fout.write(link.get("title"))
            fout.write("\n")

def crawl_simple_wikipedia(n=200000):
    """Crawl Simple Wikipedia and scrape n random articles. There is a one second delay between scrape requests.

    Parameters:
        n (int): Number of articles to scrape.
    """
    start_time = time.time()
    for i in range(n):
        scrape_article(article="https://simple.wikipedia.org/wiki/Special:Random", file="simple_wiki_data.txt")
        time.sleep(1)
    print(time.time() - start_time)
