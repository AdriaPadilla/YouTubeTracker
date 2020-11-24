import pandas as pd
import scraper as sc
import time

df = pd.read_csv("your_dataset.csv")

video_id_list = df["videoId"].tolist()
works_index = []

for element in video_id_list:
    index = video_id_list.index(element)
    index = index+1
    works_index.append(index)

if __name__ == '__main__':
    start_time = time.time()

    content = sc.controller(video_id_list, works_index)

    print("--- %s seconds ---" % (time.time() - start_time))