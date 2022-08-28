#!/usr/bin/env python3

import boto3

AWS_REGION = "us-east-2"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_ID = 'i-04091b10d2cdc86aa'

instance = EC2_RESOURCE.Instance(INSTANCE_ID)

instance.stop()
instance.wait_until_stopped()

instance.modify_attribute(
    InstanceType={
        'Value': 't2.small'
    }
)

instance.start()
instance.wait_until_running()

print(f'Instance type has been successfully changed')
