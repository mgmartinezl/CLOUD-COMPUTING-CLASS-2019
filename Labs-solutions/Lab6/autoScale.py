import boto3
import environ
#from boto.ec2.autoscale import LaunchConfiguration, AutoScalingGroup, ScalingPolicy

region_name = 'eu-west-1'

#Connection
env = environ.Env.read_env() # reading .env file
conn = boto3.client('ec2', region_name, aws_access_key_id = env('AWS_ACCESS_KEY_ID'),
                    aws_secret_access_key = env('AWS_SECRET_ACCESS_KEY'))

#Launch config

conn.create_launch_configuration(name='web-server-auto-scaling-group2', image_id='ami-05dc3a6ca9ac9f167',
                                 key_name='keyLab6',
                                 security_groups=['sg-0f0031ab70c065715'], instance_type='t2.micro')


#AutoScaling group

#Create autoscaling group
response = conn.create_auto_scaling_group(AutoScalingGroupName='web-server-auto-scaling-group2',
                      availability_zones=['eu-west-1a', 'eu-west-1b'],
                      HealthCheckGracePeriod=120,
                      HealthCheckType='ELB',
                      launch_config=lc,
                      min_size=2, max_size=2,
                      TargetGroupARNs=['arn:aws:elasticloadbalancing:eu-west-1:424471540912:'
                                       'targetgroup/primary-apache-web-server-target/b88b457f42520bdf'])

print (response)


#Attach targets
#response = conn.attach_load_balancer_target_groups(
    #AutoScalingGroupName='web-server-auto-scaling-group2',






