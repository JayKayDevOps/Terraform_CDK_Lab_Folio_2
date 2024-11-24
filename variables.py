# Variables class to store all the VPC and EC2 Instance variables
from constructs import Construct


class ProjectVariables(Construct):
    def __init__(self, scope, name):
        super().__init__(scope, name)

        self.region = "us-east-1"
        self.cidr_vpc = "10.0.0.0/16"
        self.pub_sub = ["10.0.1.0/24"]
        self.priv_sub = ["10.0.4.0/24"]
        self.azs = ["us-east-1a"]
        self.ami = "ami-0866a3c8686eaeeba"
        self.instance_type = "t2.micro"
        self.key_name = "testKey"
