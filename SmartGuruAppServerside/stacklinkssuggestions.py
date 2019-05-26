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


def stacklinks(user_id):

    mySQLconnection = mysql.connector.connect(
        host="www.remotemysql.com",
        user="u2oI1tyJuT",
        passwd="joBxFoudcl",
        database="u2oI1tyJuT"
        )

    sql_select_Query = "SELECT QuestionTopic FROM (SELECT * FROM sessionsdata WHERE userID='" + user_id + "' ORDER BY sessiondataID DESC LIMIT 20) as sessionsdata GROUP BY QuestionTopic HAVING COUNT(sessiondataID) > 3"
    # get the most duplicate topic that users give the wrong answers from the database
    cursor = mySQLconnection.cursor()

    cursor.execute(sql_select_Query,)
    nrecords = cursor.fetchall()

    print(nrecords)

    stacklist = []

    for row in nrecords:

        print(row[0])
        results = google_search(
            'java '+row[0]+':en.stackoverflow.com', my_api_key, my_cse_id, num=10)
             #search result using by google api

        for result in results:
            pprint.pprint(result)

            result_json = json.dumps(results)
            json_list = json.loads(result_json)
    for item in json_list:
        if item['displayLink'] == 'stackoverflow.com':
            #if the link is stack overflow link the this will be excicute
            print(item['link'])

            stacklinks = (item['link'])
            #append links to the list
            stacklist.append(stacklinks)
            print(stacklist)

    video = []

    video.append(stacklist)
    stackobj = json.dumps(stacklist) #convert in to json object
    return stackobj

