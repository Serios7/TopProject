import requests

search = 'linkin park'
url = 'http://go.mail.ru/zaycev?q=%s' % (search)
r = requests.get(url)

print(r.text)
