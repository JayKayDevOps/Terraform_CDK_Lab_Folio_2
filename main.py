#!/usr/bin/env python
from cdktf_cdktf_provider_aws.instance import Instance
from cdktf_cdktf_provider_aws.security_group import SecurityGroup
from cdktf_cdktf_provider_aws.vpc_security_group_egress_rule import VpcSecurityGroupEgressRule
from cdktf_cdktf_provider_aws.vpc_security_group_ingress_rule import VpcSecurityGroupIngressRule
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from cdktf_cdktf_provider_aws.provider import AwsProvider
from variables import ProjectVariables
from imports.vpc import Vpc
from cdktf import Token, Fn


class LabFolio2Stack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # define resources here
        # Creating an instance of the variables class and adding the AWS provider
        vars = ProjectVariables(self, "main")
        AwsProvider(self, "aws",
                    region=vars.region
                    )

        # Adding instances of the VPC, Security Group and EC2 Instance
        # VPC Instance with cidr, public and private subnets and availability zones (azs)
        cdktf_vpc = Vpc(self, "cdktf_vpc",
                        name="jason_tf_vpc",
                        cidr=vars.cidr_vpc,
                        public_subnets=vars.pub_sub,
                        private_subnets=vars.priv_sub,
                        azs=vars.azs,
                        instance_tenancy="default",
                        )

        # Security Group with Ingress and Egress rules
        cdktf_security_group = SecurityGroup(self, "stack_sg",
                                             vpc_id=Token().as_string(cdktf_vpc.vpc_id_output),
                                             name="cdktf-sg",
                                             tags={"Name": "cdktf-sg-tag"}
                                             )

        # Ingress rule to allow incoming http and ssh traffic from anywhere on port 80
        VpcSecurityGroupIngressRule(self, "stack_sg_ingress",
                                    ip_protocol="TCP",
                                    from_port=22,
                                    to_port=22,
                                    cidr_ipv4="0.0.0.0/0",
                                    security_group_id=cdktf_security_group.id
                                    )

        # Egress rule to allow traffic out to anywhere
        VpcSecurityGroupEgressRule(self, "stack_sg_egress",
                                   ip_protocol="-1",
                                   cidr_ipv4="0.0.0.0/0",
                                   security_group_id=cdktf_security_group.id
                                   )

        # Adding the EC2 Instance and assigning it to the above VPC and Security Group
        cdktf_instance = Instance(self, "jason-cdk-instance",
                                  ami=vars.ami,
                                  instance_type=vars.instance_type,
                                  key_name=vars.key_name,
                                  vpc_security_group_ids=[cdktf_security_group.id],
                                  associate_public_ip_address=True,
                                  subnet_id=Fn.element(Token.as_list(cdktf_vpc.public_subnets_output), 0),
                                  tags={"Name": "cdktf-instance"}
                                  )

        # Generates an output at the end of the deployment showing the ID of the VPC
        TerraformOutput(self, "vpc",
                        value=cdktf_vpc.vpc_id_output)

        # Generates an output at the end of the deployment showing the ID of the EC2 Instance
        TerraformOutput(self, "ec2_instance",
                        value=cdktf_instance.id)

        # Generates an output at the end of the deployment showing the ID of the Security Group
        TerraformOutput(self, "security_group",
                        value=cdktf_security_group.id)


app = App()
LabFolio2Stack(app, "Terraform_CDK_Lab_Folio_2")

app.synth()
