import requests
from ..utils.helpers import load_config

cfg = load_config()
integrate_dextools_api_url = cfg['INTEGRATE_DEXTOOLS_API_URL']

def api_get_token_info(token):
    url = integrate_dextools_api_url.replace('token', token.lower())
    print(url)
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        return response.json()
    except Exception as e:
        print(e)
        return None