import requests
import os
import boto3


def make_request_service(endpoint):

    # Read in client ID and client secret from ssm parameter store
    ssm = boto3.client('ssm')
    client_id = ssm.get_parameter(Name='/apis/sand01/key/se/client-id', WithDecryption=True)['Parameter']['Value']
    client_secret = ssm.get_parameter(Name='/apis/sand01/key/se/client-secret', WithDecryption=True)['Parameter'][
        'Value']
    api_endpoint = endpoint

    # Get Access Token
    token_url = "https://service-providers-sand01.auth.us-east-1.amazoncognito.com/oauth2/token"
    token_data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(token_url, data=token_data)
    access_token = response.json()["access_token"]

    # Send request to Service Endpoint
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    request_body = {
        "application_open": {"VerityLeadId": 212121, "ExternalLeadId": "356f3724-edc2-41ff-b422-57d3b0b7bc26",
                             "Source": "VERITY", "School": "PKH College 2",
                             "EventType": "Student Registration Completed", "Version": "06152023",
                             "EventDateTime": "2023-06-16T17:00:13.4924145Z", "FirstName": "Bianka", "LastName": "Rowe",
                             "Email": "Ike52@yahoo.com", "Applications": [
                {"ApplicationId": "1a3b2159-311a-4c58-83aa-4548de3db20d", "School": "PKH College 2", "Status": "Open",
                 "StatusId": 1, "Program": "PKH 2 BA Business Admin", "ProgramId": "PKH 2 BA Business Admin",
                 "Campus": "PKH College 2 Online"}]},
        "application_completed": {

        }
    }

    response = requests.post(api_endpoint, headers=headers, json=request_body["application_open"])
    return response