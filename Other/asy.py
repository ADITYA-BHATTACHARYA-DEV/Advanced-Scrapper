from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
from dataclasses import dataclass
from rich import print
import csv

@dataclass
class Item:
  asin: str
  title: str
  price: str

def get_html(page, asin):
  url=f"https://www.amazon.in/dp/{asin}"
  page.goto(url)
  html=HTMLParser(page.content())
  return html

def parse_html(html,asin):
  item=Item(
    asin=asin,
    title=html.css_first("span#productTitle").text(strip=True),
    price=html.css_first("span.aok-offscreen").text(strip=True)
  )

  return item
  # print(html.css_first("title").text())
  # print(asin)

def read_csv():
  with open('products.csv', 'r') as f:
    reader =csv.reader(f)
    return [item[0] for item in reader]
def run(asin):
  asin="B095CRM8NF"
  pw=sync_playwright().start()
  browser=pw.chromium.launch()
  page=browser.new_page()
  html=get_html(page,asin)
  product=parse_html(html,asin)
  print(product)
  browser.close()
  pw.stop()

def main():
  asins=read_csv()
  for asin in asins:
    run(asin)



if __name__ == "__main__":
  main()
