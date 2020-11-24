# YouTubeTracker

This Script will help you to "track" and save YouTube video metrics and evolution in time via scraping method. 

**What do you need?**
- A list of video id's you want to track, in csv format, under a column named "videoId".
- A server to automate script execution with cronjobs.

**what will you get**
- The script will scrape video metrics and save a JSON file for each capture.
- in "output/" directory, with format: yyyy-mm-dd-HH-MM-video_id.json

**Process the JSON data**
- create a script to process JSON data to pandas dataframe or similar :)

**JSON file example**
filename: 2020-11-24_ERhi8yTfW5Q.json
```JSON
{
    "capture_info": {
        "date": "2020-11-24-10-06",
        "method": "scrapping"
    },
    "channel_info": {
        "channel_id": "UCFOSg71CRAJ58IPuV_-jMbw",
        "channel_title": "Tecnonauta"
    },
    "video_info": {
        "family": "True",
        "keywords": [
            "Sony",
            "Mejores Teléfonos",
            "Duras Pruebas",
            "Tecnonauta",
            "iPhone 12"
        ],
        "live": "false",
        "live_end": "false",
        "live_start": "false",
        "paid": "False",
        "published_at": "2020-10-26",
        "video_genre": "Entertainment",
        "video_title": "EL iPHONE 12 de SONY!!!!!!! ¿Es mejor?"
    },
    "video_statistics": {
        "video_comment": "null",
        "video_dislikes": 905,
        "video_duration": "PT19M8S",
        "video_id": "ERhi8yTfW5Q",
        "video_likes": 39774,
        "video_views": 886663
    }
}
```


