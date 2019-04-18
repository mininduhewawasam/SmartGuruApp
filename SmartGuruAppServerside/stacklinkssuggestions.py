

from googleapiclient.discovery import build
import pprint
import json

# from test import response

my_api_key = "AIzaSyALfLVvJfvu2PNFE8mLdMqef7EwY1OtxR8"
my_cse_id = "003757576047006749371:yur5pb9japo"


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(
    'java loops:en.stackoverflow.com', my_api_key, my_cse_id, num=10)

result_list = [results]
for result in results:
    pprint.pprint(result)

# result_json = json.dumps(results)
# json_list = json.loads(result_json)
# for item in json_list:
#     # print(item['link'])
#
#     if item['pagemap']!=0 :
#         print(item['link'])
result_json = json.dumps(results)
json_list = json.loads(result_json)
for item in json_list:
  if item['displayLink'] == 'stackoverflow.com':
    print(item['link'])

