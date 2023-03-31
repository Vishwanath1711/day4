## Instructions for Creating an EC2 Instance

Try checking whether any instances are running or not, by clicking on the EC2 Service. You will get a list of instances which are running if any are in a running state, otherwise, you will get instances running zero.

Choose the region which is nearer to you to achieve low latency.

Following are the steps to be followed:

- 1: Click on Launch Instance or go to instances and click Launch Instance.
- 2: Once you click on Launch Instance, you need to
    * Enter the basic details like the name of the Instance.
    * Choose AMI, which specifies the configuration like which Operating System and which software you are going to install on EC2 Instance (leave it as default which is Amazon Linux).
    * Choose Instance type which refers to specifying what are the hardwares we need like each contains different types of memory, CPU, etc (Choose the default one which is t2 micro).
    * Choose KeyPair which is to specify the way you can connect these instances.
    * Create a new keypair if you don't have.
- 3: Configure the network settings
    * Create a Security group which is to specify the control of what traffic is allowed into your instance and what traffic can be going out from your EC2 instance.
    * Create a new Security group and allow SSH traffic from anywhere.
    * Configure the storage that needs to be attached to EC2 Instance (select defaults).
- 4: Once verified, then go ahead with launch instance and once done, check the     instance state it should be running.
- 5: Start connecting to the EC2 instance by clicking connect and execute a few     commands against it.
    Once you say connect, a new tab will open up and start typing the commands for checking the installed software or installing new software that you require.
- 6: You can see all the details of the instance running like:
    * The Instance ID which refers to the instance uniquely.
    * The type of access like private or public and instance type.
    * The number of operations performed on the instance like stop, reboot, terminate, or restart.
    * The AMI details and KeyPair details.
    * The Security group details like VPC and subnets.
    * If you go to monitoring, you can look at all the metrics related to our EC2 instance.
- 7: Add Tags which are like different environments for different resources.
- 8: Finally, you can terminate the instance by the terminate option. It is best    practice to terminate the instance after use.
