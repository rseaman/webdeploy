# Setup
## Requirements
- Python
- pip
- Environment variables with AWS Access Key that has permissions to create all resources in the CloudFormation template.
-- AWS_ACCESS_KEY_ID - Your AWS Access Key ID
-- AWS_SECRET_ACCESS_KEY - Your AWS Secret Access Key
- Compatible with Linux and Mac

## Installation
Download the files in this repository into their own folder and run "pip install" to download dependencies.

## Deployment
Open a terminal session
'cd' to the directory where these files are located
Run "python deploy.py"
The script will wait for deploy to complete and verify that the site is online