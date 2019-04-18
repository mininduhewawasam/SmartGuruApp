import pandas as pd
from sqlalchemy import create_engine

db_connection = 'mysql+pymysql://root:@localhost/test'

conn = create_engine(db_connection)
metadata = pd.read_sql("select * from questions", conn)

# metadata = pd.read_csv('quizes.csv')

print(metadata.head(2))

features = ['question', 'chapter', 'topic']



print(metadata[['question', 'chapter', 'topic']].head(3))

def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        #Check if director exists. If not, return empty string
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''


features = ['question', 'chapter', 'topic']

for feature in features:
    metadata[feature] = metadata[feature].apply(clean_data)


def create_soup(x):
    return ' ' + x['question'] + ' ' + x['topic'] + ' ' + x['chapter']


metadata['soup'] = metadata.apply(create_soup, axis=1)

from sklearn.feature_extraction.text import CountVectorizer

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(metadata['soup'])

# Compute the Cosine Similarity matrix based on the count_matrix
from sklearn.metrics.pairwise import cosine_similarity

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

metadata = metadata.reset_index()
indices = pd.Series(metadata.index, index=metadata['question'])


def get_recommendations(idno, cosine_sim=cosine_sim2):
    idx = indices[idno]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[0:5]

    question_indices = [i[0] for i in sim_scores]

    return metadata['idno'].iloc[question_indices]


def main(idNum):
    print(get_recommendations(idNum, cosine_sim2))


if __name__ == '__main__':

    while(True):
        idnumber = int(input("enter question id"))
        print(idnumber)

        main(idnumber)
