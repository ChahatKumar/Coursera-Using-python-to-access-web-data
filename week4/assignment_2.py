from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

url = input("Enter URL - ")

pos = int(input("Enter the position - ")) - 1
count = int(input("Enter the count - "))
count1 = 0
while(count1 < count):

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    url = tags[pos].get('href')
    name = tags[pos].contents[0]
    count1 = count1 + 1

print(name)



