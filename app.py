import os
import boto3
import json
from dotenv import load_dotenv
load_dotenv()


def load_results_to_s3():
	client = boto3.client(
	    's3', 
	    endpoint_url='https://s3.amazonaws.com',
	    aws_access_key_id=os.getenv('ACCESS_KEY'),
	    aws_secret_access_key=os.getenv('SECRET_ACCESS_KEY')
	)
	json_data = json.dumps({'test': 'hello'})
	client.put_object(
		Bucket=os.getenv('BUCKET_NAME'), 
		Key=f'real_estate/test.json',
		Body=json_data
	)

def main():
	load_results_to_s3()


if __name__ == '__main__':
	main()
