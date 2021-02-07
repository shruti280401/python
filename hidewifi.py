import requests
import webbrowser
url="https://abcxyz.com"
#req = requests.get(url)
try:
    if(requests.get(url)):
            print("found")
            webbrowser.open(url)

except requests.exceptions.ConnectionError:
            print("not found")