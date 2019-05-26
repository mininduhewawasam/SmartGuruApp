import youtubecommentscrapper as a
from nltk.sentiment import SentimentIntensityAnalyzer
from googleapiclient.errors import HttpError
import json
import mysql.connector

def vediolinks(user_id):


        mySQLconnection = mysql.connector.connect(
            host="www.remotemysql.com",
            user="u2oI1tyJuT",
            passwd="joBxFoudcl",
            database="u2oI1tyJuT"
        )

        sql_select_Query = "SELECT QuestionTopic FROM (SELECT * FROM sessionsdata WHERE userID='" + user_id + "' ORDER BY sessiondataID DESC LIMIT 20) as sessionsdata GROUP BY QuestionTopic HAVING COUNT(sessiondataID) > 3"
         #get the most duplicate topic that users give the wrong answers from the database
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
            #search the topic name and get the 10 youtube vedios related to topic

            comments = []

            for video in videos:
                try:
                    comments = a.get_comments(video) #get the comments
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
                #write the in the txt file and read them back
                with open("demofile.txt", "r", encoding='utf-8') as f:
                    for line in f.read().split('\n'):
                        analysis = SentimentIntensityAnalyzer()
                        #get the compound value of each comments using vader sentiment analysis
                        score = analysis.polarity_scores(line)
                        total = total + score['compound']


                if (length > 0):  #if the vedio has comments this will excicute
                    avg = total / length

                print("compound sum of all comments: ")
                print(total)
                print("average: ")
                print(avg)

                if avg >= 0.30:   #if the avarage of all compounds is greater than 0.30 this will excicute

                    if length >= 30:   #check whethe the vedio has minimumly 30 comments

                        print("its a good vedio")
                        videolink = 'https://www.youtube.com/watch?v=' + video
                        print('https://www.youtube.com/watch?v=' + video)



                        list.append(videolink)   #insert suggested links to the list
                        print(list)



                    else:

                        print("its a bad vedio")

                else:

                    print("its a bad vedio")




        video = []



        video.append(list )
        obj = json.dumps(list)  #convert to the json object
        return obj