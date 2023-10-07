from selenium import webdriver
from selenium.webdriver.common.by import By

import random
import time

browser = webdriver.Firefox()

url = ("https://campus.datacamp.com/courses/free-introduction-to-r/chapter-6-lists?ex=")

entries=[]
entrycount=1
pagecount = 1


for i in range(1,8):
    newurl = url+str(i)
    browser.get(newurl)


    elements = browser.find_elements(By.CSS_SELECTOR, ".exercise--sidebar-content")
    for element in elements:
        entries.append(element.text)

    time.sleep(4)
    
    

    


with open("List.txt","w",encoding="UTF-8") as file:
    for entry in entries:
        file.write(str(entrycount)  + ".\n" + entry + "\n")
        entrycount +=1
            
        
browser.quit()
