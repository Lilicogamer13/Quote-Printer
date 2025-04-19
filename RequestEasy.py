import requests

def request(url):
    try:
        response = requests.get(f"http://{url}")
    except:
        response = requests.get(f"https://{url}")
    
    return response