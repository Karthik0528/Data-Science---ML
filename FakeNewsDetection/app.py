import pickle
import os

# get current directory path
current_dir = os.path.dirname(__file__)

model_path = os.path.join(current_dir, 'model.pkl')
vectorizer_path = os.path.join(current_dir, 'vectorizer.pkl')

model = pickle.load(open(model_path, 'rb'))
vectorizer = pickle.load(open(vectorizer_path, 'rb'))

