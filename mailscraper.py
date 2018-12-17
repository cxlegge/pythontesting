import requests
import re

f = open('emails.txt', 'w+')

url_input = input('Website to scrape from: ')
url = 'http://' + url_input

r = requests.get(url)

emails = re.findall(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", r.text)

print(emails)
 
for i in emails:
    f.write(i + '\n')
