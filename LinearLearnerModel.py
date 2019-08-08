import numpy as np
import pandas as pd
import boto3
import sagemaker
import io
import os
import sagemaker.amazon.common as smac
from sagemaker import get_execution_role

data = pd.read_csv('amazon_locker_dataset.csv', sep=',', encoding='latin1')
modelData = np.array(data.iloc[:, 1:11]).astype('float32')
target = np.array(data.iloc[:, 11]).astype('float32')

sess = sagemaker.Session()
bucket = "model-artefacts-sagemaker"
prefix = "Model/test"
buf = io.BytesIO()
smac.write_numpy_to_dense_tensor(buf, modelData, target)
buf.seek(0)
key = 'linearlearner'
boto3.resource('s3').Bucket(bucket).Object(os.path.join(prefix, 'train', key)).upload_fileobj(buf)
s3_train_data = 's3://{}/{}/train/{}'.format(bucket, prefix, key)
print('uploaded training data location: {}'.format(s3_train_data))
output_location = 's3://{}/{}/output'.format(bucket, prefix)
print('training artifacts will be uploaded to: {}'.format(output_location))

containers = {'us-east-2': '404615174143.dkr.ecr.us-east-2.amazonaws.com/linear-learner:latest'}
role = get_execution_role()

linear = sagemaker.estimator.Estimator(containers[boto3.Session().region_name],
	                                   role, 
                                       train_instance_count=1, 
                                       train_instance_type='ml.m4.xlarge',
                                       output_path=output_location,
                                       sagemaker_session=sess)

linear.set_hyperparameters(feature_dim=10,
                           mini_batch_size=25,
                           predictor_type='regressor',
                           normalize_data=False)

linear.fit({'train': s3_train_data})

linear_predictor = linear.deploy(initial_instance_count=1,
                                 instance_type='ml.m4.xlarge')

from sagemaker.predictor import csv_serializer, json_deserializer
linear_predictor.content_type = 'text/csv'
linear_predictor.serializer = csv_serializer
linear_predictor.deserializer = json_deserializer

result = linear_predictor.predict(modelData)
print(result)

