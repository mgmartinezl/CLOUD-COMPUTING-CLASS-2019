# Lab 4 answers

## Names: Sara Díaz - Gabriela Martinez

### Q45b: What has happened? Why do you think that has happened? Check both EC2 and EB consoles.
The first thing we did was terminating the EC2 instance that was being used for the deployment of the application. After a couple of minutes, the EC2 console showed that the instance was "terminated". However, the EB console was still showing as "Healthy" the environment we had to host our app, as can be seen in the following images:

#### Terminating EC2 instance:

![TerminateEC2](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab4/instanceterminatedEC2console.png)

#### EB console logging info showing that instance was terminated:

![TerminateEB](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab4/EBconsoleinstanceterminated.png)

#### EB created another instance for us:

![CreateNewEB](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab4/EBaddsnewinstance.png)

#### Finally, this new instance can be visualized from the EC2 console:

![NewInstanceEC2](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab4/newinstanceEC2console.png)

The previous happened because the EC2 console created automatically another EC2 instance to replace the one that we shuted down. This way, the service was still available in the cloud and the "failure" of our first EC2 instance was transparently corrected.

Also, note that EB created another EC2 instance because we have already set this option in the autoscaling and modify capacity tab within the EB console:

![Capacity](https://github.com/mgmartinezl/CLOUD-COMPUTING-CLASS-2019/blob/master/Labs-solutions/Lab4/ebCapacity.png)

### Q45c: Can you terminate the application using the command line? What is the command? if it exists.

### Q45d: What parameters have you added to the eb create command to create your environment? Explain why you have selected each parameter.

### Q46: How long have you been working on this session? What have been the main difficulties you have faced and how have you solved them? Add your answers to README.md.
