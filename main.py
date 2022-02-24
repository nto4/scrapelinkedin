from gs import search

from time import sleep
from selenium import webdriver
import chromedriver_binary

key_word = "linkedin mehmet-basaran"

#template = "site:linkedin.com/in \“"+key_word +"\”"
test = "mehmet"
print(key_word)
# x = search(key_word, num_results=40 )

# for i in x:
#     print(i)



import requests
# URL = "https://tr.linkedin.com/in/mehmet-basaran"
URL = "https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjzjKTnrZn2AhUcRfEDHdTFDmoQFnoECAIQAQ&url=https%3A%2F%2Ftr.linkedin.com%2Fin%2Fmehmet-basaran&usg=AOvVaw0H8wBEPXZo4KERWJOVXono"
#

# headersparam = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

headersparam={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                              'accept-encoding': 'gzip, deflate, br',
                              'accept-language': 'en-US,en;q=0.9',
                              'upgrade-insecure-requests': '1',
                              'scheme': 'https'}

# print("URL")
# print(URL)
page_content = requests.get(URL, headers=headersparam)

print(page_content.status_code)
print(page_content.content)

URL2 = "https://tr.linkedin.com/in/mehmet-basaran"

page_content = requests.get(URL, headers=headersparam)

print(page_content.status_code)
print(page_content.content)

