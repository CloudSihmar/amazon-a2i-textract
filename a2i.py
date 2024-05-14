import boto3

textract = boto3.client('textract', region_name='us-east-1')

response = textract.analyze_document(
    Document={
        'S3Object': {
            'Bucket': 'sandeep-ai-new',
            'Name': 'sample-document-final.png'
        }
    },
    FeatureTypes=["TABLES", "FORMS"],
    HumanLoopConfig={
        'FlowDefinitionArn': 'arn:aws:sagemaker:us-east-1:685421549691:flow-definition/textract',
        'HumanLoopName': 'sandeep-human-loop1',
        'DataAttributes': {'ContentClassifiers': ['FreeOfPersonallyIdentifiableInformation', 'FreeOfAdultContent']}
    }
)

print(response)
