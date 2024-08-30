import sys
import boto3

if len(sys.argv) != 2:
    print("Usage: python3 packages.py <layer_name>")
    sys.exit(1)

layer_name = sys.argv[1]
description = 'Layer with the latest boto3 version.'
zip_file_path = 'latest-sdk-layer/latest-sdk-layer.zip'
compatible_runtimes = ['python3.12']

lambda_client = boto3.client('lambda', region_name='us-east-1')

def publish_lambda_layer(layer_name, description, zip_file_path, compatible_runtimes):
    with open(zip_file_path, 'rb') as f:
        response = lambda_client.publish_layer_version(
            LayerName=layer_name,
            Description=description,
            Content={
                'ZipFile': f.read(),
            },
            CompatibleRuntimes=compatible_runtimes
        )
    return response['LayerVersionArn']

layer_version_arn = publish_lambda_layer(layer_name, description, zip_file_path, compatible_runtimes)
print("Layer version ARN:", layer_version_arn)
