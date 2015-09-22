import requests


try:
    r = requests.get('http://mdk.fr/ip')
    print(r.text.split('\n', 1)[0])
except Exception:
    print("No internet connectivity.")
