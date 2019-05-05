import pandas as pd
from sqlalchemy import create_engine
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#/class of recquizGenerator is used to pick similar quiestions for recomanded questions

db_connection = 'mysql+pymysql://u2oI1tyJuT:joBxFoudcl@www.remotemysql.com/u2oI1tyJuT'


conn = create_engine(db_connection)
QuestionMetadata = pd.read_sql("select * from questions", conn)


def clean_epmty_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''


features = ['question', 'chapter', 'topic', 'difficulty']

for feature in features:
    QuestionMetadata[feature] = QuestionMetadata[feature].apply(clean_epmty_data)


def createSoupOfQuestions(x):
    return ' ' + x['question'] + ' ' + x['topic'] + ' ' + x['chapter'] + ' ' + x['difficulty']


QuestionMetadata['soup'] = QuestionMetadata.apply(createSoupOfQuestions, axis=1)

count = CountVectorizer(stop_words='english')

count_matrix = count.fit_transform(QuestionMetadata['soup'])

# Compute the Cosine Similarity matrix based on the count_matrix


cosine_similarty = cosine_similarity(count_matrix, count_matrix)

metadata = QuestionMetadata.reset_index()
indices = pd.Series(metadata.index, index=metadata['question'])


def get_recommendations(questionID, cosine_sim=cosine_similarty):
    idx = indices[questionID]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    question_indices = [i[0] for i in sim_scores]
    return question_indices

