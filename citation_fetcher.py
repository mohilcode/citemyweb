from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError
import re


def setup_webdriver():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--no-sandbox") 
    options.add_argument("--disable-dev-shm-usage") 
    options.add_argument('--headless')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    return driver


def get_doi_from_soup(soup, url):
    if "researchgate.net" in url:
        meta_doi = soup.find("meta", {"property": "citation_doi"})
    elif "thelancet.com" in url:
        meta_doi = soup.find("meta", {"name": "citation_doi"})
    else:
        meta_doi = None

    if meta_doi:
        doi_value = meta_doi["content"]
    else:
        doi_regex = r"\b(10\.\d{4,}/[\w./-]+)\b"
        doi_matches = re.findall(doi_regex, str(soup))

        if doi_matches:
            doi_value = max(doi_matches, key = doi_matches.count)
        else:
            doi_value = None

    return doi_value


def get_citation(url, style):
    driver = setup_webdriver()

    try:
        driver.get(url)

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")

        doi_value = get_doi_from_soup(soup, url)
        if doi_value is None:
            raise ValueError("DOI not found.")

        BASE_URL = 'http://dx.doi.org/'
        url = BASE_URL + doi_value.strip()
        req = urllib.request.Request(url)
        req.add_header('Accept', f'text/x-bibliography; style={style}')

        with urllib.request.urlopen(req) as f:
            citation = f.read().decode()
        citation = citation.replace("Crossref", "")
        citation = citation.replace("<i>", "")
        citation = citation.replace("</i>", "")

    except HTTPError as e:
        if e.code == 404:
            raise ValueError("DOI not found.")
        else:
            raise ValueError("Service unavailable.")
    except Exception as e:
        raise ValueError(str(e))
    finally:
        driver.quit()

    return citation
