#!/usr/bin/env python
from cdktf_cdktf_provider_aws.vpc import Vpc
from constructs import Construct
from cdktf import App, TerraformStack
from cdktf_cdktf_provider_aws.provider import AwsProvider
from variables import ProjectVariables


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # define resources here
        # Creating an instance of the variables class and adding the AWS provider
        vars = ProjectVariables(self, "main")
        AwsProvider(self, "aws",
                    region=vars.region)

        # Adding instances of the VPC, Security Group and EC2 Instance
        cdktf_vpc = Vpc(self, "cdktf_vpc",
                        name="jason_tf_vpc",
                        cidr=vars.cidr_vpc,
                        public_subnets=vars.pub_sub,
                        private_subnets=vars.priv_sub,
                        azs=vars.azs,
                        instance_tenancy="default",
                        enable_nat_gateway=True,
                        tags={"Name": "cdktf-vpc-tag"}
                        )


app = App()
MyStack(app, "Terraform_CDK_Lab_Folio_2")

app.synth()
