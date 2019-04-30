from selenium import webdriver
from seleniumrequests import Chrome
import requests
chrome_options = webdriver.ChromeOptions()
# 无头模式
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 实例化Chrome driver
# browser = webdriver.Chrome(chrome_options=chrome_options)
browser = webdriver.Chrome()

browser.get('https://map.baidu.com/')
browser.save_screenshot("baidu-map.png")
browser.quit()

Chrome

# headers = {'Content-Type': 'application/json;charset=UTF-8',
#            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
#            'xToken': 'eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE1NTYwODMyMjAsInN1YiI6IntcImxvZ2luTmFtZVwiOlwiYWRtaW5cIixcIm9yZ0lkXCI6NixcIm9yZ05hbWVcIjpcIuaNt-i2iuiBlOWQiFwiLFwib3JnUGFyZW50SWRcIjpcIjBcIixcInN5c0NvZGVcIjpcIlMwLTAxMDFcIixcInVzZXJJZFwiOjEsXCJ1c2VyTmFtZVwiOlwi566h55CG5ZGYMTJcIixcInVzZXJOb1wiOlwiMVwifSJ9.n1XNaYpsqzjPcwbavlriT1FW8hQMwv3BSnMXZBlLztI8KHLV8rOgKBk4u70vQGm1ABzTEFK46KQ-EAvpMYewqA'}
#
# url = 'http://localhost:3000/fqz/api/faApplication/searchByPage/v1'
# pars = {"pageParameter": {"pageSize": 10, "currentPage": 1}, "searchParams": {"dto": {}}}
# postSession = requests.post(url, json=pars, headers=headers)
# print(postSession.json())
