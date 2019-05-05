@@ -0,0 +1,63 @@
import pandas as pd
from sqlalchemy import create_engine
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

db_connection = 'mysql+pymysql://u2oI1tyJuT:joBxFoudcl@www.remotemysql.com/u2oI1tyJuT'
# engine = create_engine("mysql+pymysql://u2oI1tyJuT:joBxFoudcl@www.remotemysql.com/u2oI1tyJuT")me widiyata conncte karana eka karpn

# mySQLconnection = mysql.connector.connect(host='www.remotemysql.com',
#                                           database='u2oI1tyJuT',
#                                           user='u2oI1tyJuT',
#                                           password='joBxFoudcl')


conn = create_engine(db_connection)
metadata = pd.read_sql("select * from users", conn)

features = ['id', 'name', 'email', 'password', 'userType']


def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        #Check if director exists. If not, return empty string
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''


features = ['id', 'name', 'email', 'password', 'userType']

for feature in features:
    metadata[feature] = metadata[feature].apply(clean_data)


def create_soup(x):
    return ' ' + x['id'] + ' ' + x['name'] + ' ' + x['email'] + ' ' + x['password']+ ' ' + x['userType']


metadata['soup'] = metadata.apply(create_soup, axis=1)

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(metadata['soup'])

# Compute the Cosine Similarity matrix based on the count_matrix


cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

metadata = metadata.reset_index()
indices = pd.Series(metadata.index, index=metadata['id'])


def get_recommendations(userID, cosine_sim=cosine_sim2):
    idx = indices[userID]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    question_indices = [i[0] for i in sim_scores]
    return question_indices
