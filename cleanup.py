import time

def remove_duplicates(file):
    """Removes duplicate lines from a file.

    Parameters:
        file (string): The name of the file to clean up.
    """
    start_time = time.time()
    articles = set()                #Create a set object.
    lines_removed = 0
    with open(file, 'r') as fin:
        lines = fin.readlines()     #Read in the lines of the file.
    with open(file, 'w') as fout:
        for line in lines:
            n = len(articles)
            articles.add(line)      #Try to add each line to the set.
            if len(articles) != n:
                fout.write(line)    #If the line was added, write it to the file.
            else:
                lines_removed += 1  #Otherwise increment the count of lines removed.
    print(lines_removed, "duplicate lines removed in", time.time()-start_time, "seconds.")
    return lines_removed

def remove_isolated_articles(file):
    """Removes articles with no hyperlinks to other articles.

    Parameters:
        file (string): The name of the file to cleanup.
    """
    start_time = time.time()
    lines_removed = 0
    with open(file, 'r') as fin:
        lines = fin.readlines()     #Read in the line of each file.
    with open(file, 'w') as fout:
        for line in lines:
            if '/' in line:         #If the line has a '/' character that means it has a hyperlink, so keep it.
                fout.write(line)
            else:
                lines_removed += 1  #Otherwise, remove it.
    print(lines_removed, "isolated articles removed in", time.time()-start_time, "seconds.")
    return lines_removed

def clean_article_titles(file):
    """Replaces any '/' characters in article titles with a '|'.

    Parameters:
        file (string): The name of the file to cleanup.
    """
    start_time = time.time()
    lines_altered = 0
    with open(file, 'r') as fin:
        lines = fin.readlines()         #Read in the lines of each file.
    with open(file, 'w') as fout:
        for line in lines:
            data = line.split("/")      #Split the lines on the '/' character.
            new_line = ""
            if data[0][-6:] == "(None)" or data[0][-6:] == "(Misc)":
                new_line = line
            elif data[0][-7:] == "(Place)":
                new_line = line
            elif data[0][-8:] == "(Person)":
                new_line = line
            elif data[0][-10:] == "(Wildlife)":
                new_line = line         #If the title meets one of the above chriteria it is correct.
            else:                       #Otherwise is has a '/' in the title. Replace that with a '|'.
                data[0] = data[0] + "|" + data[1]
                lines_altered += 1
                new_line = data[0]
                for i in range(2,len(data)):#Reassemble the new title and the hyperlinks.
                    new_line = new_line + '/' + data[i]
            fout.write(new_line)        #Write the new line back to the file.
    print(lines_altered, "titles corrected in", time.time()-start_time, "seconds.")
    return lines_altered

def safe_cleanup(file):
    """A fixed point algorithm that removes duplicate articles, isolated articles,
    and corrects article titles. It will safely correct titles and remove isolated
    articles until no changes are made.

    Parameters:
        file (string): The name of the file to cleanup.
    """
    remove_duplicates(file)
    remove_isolated_articles(file)
    lines_altered = clean_article_titles(file)
    while lines_altered > 0:
        remove_isolated_articles(file)
        lines_altered = clean_article_titles(file)
    print("Fixed point reached.")
