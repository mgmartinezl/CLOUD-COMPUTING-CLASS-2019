# Lab 6 answers

## Names: Sara Díaz - Gabriela Martinez


### Task 6.1: Bootstrap the creation of your web server

#### Q611. What happens when you use https://your-load-balancer-url instead of http://your-load-balancer-url ? Why does that happen? How could you fix it?

If we access the load balancer without the security protocol, we will see that our instance is running on AWS. But, if we do include the https protocol in the DNS of our instance, even though we still can access the content of the load balancer but we are warned about the lack of validity of our certificate. This is happening because we have not bought a SSL standard license from any valid provider (a Certificate Authority). The warning is shown below:

![WithHttps](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab6/https.png)

If we want to fix this issue we would have to contact a Certificate Authority that reviews our service and allows us securing it with a SSL protocol.


#### Q612. Stop all three EC2 instances and wait aprox. 5 minutes. What happens? Why?

We stoped the EC2 instances:

![WithHttps](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab6/stopped3instances.png)

The first thing that happened after this was that we received an AWS notification that alerted us about the state of the machine and also states that the auto-scaling group will be launched:

![WithHttps](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab6/launchMail.png)

As a result, 2 more machines started to run in the EC2 console. We also noted that the machines we stopped started to appeared as "terminated", so that only 2 machines are active and running:

![WithHttps](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab6/started2newmachines.png)

![WithHttps](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab6/terminatedWhenStopped.png)


#### Q613. Terminate all three EC2 instances and wait aprox. 5 minutes. What happens? Why?

We terminated the EC2 instances:

![WithHttps](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab6/terminate3instances.png)

As a results, all the machines were terminated:

![WithHttps](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab6/instancesTerminating.png)

Again, we received a notification stating the launch of the auto-scaling group and therefore, two new machines were created and running:

![WithHttps](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab6/newInstancesLaunching.png)


#### Q614. How are you going to end this section regarding the use of AWS resources?

For this lab exercise, we used the micro EC2 instance that is eligible for free trier. Therefore, we do not have associated costs to the usage of this lab. However, for the past sessions we experienced some low charges due to the usage of the nano EC2 instances. Information about billing can be seen as follows:

![WithHttps](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab6/costs.png)

#### Q615. Create a piece of code (Python or bash) to reproduce the above steps required to launch a new set of web servers with a load balancer. Start using the AMI that you have already created.

```
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
                                     {'Key': 'Cost-center', 'Value': 'laboratory'}])

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
                                      TopicARN=TopicARN)
                                      
```                                      

### Task 6.2: Serverless example

#### Q621. What is the list of events that the above URL triggers? 

The URL is not showing the result of any event because we have not defined the "test" event. However, if we change the URL so that it contains the word "default" instead of "test", the API allows in principle the execution of the GET event. However, in principle we can execute any event (GET, POST, PUT and DELETE) by configuring so.

#### Q622. Does the reply of the above URL match what it should be expected? Why?

Yes, as GET is the default event that the HTTP protocol manages. We would have to configure additional steps in order to explicitly able the triggering of the other events.

#### Q623. Explain what happens (actions and parts activated) when you type the URL in your browser to obtain the page updated with the shopping list.

1. Activate the S3 web server, which contains the index.html, the script.js and the styles.css. 
2. This server is calling an endpoint of the Gateway API through the javascript code. In this call, the parameter used is the table name "shopping-list".
3. The Gateway API executes the Lambda function, which executes the GET event by default and a POST when we insert a new element to the database.
4. The Lambda function calls the DynamoDB table we have created.
5. The URL shows the GET output for the "shopping-list" table.

#### Q624. Explain what happens (actions and parts activated) when you type a new item in the New Thing box.

1. Activate the S3 web server, which contains the index.html, the script.js and the styles.css. 
2. This server is calling an endpoint of the Gateway API through the javascript code. In this call, the parameter used is the table name "shopping-list".
3. The Gateway API executes the Lambda function, which executes the POST event to insert a new element to the Dynamo table.

#### Q625. Have you been able to debug the code of the Lambda function? If the answer is yes, check that you are using the root API keys. Erase such keys and create a new testing user with the required permissions.

We debugged the lambda function with the root user:

![RootUser](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab6/nImg/executionRootKeys.png)

Afterward, we created another test user with a single permission to change passwords, so we could try the debugging again:

![testUser](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab6/nImg/testUserNoPermissions.png)

Later on, we tried to run the code with the keys related to that user, but we got an error:

![ErrorTestUser](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab6/nImg/ExecutionUserNoPermission.png)

Therefore, we needed to grant the necessary permission to this test role: **Microservice execution role**. We also added the permission **LambdaBasicExecutionRole**:

![Permissions](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab6/nImg/permissionsNeeded.png)

As a result, we were able to execute the code with the test user:

![SuccessfulTestUser](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab6/nImg/ExecutionAddedRedApples.png)

![SuccessfulTestUser2](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab6/nImg/ExecutionAddedRedApples2.png)

Note that the item "Red apples2" was added to our wishlist under the test user domain.

#### Q626. What are the minimum permissions that the user's API keys needs to execute the Lambda function locally?

We granted the **MicroserviceExecutionEole** to the test user. With this single permission we were able to run the application. However, we also added the permission **LambdaBasicExecutionRole** that we used in a previous lab session.

#### Q627. Create a piece of code (Python or bash) to reproduce the above steps required to launch a new AWS Lambda function and AWS API gateway.

*Launching a new Lambda function*<br/>
Step 0: install/update python virtual environment
```
sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip3 install virtualenv
```

Step 1: create virtual environment directory
```
mkdir -p serverless-use-cases/groceries/app
cd serverless-use-cases/groceries/app
```

Step 2: create and activate virtual environment
```
virtualenv -p python3 venv
. venv/bin/activate
```

Step 3: install and configure serverless framework
```
sudo npm install -g serverless
serverless config credentials --provider aws --key <ACCESS KEY ID> --secret <SECRET KEY>
```

Use the desired profile to deploy serverless framework:
```
serverless deploy --aws-profile serverless
```

Or export the profile and other environment variables direclty with:
```
export AWS_PROFILE="serverless" && export AWS_REGION=eu-west-1
```

Step 4: initialize project by creating a handler that will set up the behavior of our app. 
```
serverless create --template aws-python3 --path myLambdaFunction
```
We also need to define a handler file. In our case, the lambda function that has already been defined as handler.py will be ok for this purpose and will be replaces in the "myService" path. Note that for this particular case we are using the **aws-python3** template. However, many others can be used such as *ruby or nodejs*.

Step 5: deploy the project
```
export AWS_PROFILE="serverless"
serverless deploy
```
Step 6: adding events

*Launching AWS API Gateway*<br/>
Up to this point, we have defined our own lambda function but we have not defined a way to trigger it from a request or an API. To do so, we need to define a new **event**. 

Our serverless.yml file created in step 4 will have the following structure:

```
provider:
  name: aws
  runtime: python3.6
functions:
    handler: PathToMyLambdaFunction
```

In the *functions* part we have to define the new events we want to trigger through the handler. For instance, if we want to trigger the GET event, we add the following:

```
provider:
  name: aws
  runtime: python3.6
functions:
    handler: PathToMyLambdaFunction
    events:
      - http:
          path:  https://YOUR-API-HOST/test/serverless-controller?TableName=shopping-list
          method: get
```

In general, we have the following options available to define events (this includes the enabling of CORS):
```
events: # The Events that trigger this Function
      - http: # This creates an API Gateway HTTP endpoint which can be used to trigger this function.  Learn more in "events/apigateway"
          path: users/create # Path for this endpoint
          method: get # HTTP method for this endpoint
          cors: true # Turn on CORS for this endpoint, but don't forget to return the right header in your response
          private: true # Requires clients to add API keys values in the `x-api-key` header of their request
          authorizer: # An AWS API Gateway custom authorizer function
            name: authorizerFunc # The name of the authorizer function (must be in this service)
            arn:  xxx:xxx:Lambda-Name # Can be used instead of name to reference a function outside of service
            resultTtlInSeconds: 0
            identitySource: method.request.header.Authorization
            identityValidationExpression: someRegex
            type: token # token or request. Determines input to the authorier function, called with the auth token or the entire request event. Defaults to token
      - websocket:
       route: $connect
          authorizer:
            # name: auth    NOTE: you can either use "name" or arn" properties
            arn: arn:aws:lambda:us-east-1:1234567890:function:auth
            identitySource:
              - 'route.request.header.Auth'
              - 'route.request.querystring.Auth'
      - s3:
          bucket: photos
          event: s3:ObjectCreated:*
          rules:
            - prefix: uploads/
            - suffix: .jpg
      - schedule:
          name: my scheduled event
          description: a description of my scheduled event's purpose
          rate: rate(10 minutes)
          enabled: false
```
More information about this parameters at: https://serverless.com/framework/docs/providers/aws/guide/serverless.yml/

Step 7: redeploy the project
```
serverless deploy -v
```

As a result, we will get a new service endpoint: CHANGE THIS FOR OUR OWN URL
```
ServiceEndpoint: https://x7o0xwsbkd.execute-api.us-east-1.amazonaws.com/dev
```

Step 8: test our app CHANGE THIS FOR OUR OWN URL
```
curl -X GET https://x7o0xwsbkd.execute-api.us-east-1.amazonaws.com/dev/hello
```
Finally, we have gotten the result of the GET event as follows:
PASTE IT HERE!!
