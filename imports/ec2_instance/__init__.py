from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class Ec2Instance(
    _cdktf_9a9027ec.TerraformModule,
    metaclass=jsii.JSIIMeta,
    jsii_type="ec2-instance.Ec2Instance",
):
    '''Defines an Ec2Instance based on a Terraform module.

    Docs at Terraform Registry: {@link https://registry.terraform.io/modules/terraform-aws-modules/ec2-instance/aws/latest terraform-aws-modules/ec2-instance/aws}
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        ami: typing.Optional[builtins.str] = None,
        ami_ssm_parameter: typing.Optional[builtins.str] = None,
        associate_public_ip_address: typing.Optional[builtins.bool] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        capacity_reservation_specification: typing.Any = None,
        cpu_core_count: typing.Optional[jsii.Number] = None,
        cpu_credits: typing.Optional[builtins.str] = None,
        cpu_options: typing.Any = None,
        cpu_threads_per_core: typing.Optional[jsii.Number] = None,
        create: typing.Optional[builtins.bool] = None,
        create_eip: typing.Optional[builtins.bool] = None,
        create_iam_instance_profile: typing.Optional[builtins.bool] = None,
        create_spot_instance: typing.Optional[builtins.bool] = None,
        disable_api_stop: typing.Optional[builtins.bool] = None,
        disable_api_termination: typing.Optional[builtins.bool] = None,
        ebs_block_device: typing.Optional[typing.Sequence[typing.Any]] = None,
        ebs_optimized: typing.Optional[builtins.bool] = None,
        eip_domain: typing.Optional[builtins.str] = None,
        eip_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        enable_volume_tags: typing.Optional[builtins.bool] = None,
        enclave_options_enabled: typing.Optional[builtins.bool] = None,
        ephemeral_block_device: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        fetch_password_data: typing.Optional[builtins.bool] = None,
        hibernation: typing.Optional[builtins.bool] = None,
        host_id: typing.Optional[builtins.str] = None,
        iam_instance_profile: typing.Optional[builtins.str] = None,
        iam_role_description: typing.Optional[builtins.str] = None,
        iam_role_name: typing.Optional[builtins.str] = None,
        iam_role_path: typing.Optional[builtins.str] = None,
        iam_role_permissions_boundary: typing.Optional[builtins.str] = None,
        iam_role_policies: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        iam_role_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        iam_role_use_name_prefix: typing.Optional[builtins.bool] = None,
        ignore_ami_changes: typing.Optional[builtins.bool] = None,
        instance_initiated_shutdown_behavior: typing.Optional[builtins.str] = None,
        instance_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instance_type: typing.Optional[builtins.str] = None,
        ipv6_address_count: typing.Optional[jsii.Number] = None,
        ipv6_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        key_name: typing.Optional[builtins.str] = None,
        launch_template: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        maintenance_options: typing.Any = None,
        metadata_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        monitoring: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
        network_interface: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        placement_group: typing.Optional[builtins.str] = None,
        private_dns_name_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        private_ip: typing.Optional[builtins.str] = None,
        putin_khuylo: typing.Optional[builtins.bool] = None,
        root_block_device: typing.Optional[typing.Sequence[typing.Any]] = None,
        secondary_private_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_dest_check: typing.Optional[builtins.bool] = None,
        spot_block_duration_minutes: typing.Optional[jsii.Number] = None,
        spot_instance_interruption_behavior: typing.Optional[builtins.str] = None,
        spot_launch_group: typing.Optional[builtins.str] = None,
        spot_price: typing.Optional[builtins.str] = None,
        spot_type: typing.Optional[builtins.str] = None,
        spot_valid_from: typing.Optional[builtins.str] = None,
        spot_valid_until: typing.Optional[builtins.str] = None,
        spot_wait_for_fulfillment: typing.Optional[builtins.bool] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tenancy: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        user_data: typing.Optional[builtins.str] = None,
        user_data_base64: typing.Optional[builtins.str] = None,
        user_data_replace_on_change: typing.Optional[builtins.bool] = None,
        volume_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        providers: typing.Optional[typing.Sequence[typing.Union[_cdktf_9a9027ec.TerraformProvider, typing.Union[_cdktf_9a9027ec.TerraformModuleProvider, typing.Dict[builtins.str, typing.Any]]]]] = None,
        skip_asset_creation_from_local_modules: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param ami: ID of AMI to use for the instance.
        :param ami_ssm_parameter: SSM parameter name for the AMI ID. For Amazon Linux AMI SSM parameters see `reference <https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-public-parameters-ami.html>`_ /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
        :param associate_public_ip_address: Whether to associate a public IP address with an instance in a VPC.
        :param availability_zone: AZ to start the instance in.
        :param capacity_reservation_specification: Describes an instance's Capacity Reservation targeting option.
        :param cpu_core_count: Sets the number of CPU cores for an instance.
        :param cpu_credits: The credit option for CPU usage (unlimited or standard).
        :param cpu_options: Defines CPU options to apply to the instance at launch time.
        :param cpu_threads_per_core: Sets the number of CPU threads per core for an instance (has no effect unless cpu_core_count is also set).
        :param create: Whether to create an instance true.
        :param create_eip: Determines whether a public EIP will be created and associated with the instance.
        :param create_iam_instance_profile: Determines whether an IAM instance profile is created or to use an existing IAM instance profile.
        :param create_spot_instance: Depicts if the instance is a spot instance.
        :param disable_api_stop: If true, enables EC2 Instance Stop Protection.
        :param disable_api_termination: If true, enables EC2 Instance Termination Protection.
        :param ebs_block_device: Additional EBS block devices to attach to the instance.
        :param ebs_optimized: If true, the launched EC2 instance will be EBS-optimized.
        :param eip_domain: Indicates if this EIP is for use in VPC vpc.
        :param eip_tags: A map of additional tags to add to the eip The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param enable_volume_tags: Whether to enable volume tags (if enabled it conflicts with root_block_device tags) true.
        :param enclave_options_enabled: Whether Nitro Enclaves will be enabled on the instance. Defaults to ``false``
        :param ephemeral_block_device: Customize Ephemeral (also known as Instance Store) volumes on the instance. The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}
        :param fetch_password_data: If true, wait for password data to become available and retrieve it.
        :param hibernation: If true, the launched EC2 instance will support hibernation.
        :param host_id: ID of a dedicated host that the instance will be assigned to. Use when an instance is to be launched on a specific dedicated host
        :param iam_instance_profile: IAM Instance Profile to launch the instance with. Specified as the name of the Instance Profile
        :param iam_role_description: Description of the role.
        :param iam_role_name: Name to use on IAM role created.
        :param iam_role_path: IAM role path.
        :param iam_role_permissions_boundary: ARN of the policy that is used to set the permissions boundary for the IAM role.
        :param iam_role_policies: Policies attached to the IAM role The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param iam_role_tags: A map of additional tags to add to the IAM role/profile created The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param iam_role_use_name_prefix: Determines whether the IAM role name (``iam_role_name`` or ``name``) is used as a prefix true.
        :param ignore_ami_changes: Whether changes to the AMI ID changes should be ignored by Terraform. Note - changing this value will result in the replacement of the instance
        :param instance_initiated_shutdown_behavior: Shutdown behavior for the instance. Amazon defaults this to stop for EBS-backed instances and terminate for instance-store instances. Cannot be set on instance-store instance
        :param instance_tags: Additional tags for the instance The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param instance_type: The type of instance to start t3.micro.
        :param ipv6_address_count: A number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet
        :param ipv6_addresses: Specify one or more IPv6 addresses from the range of the subnet to associate with the primary network interface.
        :param key_name: Key name of the Key Pair to use for the instance; which can be managed using the ``aws_key_pair`` resource
        :param launch_template: Specifies a Launch Template to configure the instance. Parameters configured on this resource will override the corresponding parameters in the Launch Template The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}
        :param maintenance_options: The maintenance options for the instance.
        :param metadata_options: Customize the metadata options of the instance The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param monitoring: If true, the launched EC2 instance will have detailed monitoring enabled.
        :param name: Name to be used on EC2 instance created.
        :param network_interface: Customize network interfaces to be attached at instance boot time. The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}
        :param placement_group: The Placement Group to start the instance in.
        :param private_dns_name_options: Customize the private DNS name options of the instance The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param private_ip: Private IP address to associate with the instance in a VPC.
        :param putin_khuylo: Do you agree that Putin doesn't respect Ukrainian sovereignty and territorial integrity? More info: https://en.wikipedia.org/wiki/Putin_khuylo! true
        :param root_block_device: Customize details about the root block device of the instance. See Block Devices below for details
        :param secondary_private_ips: A list of secondary private IPv4 addresses to assign to the instance's primary network interface (eth0) in a VPC. Can only be assigned to the primary network interface (eth0) attached at instance creation, not a pre-existing network interface i.e. referenced in a ``network_interface block``
        :param source_dest_check: Controls if traffic is routed to the instance when the destination address does not match the instance. Used for NAT or VPNs
        :param spot_block_duration_minutes: The required duration for the Spot instances, in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360)
        :param spot_instance_interruption_behavior: Indicates Spot instance behavior when it is interrupted. Valid values are ``terminate``, ``stop``, or ``hibernate``
        :param spot_launch_group: A launch group is a group of spot instances that launch together and terminate together. If left empty instances are launched and terminated individually
        :param spot_price: The maximum price to request on the spot market. Defaults to on-demand price
        :param spot_type: If set to one-time, after the instance is terminated, the spot request will be closed. Default ``persistent``
        :param spot_valid_from: The start date and time of the request, in UTC RFC3339 format(for example, YYYY-MM-DDTHH:MM:SSZ).
        :param spot_valid_until: The end date and time of the request, in UTC RFC3339 format(for example, YYYY-MM-DDTHH:MM:SSZ).
        :param spot_wait_for_fulfillment: If set, Terraform will wait for the Spot Request to be fulfilled, and will throw an error if the timeout of 10m is reached.
        :param subnet_id: The VPC Subnet ID to launch in.
        :param tags: A mapping of tags to assign to the resource The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param tenancy: The tenancy of the instance (if the instance is running in a VPC). Available values: default, dedicated, host
        :param timeouts: Define maximum timeout for creating, updating, and deleting EC2 instance resources The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param user_data: The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see user_data_base64 instead
        :param user_data_base64: Can be used instead of user_data to pass base64-encoded binary data directly. Use this instead of user_data whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption
        :param user_data_replace_on_change: When used in combination with user_data or user_data_base64 will trigger a destroy and recreate when set to true. Defaults to false if not set
        :param volume_tags: A mapping of tags to assign to the devices created by the instance at launch time The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param vpc_security_group_ids: A list of security group IDs to associate with.
        :param depends_on: 
        :param for_each: 
        :param providers: 
        :param skip_asset_creation_from_local_modules: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c49908fc6353830b69e0c67909cdecbc95ff4bab4bc31e0fef6c3e7abff833d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = Ec2InstanceConfig(
            ami=ami,
            ami_ssm_parameter=ami_ssm_parameter,
            associate_public_ip_address=associate_public_ip_address,
            availability_zone=availability_zone,
            capacity_reservation_specification=capacity_reservation_specification,
            cpu_core_count=cpu_core_count,
            cpu_credits=cpu_credits,
            cpu_options=cpu_options,
            cpu_threads_per_core=cpu_threads_per_core,
            create=create,
            create_eip=create_eip,
            create_iam_instance_profile=create_iam_instance_profile,
            create_spot_instance=create_spot_instance,
            disable_api_stop=disable_api_stop,
            disable_api_termination=disable_api_termination,
            ebs_block_device=ebs_block_device,
            ebs_optimized=ebs_optimized,
            eip_domain=eip_domain,
            eip_tags=eip_tags,
            enable_volume_tags=enable_volume_tags,
            enclave_options_enabled=enclave_options_enabled,
            ephemeral_block_device=ephemeral_block_device,
            fetch_password_data=fetch_password_data,
            hibernation=hibernation,
            host_id=host_id,
            iam_instance_profile=iam_instance_profile,
            iam_role_description=iam_role_description,
            iam_role_name=iam_role_name,
            iam_role_path=iam_role_path,
            iam_role_permissions_boundary=iam_role_permissions_boundary,
            iam_role_policies=iam_role_policies,
            iam_role_tags=iam_role_tags,
            iam_role_use_name_prefix=iam_role_use_name_prefix,
            ignore_ami_changes=ignore_ami_changes,
            instance_initiated_shutdown_behavior=instance_initiated_shutdown_behavior,
            instance_tags=instance_tags,
            instance_type=instance_type,
            ipv6_address_count=ipv6_address_count,
            ipv6_addresses=ipv6_addresses,
            key_name=key_name,
            launch_template=launch_template,
            maintenance_options=maintenance_options,
            metadata_options=metadata_options,
            monitoring=monitoring,
            name=name,
            network_interface=network_interface,
            placement_group=placement_group,
            private_dns_name_options=private_dns_name_options,
            private_ip=private_ip,
            putin_khuylo=putin_khuylo,
            root_block_device=root_block_device,
            secondary_private_ips=secondary_private_ips,
            source_dest_check=source_dest_check,
            spot_block_duration_minutes=spot_block_duration_minutes,
            spot_instance_interruption_behavior=spot_instance_interruption_behavior,
            spot_launch_group=spot_launch_group,
            spot_price=spot_price,
            spot_type=spot_type,
            spot_valid_from=spot_valid_from,
            spot_valid_until=spot_valid_until,
            spot_wait_for_fulfillment=spot_wait_for_fulfillment,
            subnet_id=subnet_id,
            tags=tags,
            tenancy=tenancy,
            timeouts=timeouts,
            user_data=user_data,
            user_data_base64=user_data_base64,
            user_data_replace_on_change=user_data_replace_on_change,
            volume_tags=volume_tags,
            vpc_security_group_ids=vpc_security_group_ids,
            depends_on=depends_on,
            for_each=for_each,
            providers=providers,
            skip_asset_creation_from_local_modules=skip_asset_creation_from_local_modules,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="synthesizeHclAttributes")
    def _synthesize_hcl_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeHclAttributes", []))

    @builtins.property
    @jsii.member(jsii_name="amiOutput")
    def ami_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "amiOutput"))

    @builtins.property
    @jsii.member(jsii_name="arnOutput")
    def arn_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arnOutput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneOutput")
    def availability_zone_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityZoneOutput"))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationSpecificationOutput")
    def capacity_reservation_specification_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityReservationSpecificationOutput"))

    @builtins.property
    @jsii.member(jsii_name="ebsBlockDeviceOutput")
    def ebs_block_device_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ebsBlockDeviceOutput"))

    @builtins.property
    @jsii.member(jsii_name="ephemeralBlockDeviceOutput")
    def ephemeral_block_device_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ephemeralBlockDeviceOutput"))

    @builtins.property
    @jsii.member(jsii_name="iamInstanceProfileArnOutput")
    def iam_instance_profile_arn_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamInstanceProfileArnOutput"))

    @builtins.property
    @jsii.member(jsii_name="iamInstanceProfileIdOutput")
    def iam_instance_profile_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamInstanceProfileIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="iamInstanceProfileUniqueOutput")
    def iam_instance_profile_unique_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamInstanceProfileUniqueOutput"))

    @builtins.property
    @jsii.member(jsii_name="iamRoleArnOutput")
    def iam_role_arn_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamRoleArnOutput"))

    @builtins.property
    @jsii.member(jsii_name="iamRoleNameOutput")
    def iam_role_name_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamRoleNameOutput"))

    @builtins.property
    @jsii.member(jsii_name="iamRoleUniqueIdOutput")
    def iam_role_unique_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamRoleUniqueIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="idOutput")
    def id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "idOutput"))

    @builtins.property
    @jsii.member(jsii_name="instanceStateOutput")
    def instance_state_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceStateOutput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6AddressesOutput")
    def ipv6_addresses_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv6AddressesOutput"))

    @builtins.property
    @jsii.member(jsii_name="outpostArnOutput")
    def outpost_arn_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outpostArnOutput"))

    @builtins.property
    @jsii.member(jsii_name="passwordDataOutput")
    def password_data_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passwordDataOutput"))

    @builtins.property
    @jsii.member(jsii_name="primaryNetworkInterfaceIdOutput")
    def primary_network_interface_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryNetworkInterfaceIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="privateDnsOutput")
    def private_dns_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateDnsOutput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpOutput")
    def private_ip_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpOutput"))

    @builtins.property
    @jsii.member(jsii_name="publicDnsOutput")
    def public_dns_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicDnsOutput"))

    @builtins.property
    @jsii.member(jsii_name="publicIpOutput")
    def public_ip_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicIpOutput"))

    @builtins.property
    @jsii.member(jsii_name="rootBlockDeviceOutput")
    def root_block_device_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootBlockDeviceOutput"))

    @builtins.property
    @jsii.member(jsii_name="spotBidStatusOutput")
    def spot_bid_status_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spotBidStatusOutput"))

    @builtins.property
    @jsii.member(jsii_name="spotInstanceIdOutput")
    def spot_instance_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spotInstanceIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="spotRequestStateOutput")
    def spot_request_state_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "spotRequestStateOutput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllOutput")
    def tags_all_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagsAllOutput"))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationSpecification")
    def capacity_reservation_specification(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "capacityReservationSpecification"))

    @capacity_reservation_specification.setter
    def capacity_reservation_specification(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c8954bdbfc5a10444da1f10ec452da8973aceed6a45746b5b76c239eafa6d0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityReservationSpecification", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cpuOptions")
    def cpu_options(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "cpuOptions"))

    @cpu_options.setter
    def cpu_options(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebe30285e9c787842cc787c3e2e575ade1988ebc20c9d5fceffb3ff2a71be3ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuOptions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maintenanceOptions")
    def maintenance_options(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "maintenanceOptions"))

    @maintenance_options.setter
    def maintenance_options(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6de9a5c08d984067dcdc47954cf12282fd2bf98cca0d2277c87e4213523880c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceOptions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ami")
    def ami(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ami"))

    @ami.setter
    def ami(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee7264ad4b6897bca758354a94325d5c7628f4033ad618af2add6374f87b1396)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ami", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="amiSsmParameter")
    def ami_ssm_parameter(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "amiSsmParameter"))

    @ami_ssm_parameter.setter
    def ami_ssm_parameter(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b6377e18a227544a1a9f6e3bdd198a2a4f8305a9071ab41196f7b04deb138bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amiSsmParameter", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="associatePublicIpAddress")
    def associate_public_ip_address(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "associatePublicIpAddress"))

    @associate_public_ip_address.setter
    def associate_public_ip_address(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd52a1524ee836126c63cfb8622070b10a339ad3d303247119841d0e687fc288)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatePublicIpAddress", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b3330a4e9202b8f098efdac21e9b2c0f9fd23bc911dabce6ee9eec599e3d8b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cpuCoreCount")
    def cpu_core_count(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuCoreCount"))

    @cpu_core_count.setter
    def cpu_core_count(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d292897665016afa5c5b927a032c61eb7ce944d38d671bb42b64d78edef60fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuCoreCount", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cpuCredits")
    def cpu_credits(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuCredits"))

    @cpu_credits.setter
    def cpu_credits(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2494c4f8f1bd166d782e7e99e278e873fbf49302c9f2f08eba66723859085d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuCredits", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cpuThreadsPerCore")
    def cpu_threads_per_core(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuThreadsPerCore"))

    @cpu_threads_per_core.setter
    def cpu_threads_per_core(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__376180ea154c6a494a4ae471a61408e6a0b5c34438fd73d2bc30d10176ead960)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuThreadsPerCore", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "create"))

    @create.setter
    def create(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf7669ef426694ed0f66ca60b0d44ecd5a4b263fd8ec79ecbdd28de5b3dcf439)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createEip")
    def create_eip(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createEip"))

    @create_eip.setter
    def create_eip(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abcd19d2224728e350be0e2044655fcc6b657bc8c59ec70a8fd736737cfa8a14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createEip", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createIamInstanceProfile")
    def create_iam_instance_profile(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createIamInstanceProfile"))

    @create_iam_instance_profile.setter
    def create_iam_instance_profile(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2addb76579eb1a82b98b8bbe4b03d8bda34c771bfba8ca425138905d16bc137)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createIamInstanceProfile", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createSpotInstance")
    def create_spot_instance(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createSpotInstance"))

    @create_spot_instance.setter
    def create_spot_instance(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f5f4672a41c483c5d63c9945353e8c2b79583b1150058b967056ec886392e36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createSpotInstance", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="disableApiStop")
    def disable_api_stop(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "disableApiStop"))

    @disable_api_stop.setter
    def disable_api_stop(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14a5eca1df7196c2577c9fdf0645d3b5e7176c194d90118d48911de059297855)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableApiStop", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="disableApiTermination")
    def disable_api_termination(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "disableApiTermination"))

    @disable_api_termination.setter
    def disable_api_termination(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4724c59e8fadbff829870b8998c7e44aba02f221780220bf08b68eee8dedd4df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableApiTermination", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ebsBlockDevice")
    def ebs_block_device(self) -> typing.Optional[typing.List[typing.Any]]:
        return typing.cast(typing.Optional[typing.List[typing.Any]], jsii.get(self, "ebsBlockDevice"))

    @ebs_block_device.setter
    def ebs_block_device(self, value: typing.Optional[typing.List[typing.Any]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5385a7c48e371f3ee2b86236fc5e09e6de849d3f6379b60f8cb5a53143973c37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsBlockDevice", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ebsOptimized")
    def ebs_optimized(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "ebsOptimized"))

    @ebs_optimized.setter
    def ebs_optimized(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53696e37b20b66d446953438ae397b9d910fd1071f021a6fedd66e636ee81f66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsOptimized", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="eipDomain")
    def eip_domain(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eipDomain"))

    @eip_domain.setter
    def eip_domain(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__703bf950faa8db57bcf1099aea45b4a1b811174a41f1a110c66da2eeeb7441d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eipDomain", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="eipTags")
    def eip_tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "eipTags"))

    @eip_tags.setter
    def eip_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a56b7b549ae20d297b604217950864f00c506f972e9b57edd776f8da8b4833be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eipTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enableVolumeTags")
    def enable_volume_tags(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enableVolumeTags"))

    @enable_volume_tags.setter
    def enable_volume_tags(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64719ca7ef322e9e3d9362ae85a3770257e1e2da0704b10166dd2410ddb3e5c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableVolumeTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enclaveOptionsEnabled")
    def enclave_options_enabled(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enclaveOptionsEnabled"))

    @enclave_options_enabled.setter
    def enclave_options_enabled(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a54b45ad1af794cb63bb380a492e2e2f627ad01c20596d2787747cd58c43afe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enclaveOptionsEnabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ephemeralBlockDevice")
    def ephemeral_block_device(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "ephemeralBlockDevice"))

    @ephemeral_block_device.setter
    def ephemeral_block_device(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a33b602a6b5d897fdb7fd8e230f093b492437633704f0e483ea4ff7743b1182d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ephemeralBlockDevice", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fetchPasswordData")
    def fetch_password_data(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "fetchPasswordData"))

    @fetch_password_data.setter
    def fetch_password_data(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b31c02ce7eb2553be010b3d970c1a332a4051007180fdcd899bee5416d00b6ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchPasswordData", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hibernation")
    def hibernation(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "hibernation"))

    @hibernation.setter
    def hibernation(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60a4326ed7ca48c03f114a374e00e0b6eb8fd3e2c52d0e1ece648774aa0c9cc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hibernation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hostId")
    def host_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostId"))

    @host_id.setter
    def host_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8272bbef7958ab637086709f6ec909af52267a873c339860a9af173a3eb8446e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="iamInstanceProfile")
    def iam_instance_profile(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamInstanceProfile"))

    @iam_instance_profile.setter
    def iam_instance_profile(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1591f291e4fc174ba975c5c1bc596177632609e4707d7ffd8471519d6fddae81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamInstanceProfile", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="iamRoleDescription")
    def iam_role_description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRoleDescription"))

    @iam_role_description.setter
    def iam_role_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6b9184344fe74872acb8c128c32ce2562c1f4cac348becd9263ed0037369582)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoleDescription", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="iamRoleName")
    def iam_role_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRoleName"))

    @iam_role_name.setter
    def iam_role_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2efdaab6777030185ed492601b38226d2216272b2dda06d3f5c13b97a003d26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoleName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="iamRolePath")
    def iam_role_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRolePath"))

    @iam_role_path.setter
    def iam_role_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fb651d550b0427098224c6e53665bb08c2e50a3ae508c83092a4e3e717c3c39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRolePath", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="iamRolePermissionsBoundary")
    def iam_role_permissions_boundary(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRolePermissionsBoundary"))

    @iam_role_permissions_boundary.setter
    def iam_role_permissions_boundary(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9ed43bf4ec3bc9eec4a8a10d37d6930ab6815ba82d189d4a7ffe381dcb94b89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRolePermissionsBoundary", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="iamRolePolicies")
    def iam_role_policies(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "iamRolePolicies"))

    @iam_role_policies.setter
    def iam_role_policies(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f0a7eece83620a18da77af1ae1cb11d4a6d16268907f6e364dabd41d8580ba7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRolePolicies", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="iamRoleTags")
    def iam_role_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "iamRoleTags"))

    @iam_role_tags.setter
    def iam_role_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ffa722dbbf981ddfa636a8831fdf3017d4e7652a65055a6fd09d8a02127b7f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoleTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="iamRoleUseNamePrefix")
    def iam_role_use_name_prefix(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "iamRoleUseNamePrefix"))

    @iam_role_use_name_prefix.setter
    def iam_role_use_name_prefix(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6169f4b399ba0df18598c24e5eeba6ca0b22ccc3decf1cb66791e3ef7d4fa406)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoleUseNamePrefix", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ignoreAmiChanges")
    def ignore_ami_changes(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "ignoreAmiChanges"))

    @ignore_ami_changes.setter
    def ignore_ami_changes(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2cd4fbfd2d4b6e4585ce176f4240ccd75abcb7f0889720dd74a6b3c1fa7eaca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreAmiChanges", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="instanceInitiatedShutdownBehavior")
    def instance_initiated_shutdown_behavior(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceInitiatedShutdownBehavior"))

    @instance_initiated_shutdown_behavior.setter
    def instance_initiated_shutdown_behavior(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__398a4823ac6c819bd554f49539a3d8c4e4788ce4de3ade5c74b2c4e16e2c5a08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceInitiatedShutdownBehavior", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="instanceTags")
    def instance_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "instanceTags"))

    @instance_tags.setter
    def instance_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a48d813519214458603e824ced6fb43f766abc478030a242222b1d2bd6ec3c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b66131af814d60903e85334452e557337d412951c302559d7ecf98a439061db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipv6AddressCount")
    def ipv6_address_count(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ipv6AddressCount"))

    @ipv6_address_count.setter
    def ipv6_address_count(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e35657713a9098375b7e36fe6d53675578891c7ebb8dbad1e08df6bd65333de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6AddressCount", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipv6Addresses")
    def ipv6_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipv6Addresses"))

    @ipv6_addresses.setter
    def ipv6_addresses(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9ad279954d00c67e1a31de877696de73e10c0802a6b596cfd28fa6c2c711781)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6Addresses", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyName"))

    @key_name.setter
    def key_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52dd1412d395b33f7f85a129276ff9d9b03f59f1e9814d7f8ff818dbc49b87b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="launchTemplate")
    def launch_template(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "launchTemplate"))

    @launch_template.setter
    def launch_template(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deee6c79d4f65c5eb7cd751c5069d7502d40147037172b7695ea02cfcf9d3c94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchTemplate", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="metadataOptions")
    def metadata_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "metadataOptions"))

    @metadata_options.setter
    def metadata_options(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36ee7d488c7bd8db1f70837ee6647a9becae4ff739408dd0a67facb85a152282)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadataOptions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="monitoring")
    def monitoring(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "monitoring"))

    @monitoring.setter
    def monitoring(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98e594bcf20a631574c9d3e3d249bf862d2e17d6e1b2c27d8c5d03b1312bc7ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitoring", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af9d6fe0593f984e8c7bf84175b3db10fa85887d93a60532d0b4904a00f408ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkInterface")
    def network_interface(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "networkInterface"))

    @network_interface.setter
    def network_interface(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c350d6bdeeb81f638695dd1267c87a6a02f4289102fa2379f8fd079d4ab4ce2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkInterface", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="placementGroup")
    def placement_group(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "placementGroup"))

    @placement_group.setter
    def placement_group(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d7cc84e246e8448c2edab3b9640b95eef0beabeb27ae581592f8f9c3c4af490)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "placementGroup", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privateDnsNameOptions")
    def private_dns_name_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "privateDnsNameOptions"))

    @private_dns_name_options.setter
    def private_dns_name_options(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__141b4a8759b7974d78c868323be38b6a4c9ea336b2669c4ce0e06d65070a1542)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateDnsNameOptions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privateIp")
    def private_ip(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIp"))

    @private_ip.setter
    def private_ip(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62228ec0db5c379e90ec8f0c5d3b8674cf9f5bff0852f6b5f4bb67f7fd786e91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIp", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="putinKhuylo")
    def putin_khuylo(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "putinKhuylo"))

    @putin_khuylo.setter
    def putin_khuylo(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b354904500dd4d36d0616f9b2c6e254abc747babbea580f18767b2e4bb21aa29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "putinKhuylo", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rootBlockDevice")
    def root_block_device(self) -> typing.Optional[typing.List[typing.Any]]:
        return typing.cast(typing.Optional[typing.List[typing.Any]], jsii.get(self, "rootBlockDevice"))

    @root_block_device.setter
    def root_block_device(
        self,
        value: typing.Optional[typing.List[typing.Any]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7517bd1f08cc5c17f50b15a41c59adaec599985b442287794ce13fc7825e5bde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rootBlockDevice", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="secondaryPrivateIps")
    def secondary_private_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "secondaryPrivateIps"))

    @secondary_private_ips.setter
    def secondary_private_ips(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02d23b75ec6208caf0d42c8138c8acc52c877d7b28e941c8dd3b8c36c8545ff4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secondaryPrivateIps", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceDestCheck")
    def source_dest_check(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "sourceDestCheck"))

    @source_dest_check.setter
    def source_dest_check(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a74dc80bf06afd817039d8e0d10f089a3505ea505ff1ee74acaefb3e86ea6d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDestCheck", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="spotBlockDurationMinutes")
    def spot_block_duration_minutes(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "spotBlockDurationMinutes"))

    @spot_block_duration_minutes.setter
    def spot_block_duration_minutes(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d27fb4e35a1c9972ed4236333d26eded0f2bc011dfd9294b5c0c16daf1acfc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotBlockDurationMinutes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="spotInstanceInterruptionBehavior")
    def spot_instance_interruption_behavior(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spotInstanceInterruptionBehavior"))

    @spot_instance_interruption_behavior.setter
    def spot_instance_interruption_behavior(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b687bc2a6b81aa3fdaf0dd4737df3e77893e35e6fe24093a6de1298528a89ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotInstanceInterruptionBehavior", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="spotLaunchGroup")
    def spot_launch_group(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spotLaunchGroup"))

    @spot_launch_group.setter
    def spot_launch_group(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7162d13556540bfdc1a43721c35722966c47ef8b26a81cb2a50ccf7de63ab584)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotLaunchGroup", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="spotPrice")
    def spot_price(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spotPrice"))

    @spot_price.setter
    def spot_price(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75d570458e1320701dde746b99ac4883116574f6a937be94f749126f0fab27b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotPrice", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="spotType")
    def spot_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spotType"))

    @spot_type.setter
    def spot_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfdb8082d31d285d2daa782f0ea751c04e09b5d75c68d3dcd4cc2e7109e6a430)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="spotValidFrom")
    def spot_valid_from(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spotValidFrom"))

    @spot_valid_from.setter
    def spot_valid_from(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5619160754f7d8776a1b72b1d8f226344a1cff71635c357196ba460178218a66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotValidFrom", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="spotValidUntil")
    def spot_valid_until(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spotValidUntil"))

    @spot_valid_until.setter
    def spot_valid_until(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c382ad107fa26b608149b830d2bd0d7f9b818794db8d072c6911c085fbb7ffa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotValidUntil", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="spotWaitForFulfillment")
    def spot_wait_for_fulfillment(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "spotWaitForFulfillment"))

    @spot_wait_for_fulfillment.setter
    def spot_wait_for_fulfillment(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4fe59fc34b24d6a9d34cd9ae42fe71d6f59fda4f7a1524afc426c15a14f9968)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotWaitForFulfillment", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c53c84edba684af533fafb4b15057358b963cb765e93626471f979b2a8165970)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb61c46c544f4195baadae740e485c4c72a52eda0bd2496269ffb8a11e9b91d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tenancy")
    def tenancy(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenancy"))

    @tenancy.setter
    def tenancy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f709bffc64edf8bff4b6134bc542041abf97d16993281ddc82d004c47f1ca7ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenancy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "timeouts"))

    @timeouts.setter
    def timeouts(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__569ae3c25db1781a260348ae519579f508b02a72adc9f1472527a7e43fa05f1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeouts", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="userData")
    def user_data(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userData"))

    @user_data.setter
    def user_data(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7badeb1f0c91ecf157d6d905d37a06f56dc30ec5c7dfb7f04da5fc9c436d9baf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userData", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="userDataBase64")
    def user_data_base64(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userDataBase64"))

    @user_data_base64.setter
    def user_data_base64(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c1c23efd8db42444c01306350a57fdda9e2662d6598a176565b57dce8d84fb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userDataBase64", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="userDataReplaceOnChange")
    def user_data_replace_on_change(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "userDataReplaceOnChange"))

    @user_data_replace_on_change.setter
    def user_data_replace_on_change(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afcc27f6fe667b376dd84dccd2132c99f68a35e3828fbcddf398a07cdad2481f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userDataReplaceOnChange", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="volumeTags")
    def volume_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "volumeTags"))

    @volume_tags.setter
    def volume_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0dcb7ca26abdeab3347d9a743fff0b66fe465da7c9723b561558666b3a940e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSecurityGroupIds"))

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11d3d87cc615ad1c7fa52982e4f4ba2ab732c1b2fa1ddaff105ca78ff322e4f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSecurityGroupIds", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="ec2-instance.Ec2InstanceConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformModuleUserConfig],
    name_mapping={
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "providers": "providers",
        "skip_asset_creation_from_local_modules": "skipAssetCreationFromLocalModules",
        "ami": "ami",
        "ami_ssm_parameter": "amiSsmParameter",
        "associate_public_ip_address": "associatePublicIpAddress",
        "availability_zone": "availabilityZone",
        "capacity_reservation_specification": "capacityReservationSpecification",
        "cpu_core_count": "cpuCoreCount",
        "cpu_credits": "cpuCredits",
        "cpu_options": "cpuOptions",
        "cpu_threads_per_core": "cpuThreadsPerCore",
        "create": "create",
        "create_eip": "createEip",
        "create_iam_instance_profile": "createIamInstanceProfile",
        "create_spot_instance": "createSpotInstance",
        "disable_api_stop": "disableApiStop",
        "disable_api_termination": "disableApiTermination",
        "ebs_block_device": "ebsBlockDevice",
        "ebs_optimized": "ebsOptimized",
        "eip_domain": "eipDomain",
        "eip_tags": "eipTags",
        "enable_volume_tags": "enableVolumeTags",
        "enclave_options_enabled": "enclaveOptionsEnabled",
        "ephemeral_block_device": "ephemeralBlockDevice",
        "fetch_password_data": "fetchPasswordData",
        "hibernation": "hibernation",
        "host_id": "hostId",
        "iam_instance_profile": "iamInstanceProfile",
        "iam_role_description": "iamRoleDescription",
        "iam_role_name": "iamRoleName",
        "iam_role_path": "iamRolePath",
        "iam_role_permissions_boundary": "iamRolePermissionsBoundary",
        "iam_role_policies": "iamRolePolicies",
        "iam_role_tags": "iamRoleTags",
        "iam_role_use_name_prefix": "iamRoleUseNamePrefix",
        "ignore_ami_changes": "ignoreAmiChanges",
        "instance_initiated_shutdown_behavior": "instanceInitiatedShutdownBehavior",
        "instance_tags": "instanceTags",
        "instance_type": "instanceType",
        "ipv6_address_count": "ipv6AddressCount",
        "ipv6_addresses": "ipv6Addresses",
        "key_name": "keyName",
        "launch_template": "launchTemplate",
        "maintenance_options": "maintenanceOptions",
        "metadata_options": "metadataOptions",
        "monitoring": "monitoring",
        "name": "name",
        "network_interface": "networkInterface",
        "placement_group": "placementGroup",
        "private_dns_name_options": "privateDnsNameOptions",
        "private_ip": "privateIp",
        "putin_khuylo": "putinKhuylo",
        "root_block_device": "rootBlockDevice",
        "secondary_private_ips": "secondaryPrivateIps",
        "source_dest_check": "sourceDestCheck",
        "spot_block_duration_minutes": "spotBlockDurationMinutes",
        "spot_instance_interruption_behavior": "spotInstanceInterruptionBehavior",
        "spot_launch_group": "spotLaunchGroup",
        "spot_price": "spotPrice",
        "spot_type": "spotType",
        "spot_valid_from": "spotValidFrom",
        "spot_valid_until": "spotValidUntil",
        "spot_wait_for_fulfillment": "spotWaitForFulfillment",
        "subnet_id": "subnetId",
        "tags": "tags",
        "tenancy": "tenancy",
        "timeouts": "timeouts",
        "user_data": "userData",
        "user_data_base64": "userDataBase64",
        "user_data_replace_on_change": "userDataReplaceOnChange",
        "volume_tags": "volumeTags",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
    },
)
class Ec2InstanceConfig(_cdktf_9a9027ec.TerraformModuleUserConfig):
    def __init__(
        self,
        *,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        providers: typing.Optional[typing.Sequence[typing.Union[_cdktf_9a9027ec.TerraformProvider, typing.Union[_cdktf_9a9027ec.TerraformModuleProvider, typing.Dict[builtins.str, typing.Any]]]]] = None,
        skip_asset_creation_from_local_modules: typing.Optional[builtins.bool] = None,
        ami: typing.Optional[builtins.str] = None,
        ami_ssm_parameter: typing.Optional[builtins.str] = None,
        associate_public_ip_address: typing.Optional[builtins.bool] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        capacity_reservation_specification: typing.Any = None,
        cpu_core_count: typing.Optional[jsii.Number] = None,
        cpu_credits: typing.Optional[builtins.str] = None,
        cpu_options: typing.Any = None,
        cpu_threads_per_core: typing.Optional[jsii.Number] = None,
        create: typing.Optional[builtins.bool] = None,
        create_eip: typing.Optional[builtins.bool] = None,
        create_iam_instance_profile: typing.Optional[builtins.bool] = None,
        create_spot_instance: typing.Optional[builtins.bool] = None,
        disable_api_stop: typing.Optional[builtins.bool] = None,
        disable_api_termination: typing.Optional[builtins.bool] = None,
        ebs_block_device: typing.Optional[typing.Sequence[typing.Any]] = None,
        ebs_optimized: typing.Optional[builtins.bool] = None,
        eip_domain: typing.Optional[builtins.str] = None,
        eip_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        enable_volume_tags: typing.Optional[builtins.bool] = None,
        enclave_options_enabled: typing.Optional[builtins.bool] = None,
        ephemeral_block_device: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        fetch_password_data: typing.Optional[builtins.bool] = None,
        hibernation: typing.Optional[builtins.bool] = None,
        host_id: typing.Optional[builtins.str] = None,
        iam_instance_profile: typing.Optional[builtins.str] = None,
        iam_role_description: typing.Optional[builtins.str] = None,
        iam_role_name: typing.Optional[builtins.str] = None,
        iam_role_path: typing.Optional[builtins.str] = None,
        iam_role_permissions_boundary: typing.Optional[builtins.str] = None,
        iam_role_policies: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        iam_role_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        iam_role_use_name_prefix: typing.Optional[builtins.bool] = None,
        ignore_ami_changes: typing.Optional[builtins.bool] = None,
        instance_initiated_shutdown_behavior: typing.Optional[builtins.str] = None,
        instance_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instance_type: typing.Optional[builtins.str] = None,
        ipv6_address_count: typing.Optional[jsii.Number] = None,
        ipv6_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        key_name: typing.Optional[builtins.str] = None,
        launch_template: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        maintenance_options: typing.Any = None,
        metadata_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        monitoring: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
        network_interface: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        placement_group: typing.Optional[builtins.str] = None,
        private_dns_name_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        private_ip: typing.Optional[builtins.str] = None,
        putin_khuylo: typing.Optional[builtins.bool] = None,
        root_block_device: typing.Optional[typing.Sequence[typing.Any]] = None,
        secondary_private_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_dest_check: typing.Optional[builtins.bool] = None,
        spot_block_duration_minutes: typing.Optional[jsii.Number] = None,
        spot_instance_interruption_behavior: typing.Optional[builtins.str] = None,
        spot_launch_group: typing.Optional[builtins.str] = None,
        spot_price: typing.Optional[builtins.str] = None,
        spot_type: typing.Optional[builtins.str] = None,
        spot_valid_from: typing.Optional[builtins.str] = None,
        spot_valid_until: typing.Optional[builtins.str] = None,
        spot_wait_for_fulfillment: typing.Optional[builtins.bool] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tenancy: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        user_data: typing.Optional[builtins.str] = None,
        user_data_base64: typing.Optional[builtins.str] = None,
        user_data_replace_on_change: typing.Optional[builtins.bool] = None,
        volume_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param depends_on: 
        :param for_each: 
        :param providers: 
        :param skip_asset_creation_from_local_modules: 
        :param ami: ID of AMI to use for the instance.
        :param ami_ssm_parameter: SSM parameter name for the AMI ID. For Amazon Linux AMI SSM parameters see `reference <https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-public-parameters-ami.html>`_ /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
        :param associate_public_ip_address: Whether to associate a public IP address with an instance in a VPC.
        :param availability_zone: AZ to start the instance in.
        :param capacity_reservation_specification: Describes an instance's Capacity Reservation targeting option.
        :param cpu_core_count: Sets the number of CPU cores for an instance.
        :param cpu_credits: The credit option for CPU usage (unlimited or standard).
        :param cpu_options: Defines CPU options to apply to the instance at launch time.
        :param cpu_threads_per_core: Sets the number of CPU threads per core for an instance (has no effect unless cpu_core_count is also set).
        :param create: Whether to create an instance true.
        :param create_eip: Determines whether a public EIP will be created and associated with the instance.
        :param create_iam_instance_profile: Determines whether an IAM instance profile is created or to use an existing IAM instance profile.
        :param create_spot_instance: Depicts if the instance is a spot instance.
        :param disable_api_stop: If true, enables EC2 Instance Stop Protection.
        :param disable_api_termination: If true, enables EC2 Instance Termination Protection.
        :param ebs_block_device: Additional EBS block devices to attach to the instance.
        :param ebs_optimized: If true, the launched EC2 instance will be EBS-optimized.
        :param eip_domain: Indicates if this EIP is for use in VPC vpc.
        :param eip_tags: A map of additional tags to add to the eip The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param enable_volume_tags: Whether to enable volume tags (if enabled it conflicts with root_block_device tags) true.
        :param enclave_options_enabled: Whether Nitro Enclaves will be enabled on the instance. Defaults to ``false``
        :param ephemeral_block_device: Customize Ephemeral (also known as Instance Store) volumes on the instance. The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}
        :param fetch_password_data: If true, wait for password data to become available and retrieve it.
        :param hibernation: If true, the launched EC2 instance will support hibernation.
        :param host_id: ID of a dedicated host that the instance will be assigned to. Use when an instance is to be launched on a specific dedicated host
        :param iam_instance_profile: IAM Instance Profile to launch the instance with. Specified as the name of the Instance Profile
        :param iam_role_description: Description of the role.
        :param iam_role_name: Name to use on IAM role created.
        :param iam_role_path: IAM role path.
        :param iam_role_permissions_boundary: ARN of the policy that is used to set the permissions boundary for the IAM role.
        :param iam_role_policies: Policies attached to the IAM role The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param iam_role_tags: A map of additional tags to add to the IAM role/profile created The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param iam_role_use_name_prefix: Determines whether the IAM role name (``iam_role_name`` or ``name``) is used as a prefix true.
        :param ignore_ami_changes: Whether changes to the AMI ID changes should be ignored by Terraform. Note - changing this value will result in the replacement of the instance
        :param instance_initiated_shutdown_behavior: Shutdown behavior for the instance. Amazon defaults this to stop for EBS-backed instances and terminate for instance-store instances. Cannot be set on instance-store instance
        :param instance_tags: Additional tags for the instance The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param instance_type: The type of instance to start t3.micro.
        :param ipv6_address_count: A number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet
        :param ipv6_addresses: Specify one or more IPv6 addresses from the range of the subnet to associate with the primary network interface.
        :param key_name: Key name of the Key Pair to use for the instance; which can be managed using the ``aws_key_pair`` resource
        :param launch_template: Specifies a Launch Template to configure the instance. Parameters configured on this resource will override the corresponding parameters in the Launch Template The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}
        :param maintenance_options: The maintenance options for the instance.
        :param metadata_options: Customize the metadata options of the instance The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param monitoring: If true, the launched EC2 instance will have detailed monitoring enabled.
        :param name: Name to be used on EC2 instance created.
        :param network_interface: Customize network interfaces to be attached at instance boot time. The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}
        :param placement_group: The Placement Group to start the instance in.
        :param private_dns_name_options: Customize the private DNS name options of the instance The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param private_ip: Private IP address to associate with the instance in a VPC.
        :param putin_khuylo: Do you agree that Putin doesn't respect Ukrainian sovereignty and territorial integrity? More info: https://en.wikipedia.org/wiki/Putin_khuylo! true
        :param root_block_device: Customize details about the root block device of the instance. See Block Devices below for details
        :param secondary_private_ips: A list of secondary private IPv4 addresses to assign to the instance's primary network interface (eth0) in a VPC. Can only be assigned to the primary network interface (eth0) attached at instance creation, not a pre-existing network interface i.e. referenced in a ``network_interface block``
        :param source_dest_check: Controls if traffic is routed to the instance when the destination address does not match the instance. Used for NAT or VPNs
        :param spot_block_duration_minutes: The required duration for the Spot instances, in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360)
        :param spot_instance_interruption_behavior: Indicates Spot instance behavior when it is interrupted. Valid values are ``terminate``, ``stop``, or ``hibernate``
        :param spot_launch_group: A launch group is a group of spot instances that launch together and terminate together. If left empty instances are launched and terminated individually
        :param spot_price: The maximum price to request on the spot market. Defaults to on-demand price
        :param spot_type: If set to one-time, after the instance is terminated, the spot request will be closed. Default ``persistent``
        :param spot_valid_from: The start date and time of the request, in UTC RFC3339 format(for example, YYYY-MM-DDTHH:MM:SSZ).
        :param spot_valid_until: The end date and time of the request, in UTC RFC3339 format(for example, YYYY-MM-DDTHH:MM:SSZ).
        :param spot_wait_for_fulfillment: If set, Terraform will wait for the Spot Request to be fulfilled, and will throw an error if the timeout of 10m is reached.
        :param subnet_id: The VPC Subnet ID to launch in.
        :param tags: A mapping of tags to assign to the resource The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param tenancy: The tenancy of the instance (if the instance is running in a VPC). Available values: default, dedicated, host
        :param timeouts: Define maximum timeout for creating, updating, and deleting EC2 instance resources The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param user_data: The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see user_data_base64 instead
        :param user_data_base64: Can be used instead of user_data to pass base64-encoded binary data directly. Use this instead of user_data whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption
        :param user_data_replace_on_change: When used in combination with user_data or user_data_base64 will trigger a destroy and recreate when set to true. Defaults to false if not set
        :param volume_tags: A mapping of tags to assign to the devices created by the instance at launch time The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param vpc_security_group_ids: A list of security group IDs to associate with.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76c4b8200869d35a0d1f7dc9b992e4cd145268ef7d2f17ff61aef344ca2fb537)
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument providers", value=providers, expected_type=type_hints["providers"])
            check_type(argname="argument skip_asset_creation_from_local_modules", value=skip_asset_creation_from_local_modules, expected_type=type_hints["skip_asset_creation_from_local_modules"])
            check_type(argname="argument ami", value=ami, expected_type=type_hints["ami"])
            check_type(argname="argument ami_ssm_parameter", value=ami_ssm_parameter, expected_type=type_hints["ami_ssm_parameter"])
            check_type(argname="argument associate_public_ip_address", value=associate_public_ip_address, expected_type=type_hints["associate_public_ip_address"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument capacity_reservation_specification", value=capacity_reservation_specification, expected_type=type_hints["capacity_reservation_specification"])
            check_type(argname="argument cpu_core_count", value=cpu_core_count, expected_type=type_hints["cpu_core_count"])
            check_type(argname="argument cpu_credits", value=cpu_credits, expected_type=type_hints["cpu_credits"])
            check_type(argname="argument cpu_options", value=cpu_options, expected_type=type_hints["cpu_options"])
            check_type(argname="argument cpu_threads_per_core", value=cpu_threads_per_core, expected_type=type_hints["cpu_threads_per_core"])
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument create_eip", value=create_eip, expected_type=type_hints["create_eip"])
            check_type(argname="argument create_iam_instance_profile", value=create_iam_instance_profile, expected_type=type_hints["create_iam_instance_profile"])
            check_type(argname="argument create_spot_instance", value=create_spot_instance, expected_type=type_hints["create_spot_instance"])
            check_type(argname="argument disable_api_stop", value=disable_api_stop, expected_type=type_hints["disable_api_stop"])
            check_type(argname="argument disable_api_termination", value=disable_api_termination, expected_type=type_hints["disable_api_termination"])
            check_type(argname="argument ebs_block_device", value=ebs_block_device, expected_type=type_hints["ebs_block_device"])
            check_type(argname="argument ebs_optimized", value=ebs_optimized, expected_type=type_hints["ebs_optimized"])
            check_type(argname="argument eip_domain", value=eip_domain, expected_type=type_hints["eip_domain"])
            check_type(argname="argument eip_tags", value=eip_tags, expected_type=type_hints["eip_tags"])
            check_type(argname="argument enable_volume_tags", value=enable_volume_tags, expected_type=type_hints["enable_volume_tags"])
            check_type(argname="argument enclave_options_enabled", value=enclave_options_enabled, expected_type=type_hints["enclave_options_enabled"])
            check_type(argname="argument ephemeral_block_device", value=ephemeral_block_device, expected_type=type_hints["ephemeral_block_device"])
            check_type(argname="argument fetch_password_data", value=fetch_password_data, expected_type=type_hints["fetch_password_data"])
            check_type(argname="argument hibernation", value=hibernation, expected_type=type_hints["hibernation"])
            check_type(argname="argument host_id", value=host_id, expected_type=type_hints["host_id"])
            check_type(argname="argument iam_instance_profile", value=iam_instance_profile, expected_type=type_hints["iam_instance_profile"])
            check_type(argname="argument iam_role_description", value=iam_role_description, expected_type=type_hints["iam_role_description"])
            check_type(argname="argument iam_role_name", value=iam_role_name, expected_type=type_hints["iam_role_name"])
            check_type(argname="argument iam_role_path", value=iam_role_path, expected_type=type_hints["iam_role_path"])
            check_type(argname="argument iam_role_permissions_boundary", value=iam_role_permissions_boundary, expected_type=type_hints["iam_role_permissions_boundary"])
            check_type(argname="argument iam_role_policies", value=iam_role_policies, expected_type=type_hints["iam_role_policies"])
            check_type(argname="argument iam_role_tags", value=iam_role_tags, expected_type=type_hints["iam_role_tags"])
            check_type(argname="argument iam_role_use_name_prefix", value=iam_role_use_name_prefix, expected_type=type_hints["iam_role_use_name_prefix"])
            check_type(argname="argument ignore_ami_changes", value=ignore_ami_changes, expected_type=type_hints["ignore_ami_changes"])
            check_type(argname="argument instance_initiated_shutdown_behavior", value=instance_initiated_shutdown_behavior, expected_type=type_hints["instance_initiated_shutdown_behavior"])
            check_type(argname="argument instance_tags", value=instance_tags, expected_type=type_hints["instance_tags"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument ipv6_address_count", value=ipv6_address_count, expected_type=type_hints["ipv6_address_count"])
            check_type(argname="argument ipv6_addresses", value=ipv6_addresses, expected_type=type_hints["ipv6_addresses"])
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument launch_template", value=launch_template, expected_type=type_hints["launch_template"])
            check_type(argname="argument maintenance_options", value=maintenance_options, expected_type=type_hints["maintenance_options"])
            check_type(argname="argument metadata_options", value=metadata_options, expected_type=type_hints["metadata_options"])
            check_type(argname="argument monitoring", value=monitoring, expected_type=type_hints["monitoring"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_interface", value=network_interface, expected_type=type_hints["network_interface"])
            check_type(argname="argument placement_group", value=placement_group, expected_type=type_hints["placement_group"])
            check_type(argname="argument private_dns_name_options", value=private_dns_name_options, expected_type=type_hints["private_dns_name_options"])
            check_type(argname="argument private_ip", value=private_ip, expected_type=type_hints["private_ip"])
            check_type(argname="argument putin_khuylo", value=putin_khuylo, expected_type=type_hints["putin_khuylo"])
            check_type(argname="argument root_block_device", value=root_block_device, expected_type=type_hints["root_block_device"])
            check_type(argname="argument secondary_private_ips", value=secondary_private_ips, expected_type=type_hints["secondary_private_ips"])
            check_type(argname="argument source_dest_check", value=source_dest_check, expected_type=type_hints["source_dest_check"])
            check_type(argname="argument spot_block_duration_minutes", value=spot_block_duration_minutes, expected_type=type_hints["spot_block_duration_minutes"])
            check_type(argname="argument spot_instance_interruption_behavior", value=spot_instance_interruption_behavior, expected_type=type_hints["spot_instance_interruption_behavior"])
            check_type(argname="argument spot_launch_group", value=spot_launch_group, expected_type=type_hints["spot_launch_group"])
            check_type(argname="argument spot_price", value=spot_price, expected_type=type_hints["spot_price"])
            check_type(argname="argument spot_type", value=spot_type, expected_type=type_hints["spot_type"])
            check_type(argname="argument spot_valid_from", value=spot_valid_from, expected_type=type_hints["spot_valid_from"])
            check_type(argname="argument spot_valid_until", value=spot_valid_until, expected_type=type_hints["spot_valid_until"])
            check_type(argname="argument spot_wait_for_fulfillment", value=spot_wait_for_fulfillment, expected_type=type_hints["spot_wait_for_fulfillment"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tenancy", value=tenancy, expected_type=type_hints["tenancy"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
            check_type(argname="argument user_data_base64", value=user_data_base64, expected_type=type_hints["user_data_base64"])
            check_type(argname="argument user_data_replace_on_change", value=user_data_replace_on_change, expected_type=type_hints["user_data_replace_on_change"])
            check_type(argname="argument volume_tags", value=volume_tags, expected_type=type_hints["volume_tags"])
            check_type(argname="argument vpc_security_group_ids", value=vpc_security_group_ids, expected_type=type_hints["vpc_security_group_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if providers is not None:
            self._values["providers"] = providers
        if skip_asset_creation_from_local_modules is not None:
            self._values["skip_asset_creation_from_local_modules"] = skip_asset_creation_from_local_modules
        if ami is not None:
            self._values["ami"] = ami
        if ami_ssm_parameter is not None:
            self._values["ami_ssm_parameter"] = ami_ssm_parameter
        if associate_public_ip_address is not None:
            self._values["associate_public_ip_address"] = associate_public_ip_address
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if capacity_reservation_specification is not None:
            self._values["capacity_reservation_specification"] = capacity_reservation_specification
        if cpu_core_count is not None:
            self._values["cpu_core_count"] = cpu_core_count
        if cpu_credits is not None:
            self._values["cpu_credits"] = cpu_credits
        if cpu_options is not None:
            self._values["cpu_options"] = cpu_options
        if cpu_threads_per_core is not None:
            self._values["cpu_threads_per_core"] = cpu_threads_per_core
        if create is not None:
            self._values["create"] = create
        if create_eip is not None:
            self._values["create_eip"] = create_eip
        if create_iam_instance_profile is not None:
            self._values["create_iam_instance_profile"] = create_iam_instance_profile
        if create_spot_instance is not None:
            self._values["create_spot_instance"] = create_spot_instance
        if disable_api_stop is not None:
            self._values["disable_api_stop"] = disable_api_stop
        if disable_api_termination is not None:
            self._values["disable_api_termination"] = disable_api_termination
        if ebs_block_device is not None:
            self._values["ebs_block_device"] = ebs_block_device
        if ebs_optimized is not None:
            self._values["ebs_optimized"] = ebs_optimized
        if eip_domain is not None:
            self._values["eip_domain"] = eip_domain
        if eip_tags is not None:
            self._values["eip_tags"] = eip_tags
        if enable_volume_tags is not None:
            self._values["enable_volume_tags"] = enable_volume_tags
        if enclave_options_enabled is not None:
            self._values["enclave_options_enabled"] = enclave_options_enabled
        if ephemeral_block_device is not None:
            self._values["ephemeral_block_device"] = ephemeral_block_device
        if fetch_password_data is not None:
            self._values["fetch_password_data"] = fetch_password_data
        if hibernation is not None:
            self._values["hibernation"] = hibernation
        if host_id is not None:
            self._values["host_id"] = host_id
        if iam_instance_profile is not None:
            self._values["iam_instance_profile"] = iam_instance_profile
        if iam_role_description is not None:
            self._values["iam_role_description"] = iam_role_description
        if iam_role_name is not None:
            self._values["iam_role_name"] = iam_role_name
        if iam_role_path is not None:
            self._values["iam_role_path"] = iam_role_path
        if iam_role_permissions_boundary is not None:
            self._values["iam_role_permissions_boundary"] = iam_role_permissions_boundary
        if iam_role_policies is not None:
            self._values["iam_role_policies"] = iam_role_policies
        if iam_role_tags is not None:
            self._values["iam_role_tags"] = iam_role_tags
        if iam_role_use_name_prefix is not None:
            self._values["iam_role_use_name_prefix"] = iam_role_use_name_prefix
        if ignore_ami_changes is not None:
            self._values["ignore_ami_changes"] = ignore_ami_changes
        if instance_initiated_shutdown_behavior is not None:
            self._values["instance_initiated_shutdown_behavior"] = instance_initiated_shutdown_behavior
        if instance_tags is not None:
            self._values["instance_tags"] = instance_tags
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if ipv6_address_count is not None:
            self._values["ipv6_address_count"] = ipv6_address_count
        if ipv6_addresses is not None:
            self._values["ipv6_addresses"] = ipv6_addresses
        if key_name is not None:
            self._values["key_name"] = key_name
        if launch_template is not None:
            self._values["launch_template"] = launch_template
        if maintenance_options is not None:
            self._values["maintenance_options"] = maintenance_options
        if metadata_options is not None:
            self._values["metadata_options"] = metadata_options
        if monitoring is not None:
            self._values["monitoring"] = monitoring
        if name is not None:
            self._values["name"] = name
        if network_interface is not None:
            self._values["network_interface"] = network_interface
        if placement_group is not None:
            self._values["placement_group"] = placement_group
        if private_dns_name_options is not None:
            self._values["private_dns_name_options"] = private_dns_name_options
        if private_ip is not None:
            self._values["private_ip"] = private_ip
        if putin_khuylo is not None:
            self._values["putin_khuylo"] = putin_khuylo
        if root_block_device is not None:
            self._values["root_block_device"] = root_block_device
        if secondary_private_ips is not None:
            self._values["secondary_private_ips"] = secondary_private_ips
        if source_dest_check is not None:
            self._values["source_dest_check"] = source_dest_check
        if spot_block_duration_minutes is not None:
            self._values["spot_block_duration_minutes"] = spot_block_duration_minutes
        if spot_instance_interruption_behavior is not None:
            self._values["spot_instance_interruption_behavior"] = spot_instance_interruption_behavior
        if spot_launch_group is not None:
            self._values["spot_launch_group"] = spot_launch_group
        if spot_price is not None:
            self._values["spot_price"] = spot_price
        if spot_type is not None:
            self._values["spot_type"] = spot_type
        if spot_valid_from is not None:
            self._values["spot_valid_from"] = spot_valid_from
        if spot_valid_until is not None:
            self._values["spot_valid_until"] = spot_valid_until
        if spot_wait_for_fulfillment is not None:
            self._values["spot_wait_for_fulfillment"] = spot_wait_for_fulfillment
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if tags is not None:
            self._values["tags"] = tags
        if tenancy is not None:
            self._values["tenancy"] = tenancy
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if user_data is not None:
            self._values["user_data"] = user_data
        if user_data_base64 is not None:
            self._values["user_data_base64"] = user_data_base64
        if user_data_replace_on_change is not None:
            self._values["user_data_replace_on_change"] = user_data_replace_on_change
        if volume_tags is not None:
            self._values["volume_tags"] = volume_tags
        if vpc_security_group_ids is not None:
            self._values["vpc_security_group_ids"] = vpc_security_group_ids

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def providers(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.TerraformProvider, _cdktf_9a9027ec.TerraformModuleProvider]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("providers")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.TerraformProvider, _cdktf_9a9027ec.TerraformModuleProvider]]], result)

    @builtins.property
    def skip_asset_creation_from_local_modules(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("skip_asset_creation_from_local_modules")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ami(self) -> typing.Optional[builtins.str]:
        '''ID of AMI to use for the instance.'''
        result = self._values.get("ami")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ami_ssm_parameter(self) -> typing.Optional[builtins.str]:
        '''SSM parameter name for the AMI ID.

        For Amazon Linux AMI SSM parameters see `reference <https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-public-parameters-ami.html>`_
        /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
        '''
        result = self._values.get("ami_ssm_parameter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def associate_public_ip_address(self) -> typing.Optional[builtins.bool]:
        '''Whether to associate a public IP address with an instance in a VPC.'''
        result = self._values.get("associate_public_ip_address")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''AZ to start the instance in.'''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capacity_reservation_specification(self) -> typing.Any:
        '''Describes an instance's Capacity Reservation targeting option.'''
        result = self._values.get("capacity_reservation_specification")
        return typing.cast(typing.Any, result)

    @builtins.property
    def cpu_core_count(self) -> typing.Optional[jsii.Number]:
        '''Sets the number of CPU cores for an instance.'''
        result = self._values.get("cpu_core_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cpu_credits(self) -> typing.Optional[builtins.str]:
        '''The credit option for CPU usage (unlimited or standard).'''
        result = self._values.get("cpu_credits")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cpu_options(self) -> typing.Any:
        '''Defines CPU options to apply to the instance at launch time.'''
        result = self._values.get("cpu_options")
        return typing.cast(typing.Any, result)

    @builtins.property
    def cpu_threads_per_core(self) -> typing.Optional[jsii.Number]:
        '''Sets the number of CPU threads per core for an instance (has no effect unless cpu_core_count is also set).'''
        result = self._values.get("cpu_threads_per_core")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def create(self) -> typing.Optional[builtins.bool]:
        '''Whether to create an instance true.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_eip(self) -> typing.Optional[builtins.bool]:
        '''Determines whether a public EIP will be created and associated with the instance.'''
        result = self._values.get("create_eip")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_iam_instance_profile(self) -> typing.Optional[builtins.bool]:
        '''Determines whether an IAM instance profile is created or to use an existing IAM instance profile.'''
        result = self._values.get("create_iam_instance_profile")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_spot_instance(self) -> typing.Optional[builtins.bool]:
        '''Depicts if the instance is a spot instance.'''
        result = self._values.get("create_spot_instance")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def disable_api_stop(self) -> typing.Optional[builtins.bool]:
        '''If true, enables EC2 Instance Stop Protection.'''
        result = self._values.get("disable_api_stop")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def disable_api_termination(self) -> typing.Optional[builtins.bool]:
        '''If true, enables EC2 Instance Termination Protection.'''
        result = self._values.get("disable_api_termination")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ebs_block_device(self) -> typing.Optional[typing.List[typing.Any]]:
        '''Additional EBS block devices to attach to the instance.'''
        result = self._values.get("ebs_block_device")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def ebs_optimized(self) -> typing.Optional[builtins.bool]:
        '''If true, the launched EC2 instance will be EBS-optimized.'''
        result = self._values.get("ebs_optimized")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def eip_domain(self) -> typing.Optional[builtins.str]:
        '''Indicates if this EIP is for use in VPC vpc.'''
        result = self._values.get("eip_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def eip_tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of additional tags to add to the eip The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("eip_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def enable_volume_tags(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable volume tags (if enabled it conflicts with root_block_device tags) true.'''
        result = self._values.get("enable_volume_tags")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enclave_options_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether Nitro Enclaves will be enabled on the instance.

        Defaults to ``false``
        '''
        result = self._values.get("enclave_options_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ephemeral_block_device(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''Customize Ephemeral (also known as Instance Store) volumes on the instance.

        The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}
        '''
        result = self._values.get("ephemeral_block_device")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def fetch_password_data(self) -> typing.Optional[builtins.bool]:
        '''If true, wait for password data to become available and retrieve it.'''
        result = self._values.get("fetch_password_data")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def hibernation(self) -> typing.Optional[builtins.bool]:
        '''If true, the launched EC2 instance will support hibernation.'''
        result = self._values.get("hibernation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def host_id(self) -> typing.Optional[builtins.str]:
        '''ID of a dedicated host that the instance will be assigned to.

        Use when an instance is to be launched on a specific dedicated host
        '''
        result = self._values.get("host_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_instance_profile(self) -> typing.Optional[builtins.str]:
        '''IAM Instance Profile to launch the instance with.

        Specified as the name of the Instance Profile
        '''
        result = self._values.get("iam_instance_profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_role_description(self) -> typing.Optional[builtins.str]:
        '''Description of the role.'''
        result = self._values.get("iam_role_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_role_name(self) -> typing.Optional[builtins.str]:
        '''Name to use on IAM role created.'''
        result = self._values.get("iam_role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_role_path(self) -> typing.Optional[builtins.str]:
        '''IAM role path.'''
        result = self._values.get("iam_role_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_role_permissions_boundary(self) -> typing.Optional[builtins.str]:
        '''ARN of the policy that is used to set the permissions boundary for the IAM role.'''
        result = self._values.get("iam_role_permissions_boundary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_role_policies(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Policies attached to the IAM role The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("iam_role_policies")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def iam_role_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of additional tags to add to the IAM role/profile created The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("iam_role_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def iam_role_use_name_prefix(self) -> typing.Optional[builtins.bool]:
        '''Determines whether the IAM role name (``iam_role_name`` or ``name``) is used as a prefix true.'''
        result = self._values.get("iam_role_use_name_prefix")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def ignore_ami_changes(self) -> typing.Optional[builtins.bool]:
        '''Whether changes to the AMI ID changes should be ignored by Terraform.

        Note - changing this value will result in the replacement of the instance
        '''
        result = self._values.get("ignore_ami_changes")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def instance_initiated_shutdown_behavior(self) -> typing.Optional[builtins.str]:
        '''Shutdown behavior for the instance.

        Amazon defaults this to stop for EBS-backed instances and terminate for instance-store instances. Cannot be set on instance-store instance
        '''
        result = self._values.get("instance_initiated_shutdown_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the instance The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("instance_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''The type of instance to start t3.micro.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv6_address_count(self) -> typing.Optional[jsii.Number]:
        '''A number of IPv6 addresses to associate with the primary network interface.

        Amazon EC2 chooses the IPv6 addresses from the range of your subnet
        '''
        result = self._values.get("ipv6_address_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ipv6_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify one or more IPv6 addresses from the range of the subnet to associate with the primary network interface.'''
        result = self._values.get("ipv6_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def key_name(self) -> typing.Optional[builtins.str]:
        '''Key name of the Key Pair to use for the instance;

        which can be managed using the ``aws_key_pair`` resource
        '''
        result = self._values.get("key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_template(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Specifies a Launch Template to configure the instance.

        Parameters configured on this resource will override the corresponding parameters in the Launch Template
        The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}
        '''
        result = self._values.get("launch_template")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def maintenance_options(self) -> typing.Any:
        '''The maintenance options for the instance.'''
        result = self._values.get("maintenance_options")
        return typing.cast(typing.Any, result)

    @builtins.property
    def metadata_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Customize the metadata options of the instance The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("metadata_options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def monitoring(self) -> typing.Optional[builtins.bool]:
        '''If true, the launched EC2 instance will have detailed monitoring enabled.'''
        result = self._values.get("monitoring")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name to be used on EC2 instance created.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_interface(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''Customize network interfaces to be attached at instance boot time.

        The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}
        '''
        result = self._values.get("network_interface")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def placement_group(self) -> typing.Optional[builtins.str]:
        '''The Placement Group to start the instance in.'''
        result = self._values.get("placement_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_dns_name_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Customize the private DNS name options of the instance The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("private_dns_name_options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def private_ip(self) -> typing.Optional[builtins.str]:
        '''Private IP address to associate with the instance in a VPC.'''
        result = self._values.get("private_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def putin_khuylo(self) -> typing.Optional[builtins.bool]:
        '''Do you agree that Putin doesn't respect Ukrainian sovereignty and territorial integrity?

        More info: https://en.wikipedia.org/wiki/Putin_khuylo!
        true
        '''
        result = self._values.get("putin_khuylo")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def root_block_device(self) -> typing.Optional[typing.List[typing.Any]]:
        '''Customize details about the root block device of the instance.

        See Block Devices below for details
        '''
        result = self._values.get("root_block_device")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def secondary_private_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of secondary private IPv4 addresses to assign to the instance's primary network interface (eth0) in a VPC.

        Can only be assigned to the primary network interface (eth0) attached at instance creation, not a pre-existing network interface i.e. referenced in a ``network_interface block``
        '''
        result = self._values.get("secondary_private_ips")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_dest_check(self) -> typing.Optional[builtins.bool]:
        '''Controls if traffic is routed to the instance when the destination address does not match the instance.

        Used for NAT or VPNs
        '''
        result = self._values.get("source_dest_check")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def spot_block_duration_minutes(self) -> typing.Optional[jsii.Number]:
        '''The required duration for the Spot instances, in minutes.

        This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360)
        '''
        result = self._values.get("spot_block_duration_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def spot_instance_interruption_behavior(self) -> typing.Optional[builtins.str]:
        '''Indicates Spot instance behavior when it is interrupted.

        Valid values are ``terminate``, ``stop``, or ``hibernate``
        '''
        result = self._values.get("spot_instance_interruption_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_launch_group(self) -> typing.Optional[builtins.str]:
        '''A launch group is a group of spot instances that launch together and terminate together.

        If left empty instances are launched and terminated individually
        '''
        result = self._values.get("spot_launch_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_price(self) -> typing.Optional[builtins.str]:
        '''The maximum price to request on the spot market.

        Defaults to on-demand price
        '''
        result = self._values.get("spot_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_type(self) -> typing.Optional[builtins.str]:
        '''If set to one-time, after the instance is terminated, the spot request will be closed.

        Default ``persistent``
        '''
        result = self._values.get("spot_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_valid_from(self) -> typing.Optional[builtins.str]:
        '''The start date and time of the request, in UTC RFC3339 format(for example, YYYY-MM-DDTHH:MM:SSZ).'''
        result = self._values.get("spot_valid_from")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_valid_until(self) -> typing.Optional[builtins.str]:
        '''The end date and time of the request, in UTC RFC3339 format(for example, YYYY-MM-DDTHH:MM:SSZ).'''
        result = self._values.get("spot_valid_until")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_wait_for_fulfillment(self) -> typing.Optional[builtins.bool]:
        '''If set, Terraform will wait for the Spot Request to be fulfilled, and will throw an error if the timeout of 10m is reached.'''
        result = self._values.get("spot_wait_for_fulfillment")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''The VPC Subnet ID to launch in.'''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A mapping of tags to assign to the resource The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tenancy(self) -> typing.Optional[builtins.str]:
        '''The tenancy of the instance (if the instance is running in a VPC).

        Available values: default, dedicated, host
        '''
        result = self._values.get("tenancy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Define maximum timeout for creating, updating, and deleting EC2 instance resources The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''The user data to provide when launching the instance.

        Do not pass gzip-compressed data via this argument; see user_data_base64 instead
        '''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_data_base64(self) -> typing.Optional[builtins.str]:
        '''Can be used instead of user_data to pass base64-encoded binary data directly.

        Use this instead of user_data whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption
        '''
        result = self._values.get("user_data_base64")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_data_replace_on_change(self) -> typing.Optional[builtins.bool]:
        '''When used in combination with user_data or user_data_base64 will trigger a destroy and recreate when set to true.

        Defaults to false if not set
        '''
        result = self._values.get("user_data_replace_on_change")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def volume_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A mapping of tags to assign to the devices created by the instance at launch time The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("volume_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security group IDs to associate with.'''
        result = self._values.get("vpc_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2InstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Ec2Instance",
    "Ec2InstanceConfig",
]

publication.publish()

def _typecheckingstub__1c49908fc6353830b69e0c67909cdecbc95ff4bab4bc31e0fef6c3e7abff833d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ami: typing.Optional[builtins.str] = None,
    ami_ssm_parameter: typing.Optional[builtins.str] = None,
    associate_public_ip_address: typing.Optional[builtins.bool] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    capacity_reservation_specification: typing.Any = None,
    cpu_core_count: typing.Optional[jsii.Number] = None,
    cpu_credits: typing.Optional[builtins.str] = None,
    cpu_options: typing.Any = None,
    cpu_threads_per_core: typing.Optional[jsii.Number] = None,
    create: typing.Optional[builtins.bool] = None,
    create_eip: typing.Optional[builtins.bool] = None,
    create_iam_instance_profile: typing.Optional[builtins.bool] = None,
    create_spot_instance: typing.Optional[builtins.bool] = None,
    disable_api_stop: typing.Optional[builtins.bool] = None,
    disable_api_termination: typing.Optional[builtins.bool] = None,
    ebs_block_device: typing.Optional[typing.Sequence[typing.Any]] = None,
    ebs_optimized: typing.Optional[builtins.bool] = None,
    eip_domain: typing.Optional[builtins.str] = None,
    eip_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    enable_volume_tags: typing.Optional[builtins.bool] = None,
    enclave_options_enabled: typing.Optional[builtins.bool] = None,
    ephemeral_block_device: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    fetch_password_data: typing.Optional[builtins.bool] = None,
    hibernation: typing.Optional[builtins.bool] = None,
    host_id: typing.Optional[builtins.str] = None,
    iam_instance_profile: typing.Optional[builtins.str] = None,
    iam_role_description: typing.Optional[builtins.str] = None,
    iam_role_name: typing.Optional[builtins.str] = None,
    iam_role_path: typing.Optional[builtins.str] = None,
    iam_role_permissions_boundary: typing.Optional[builtins.str] = None,
    iam_role_policies: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    iam_role_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    iam_role_use_name_prefix: typing.Optional[builtins.bool] = None,
    ignore_ami_changes: typing.Optional[builtins.bool] = None,
    instance_initiated_shutdown_behavior: typing.Optional[builtins.str] = None,
    instance_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    instance_type: typing.Optional[builtins.str] = None,
    ipv6_address_count: typing.Optional[jsii.Number] = None,
    ipv6_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    key_name: typing.Optional[builtins.str] = None,
    launch_template: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    maintenance_options: typing.Any = None,
    metadata_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    monitoring: typing.Optional[builtins.bool] = None,
    name: typing.Optional[builtins.str] = None,
    network_interface: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    placement_group: typing.Optional[builtins.str] = None,
    private_dns_name_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    private_ip: typing.Optional[builtins.str] = None,
    putin_khuylo: typing.Optional[builtins.bool] = None,
    root_block_device: typing.Optional[typing.Sequence[typing.Any]] = None,
    secondary_private_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_dest_check: typing.Optional[builtins.bool] = None,
    spot_block_duration_minutes: typing.Optional[jsii.Number] = None,
    spot_instance_interruption_behavior: typing.Optional[builtins.str] = None,
    spot_launch_group: typing.Optional[builtins.str] = None,
    spot_price: typing.Optional[builtins.str] = None,
    spot_type: typing.Optional[builtins.str] = None,
    spot_valid_from: typing.Optional[builtins.str] = None,
    spot_valid_until: typing.Optional[builtins.str] = None,
    spot_wait_for_fulfillment: typing.Optional[builtins.bool] = None,
    subnet_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tenancy: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    user_data: typing.Optional[builtins.str] = None,
    user_data_base64: typing.Optional[builtins.str] = None,
    user_data_replace_on_change: typing.Optional[builtins.bool] = None,
    volume_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    providers: typing.Optional[typing.Sequence[typing.Union[_cdktf_9a9027ec.TerraformProvider, typing.Union[_cdktf_9a9027ec.TerraformModuleProvider, typing.Dict[builtins.str, typing.Any]]]]] = None,
    skip_asset_creation_from_local_modules: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c8954bdbfc5a10444da1f10ec452da8973aceed6a45746b5b76c239eafa6d0d(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebe30285e9c787842cc787c3e2e575ade1988ebc20c9d5fceffb3ff2a71be3ca(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6de9a5c08d984067dcdc47954cf12282fd2bf98cca0d2277c87e4213523880c2(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee7264ad4b6897bca758354a94325d5c7628f4033ad618af2add6374f87b1396(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b6377e18a227544a1a9f6e3bdd198a2a4f8305a9071ab41196f7b04deb138bb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd52a1524ee836126c63cfb8622070b10a339ad3d303247119841d0e687fc288(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b3330a4e9202b8f098efdac21e9b2c0f9fd23bc911dabce6ee9eec599e3d8b7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d292897665016afa5c5b927a032c61eb7ce944d38d671bb42b64d78edef60fa(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2494c4f8f1bd166d782e7e99e278e873fbf49302c9f2f08eba66723859085d1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__376180ea154c6a494a4ae471a61408e6a0b5c34438fd73d2bc30d10176ead960(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf7669ef426694ed0f66ca60b0d44ecd5a4b263fd8ec79ecbdd28de5b3dcf439(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abcd19d2224728e350be0e2044655fcc6b657bc8c59ec70a8fd736737cfa8a14(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2addb76579eb1a82b98b8bbe4b03d8bda34c771bfba8ca425138905d16bc137(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f5f4672a41c483c5d63c9945353e8c2b79583b1150058b967056ec886392e36(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14a5eca1df7196c2577c9fdf0645d3b5e7176c194d90118d48911de059297855(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4724c59e8fadbff829870b8998c7e44aba02f221780220bf08b68eee8dedd4df(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5385a7c48e371f3ee2b86236fc5e09e6de849d3f6379b60f8cb5a53143973c37(
    value: typing.Optional[typing.List[typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53696e37b20b66d446953438ae397b9d910fd1071f021a6fedd66e636ee81f66(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__703bf950faa8db57bcf1099aea45b4a1b811174a41f1a110c66da2eeeb7441d9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a56b7b549ae20d297b604217950864f00c506f972e9b57edd776f8da8b4833be(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64719ca7ef322e9e3d9362ae85a3770257e1e2da0704b10166dd2410ddb3e5c0(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a54b45ad1af794cb63bb380a492e2e2f627ad01c20596d2787747cd58c43afe(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a33b602a6b5d897fdb7fd8e230f093b492437633704f0e483ea4ff7743b1182d(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b31c02ce7eb2553be010b3d970c1a332a4051007180fdcd899bee5416d00b6ea(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60a4326ed7ca48c03f114a374e00e0b6eb8fd3e2c52d0e1ece648774aa0c9cc3(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8272bbef7958ab637086709f6ec909af52267a873c339860a9af173a3eb8446e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1591f291e4fc174ba975c5c1bc596177632609e4707d7ffd8471519d6fddae81(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6b9184344fe74872acb8c128c32ce2562c1f4cac348becd9263ed0037369582(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2efdaab6777030185ed492601b38226d2216272b2dda06d3f5c13b97a003d26(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fb651d550b0427098224c6e53665bb08c2e50a3ae508c83092a4e3e717c3c39(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9ed43bf4ec3bc9eec4a8a10d37d6930ab6815ba82d189d4a7ffe381dcb94b89(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f0a7eece83620a18da77af1ae1cb11d4a6d16268907f6e364dabd41d8580ba7(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ffa722dbbf981ddfa636a8831fdf3017d4e7652a65055a6fd09d8a02127b7f7(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6169f4b399ba0df18598c24e5eeba6ca0b22ccc3decf1cb66791e3ef7d4fa406(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2cd4fbfd2d4b6e4585ce176f4240ccd75abcb7f0889720dd74a6b3c1fa7eaca(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__398a4823ac6c819bd554f49539a3d8c4e4788ce4de3ade5c74b2c4e16e2c5a08(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a48d813519214458603e824ced6fb43f766abc478030a242222b1d2bd6ec3c4(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b66131af814d60903e85334452e557337d412951c302559d7ecf98a439061db(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e35657713a9098375b7e36fe6d53675578891c7ebb8dbad1e08df6bd65333de(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9ad279954d00c67e1a31de877696de73e10c0802a6b596cfd28fa6c2c711781(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52dd1412d395b33f7f85a129276ff9d9b03f59f1e9814d7f8ff818dbc49b87b4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deee6c79d4f65c5eb7cd751c5069d7502d40147037172b7695ea02cfcf9d3c94(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36ee7d488c7bd8db1f70837ee6647a9becae4ff739408dd0a67facb85a152282(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98e594bcf20a631574c9d3e3d249bf862d2e17d6e1b2c27d8c5d03b1312bc7ae(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af9d6fe0593f984e8c7bf84175b3db10fa85887d93a60532d0b4904a00f408ae(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c350d6bdeeb81f638695dd1267c87a6a02f4289102fa2379f8fd079d4ab4ce2e(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d7cc84e246e8448c2edab3b9640b95eef0beabeb27ae581592f8f9c3c4af490(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__141b4a8759b7974d78c868323be38b6a4c9ea336b2669c4ce0e06d65070a1542(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62228ec0db5c379e90ec8f0c5d3b8674cf9f5bff0852f6b5f4bb67f7fd786e91(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b354904500dd4d36d0616f9b2c6e254abc747babbea580f18767b2e4bb21aa29(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7517bd1f08cc5c17f50b15a41c59adaec599985b442287794ce13fc7825e5bde(
    value: typing.Optional[typing.List[typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02d23b75ec6208caf0d42c8138c8acc52c877d7b28e941c8dd3b8c36c8545ff4(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a74dc80bf06afd817039d8e0d10f089a3505ea505ff1ee74acaefb3e86ea6d3(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d27fb4e35a1c9972ed4236333d26eded0f2bc011dfd9294b5c0c16daf1acfc5(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b687bc2a6b81aa3fdaf0dd4737df3e77893e35e6fe24093a6de1298528a89ec(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7162d13556540bfdc1a43721c35722966c47ef8b26a81cb2a50ccf7de63ab584(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75d570458e1320701dde746b99ac4883116574f6a937be94f749126f0fab27b4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfdb8082d31d285d2daa782f0ea751c04e09b5d75c68d3dcd4cc2e7109e6a430(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5619160754f7d8776a1b72b1d8f226344a1cff71635c357196ba460178218a66(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c382ad107fa26b608149b830d2bd0d7f9b818794db8d072c6911c085fbb7ffa3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4fe59fc34b24d6a9d34cd9ae42fe71d6f59fda4f7a1524afc426c15a14f9968(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c53c84edba684af533fafb4b15057358b963cb765e93626471f979b2a8165970(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb61c46c544f4195baadae740e485c4c72a52eda0bd2496269ffb8a11e9b91d1(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f709bffc64edf8bff4b6134bc542041abf97d16993281ddc82d004c47f1ca7ba(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__569ae3c25db1781a260348ae519579f508b02a72adc9f1472527a7e43fa05f1e(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7badeb1f0c91ecf157d6d905d37a06f56dc30ec5c7dfb7f04da5fc9c436d9baf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c1c23efd8db42444c01306350a57fdda9e2662d6598a176565b57dce8d84fb9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afcc27f6fe667b376dd84dccd2132c99f68a35e3828fbcddf398a07cdad2481f(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0dcb7ca26abdeab3347d9a743fff0b66fe465da7c9723b561558666b3a940e6(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11d3d87cc615ad1c7fa52982e4f4ba2ab732c1b2fa1ddaff105ca78ff322e4f4(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76c4b8200869d35a0d1f7dc9b992e4cd145268ef7d2f17ff61aef344ca2fb537(
    *,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    providers: typing.Optional[typing.Sequence[typing.Union[_cdktf_9a9027ec.TerraformProvider, typing.Union[_cdktf_9a9027ec.TerraformModuleProvider, typing.Dict[builtins.str, typing.Any]]]]] = None,
    skip_asset_creation_from_local_modules: typing.Optional[builtins.bool] = None,
    ami: typing.Optional[builtins.str] = None,
    ami_ssm_parameter: typing.Optional[builtins.str] = None,
    associate_public_ip_address: typing.Optional[builtins.bool] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    capacity_reservation_specification: typing.Any = None,
    cpu_core_count: typing.Optional[jsii.Number] = None,
    cpu_credits: typing.Optional[builtins.str] = None,
    cpu_options: typing.Any = None,
    cpu_threads_per_core: typing.Optional[jsii.Number] = None,
    create: typing.Optional[builtins.bool] = None,
    create_eip: typing.Optional[builtins.bool] = None,
    create_iam_instance_profile: typing.Optional[builtins.bool] = None,
    create_spot_instance: typing.Optional[builtins.bool] = None,
    disable_api_stop: typing.Optional[builtins.bool] = None,
    disable_api_termination: typing.Optional[builtins.bool] = None,
    ebs_block_device: typing.Optional[typing.Sequence[typing.Any]] = None,
    ebs_optimized: typing.Optional[builtins.bool] = None,
    eip_domain: typing.Optional[builtins.str] = None,
    eip_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    enable_volume_tags: typing.Optional[builtins.bool] = None,
    enclave_options_enabled: typing.Optional[builtins.bool] = None,
    ephemeral_block_device: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    fetch_password_data: typing.Optional[builtins.bool] = None,
    hibernation: typing.Optional[builtins.bool] = None,
    host_id: typing.Optional[builtins.str] = None,
    iam_instance_profile: typing.Optional[builtins.str] = None,
    iam_role_description: typing.Optional[builtins.str] = None,
    iam_role_name: typing.Optional[builtins.str] = None,
    iam_role_path: typing.Optional[builtins.str] = None,
    iam_role_permissions_boundary: typing.Optional[builtins.str] = None,
    iam_role_policies: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    iam_role_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    iam_role_use_name_prefix: typing.Optional[builtins.bool] = None,
    ignore_ami_changes: typing.Optional[builtins.bool] = None,
    instance_initiated_shutdown_behavior: typing.Optional[builtins.str] = None,
    instance_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    instance_type: typing.Optional[builtins.str] = None,
    ipv6_address_count: typing.Optional[jsii.Number] = None,
    ipv6_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    key_name: typing.Optional[builtins.str] = None,
    launch_template: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    maintenance_options: typing.Any = None,
    metadata_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    monitoring: typing.Optional[builtins.bool] = None,
    name: typing.Optional[builtins.str] = None,
    network_interface: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    placement_group: typing.Optional[builtins.str] = None,
    private_dns_name_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    private_ip: typing.Optional[builtins.str] = None,
    putin_khuylo: typing.Optional[builtins.bool] = None,
    root_block_device: typing.Optional[typing.Sequence[typing.Any]] = None,
    secondary_private_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_dest_check: typing.Optional[builtins.bool] = None,
    spot_block_duration_minutes: typing.Optional[jsii.Number] = None,
    spot_instance_interruption_behavior: typing.Optional[builtins.str] = None,
    spot_launch_group: typing.Optional[builtins.str] = None,
    spot_price: typing.Optional[builtins.str] = None,
    spot_type: typing.Optional[builtins.str] = None,
    spot_valid_from: typing.Optional[builtins.str] = None,
    spot_valid_until: typing.Optional[builtins.str] = None,
    spot_wait_for_fulfillment: typing.Optional[builtins.bool] = None,
    subnet_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tenancy: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    user_data: typing.Optional[builtins.str] = None,
    user_data_base64: typing.Optional[builtins.str] = None,
    user_data_replace_on_change: typing.Optional[builtins.bool] = None,
    volume_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
