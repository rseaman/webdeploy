#!/usr/bin/env python

import boto.cloudformation
import requests
import time
import sys

# Create stack
# -Create AWS connection
cf = boto.cloudformation.connect_to_region('us-east-1')

# -Pull template data from web.json file
with open('web.json', 'r') as f:
    webTemplate = f.read()

# -Validate template data
cf.validate_template(webTemplate)

cf.create_stack('Web1', template_body=webTemplate)


# Test infrastructure
# -Keep checking for Stack CREATE_COMPLETE event.
stackDoneStr = 'StackEvent AWS::CloudFormation::Stack Web1 CREATE_COMPLETE'
lastStackEvent = str(cf.describe_stack_events('Web1')[0])
while lastStackEvent != stackDoneStr:
    sys.stdout.write("Waiting for Stack to deploy...\r")
    sys.stdout.flush()
    time.sleep(5)

    # Update for comparison on next loop
    lastStackEvent = str(cf.describe_stack_events('Web1')[0])



# -Get instance public IP
for i in cf.describe_stack_resources('Web1'):
    if repr(i) == "StackResource:EIP1 (AWS::EC2::EIP)":
        ip = i.physical_resource_id

# -Send web request
validHtml = "<html><body>Automation for the People</body></html>"
counter = 0
while True:
    try:
        req = requests.get("http://" + ip).text
        if req == validHtml:
            # Site has come online.
            print "\nTest 1: Website Online"
            break
        else:
            # Responding but not expected data.
            print "\nTest 1: FAILED - UNEXPECTED RESPONSE - Please delete 'Web1' stack and redeploy"
            print "Response text: ", req
            break
    except requests.exceptions.ConnectionError as e:
        # Wait for a maxiumum of 5 minutes for system to come online.
        if counter >= 100:
            print "Test 1: FAILED - SITE NOT RESPONDING - Please delete 'Web1' stack and redeploy"
            break
        sys.stdout.write("Waiting for site to respond...\r")
        sys.stdout.flush()
        time.sleep(5)
        counter += 1
