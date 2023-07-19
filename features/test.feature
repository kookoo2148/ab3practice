Feature: api test case
    Scenario: Verify if DynamoDB accept api calls
        Given if a service provide the gateway api end-point
        When send a POST request
        And wait for a min
        And Check DynamoDB for api call
        Then report if it success or not