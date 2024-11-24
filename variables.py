from constructs import Construct


class ProjectVariables(Construct):
    def __init__(self, scope, name):
        super().__init__(scope, name)

        self.region = "us-east-1"
        self.cidr_vpc = "10.0.0.0/16"
        self.pub_sub = ["10.0.1.0/24"]
        self.priv_sub = ["10.0.4.0/24"]
        self.azs = ["us-east-1a"]
