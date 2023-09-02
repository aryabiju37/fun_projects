#import statements
import boto3
import schedule
from datetime import time

# create ec2 resource and instance name
ec2 = boto3.resource('ec2')
instance_name = 'test-ec2-ary'

# store instance id
instance_id = None


# Stop an instance 
def stop_instance(instances):
    for instance in instances:
        ec2.Instance(instance_id).stop()
        print(f"Instance '{instance_name}-{instance.id}' stopped.")

# Start an instance 
def start_instance(instances):
    for instance in instances:
        ec2.Instance(instance.id).start()
        print(f"Instance '{instance_name}-{instance.id}' started.")

#store all instances
instances = ec2.instances.all()
#start_instance(instances)


schedule.every().monday.at("09:00:00", "Europe/Lisbon").until(time(11,30,00)).do(start_instance(instances))
schedule.every().monday.at("11:31:00", "Europe/Lisbon").do(stop_instance(instances))


schedule.every().wednesday.at("09:00:00", "Europe/Lisbon").until(time(11,30,00)).do(start_instance(instances))
schedule.every().wednesday.at("11:31:00", "Europe/Lisbon").do(stop_instance(instances))


schedule.every().friday.at("09:00:00", "Europe/Lisbon").until(time(11,30,00)).do(start_instance(instances))
schedule.every().friday.at("11:31:00", "Europe/Lisbon").do(stop_instance(instances))


schedule.every().sunday.at("09:00:00", "Europe/Lisbon").until(time(11,30,00)).do(start_instance(instances))
schedule.every().sunday.at("11:31:00", "Europe/Lisbon").do(stop_instance(instances))

# Check if instance which you are trying to create already exists 
# and only work with an instance that hasn't been terminated
instance_exists = False
for instance in instances:
  
    for tag in instance.tags:
        if tag['Key'] == 'Name' and tag['Value'] == instance_name:
            instance_exists = True
            instance_id = instance.id
            print(f"An instance named '{instance_name}' with id '{instance_id}' already exists.")
            break
    if instance_exists:
        break


if not instance_exists:
    # Launch a new EC2 instance if it hasn't already been created
    new_instance = ec2.create_instances(
            ImageId='ami-06f621d90fa29f6d0',  # a valid AMI id from AWS Linux
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',
            KeyName='IN-south-1',  # create a key pair and keep the name here
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': instance_name
                        },
                        
                    ]
                },
            ]
    )
    instance_id = new_instance[0].id    
    print(f"Instance named '{instance_name}' with id '{instance_id}' created.")




while True:
    schedule.run_pending()
    time.sleep(1)