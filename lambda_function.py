import json
import boto3
from news import main

some_list_of_contacts = [PhoneNumber]

message = main()
client = boto3.client("sns",
    aws_access_key_id="ACCES_KEY",
    aws_secret_access_key="SECRET_KEY",
    region_name="us-east-1"
)

# Create the topic if it doesn't exist (this is idempotent)
topic = client.create_topic(Name="notifications")
topic_arn = topic['TopicArn']  # get its Amazon Resource Name

# Add SMS Subscribers
for number in some_list_of_contacts:
    client.subscribe(
        TopicArn=topic_arn,
        Protocol='sms',
        Endpoint=PhoneNumber  # <-- number who'll receive an SMS message.
    )

# Publish a message.
response = client.publish(
    TopicArn=topic_arn,
    MessageStructure='json'
)