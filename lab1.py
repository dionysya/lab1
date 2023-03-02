import requests  # εισαγωγή της βιβλιοθήκης
import datetime


#url = 'https://chat.openai.com/chat'  # προσδιορισμός του url
url = input("Enter a URL: ")

print("URL:", url)

with requests.get(url) as response:  # το αντικείμενο response
    html = response.text
    r = response.headers
    print('\n')
    print("Server:\n" + r['server'])
    print('\nCookies:')
    cookies = response.cookies
    for cookie in cookies:
        expires_timestamp = cookie.expires
        expires_datetime = datetime.datetime.fromtimestamp(expires_timestamp)
        print(cookie.name, expires_datetime ,'\n')
    print('All headers:')
    print(r)
