
from heapq import heappush, heappushpop
import mysql.connector
import json



mydb = mysql.connector.connect(
        host="www.remotemysql.com",
        user="u2oI1tyJuT",
        passwd="joBxFoudcl",
        database="u2oI1tyJuT"
    )

mycursor = mydb.cursor()


sql_select_Query = "SELECT userID FROM sessionsdetails GROUP BY userID HAVING COUNT(sessionID) >= 1"



mycursor.execute(sql_select_Query,)
nrecords = mycursor.fetchall()

usermarkslist = []
for userid in nrecords:

    print(userid[0])

    id = userid[0]


    sql1 = "SELECT * FROM sessionsdetails where userID= ('%s')"%(id)

    mycursor.execute(sql1)

    myresult1 = mycursor.fetchall()


    userlocallist = []

    maximum=0

    for umarks in myresult1:
        full = umarks[6]


        userlocallist.append(full)

    num = userlocallist
    print('Maximum number of user id is:', max(num))
    maximum = max(num)

    usermarkslist.append(maximum)
print(usermarkslist)



heap = []
for x in usermarkslist:
        calculation_result = x
        if len(heap) < 100:
            heappush(heap, calculation_result)
        else:
            heappushpop(heap, calculation_result)

globaltop = sorted(heap, reverse=True)
print("--------------------------")
print(globaltop)




