from behave import *
from pytest_bdd import *
from api_call import make_request_service
from lambda_function import lambda_handler
from time import sleep

@given('if a service provide the gateway api end-point')
def given_gateway(context, endpoint):
    context.endpoint = endpoint

@when(u'send a POST request')
def when_test(context):
    response = make_request_service(context.endpoint, )
    context.response = response

@when(u'wait for a min')
def when_wait(context):
    sleep(10)

    sleep(10)

    sleep(10)

@when(u'Check DynamoDB for api calls')
def when_check(context):
    response1 = lambda_handler(event, context)


@then(u'report if it success or not')
def then_report(context):
    if response == response2:
        print("DynamoDB value is the same")
    else:
        print("DynamoDB value is not the same")