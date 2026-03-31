import requests
from config import API_KEY, SEARCH_URL, VIDEO_URL, MAX_RESULTS


def search_videos(query):

    params = {
        "key": API_KEY,
        "q": query,
        "part": "snippet",
        "type": "video",
        "maxResults": MAX_RESULTS
    }

    response = requests.get(SEARCH_URL, params=params)
    data = response.json()

    video_ids = []

    for item in data.get("items", []):
        video_ids.append(item["id"]["videoId"])

    return video_ids


def get_video_details(video_ids):

    ids = ",".join(video_ids)

    params = {
        "key": API_KEY,
        "id": ids,
        "part": "snippet,statistics"
    }

    response = requests.get(VIDEO_URL, params=params)
    data = response.json()

    return data.get("items", [])