from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

url = input("Enter URL - ")

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
sum = 0
for value in tags:
    temp = int(value.contents[0])
    sum = sum + temp
print(sum)

