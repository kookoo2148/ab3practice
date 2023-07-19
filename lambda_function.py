import json
import boto3
import os
from time import sleep
from api_call import make_request_service

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    # table name & definition <--------------------change the attribute value
    table_name = 'api_test'
    params = {
        'TableName': table_name,
        'KeySchema': [
            {'AttributeName': 'Request_ID', 'KeyType': 'HASH'},
            {'AttributeName': 'Code', 'KeyType': 'RANGE'}
        ],
        'AttributeDefinitions': [
            {'AttributeName': 'Request_ID', 'AttributeType': 'S'},
            {'AttributeName': 'Code', 'AttributeType': 'S'}
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    }

    # create table
    dynamodb.create_table(**params)

    sleep(20)
    # Insert data
    table = dynamodb.Table("api_test")
    # Insert data
    # table = dynamodb.Table('api_test') <---------request body
    input_data = table.put_item(TableName='api_test', Item={'Request_ID': {11}, 'Code': {12}})

    # read dyanmodb

    response2 = table.get_item(TableName='api_test', Key={'Request_ID': Request_ID, 'Code': Code})

    response.sort()
    response2.sort()


