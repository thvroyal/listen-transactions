from ..utils.helpers import load_config
from ..utils.helpers import SeleniumChrome

cfg = load_config()
integrate_dextools_api_url = cfg['INTEGRATE_DEXTOOLS_API_URL']


def api_get_token_info(selenium_chrome: SeleniumChrome, token):
    url = integrate_dextools_api_url.replace('token', token.lower())
    try:
        data = selenium_chrome.get_data(url)
        if type(data) == dict:
            return data
        else:
            return None
    except Exception as e:
        print("Error when get token info from dextools api: ", e)
        return None
