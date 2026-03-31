from api import search_videos, get_video_details
from data import collect_video_data
from analyzer import analyze_hourly_views, analyze_daily_views, find_best_time


def main():

    print("YouTube Upload Strategy Analyzer")
    print("--------------------------------")

    topic = input("Enter video topic or niche: ")

    print("\nSearching videos...")

    video_ids = search_videos(topic)

    if not video_ids:
        print("No videos found.")
        return

    print("Collecting video data...")

    video_items = get_video_details(video_ids)

    df = collect_video_data(video_items)

    print("\nAnalyzing data...")

    hourly = analyze_hourly_views(df)
    daily = analyze_daily_views(df)

    best_hour, best_day = find_best_time(hourly, daily)

    print("\nRecommended Upload Strategy")
    print("---------------------------")
    print(f"Best Upload Hour: {best_hour}:00")
    print(f"Best Upload Day: {best_day}")

    print("\nHourly Engagement:")
    for hour, views in hourly.items():
        print(f"{hour}:00 -> {int(views)} views")


if __name__ == "__main__":
    main()