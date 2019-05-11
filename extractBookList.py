import os
import urllib
import collections
from bs4 import BeautifulSoup
from string import ascii_uppercase
from urllib.request import urlopen

# Folder to Store A-Z
downloads_folder_name = "downloaded_books"
ext_dict = ["mobi", "awz3", "epub"]

# Check if Exists
if not os.path.exists(downloads_folder_name):
    os.makedirs(downloads_folder_name)

for c in ascii_uppercase:

    # Check if Exists
    if not os.path.exists(downloads_folder_name + os.sep + c):
        os.makedirs(downloads_folder_name + os.sep + c)
    
    books = BeautifulSoup(urlopen("https://ebooks.adelaide.edu.au/meta/titles/A.html"), "html.parser")

    # Go through Each Works
    for works in books.select("ul.works > li > a"):
        title = works.get_text()
        url = works['href']

        # If Empty, Ignore. 
        if title == "":
            continue
        
        # Make Works Folder
        if not os.path.exists(downloads_folder_name + os.sep + c + os.sep + title):
            os.makedirs(downloads_folder_name + os.sep + c + os.sep + title)


        # Download Content from Book Page
        bookurl = urlopen("https://ebooks.adelaide.edu.au" + url)

        for ext in ext_dict :
            # Try downloading each extension
            url_parts = ("https://ebooks.adelaide.edu.au" + url).split('/')            

            try:
                tmp = collections.deque(url_parts)
                tmp.rotate(2)
                url_parts_rotated = list(collections.deque(tmp))

                print (bookurl + url_parts_rotated[0] + "." + ext + "\n")

                #download = urllib.URLopener()
                #download.retrieve(bookurl + url_parts[0] + ext, downloads_folder_name + os.sep + c + os.sep + title + os.sep)
            except:
                # File does not exist, skip extension. 
                continue
            