# Chapter 12: Web Scraping
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import bs4

# Part 1: Web Scraping with BeautifulSoup
# 1. Downloading a Web Page with `requests` Module
def download_web_page(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
        print(f"Successfully accessed: {url}")
        return res.text
    except Exception as exc:
        print(f"There was a problem: {exc}")
        return None

# Displaying the first 500 characters of the downloaded content.
def display_page_preview(content, length=500):
    if content:
        print(content[:length])

# 2. Parsing HTML with BeautifulSoup
def parse_html(content):
    return bs4.BeautifulSoup(content, 'html.parser') if content else None

# 3. Selecting Elements with `select()`
def find_elements_by_class(soup, class_name):
    elements = soup.select(class_name) if soup else []
    print(f"Number of elements with class '{class_name}': {len(elements)}")
    return elements

def find_elements_by_tag(soup, tag_name):
    elements = soup.select(tag_name) if soup else []
    print(f"Number of '{tag_name}' elements: {len(elements)}")
    return elements

def get_element_text(elements, index=0):
    if elements and len(elements) > index:
        print(elements[index].getText())

# 4. Accessing Attributes of Elements
def get_link_attributes(soup):
    links = soup.select('a') if soup else []
    if links:
        print(f"First link: {links[0].get('href')}")
    return links

# 5. Downloading Images
def download_image(image_url, file_name):
    try:
        res = requests.get(image_url)
        res.raise_for_status()
        with open(file_name, 'wb') as image_file:
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
        print(f"Image downloaded: {file_name}")
    except Exception as exc:
        print(f"There was a problem downloading the image: {exc}")

# 6. Scraping a Web Page for Links
def get_all_links(url):
    content = download_web_page(url)
    soup = parse_html(content)
    links = []
    if soup:
        for link_element in soup.select('a'):
            href = link_element.get('href')
            if href and href.startswith('http'):
                links.append(href)
    print(f"Found {len(links)} links.")
    return links

# 7. Downloading All Images from a Web Page
def download_all_images(url, folder='images'):
    content = download_web_page(url)
    soup = parse_html(content)

    if not soup:
        return

    if not os.path.exists(folder):
        os.makedirs(folder)

    image_elements = soup.select('img')
    for img_element in image_elements:
        img_url = img_element.get('src')
        if not img_url:
            continue

        if not img_url.startswith('http'):
            img_url = requests.compat.urljoin(url, img_url)

        img_name = os.path.basename(img_url)
        try:
            download_image(img_url, os.path.join(folder, img_name))
        except Exception as exc:
            print(f"Failed to download {img_url}: {exc}")

# Part 2: Web Scraping with Selenium (NEED TO PRATICE MORE)
# 1. Setting Up Selenium WebDriver
def set_up_driver(driver_path, browser='edge'):
    try:
        if browser == 'edge':
            driver = webdriver.Edge()
            print(f"{browser.capitalize()} WebDriver setup completed.")
            return driver
        else:
            print("Unsupported browser! Only 'edge' is supported.")
            return None
    except Exception as e:
        print(f"Error setting up the WebDriver: {e}")
        return None

# 2. Opening a Web Page
def open_web_page(driver, url):
    try:
        driver.get(url)
        print(f"Opened {url}")
    except Exception as e:
        print(f"Error opening page: {e}")

# 3. Finding Elements on a Page
def find_element_by_css(driver, selector):
    try:
        driver.get('https://automatetheboringstuff.com')
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, selector))
        )
        print(f"Found element with selector: '{selector}'")
        return element
    except NoSuchElementException:
        print(f"Element with selector '{selector}' not found.")
        return None
    except TimeoutException:
        print(f"Timed out waiting for element with selector '{selector}'.")
        return None

