# chequeo robots.txt y X-Frame-Options
import requests
url = "https://nextar.shop"
r = requests.get(url + "/robots.txt", timeout=10)
print("robots.txt:\n", r.text[:800])

r2 = requests.get("https://nextar.shop/JBOUTLET", timeout=10)
print("X-Frame-Options:", r2.headers.get("X-Frame-Options"))
print("Content-Type:", r2.headers.get("Content-Type"))
