import os
import re
import urllib
import shutil
import collections
from bs4 import BeautifulSoup
from string import ascii_uppercase
from urllib.request import urlopen

# Folder to Store A-Z
downloads_folder_name = "downloaded_books"
ext_dict = ["mobi", "azw3", "epub"]

downloaded_files = 0

# Check if Exists
if not os.path.exists(downloads_folder_name):
	os.makedirs(downloads_folder_name)

for c in ascii_uppercase:

	# Check if Exists
	if not os.path.exists(downloads_folder_name + os.sep + c):
		os.makedirs(downloads_folder_name + os.sep + c)

	try:
		books = BeautifulSoup(urlopen("https://ebooks.adelaide.edu.au/meta/titles/" + c + ".html"), "html.parser")
	except: 
		continue

	# Go through Each Works
	for works in books.select("ul.works > li > a"):
		title = works.get_text()
		url = works['href']

		title = re.sub(r"[^A-Za-z0-9 ]+", "", title) 

		title = title[:150]
		
		# If Empty, Ignore. 
		if title == "":
			continue
		
		# Make Works Folder
		if not os.path.exists(downloads_folder_name + os.sep + c + os.sep + title):
			os.makedirs(downloads_folder_name + os.sep + c + os.sep + title)

		# Download Content from Book Page
		try:
			bookurl = urlopen("https://ebooks.adelaide.edu.au" + url)
		except: 
			continue

		url_parts = ("https://ebooks.adelaide.edu.au" + url).split('/')		
		tmp = collections.deque(url_parts)
		tmp.rotate(2)
		url_parts_rotated = list(collections.deque(tmp))

		for ext in ext_dict:
			# Try downloading each extension
			try:
				download_url = "https://ebooks.adelaide.edu.au" + url + url_parts_rotated[0] + "." + ext
				file = downloads_folder_name + os.sep + c + os.sep + title + os.sep + url_parts_rotated[0] + "." + ext

				with urllib.request.urlopen(download_url) as response, open(file, 'wb') as out_file:
				    shutil.copyfileobj(response, out_file)
				
				downloaded_files = downloaded_files + 1
				print ("\rDownloaded " + str(downloaded_files) + "                          \r", end="")
			except:
				# File does not exist, skip extension.
				continue