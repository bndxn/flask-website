"""Runs training process, including querying DDB, transforming, training, and saving as tf-lite format."""

import logging
import pandas as pd
#from tensorflow import keras


def query_dynamo_ddb():
    pass

def handle_missing_data():
    
    
    logging.info('Results queried, X observations, with Y or Z% missing.')
    pass

def apply_train_test_split():
    pass

def train_model(train_df: pd.DataFrame) -> keras.Model:
    pass