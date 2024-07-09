import requests
with open("new_valid_proxies", "r") as f:
    proxies=f.read().split("\n")


sites_to_check=["https://books.toscrape.com/",
                "https://books.toscrape.com/catalogue/category/books/historical_42/index.html"]


counter =0

for site in sites_to_check:
    try:
        print(f"Using the proxy: {proxies[counter]}")
        res=requests.get(site,proxies={"http":proxies[counter],
                         "https":proxies[counter]})
        print(res.status_code)
        print(res.text)

    except:
        print("Failed")
    finally:
        counter +=1
        counter % len(proxies)
