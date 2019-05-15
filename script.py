#!/usr/bin/env python3

#
# This program was written back in 2017-2018 to try and download the collection of files from
# the e-book archive of the University of Adelaide. The collection was uploaded on some jank  
# brewed system, so I had to get creative. My hastly written notes are located in notes.md
# and have barely been changed since I originally wrote them (only some syntax changes).
# Yes I know that I could make this better, but this was uploaded so people could see how I 
# tackled this challenge, and if somebody wants to write a hyperthreaded and faster version
# of it, do it then. 
#

import collections
import os
import re
import shutil
import urllib
from string import ascii_uppercase
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Variables
downloadFolder = "downloaded_books"
fileExtensions = ["mobi", "azw3", "epub"]


# Check if the download folder does not exist, and create it if it does not.
if not os.path.exists(downloadFolder):
	os.makedirs(downloadFolder)
# Exception: The folder already exists
else:
	pass


# Main Loop; Itterate through the alphabet
for currentLetter in ascii_uppercase:

	# Check if the current letter folder does not exists, and create it if it does not.
	if not os.path.exists(downloadFolder + os.sep + currentLetter):
		os.makedirs(downloadFolder + os.sep + currentLetter)
	# Exception: The folder already exists
	else: 
  		pass


	# Assign the books variable as the current 
	try:
		books = BeautifulSoup(urlopen("https://ebooks.adelaide.edu.au/meta/titles/" + currentLetter + ".html"), "html.parser")
	# Exception: URL Does not exist or does not resolve
	except: 
		pass


	# Nested Loop; Each book located in the directory
	for book in books.select("ul.works > li > a"):

		# Set the bookTitle for the book, this includes filtering for symbols and reduces it to 150 chars
		bookTitle = book.get_text()
		bookTitle = re.sub(r"[^A-Za-z0-9 ]+", "", bookTitle)
		bookTitle = bookTitle[:150]

		# Get the directory for the book
		url = book["href"]


		# Check if the current book folder does not exist. and create it if it does not.
		if not os.path.exists(downloadFolder + os.sep + currentLetter + os.sep + bookTitle):
			os.makedirs(downloadFolder + os.sep + currentLetter + os.sep + bookTitle)
		# Exception: The directory already exists
		else:
			pass


		# If a book titles name is empty, skip it
		if bookTitle == "":
			continue
		else:
			pass


		# This is jank code and I wish I wrote it better, but it works.
		url_parts = ("https://ebooks.adelaide.edu.au" + url).split("/")		
		tmp = collections.deque(url_parts)
		tmp.rotate(2)
		url_parts_rotated = list(collections.deque(tmp))

		# Nested Loop; Try downloading each book extension
		for ext in fileExtensions:

			# Try to download the current book with its extension
			try:
				downloadURL = ("https://ebooks.adelaide.edu.au" + url + url_parts_rotated[0] + "." + ext)
				file = (downloadFolder + os.sep + currentLetter + os.sep + bookTitle + os.sep + url_parts_rotated[0] + "." + ext)

				with urllib.request.urlopen(downloadURL) as response, open(file, "wb") as out_file:
				    shutil.copyfileobj(response, out_file)
				print ("\rDownloaded " + str(downloadURL))

			# Exception: File does not exist, skip extension.
			except:
				pass