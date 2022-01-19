import requests

from src.api_config import API_ENDPOINT_DOMAIN

def get_status_by_tags(tags):
    params = {"tags": tags}
    response = requests.get(API_ENDPOINT_DOMAIN + "/twitter/status", params=params)
    search_results = response.json()
    return search_results
