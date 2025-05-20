import requests

def make_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.RequestException:
        pass



target_input = input("Enter the target domain (e.g., example.com): ")

with open("subdomainlist.txt", "r") as subdomain_list:
   for word in subdomain_list:
      word=word.strip()#strip temizler
      url="http://" +word + "."+ target_input
      response =make_request(url)
      if response:
          print(f"Subdomain found:----> {url}")
