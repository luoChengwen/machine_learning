import pandas as pd
import numpy as np
test = pd.read_csv('/Users/daisy/Downloads/test.csv')
str = unicode(str, errors='ignore')
train = pd.read_csv('/Users/daisy/Downloads/train.csv', encoding = "ISO-8859-1")
train_y = train.compliance
train_X = train[[test.columns]]


# def blight_model():
#     
#     
#     
#     return # Your answer here