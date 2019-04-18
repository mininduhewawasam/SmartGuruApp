import videocommentscrapper as a
from nltk.sentiment import SentimentIntensityAnalyzer
from googleapiclient.errors import HttpError

if __name__ == "__main__":

    videos = a.search_by_keyword("Java" + " loops")

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

        avg = total / length

        print("compound sum of all comments: ")
        print(total)
        print("average: ")
        print(avg)

        if avg >= 0.30:

            if length >= 30:

                print("its a good vedio")
                print('https://www.youtube.com/watch?v=' + video)

            else:

                print("its a bad vedio")

        else:

            print("its a bad vedio")