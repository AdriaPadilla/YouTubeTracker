import requests
import time
import os
from bs4 import BeautifulSoup
import json
from collections import defaultdict
import concurrent.futures

def scrape(id, index):
    save_path = "ouput/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    url = f"https://youtu.be/{id}"
    print("Job Nº: "+str(index)+" | Scraping url: " + url)
    requests_session = requests.Session()
    page = requests_session.get(url)
    content = page.content

    data = defaultdict(dict)
    try:
        soup = BeautifulSoup(content, 'html.parser')
        # basic_info = soup.find_all("div", class_="watch-main-col")
        try:
            video_id = str(soup.find_all("meta", itemprop="videoId")[0]).split("=")[1].split('"')[1]
        except IndexError:
            video_id = "null"
        try:
            channel_title = str(soup.find_all("link", itemprop="name")[0]).split("=")[1].split('"')[1]
        except IndexError:
            channel_title = "null"
        try:
            channel_id = str(soup.find_all("meta", itemprop="channelId")[0]).split("=")[1].split('"')[1]
        except IndexError:
            channel_id = "null"
        try:
            video_title = str(soup.find_all("meta", itemprop="name")[0]).split("=")[1].split('"')[1]
        except IndexError:
            video_title = "null"
        try:
            video_genre = str(soup.find_all("meta", itemprop="genre")[0]).split("=")[1].split('"')[1]
        except IndexError:
            video_genre = "null"
        try:
            views = str(soup.find_all("meta", itemprop="interactionCount")[0]).split("=")[1].split('"')[1].replace(
                ".", "")
            views = int(views)
        except IndexError:
            views = "null"
        try:
            likes = str(soup).split('{"iconType":"LIKE"}')[1].split('Me gusta')[0].split('"label":"')[1].replace(
                ".", "")
            likes = int(likes)
        except IndexError:
            likes = "null"
        try:
            dislikes = str(soup).split('No me gusta"}},"simpleText":"')[1].split('"')[0].replace(".", "")
            dislikes = int(dislikes)
        except IndexError:
            dislikes = "null"
        try:
            comments = "null"
        except IndexError:
            comments = "null"
        try:
            video_duration = str(soup.find_all("meta", itemprop="duration")[0]).split("=")[1].split('"')[1]
        except IndexError:
            video_duration = "null"
        try:
            published_at = str(soup.find_all("meta", itemprop="datePublished")[0]).split("=")[1].split('"')[1]
        except IndexError:
            published_at = "null"
        try:
            family = str(soup.find_all("meta", itemprop="isFamilyFriendly")[0]).split("=")[1].split('"')[1]
        except IndexError:
            family = "null"
        try:
            paid = str(soup.find_all("meta", itemprop="paid")[0]).split("=")[1].split('"')[1]
        except IndexError:
            paid = "null"

        # It's live content exception!
        try:
            live = str(soup.find_all("meta", itemprop="isLiveBroadcast")[0]).split("=")[1].split('"')[1]
        except IndexError:
            live = "false"
        if live == "True":
            live_start = str(soup.find_all("meta", itemprop="startDate")[0]).split("=")[1].split('"')[1]
            live_end = str(soup.find_all("meta", itemprop="endDate")[0]).split("=")[1].split('"')[1]
        else:
            live_start = "false"
            live_end = "false"
        # Video Keywords Meta-tag

        keywords = str(soup).split('name="description"/>')[1].split('"')[1].split(",")
        clean_keywords_list = []
        for element in keywords:
            clean = element.strip()
            clean_keywords_list.append(clean)

        data["channel_info"]["channel_title"] = channel_title
        data["channel_info"]["channel_id"] = channel_id
        data["video_statistics"]["video_id"] = video_id
        data["video_statistics"]["video_views"] = views
        data["video_statistics"]["video_likes"] = likes
        data["video_statistics"]["video_dislikes"] = dislikes
        data["video_statistics"]["video_comment"] = comments
        data["video_statistics"]["video_duration"] = video_duration
        data["video_info"]["video_title"] = video_title
        data["video_info"]["video_genre"] = video_genre
        data["video_info"]["published_at"] = published_at
        data["video_info"]["family"] = family
        data["video_info"]["paid"] = paid
        data["video_info"]["live"] = live
        data["video_info"]["live_start"] = live_start
        data["video_info"]["live_end"] = live_end
        data["video_info"]["keywords"] = clean_keywords_list
        data["capture_info"]["method"] = "scrapping"
        data["capture_info"]["date"] = time.strftime("%Y-%m-%d-%H-%M")

        captured_on = time.strftime("%Y-%m-%d")
        file_name = captured_on + "_" + id
        with open(os.path.join(save_path, file_name + ".json"), "w", encoding='utf-8') as write_file:
            json.dump(data, write_file, sort_keys=True, indent=4, ensure_ascii=False)
            print("Data saved on: "+file_name+".json")

    except IndexError:
        print("error on: "+id)
        data["video_id"] = str(id)
        data["Error"] = IndexError

        file_name = captured_on + "_" + id + "_error"
        with open(os.path.join(save_path, file_name + ".json"), "w", encoding='utf-8') as write_file:
            json.dump(data, write_file, sort_keys=True, indent=4, ensure_ascii=False)

def controller(video_id_list, works_index):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(scrape, video_id_list, works_index)