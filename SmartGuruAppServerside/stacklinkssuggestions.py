from googleapiclient.discovery import build
import pprint
import json
import mysql.connector



my_api_key = "AIzaSyALfLVvJfvu2PNFE8mLdMqef7EwY1OtxR8"
my_cse_id = "003757576047006749371:yur5pb9japo"


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']


def stacklinks():

    mySQLconnection = mysql.connector.connect(
        host="www.remotemysql.com",
        user="u2oI1tyJuT",
        passwd="joBxFoudcl",
        database="u2oI1tyJuT"
        )


    sql_select_Query = """SELECT QuestionTopic FROM sessionsdata GROUP BY QuestionTopic HAVING COUNT(QuestionID) > 5"""

    cursor = mySQLconnection.cursor()

    cursor.execute(sql_select_Query,)
    nrecords = cursor.fetchall()

    print(nrecords)

    stacklist = []

    for row in nrecords:

        print(row[0])
        results = google_search(
            'java '+row[0]+':en.stackoverflow.com', my_api_key, my_cse_id, num=10)


        for result in results:
            pprint.pprint(result)

            result_json = json.dumps(results)
            json_list = json.loads(result_json)
    for item in json_list:
        if item['displayLink'] == 'stackoverflow.com':
            print(item['link'])

            stacklinks = (item['link'])

            stacklist.append(stacklinks)
            print(stacklist)

    video = []

    video.append(stacklist)
    stackobj = json.dumps(stacklist)
    return stackobj

