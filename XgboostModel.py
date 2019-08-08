import numpy as np
import pandas as pd
import boto3
import re
import matplotlib.pyplot as plt
import os
import sagemaker
from sagemaker import get_execution_role
from sagemaker.predictor import csv_serializer


data = pd.read_csv('amazon_locker_dataset.csv', sep=',', encoding='latin1')

data=data.iloc[:,1:]
data = pd.concat([data['QoS(S)'], data.drop(['QoS(S)'], axis=1)], axis=1) 
data=np.array(data.iloc[:,:]).astype('float32')
np.savetxt("train.csv",data, delimiter=",")

containers = {'us-east-2': '825641698319.dkr.ecr.us-east-2.amazonaws.com/xgboost:latest'}

role = get_execution_role()

sess = sagemaker.Session()
bucket = "model-artefacts-sagemaker"
prefix = "model2/test"

key = 'xgboost'
boto3.resource('s3').Bucket(bucket).Object(os.path.join(prefix, 'train', key)).upload_file('train.csv')
s3_train_data = sagemaker.s3_input(s3_data='s3://{}/{}/train/{}'.format(bucket, prefix, key), content_type='csv')
print(s3_train_data)

xgb = sagemaker.estimator.Estimator(containers[boto3.Session().region_name], role, train_instance_count=1, train_instance_type='ml.m4.xlarge', output_path='s3://{}/{}/output'.format(bucket, prefix),sagemaker_session=sess)

xgb.set_hyperparameters(eta=0.1, objective='reg:linear', num_round=25)

xgb.fit({'train': s3_train_data})

xgb_predictor = xgb.deploy(initial_instance_count=1,instance_type='ml.m4.xlarge')
