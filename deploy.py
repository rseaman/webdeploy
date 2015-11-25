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
if requests.get("http://" + ip).text == validHtml:
    print "Test 1: Website Online"
else:
    print "Test 1: FAILED - ERROR OCCURRED - Please delete 'Web1' stack and redeploy"
