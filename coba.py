from bs4 import BeautifulSoup
import requests

url ="https://id.wikipedia.org/wiki/Soedirman"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

main = soup.find(id="mw-content-text")
p=main.find_all("p")
traw=""
for pp in p:
    traw+=pp.get_text()

print(traw)