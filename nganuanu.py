from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = "D:/#Kuliah/SEMESTER 7/webmining/facerap/facebook-friend-network-master/chromedriver.exe"

dr = webdriver.Chrome(path)

ling = "https://id.wikipedia.org/wiki/Soedirman"
dr.get(ling)

try:
    main = WebDriverWait(dr, 10).until(
        EC.presence_of_element_located((By.ID, "mw-content-text"))
    )
    texts = main.find_element_by_tag_name("p")
    for xx in texts:
        print(xx.text)
finally:
    dr.quit()