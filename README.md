## Step by Step Instructions for Creating an EC2 Instance

Try checking whether any instances are running or not, by clicking on the EC2 Servie. You will get a list of instances which are running if any are in running state otherwise Yuo will get instances running zero.

Choose the region which is nearer to you to achieve high latency.

Following are the steps to be followed:

1: Click on Launch Instance or go to insatnces and click Launch Instacne.
2: Once you click on Launch Instance, you need to 
    - Enter the basic details like name of Instance.
    - Choose AMI, AMI is specifying the configuration like which Operating System and which softwares you are going to install on EC2 Instance(leave it as default which is Amazon Linux).
    * Choose Instance type which refers to specifying what are the hardwares we need like each contains different types of memory, CPU etc(Choose the default one which is t2 micro).
    * Choose KeyPair which is to specify the way you can connect these instances.
    create a new keypair if you don't have.
3: Configure the network settings
    * create a Security group which is to specify the control what traffic is allowed into your instance and what traffic can be going out from your EC2 instance.
    * create a new Secutity group and allow SSH traffic from anywhere.
    * configure the storage that need to be attached to EC2 Instance(select defaults).
4: Once verify then go ahead with launch instance and once done, check the instance state it should be running.
5: Start connecting EC2 instance by clicking connect and execute few commands against it.
    once you say connect, new tab will open up ans start typing the commands for cheking the installed softwares or installing new software which you require.
6: You can see all the details of the instance running like:
    * The Instance ID which refers the instance uniquely.
    * The type of access like private or public and instnce type.
    * The number of Operations performed on the instance like stop, reboot, terminate or restart.
    * The AMI details and KeyPair details.
    * The Security group details like VPC and subnets.
    * If you go to monitoring, you can look at all the metrics related to our EC2 instance.
7: Add Tags which are like different environment for different resources.
8: Finally, you can Terminate the instance by terminate option. it is best practice to terminate the instance after use.
