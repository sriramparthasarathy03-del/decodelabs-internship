import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Interns')

response = table.scan()

print("Intern Records")

for item in response['Items']:
    print(item)
