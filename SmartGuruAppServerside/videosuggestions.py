import youtubecommentscrapper as a
from nltk.sentiment import SentimentIntensityAnalyzer
from googleapiclient.errors import HttpError
import json
import mysql.connector

def vediolinks():


        mySQLconnection = mysql.connector.connect(
            host="www.remotemysql.com",
            user="u2oI1tyJuT",
            passwd="joBxFoudcl",
            database="u2oI1tyJuT"
        )


        sql_select_Query = "SELECT QuestionTopic FROM sessionsdata WHERE userID=1 GROUP BY QuestionTopic HAVING COUNT(sessiondataID) > 4"

        cursor = mySQLconnection.cursor()

        cursor.execute(sql_select_Query,)
        nrecords = cursor.fetchall()

        print(nrecords)

        list = []

        for row in nrecords:

            print("topics  = ", row[0], "\n")

            word = row[0]

            print(word)



            videos = a.search_by_keyword("Java-" + word)

            comments = []

            for video in videos:
                try:
                    comments = a.get_comments(video)
                except HttpError:
                    print("Error")

                print("---------------------------------------- ")
                print('Video Id:\n', video)

                # print('Comments:\n', '\n'.join(comments), '\n')
                comm = '\n'.join(comments)

                length = len(comments)

                print("Number of comments: ")
                print(length)

                total = 0

                with open("demofile.txt", "w", encoding='utf-8') as document:
                    document.write(comm)

                with open("demofile.txt", "r", encoding='utf-8') as f:
                    for line in f.read().split('\n'):
                        analysis = SentimentIntensityAnalyzer()

                        score = analysis.polarity_scores(line)
                        total = total + score['compound']


                if (length > 0):
                    avg = total / length

                print("compound sum of all comments: ")
                print(total)
                print("average: ")
                print(avg)

                if avg >= 0.30:

                    if length >= 30:

                        print("its a good vedio")
                        videolink = 'https://www.youtube.com/watch?v=' + video
                        print('https://www.youtube.com/watch?v=' + video)



                        list.append(videolink)
                        print(list)



                    else:

                        print("its a bad vedio")

                else:

                    print("its a bad vedio")




        video = []



        video.append(list )
        obj = json.dumps(list)
        return obj