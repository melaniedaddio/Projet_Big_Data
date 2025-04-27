import joblib
import os
import numpy as np
import pandas as pd
from io import StringIO

def model_fn(model_dir):
    model_path = os.path.join(model_dir, "model.joblib")
    return joblib.load(model_path)

def input_fn(request_body, request_content_type):
    if request_content_type == "text/csv":
        df = pd.read_csv(StringIO(request_body), header=None)
        df.columns = ['loan', 'mortdue', 'value', 'reason', 'job', 'yoj', 'derog', 'delinq','clage', 'ninq', 
                      'clno', 'debtinc']
        return df
    else:
        raise ValueError(f"Unsupported content type: {request_content_type}")

def predict_fn(input_data, model):
    return model.predict(input_data)

def output_fn(prediction, content_type):
    res = ','.join([str(x) for x in prediction])
    return res