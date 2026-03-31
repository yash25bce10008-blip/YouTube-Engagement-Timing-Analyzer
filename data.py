import pandas as pd
from datetime import datetime, timedelta


def collect_video_data(video_items):

    data = []

    # Current time in IST
    now_utc = datetime.utcnow()
    now_ist = now_utc + timedelta(hours=5, minutes=30)

    for video in video_items:

        snippet = video["snippet"]
        stats = video["statistics"]

        published = snippet["publishedAt"]

        # Convert published time to datetime (UTC)
        dt_utc = datetime.strptime(published, "%Y-%m-%dT%H:%M:%SZ")

        # Convert upload time to IST
        dt_ist = dt_utc + timedelta(hours=5, minutes=30)

        hour = dt_ist.hour
        day = dt_ist.strftime("%A")

        views = int(stats.get("viewCount", 0))

        # Calculate days since upload using IST
        days_since_upload = (now_ist - dt_ist).days + 1

        # Engagement score
        engagement = views / days_since_upload

        data.append({
            "hour": hour,
            "day": day,
            "engagement": engagement
        })

    df = pd.DataFrame(data)

    return df