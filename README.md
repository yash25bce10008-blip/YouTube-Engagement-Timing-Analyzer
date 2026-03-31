# YouTube Upload Strategy Analyzer

## Overview

YouTube creators often struggle to decide the best time to upload their videos. Posting at the wrong time can reduce visibility and engagement.

This project is a **data-driven analytics tool** that analyzes real YouTube video data and recommends the **best day and hour to upload videos** based on engagement patterns.

The system collects video metadata using the YouTube Data API, processes upload timestamps, calculates engagement metrics, and identifies the most effective upload time for a given video topic.

---

## Problem

Many content creators rely on guesswork or generic advice when deciding when to upload videos. However, optimal upload times vary depending on the niche and audience activity.

Without analyzing real platform data, creators may miss opportunities to reach a larger audience.

---

## Solution

This tool analyzes recently uploaded videos related to a user-specified topic and calculates an **engagement score** based on how quickly videos gain views.

Using this analysis, the system recommends the **best day and time** to upload videos for that niche.

---

## Features

* Collects real video data using the YouTube Data API
* Converts upload timestamps from UTC to Indian Standard Time (IST)
* Calculates an engagement score using view growth rate
* Analyzes upload patterns by hour and day
* Recommends optimal upload time for better reach

---

## Technologies Used

* Python
* pandas
* requests
* YouTube Data API v3

---

## Project Structure

```text
youtube-upload-strategy-analyzer
│
├── main.py        # Runs the program
├── api.py         # Fetches data from YouTube API
├── data.py        # Processes video data
├── analyser.py    # Performs engagement analysis
├── config.py      # Stores API key and settings
│
├── requirements.txt
└── README.md
```

---

# How to Run the Project (Step-by-Step Guide)

These simple written instructions even for **people with no coding experience**.

---

## Step 1 — Install Python

1. Go to the official Python website:
   https://www.python.org/downloads/

2. Download the latest version of Python.

3. During installation **make sure to check**:

```
Add Python to PATH
```

4. Click **Install**.

After installation, open **Command Prompt** and check:

```
python --version
```

If Python is installed correctly, you will see the version number.

---

## Step 2 — Download the Project

You have two options.

### Option A (Recommended)

Download the project from GitHub:

1. Open the project repository on GitHub.
2. Click **Code**
3. Click **Download ZIP**
4. Extract the folder on your computer.

---

### Option B (Using Git)

If Git is installed, run:

```
git clone https://github.com/yash25bce10008-blip/YouTube-Engagement-Timing-Analyzer.git
```

---

## Step 3 — Open the Project Folder

Open **Command Prompt** and navigate to the project folder.

Example:

```
cd Downloads/Youtube-Engagement-Timing-Analyzer
```

---

## Step 4 — Install Required Libraries

The project uses two Python libraries.

Run this command:

```
pip install -r requirements.txt
```

This installs:

* pandas
* requests

---

## Step 5 — Create a YouTube API Key

This project requires a YouTube API key.

1. Go to
   https://console.cloud.google.com/

2. Create a **new project**

3. Enable
   **YouTube Data API v3**

4. Go to **Credentials**

5. Click **Create API Key**

Copy the generated API key.

---

## Step 6 — Add the API Key to the Project

Open the file:

```
config.py
```

Replace this line:

```
API_KEY = "YOUR_API_KEY_HERE"
```

with your real API key.

Example:

```
API_KEY = "AIzaSyXXXXXXXXXXXX"
```

Save the file.

---

## Step 7 — Run the Program

Run the following command:

```
python main.py
```

The program will ask for a topic.

Example:

```
Enter video topic or niche: gaming edits
```

---

## Example Output

```
YouTube Upload Strategy Analyzer
--------------------------------

Recommended Upload Strategy
Best Upload Hour: 16:00
Best Upload Day: Thursday
```

This means the analyzed data suggests that **4 PM on Thursday** may be the best time to upload videos in that niche.

---

# Methodology

1. The system fetches videos using the YouTube Data API.
2. Upload timestamps are converted to Indian Standard Time.
3. Video engagement is calculated using:

```
engagement_score = views / days_since_upload
```

4. Videos are grouped by upload hour and day using pandas.
5. The system recommends the time slot with the highest engagement score.

---

# Limitations

* Only a limited number of videos are analyzed
* Channel subscriber counts are not considered
* Results depend on YouTube search results

---

# Future Improvements

* Use machine learning for better prediction
* Analyze likes and comments
* Normalize engagement using subscriber counts
* Add visual data dashboards

---

# Author

Yash Khare
