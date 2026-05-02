
import requests
import os
from dotenv import load_dotenv
load_dotenv()


def post_data(data=None):
    """
    Send a POST request.
    """
    url = os.getenv("POST_DATA_URL")
    api_key = os.getenv("API_KEY")
    headers = {'Content-Type': 'application/json', 'X-API-Key': api_key}
    try:
        if data is None:
            raise Exception("Data to post is None.")

        if url is None or len(url) == 0:
            raise Exception(
                "POST_DATA_URL environment variable is not set or empty.")

        response = requests.post(url, headers=headers, json=data)
        # print(f"post_data Response ({response.status_code}): {response.text}")
        return response
    except Exception as e:
        print(f"Error(post_data): {e}")
        return []


def get_current_schedule():
    """
    Get the current schedule.
    """
    url = os.getenv("GET_SCHEDULE_URL")
    try:
        if url is None or len(url) == 0:
            raise Exception(
                "GET_SCHEDULE_URL environment variable is not set or empty.")
        response = requests.get(url)
        # print(f"get_current_schedule Response ({response.status_code}): {response.text}")
        return response.json()
    except Exception as e:
        print(f"Error(get_current_schedule): {e}")
        return []
