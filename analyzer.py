


def analyze_daily_views(df):

    daily = df.groupby("day")["engagement"].mean().sort_values(ascending=False)

    return daily


def find_best_time(hourly, daily):

    best_hour = hourly.idxmax()
    best_day = daily.idxmax()

    return best_hour, best_day
