import networkx as nx
from matplotlib import pyplot as plt
import numpy as np

# Problems 4-6
class WikiGraph:
    """Class for solving Clicks to Jesus problem for Wikipedia articles. The
    problem is akin to the Kevin Bacon problem. It asks, given any Wikipedia
    article, how many clicks does it take to get to the article for Jesus if
    only hyperlinks embedded in the article are used?"""

    # Problem 4
    def __init__(self, filename="simple_wiki_data.txt"):
        """Initialize a set for articles about people, places, and things; a set
        for all the articles; and a directed NetworkX Graph; and store them as attributes.
        Read the speficied file, adding each article to the set of all articles
        (and perhaps to one of the other sets), and creating a node for each article
        in the graph. The directed edges from article to article are added.

        Each line of the file represents one artlcle: the title is listed first,
        then the type, then all links from that article to other articles. For example:
        Article Name(type)/link1/link2/...

        Any '/' characters in article titles have been replaced with the
        vertical pipe character '|'.

        Parameters:
            filename (string): The name of the file to read data from.
        """
        self.people = set()             #A set of articles about people.
        self.places = set()             #A set of articles about places.
        self.wildlife = set()           #A set of articles about  plants and animals.
        self.articles = set()           #A set of all articles.
        self.graph = nx.DiGraph()       #A graph connecting one article to those it is linked to.
        with open(filename) as fin:     #Open data file:
            for line in fin:            #for each line,
                data = line.strip()
                data = data.split("/")  #seperate it by the / character,
                if data[0][-6:] == "(None)" or data[0][-6:] == "(Misc)":
                    data[0] = data[0][:-6]  #place it in the appropriate subset, if any,
                elif data[0][-7:] == "(Place)":
                    data[0] = data[0][:-7]
                    self.places.add(data[0])
                elif data[0][-8:] == "(Person)":
                    data[0] = data[0][:-8]
                    self.people.add(data[0])
                elif data[0][-10:] == "(Wildlife)":
                    data[0] = data[0][:-10]
                    self.wildlife.add(data[0])
                else:
                    raise ValueError("Invalid article title:", data[0], "on line", line)
                self.graph.add_node(data[0])#then add it to the graph as a new node,
                self.articles.add(data[0])
                for i in data[1:]:          #and add its edges to the other nodes.
                    self.graph.add_edge(data[0],i)

    # Problem 5
    def is_path(self, sourceSet, target):
        """Determines how many articles in the given set have a path to the target.

        Parameters:
            sourceSet (set): The set to search from (can be people, places, wildlife, and articles).
            target (string): The target to reach.

        Returns:
            The number of articles in the source set with no path to the target.
        """
        no_path = 0
        for i in sourceSet:                                    #For each article with no path to the target,
            if nx.has_path(self.graph, i, target) == False: #increment the number of articles with no path to the target.
                no_path += 1
        return no_path

    def path_to_target(self, source, target):
        """Compute the shortest path from source to target.

        Parameters:
            source (string): The article to search from.
            target (string): The target article.

        Returns:
            The path from the source to the target (or "no path" if necessary).
        """
        if nx.has_path(self.graph, source, target) == False:    #If there is no path return "No path".
            return "No path from", source, "to", target
        else:
            return nx.shortest_path(self.graph, source, target) #Otherwise return the path.

    def average_number(self, target="Jesus"):
        """Calculate the shortest path lenght from every article to the target.
        Print a histogram of the path length from each article to the target,
        and print the average path length in the title of the graph.

        Parameters:
            target (string): The target article. Defaults to "Jesus".
        """
        #Check that the target is in self.articles.
        if target not in self.articles:
            raise ValueError("Given article is not in the graph.")
        #Get the shortest path lengths between the target and all other articles.
        targetDict = nx.single_source_shortest_path_length(self.graph, target)
        targetNumber = []
        for i in targetDict.keys():
            targetNumber.append(targetDict[i] - 1) #Remove one from each distance because the starting article does not count as a click.
        #Plot results.
        plt.hist(targetNumber, bins=[i-.5 for i in range(8)], color="cadetblue")
        xlabel = "Distance to " + target
        plt.xlabel(xlabel)
        plt.ylabel("Number of Articles")
        average = str(round(sum(targetNumber) / len(targetNumber), 2))  #Give the average number of clicks in the title of the plot.
        title = average + " Average Clicks to " + target
        plt.title(title)
        plt.show()


    def best_center(self):
        """Calculate the best center of Wikipedia, i.e. the article that is most
        easily accessible from all other articles.

        Returns:
            The central article of Wikipedia.
        """
        center = "None"
        center_average = 10000
        target_average = 0
        for target in self.articles:                                                #For each target article in the set of articles:
            targetDict = nx.single_source_shortest_path_length(self.graph, target)  #get the shortest path lengths between the target and all other articles,
            targetNumber = []
            for i in targetDict.keys():
                targetNumber.append(targetDict[i] - 1)                              #remove one from each distance because the starting article does not count as a click.
            target_average = sum(targetNumber) / len(targetNumber)
            if target_average < center_average:                                     #If the target_average is less than the center average,
                center = target                                                     #replace the current center.
                center_average = target_average
        return center                                                               #Return the best center.
