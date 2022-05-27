import time
import pandas as pd
import requests
import re

def get_reviews(url):
    r = requests.get(url)
    movie_id = re.findall(r'(?<=movieId":")(.*)(?=","type)', r.text)[0]

    api_url = f"https://www.rottentomatoes.com/napi/movie/{movie_id}/criticsReviews/all"  # use reviews/userfor user reviews

    payload = {
        'direction': 'next',
        'endCursor': '',
        'startCursor': '',
    }

    review_data = []

    while True:
        s = requests.Session()
        r = s.get(api_url, headers=headers, params=payload)
        data = r.json()

        if not data['pageInfo']['hasNextPage']:
            break

        payload['endCursor'] = data['pageInfo']['endCursor']
        payload['startCursor'] = data['pageInfo']['startCursor'] if data['pageInfo'].get('startCursor') else ''

        review_data.extend(data['reviews'])
        time.sleep(1)

    return review_data

if __name__ == '__main__':

    headers = {
        'Referer': 'https://www.rottentomatoes.com/m/notebook/reviews?type=user',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = get_reviews('https://www.rottentomatoes.com/m/call_me_by_your_name/reviews')
    df = pd.json_normalize(data)
    df.to_csv("call_me_by_your_name.csv",encoding="utf-8")