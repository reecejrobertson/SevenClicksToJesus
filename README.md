# Seven Clicks To Jesus Christ
When I was in middle school, I used to play a game with my friends. We would go to a random article on Wikipedia, and then attempt to get from there to the article for Jesus by clicking on hyperlinks embedded in the article. The legend was that one could get from any article to Jesus in seven clicks or less. This project was created to find out if this is true.

The first challenge was scraping Wikipedia for the relevant data. I opted to use the Simple Wikipedia as opposed to the standard English Wikipedia so that I could get a more accurate representation of the Wikipedia connections with fewer samples. I wrote code that responsibly scraped a random article for hyperlinks at a rate of one article per second. This code is saved in the “scraper.py” file.

The second challenge was cleaning the data, which turned out to be a simple task once I got my algorithms right. I created an algorithm to remove duplicate articles and another to remove isolated articles, that is, articles with no hyperlinks. Isolated articles only appear on Simple Wikipedia, all corresponding articles on the English Wikipedia had hyperlinks, therefore because I am trying to model the English Wikipedia, I felt justified in removing these articles from my data set. This code is found in the “cleanup.py” file.

After collecting approximately 50% of all Simple Wikipedia data, I created a directed graph which mapped the connections between articles. I began exploring the connections given by my data. I found that one can get from any article to Jesus in less than 7 clicks (given that a path exists between the two articles), with the average number of clicks being 3.4. There were, however, several articles in my data that had no direct path to Jesus. I believe that this is due to a lack of data rather than an inherent problem in the data (many articles I sampled had only one or two hyperlinks, and if the linked article was not also sampled then no path exists). 

After answering this question, I began to further explore my data. In the collection process I implemented a rough categorization routine that divided articles into the categories of person, place, wildlife, or miscellaneous. Investigating these categories I found that places tend to be more strongly connected to Jesus than people, and by that, I mean that a higher percentage of places had a path to Jesus than people. This indicates that a higher percentage of people fall into the “one or two hyperlinks” category mentioned above. I found that wildlife (plants, animals, and other living things) also tends to be more strongly connected to Jesus.

In addition, I tested other articles in an attempt to determine which article can be considered the best “center” of Wikipedia, that meaning the article with the smallest average number of clicks to be access from anywhere on Wikipedia. I found, for example, that the United States is a better center of Wikipedia than Jesus. I would have liked to have exhaustively checked every article in my graph, but that proved to be too computationally expensive to be feasible.

After completing this project, I have discovered more questions over which to ponder and investigate. I wonder which category of articles has a shorter average path to Jesus, and I wonder still which article is the best center of Wikipedia. I invite users to join me in this pondering and investigation. Consider which articles are well connected, these represent the items of knowledge that our culture considers important. Consider the connections between articles, these represent the neural connections of humanity’s mind. Consider how your mind agrees with this “brain of humanity,” and consider where you differ. Which connections would you add, and which would you change? On Wikipedia itself we find a fitting quote from Denis Diderot, one of the editors of the first encyclopedia. He stated, “What is this world? A complex whole, subject to endless revolutions” ([Diderot](https://en.wikiquote.org/wiki/Denis_Diderot)). My project has helped us glimpse this complex whole. My hope is that those who encounter it will be inspired to participate in the comprehending of this whole, and in its endless revolutions.

## Roadmap
I do not intend to make any changes to this project.

## Contributing
Pull requests are welcome. For any changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
