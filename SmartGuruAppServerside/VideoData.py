#import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
#import urllib.parse as urlparse

DEVELOPER_KEY = 'AIzaSyA3vPlQVS46IOVjEKln3QkeRtVtctnSHhk'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def search_by_keyword(search_term):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=search_term,
        part='id,snippet',
        maxResults=10
    ).execute()

    videos = []

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append('%s' % (search_result['id']['videoId']))

    # print('Videos:\n', '\n'.join(videos), '\n')

    return videos[0]


def get_comments(video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    results = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText",
        maxResults=100
    ).execute()

    comments = []

    i = 1


    for result in results.get('items', []):


        if result['kind'] == 'youtube#commentThread':
            comments.append('%d %s' % (i, result['snippet']['topLevelComment']['snippet']['textOriginal']))
            i += 1



    # print('Comments:\n', '\n'.join(comments), '\n')

    return comments