# Ebooks @ Adelaide Scraper

Start with the root directory;

```
https://ebooks.adelaide.edu.au/meta/titles/A.html
```

Each page is referenced from A-Z, so we can assume that each directory is modified from the ".../A.html" located at the end of the the URL String, to scrape each page would mean to download each URL like so;

```
https://ebooks.adelaide.edu.au/meta/titles/A.html
https://ebooks.adelaide.edu.au/meta/titles/B.html
https://ebooks.adelaide.edu.au/meta/titles/C.html
```

Command Used for this was;

```bash
curl -O https://ebooks.adelaide.edu.au/meta/titles/[A-Z].html
```

From that, we are given a HTML structure that is assigned like so;

```html
<ul class="works">
    <li>
        <a href="/o/orwell/george/o79a/">
            ::before
            Animal Farm / George Orwell [1944]
        </a>
    </li>
```

This is a standard structure that follows for each page and gives us the individual links to each book. By stripping the HTML pages to only the "ul li" tags, and then filtering it down to the "a" tags "HREF" variable, we would gain a list from each page of every URL to every book on that page. If we were to do this on every page, we would gain a tree to which we could know every book in the collection, which we could save as some form of list, which could be interpreted by a secondary program for downloading.

//See Page 42-45 of PWK Training for a quick and dirty method

The next step is to download these ebooks from each individual page. We have a few options for downloading, so we should start with a page, in this case we will use this URL;

```
https://ebooks.adelaide.edu.au/o/orwell/george/o79a/
```

Inside this, we have a footer which has a few download options;

```html
<ul>
    <li>
        <a class="mdi mdi-information-outline" rel="author" title="About this book" href="/o/orwell/george/"> about</a>
    </li>
    <li>
        <a class="mdi mdi-book-open" title="read in browser" href="/o/orwell/george/o79a/"> read</a>
    </li>
    <li>
        <a class="mdi mdi-file" title="the complete book in a single page" href="/o/orwell/george/o79a/complete.html"> complete</a>
    </li>
    <li>
        <a class="mdi mdi-download" title="Download a zip archive" href="/cgi-bin/zip/o/orwell/george/o79a"> download</a>
    </li>
    <li>
        <a class="mdi mdi-cellphone-android" title="Download an ePub version" href="/o/orwell/george/o79a/o79a.epub"> ePub</a>
    </li>
    <li>
        <a class="mdi mdi-amazon" title="Download a Kindle version" href="/o/orwell/george/o79a/o79a.azw3"> Kindle</a>
    </li>
    ...
</ul>
```

By using the same filtering method as before, we can filter this to how we want to download this, either as a .epub or an .azw3. If we itterate through the list and filter it down just to download links, we can use a secondary program or wget them into a folder with there correct tags/names for post-processing. 