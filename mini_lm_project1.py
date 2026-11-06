import os
import re
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, top_k_accuracy_score, log_loss

def load_corpus(csv_file):
    assert os.path.isfile(csv_file), "No CSV File Found at {csv_file}"
    df = pd.read_csv(csv_file)
    return df

def tokenize(text):
    low_text = text.lower()
    return re.findall(r'\w+|[.!?]', low_text)

def build_vocabulary(train_texts, min_frequency=1):
    pass

def encode_text(text, token_to_id):
    pass

def make_examples(texts, token_to_id, context_size=3):
    pass

def vectorize_contexts(contexts, vocabulary_size):
    pass

def train_model(x_train, y_train):
    pass

def evaluate_model(model, x, y):
    pass

def predict_next_token(model, context_tokens, token_to_id, id_to_token):
    pass

def generate_text(model, prompt, token_to_id, id_to_token, max_new_tokens=20, temperature=1.0, seed=42):
    pass

def init():
    print("Loading corpus...")
    corpus = load_corpus("mini_language_corpus.csv")
    print("Corpus loaded.")
    print("Tokenizing corpus...")
    tokens = []
    for i in range(corpus.shape[0]):
        text = corpus.iloc[i, 2]
        new_tokens = tokenize(text)
        tokens.append(new_tokens)  
        print(new_tokens)
    print("Corpus tokenized.")

if __name__ == "__main__":
    init()