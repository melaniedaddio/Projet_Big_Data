import argparse
import os
import joblib
import json
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

_MODEL_TYPE = "Tree Based"

if __name__ =='__main__':

    if _MODEL_TYPE == "Logistic":
        parser = argparse.ArgumentParser()

        # hyperparameters
        parser.add_argument('--penalty', type=str, default="none")
        parser.add_argument('--solver', type=str, default="newton-cholesky")
        parser.add_argument('--random_state', type=int, default=25)

        # input data and model directories
        parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
        parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])

        args = parser.parse_args()
        print(args)

        params = {
            "penalty":args.penalty,
            "solver":args.solver,
            "random_state":args.random_state
            }
        
        input_files = [os.path.join(args.train, file) for file in os.listdir(args.train)]
        if not input_files:
            raise ValueError("Aucun fichier d'entraînement trouvé dans le répertoire fourni.")
        raw_data = [pd.read_csv(file,sep=",",engine="python") for file in input_files]
        df_train = pd.concat(raw_data)
        X = df_train.drop(columns=["bad"])
        y = df_train["bad"]
        clf = LogisticRegression(**params)
        clf.fit(X,y)

        joblib.dump(clf, os.path.join(args.model_dir, "model.joblib"))

    elif _MODEL_TYPE == "Tree Based":
        parser = argparse.ArgumentParser()

        # hyperparameters
        parser.add_argument('--criterion', type=str, default="gini")
        parser.add_argument('--splitter', type=str, default="best")
        parser.add_argument('--max_depth', type=int, default=20)
        parser.add_argument('--min_samples_split', type=int, default=5)
        parser.add_argument('--random_state', type=int, default=25)


        # input data and model directories
        parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
        parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])

        args = parser.parse_args()
        print(args)

        params = {
            "criterion":args.criterion,
            "splitter":args.splitter,
            "max_depth":args.max_depth,
            "min_samples_split":args.min_samples_split,
            "random_state":args.random_state
            }
        
        input_files = [os.path.join(args.train, file) for file in os.listdir(args.train)]
        if not input_files:
            raise ValueError("Aucun fichier d'entraînement trouvé dans le répertoire fourni.")
        raw_data = [pd.read_csv(file,sep=",",engine="python") for file in input_files]
        df_train = pd.concat(raw_data)
        X = df_train.drop(columns=["bad"])
        y = df_train["bad"]
        clf = DecisionTreeClassifier(**params)
        clf.fit(X,y)

        joblib.dump(clf, os.path.join(args.model_dir, "model.joblib"))

    else:
        parser = argparse.ArgumentParser()

        # hyperparameters
        parser.add_argument('--n_neighbors', type=int, default=5)
        parser.add_argument('--weights', type=str, default="distance")

        # input data and model directories
        parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
        parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])

        args = parser.parse_args()
        print(args)

        params = {
            "n_neighbors":args.n_neighbors,
            "weights":args.weights,
            }
        
        input_files = [os.path.join(args.train, file) for file in os.listdir(args.train)]
        if not input_files:
            raise ValueError("Aucun fichier d'entraînement trouvé dans le répertoire fourni.")
        raw_data = [pd.read_csv(file,sep=",",engine="python") for file in input_files]
        df_train = pd.concat(raw_data)
        X = df_train.drop(columns=["bad"])
        y = df_train["bad"]
        clf = KNeighborsClassifier(**params)
        clf.fit(X,y)

        joblib.dump(clf, os.path.join(args.model_dir, "model.joblib"))