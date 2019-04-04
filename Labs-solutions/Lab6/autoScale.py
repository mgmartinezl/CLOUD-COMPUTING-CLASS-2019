import boto3
import os

# Initial variables
region_name = 'eu-west-1'
LaunchConfigurationName = 'launch_configuration'
AutoScalingGroupName = 'web-server-auto-scaling-group2'
TopicARN = 'arn:aws:sns:eu-west-1:424471540912:gsg-signup-notifications'

# Connection to client - remember to add environment variables
client = boto3.client('autoscaling', region_name, aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                      aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])

# Create launch configuration
client.create_launch_configuration(LaunchConfigurationName=LaunchConfigurationName,
                                   ImageId='ami-05dc3a6ca9ac9f167',
                                   KeyName='keyLab6',
                                   SecurityGroups=['sg-0f0031ab70c065715'],
                                   InstanceType='t2.micro')

# Create autoscaling group
client.create_auto_scaling_group(AutoScalingGroupName=AutoScalingGroupName,
                                 AvailabilityZones=['eu-west-1a', 'eu-west-1b'],
                                 LaunchConfigurationName=LaunchConfigurationName,
                                 MinSize=2,
                                 MaxSize=2,
                                 TargetGroupARNs=['arn:aws:elasticloadbalancing:eu-west-1:424471540912:'
                                                  'targetgroup/primary-apache-web-server-target/b88b457f42520bdf'],
                                 VPCZoneIdentifier='subnet-5345ec09,subnet-e3e19eab',
                                 HealthCheckGracePeriod=300,
                                 HealthCheckType='ELB',
                                 Tags=[
                                     {'Key': 'Project', 'Value': 'ccbda bootstrap'},
                                     {'Key': 'Cost-center', 'Value': 'laboratory'}]
                                 )

# Add scaling policy
client.put_scaling_policy(AutoScalingGroupName=AutoScalingGroupName,
                          PolicyName='Scale Group Size',
                          PolicyType='TargetTrackingScaling',
                          TargetTrackingConfiguration={
                              'PredefinedMetricSpecification': {
                                  'PredefinedMetricType': 'ASGAverageCPUUtilization'},
                              'TargetValue': 80})

# Add notification via SNS Topic
client.put_notification_configuration(AutoScalingGroupName=AutoScalingGroupName,
                                      NotificationTypes=[
                                          'autoscaling:EC2_INSTANCE_LAUNCH',
                                          'autoscaling:EC2_INSTANCE_LAUNCH_ERROR',
                                          'autoscaling:EC2_INSTANCE_TERMINATE',
                                          'autoscaling:EC2_INSTANCE_TERMINATE_ERROR',
                                          'autoscaling:TEST_NOTIFICATION'],
                                      TopicARN=TopicARN
                                      )
