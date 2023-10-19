import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

#import dataset
dataset = pd.read_csv('mail_data.csv')

#convert into binary
dataset['Spam']=dataset['Category'].apply(lambda x:1 if x=='spam' else 0)

#break the dataset
X = dataset['Message']
y = dataset['Spam']

#model creation
model = Pipeline([
    ('vectorizer',CountVectorizer()),
    ('nb',MultinomialNB())
])

#fit into the model
model.fit(X, y)

#store the data
data = {"model": model}
with open('saved_steps.pkl', 'wb') as file:
    pickle.dump(data, file)