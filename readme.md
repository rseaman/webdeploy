# Setup
## Requirements
- Python
- pip
- virtualenv
- Compatible with Linux and Mac

## Installation
Create a virtualenv environment in a folder named 'webdeploy' with "virtualenv webdeploy"

'cd' to the 'webdeploy' directory

Run 'source bin/activate'

Export Environment variables with AWS Access Key that has permissions to create all resources in the CloudFormation template.
- AWS_ACCESS_KEY_ID - Your AWS Access Key ID
- AWS_SECRET_ACCESS_KEY - Your AWS Secret Access Key

ex: 'export AWS_ACCESS_KEY_ID=ABCDEFG1234567'

Download the files in this repository into their own subfolder and run "pip install -r requirements.txt" to download dependencies.

## Deployment
'cd' to the directory where these files are located

Run "python deploy.py"

The script will wait for deploy to complete and verify that the site is online by checking the HTML returned from a GET request at the IP address of the web instance.