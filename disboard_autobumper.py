import requests
import time

GUILD_ID = "GUILD ID HERE"
COOKIE = "COOKIE HERE"
HEADERS = {
        'User-Agent': 'Cursed Browser',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Referer': 'https://disboard.org/dashboard/servers',
        'Cookie': COOKIE
        }
while True:
    try:
        requests.get(f"https://disboard.org/server/bump/{GUILD_ID}", headers=HEADERS)
        print("Bump done!")
    except Exception as error:
        print(error)
    time.sleep(60*60*2)
