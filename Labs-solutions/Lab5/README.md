# Lab 5 answers

## Names: Sara Díaz - Gabriela Martinez

### Task 5.1: Use AWS Simple Notification Service in your web app

#### Q51: Has everything gone alright?
As according to the following image, we were able to deploy our app in the Elastic Beanstalk environment by changing the JSON of the policy we had associated to the IAM profile, in which we granted access to it.

![IAMPolicySucceeded](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab5/deployAppagain.png)

See that we received correctly one notification we generated intendedly:

![IAMPolicySucceeded](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab5/emailArrived.png)

### Task 5.2: Create a new option to retrieve the list of leads

#### Q52: Has everything gone alright? What have you changed?
We got to retrieve the list of leads successfully in the EB environment, as can be seen here:

![DeployLeadsWorking](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab5/deploymentWorking.png)

For this to work, we had to change the IAM policy again so this profile could be granted access to Scan the Dynamo table. To do so, we added the following to the JSON policy:

![JSONChanges](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab5/changePolicy.png)

### Task 5.3: Improve the web app transfer of information (optional)

#### Q53: Describe the strategy used to fulfill the requirements of this section. What have you changed in the code and the configuration of the different resources used by the web app? What are the tradeoffs of your solution?
PENDING

### Task 5.4: Deliver static content using a Content Delivery Network

The custom css template generated this look and feel:

![CustomCSS](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab5/niceInterface.png)

#### Q54: Take a couple of screenshots of you S3 and CloudFront consoles to demonstrate that everything worked all right. Commit the changes on your web app, deploy them on Elastic beanstalk and check that it also works fine from there: use Google Chrome and check the origin of the files that you are loading.

The CloudFront console was successfully set and the results we got are as follows:

![CloudFrontWorking](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab5/cloudFrontworking.png)

#### Q55: How long have you been working on this session (including the optional part)? What have been the main difficulties that you have faced and how have you solved them?

We have been working on this session approximately 6 hours (including the 2 hours from the practical session). Our main difficulty was related to the understanding of the get_leads() method.

