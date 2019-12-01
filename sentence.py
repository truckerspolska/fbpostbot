from bs4 import BeautifulSoup
from selenium import webdriver

noundriver = webdriver.Chrome("path to chromedriver.exe goes here")
adjdriver = webdriver.Chrome("path to chromedriver.exe goes here")

noundriver.get("https://randomwordgenerator.com/noun.php")
adjdriver.get("https://randomwordgenerator.com/adjective.php")

webnoun = noundriver.execute_script("return document.documentElement.outerHTML")
webadj = adjdriver.execute_script("return document.documentElement.outerHTML")

soupnoun = BeautifulSoup(webnoun, 'lxml')
soupadj = BeautifulSoup(webadj, 'lxml')

noun = soupnoun.find('span', {'class':'support'}).text
adj = soupadj.find('span', {'class':'support'}).text

noundriver.quit()
adjdriver.quit()

imgdriver = webdriver.Chrome("C:\Python\chromedriver.exe")
imgdriver.get("https://duckduckgo.com/?q=" + adj + "+" + noun + "&iax=images&ia=images")
webimg = imgdriver.execute_script("return document.documentElement.outerHTML")
soupimg = BeautifulSoup(webimg, 'lxml')

link = [img.get('src') for img in soupimg.find_all('img', class_='tile--img__img')]
link = str(link[0])
result = str(adj + " " + noun)
dic = {"sentence" : result, "image": link}

imgdriver.quit()