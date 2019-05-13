
from heapq import heappush, heappushpop
import mysql.connector
import json

def sortedmarks():
    mydb = mysql.connector.connect(
        host="www.remotemysql.com",
        user="u2oI1tyJuT",
        passwd="joBxFoudcl",
        database="u2oI1tyJuT"
    )

    mycursor = mydb.cursor()

    sql_select_Query = "SELECT userID FROM sessionsdetails GROUP BY userID HAVING COUNT(sessionID) >= 1"

    mycursor.execute(sql_select_Query, )
    nrecords = mycursor.fetchall()

    usermarkslist = []

    listing = []

    for userid in nrecords:

        print(userid[0])

        id = userid[0]

        sql2 = "SELECT * FROM users where userID= ('%s')" % (id)   #get the user names
        mycursor.execute(sql2)
        myres = mycursor.fetchall()
        print(myres)

        for name in myres:
            unames = name[1]
            print(unames)



        sql1 = "SELECT * FROM sessionsdetails where userID= ('%s')" % (id)   #get scores according to specific users
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()

        userlocallist = []

        maximum = 0
        details = 0

        for umarks in myresult1:
            full = umarks[6]

            userlocallist.append(full)

        num = userlocallist
        print('Maximum number of user id is:', max(num))
        maximum = max(num)
        print(maximum, unames)
        details = (maximum, unames)

        listing.append(details)
        usermarkslist.append(maximum)
    print(usermarkslist)
    print(listing)    #get the highest score of each users with thir names and store it in the list



    #using heapq library get the score best to worst
    heap = []
    for x in listing:
        calculation_result = x
        if len(heap) < 100:
            heappush(heap, calculation_result)
        else:
            heappushpop(heap, calculation_result)

    globaltop = sorted(heap, reverse=True)
    print("--------------------------")
    print(globaltop)


    topmarks = json.dumps(globaltop)


    return topmarks

