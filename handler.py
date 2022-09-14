import sys

sys.path.insert(0, 'vendor')
import boto3

def stop(event, context):
    ec2 = boto3.resource('ec2',
        aws_access_key_id="<ACCESS_KEY>",
        aws_secret_access_key="<SECRET_KEY>",
    )
    filters = [
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]

    instances_count = 0
    stopped_instances_count = 0

    for instance in ec2.instances.filter(Filters=filters):
        instances_count += 1
        try:
            instance.stop()
            stopped_instances_count += 1
        except:
            pass
    
    return {
        "status": 200,
        "running_instances": instances_count,
        "stopped_instances": stopped_instances_count,
    }
