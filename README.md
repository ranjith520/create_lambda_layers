# AWS Lambda Layer Creator

This project provides tools to create AWS Lambda layers using a combination of a shell script and a Python script. The Lambda layer created will include the latest versions of Python packages, managed through a virtual environment.

## Prerequisites

Before running the script, ensure you have the following installed on your system:

- Python 3.x
- `pip`
- `virtualenv`
- AWS CLI (configured with the necessary permissions to manage Lambda layers)

### Installing Virtualenv

If `virtualenv` is not installed, you can install it using pip:

```bash
pip install virtualenv

### Steps to create Lambda Layers
Update the requiremnts.txt file to create required lambda layer packages .

```bash
sh run_me_to_generate_aws_lambda_layers.sh
