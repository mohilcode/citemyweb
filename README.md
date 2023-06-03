# CiteMyWeb

CiteMyWeb is a handy web app that simplifies the citation process for research articles. It's designed to save researchers time by extracting the appropriate Digital Object Identifier (DOI) directly from the article URL, rather than requiring manual input of the DOI or article name. CiteMyWeb is an open-source project, developed using Flask, and is hosted on Railway.

This tool currently supports more than 40 research article websites and provides a range of citation styles to choose from. Users can easily copy the generated citation and paste it into their research paper, thesis, or any other document. 

In the future, I aim to extend CiteMyWeb to accommodate all types of articles, web pages, and books, broadening its usability beyond the academic community. This will include even deriving citations from Amazon URLs for books without the need for an International Standard Serial Number (ISSN) or other information.

The project is always looking for improvement, both in terms of additional features and the user interface/user experience (UI/UX). 

## Live App

Visit the live app [here](https://citemyweb-production.up.railway.app/)

## Features

- **Automatic DOI Extraction:** Uses Selenium and Beautiful Soup to scrape DOIs directly from the source page.
- **Multiple Citation Styles:** Provides multiple citation styles to choose from.
- **Direct Copy-Paste:** Easily copy the citation and use it in your research work.
- **URL-Based Citation Generation:** Just input the URL of the research article and get the citation.
- **Flask and Railway Integration:** Developed using Flask and hosted on Railway.

## Future Goals

- **Extended Support:** Planning to extend support to all kinds of articles, web pages, and books.
- **UI/UX Improvements:** Ongoing UI/UX improvements to make the citation process seamless.
- **Enhanced Recognition:** Working on the system to even recognize book citations from URLs like Amazon without requiring any other details.

## Support

If you like this project, don't forget to give it a ⭐ on GitHub!

For any queries or suggestions, please feel free to open an issue on GitHub or reach out to us directly.

With CiteMyWeb, let's make citation easy for everyone!
