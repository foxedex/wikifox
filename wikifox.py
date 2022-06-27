import requests , cowsay
from bs4 import BeautifulSoup
#Print the logo of fox
cowsay.fox("foxedex wikifox")
#Enter to page and extracing code
search = input("\n Enter the thing you want to search : ")
page = requests.get('https://en.wikipedia.org/w/index.php?search='+search+'&title=Special%3ASearch&go=Go&ns0=1')
print("\n Requesting done.")
print(page.status_code)
content = str(page.content)
#Start beautifulsoup
bs = BeautifulSoup(content , 'lxml')
#Searching text and print it
p = bs.find('h1')
print("\n                                                              "+p.text)
text = bs.find_all('p')
t = 0
for txt in text :

    if t > 3 :
        print("\n", txt.text)
    if t == 6 :
        break;
    t = t + 1
