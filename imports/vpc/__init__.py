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


class Vpc(
    _cdktf_9a9027ec.TerraformModule,
    metaclass=jsii.JSIIMeta,
    jsii_type="vpc.Vpc",
):
    '''Defines an Vpc based on a Terraform module.

    Docs at Terraform Registry: {@link https://registry.terraform.io/modules/terraform-aws-modules/vpc/aws/latest terraform-aws-modules/vpc/aws}
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        amazon_side_asn: typing.Optional[builtins.str] = None,
        azs: typing.Optional[typing.Sequence[builtins.str]] = None,
        cidr: typing.Optional[builtins.str] = None,
        create_database_internet_gateway_route: typing.Optional[builtins.bool] = None,
        create_database_nat_gateway_route: typing.Optional[builtins.bool] = None,
        create_database_subnet_group: typing.Optional[builtins.bool] = None,
        create_database_subnet_route_table: typing.Optional[builtins.bool] = None,
        create_egress_only_igw: typing.Optional[builtins.bool] = None,
        create_elasticache_subnet_group: typing.Optional[builtins.bool] = None,
        create_elasticache_subnet_route_table: typing.Optional[builtins.bool] = None,
        create_flow_log_cloudwatch_iam_role: typing.Optional[builtins.bool] = None,
        create_flow_log_cloudwatch_log_group: typing.Optional[builtins.bool] = None,
        create_igw: typing.Optional[builtins.bool] = None,
        create_multiple_intra_route_tables: typing.Optional[builtins.bool] = None,
        create_multiple_public_route_tables: typing.Optional[builtins.bool] = None,
        create_private_nat_gateway_route: typing.Optional[builtins.bool] = None,
        create_redshift_subnet_group: typing.Optional[builtins.bool] = None,
        create_redshift_subnet_route_table: typing.Optional[builtins.bool] = None,
        create_vpc: typing.Optional[builtins.bool] = None,
        customer_gateways: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]] = None,
        customer_gateway_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        customer_owned_ipv4_pool: typing.Optional[builtins.str] = None,
        database_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        database_dedicated_network_acl: typing.Optional[builtins.bool] = None,
        database_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        database_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        database_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        database_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
        database_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
        database_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
        database_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
        database_subnet_group_name: typing.Optional[builtins.str] = None,
        database_subnet_group_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        database_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
        database_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        database_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        database_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
        database_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        database_subnet_suffix: typing.Optional[builtins.str] = None,
        database_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        default_network_acl_egress: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        default_network_acl_ingress: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        default_network_acl_name: typing.Optional[builtins.str] = None,
        default_network_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        default_route_table_name: typing.Optional[builtins.str] = None,
        default_route_table_propagating_vgws: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_route_table_routes: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        default_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        default_security_group_egress: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        default_security_group_ingress: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        default_security_group_name: typing.Optional[builtins.str] = None,
        default_security_group_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        default_vpc_enable_dns_hostnames: typing.Optional[builtins.bool] = None,
        default_vpc_enable_dns_support: typing.Optional[builtins.bool] = None,
        default_vpc_name: typing.Optional[builtins.str] = None,
        default_vpc_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        dhcp_options_domain_name: typing.Optional[builtins.str] = None,
        dhcp_options_domain_name_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        dhcp_options_ipv6_address_preferred_lease_time: typing.Optional[jsii.Number] = None,
        dhcp_options_netbios_name_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        dhcp_options_netbios_node_type: typing.Optional[builtins.str] = None,
        dhcp_options_ntp_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        dhcp_options_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        elasticache_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        elasticache_dedicated_network_acl: typing.Optional[builtins.bool] = None,
        elasticache_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        elasticache_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        elasticache_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        elasticache_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
        elasticache_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
        elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
        elasticache_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
        elasticache_subnet_group_name: typing.Optional[builtins.str] = None,
        elasticache_subnet_group_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        elasticache_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
        elasticache_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        elasticache_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        elasticache_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
        elasticache_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        elasticache_subnet_suffix: typing.Optional[builtins.str] = None,
        elasticache_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        enable_dhcp_options: typing.Optional[builtins.bool] = None,
        enable_dns_hostnames: typing.Optional[builtins.bool] = None,
        enable_dns_support: typing.Optional[builtins.bool] = None,
        enable_flow_log: typing.Optional[builtins.bool] = None,
        enable_ipv6: typing.Optional[builtins.bool] = None,
        enable_nat_gateway: typing.Optional[builtins.bool] = None,
        enable_network_address_usage_metrics: typing.Optional[builtins.bool] = None,
        enable_public_redshift: typing.Optional[builtins.bool] = None,
        enable_vpn_gateway: typing.Optional[builtins.bool] = None,
        external_nat_ip_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        external_nat_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        flow_log_cloudwatch_iam_role_arn: typing.Optional[builtins.str] = None,
        flow_log_cloudwatch_iam_role_conditions: typing.Any = None,
        flow_log_cloudwatch_log_group_class: typing.Optional[builtins.str] = None,
        flow_log_cloudwatch_log_group_kms_key_id: typing.Optional[builtins.str] = None,
        flow_log_cloudwatch_log_group_name_prefix: typing.Optional[builtins.str] = None,
        flow_log_cloudwatch_log_group_name_suffix: typing.Optional[builtins.str] = None,
        flow_log_cloudwatch_log_group_retention_in_days: typing.Optional[jsii.Number] = None,
        flow_log_cloudwatch_log_group_skip_destroy: typing.Optional[builtins.bool] = None,
        flow_log_deliver_cross_account_role: typing.Optional[builtins.str] = None,
        flow_log_destination_arn: typing.Optional[builtins.str] = None,
        flow_log_destination_type: typing.Optional[builtins.str] = None,
        flow_log_file_format: typing.Optional[builtins.str] = None,
        flow_log_hive_compatible_partitions: typing.Optional[builtins.bool] = None,
        flow_log_log_format: typing.Optional[builtins.str] = None,
        flow_log_max_aggregation_interval: typing.Optional[jsii.Number] = None,
        flow_log_per_hour_partition: typing.Optional[builtins.bool] = None,
        flow_log_traffic_type: typing.Optional[builtins.str] = None,
        igw_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instance_tenancy: typing.Optional[builtins.str] = None,
        intra_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        intra_dedicated_network_acl: typing.Optional[builtins.bool] = None,
        intra_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        intra_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        intra_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        intra_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
        intra_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
        intra_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
        intra_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
        intra_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
        intra_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        intra_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        intra_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
        intra_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        intra_subnet_suffix: typing.Optional[builtins.str] = None,
        intra_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ipv4_ipam_pool_id: typing.Optional[builtins.str] = None,
        ipv4_netmask_length: typing.Optional[jsii.Number] = None,
        ipv6_cidr: typing.Optional[builtins.str] = None,
        ipv6_cidr_block_network_border_group: typing.Optional[builtins.str] = None,
        ipv6_ipam_pool_id: typing.Optional[builtins.str] = None,
        ipv6_netmask_length: typing.Optional[jsii.Number] = None,
        manage_default_network_acl: typing.Optional[builtins.bool] = None,
        manage_default_route_table: typing.Optional[builtins.bool] = None,
        manage_default_security_group: typing.Optional[builtins.bool] = None,
        manage_default_vpc: typing.Optional[builtins.bool] = None,
        map_customer_owned_ip_on_launch: typing.Optional[builtins.bool] = None,
        map_public_ip_on_launch: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
        nat_eip_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        nat_gateway_destination_cidr_block: typing.Optional[builtins.str] = None,
        nat_gateway_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        one_nat_gateway_per_az: typing.Optional[builtins.bool] = None,
        outpost_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        outpost_arn: typing.Optional[builtins.str] = None,
        outpost_az: typing.Optional[builtins.str] = None,
        outpost_dedicated_network_acl: typing.Optional[builtins.bool] = None,
        outpost_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        outpost_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        outpost_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
        outpost_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
        outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
        outpost_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
        outpost_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
        outpost_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        outpost_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        outpost_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
        outpost_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        outpost_subnet_suffix: typing.Optional[builtins.str] = None,
        outpost_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        private_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        private_dedicated_network_acl: typing.Optional[builtins.bool] = None,
        private_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        private_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        private_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        private_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
        private_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
        private_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
        private_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
        private_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
        private_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        private_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        private_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
        private_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        private_subnet_suffix: typing.Optional[builtins.str] = None,
        private_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        private_subnet_tags_per_az: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]] = None,
        propagate_intra_route_tables_vgw: typing.Optional[builtins.bool] = None,
        propagate_private_route_tables_vgw: typing.Optional[builtins.bool] = None,
        propagate_public_route_tables_vgw: typing.Optional[builtins.bool] = None,
        public_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        public_dedicated_network_acl: typing.Optional[builtins.bool] = None,
        public_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        public_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        public_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        public_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
        public_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
        public_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
        public_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
        public_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
        public_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        public_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        public_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
        public_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        public_subnet_suffix: typing.Optional[builtins.str] = None,
        public_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        public_subnet_tags_per_az: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]] = None,
        putin_khuylo: typing.Optional[builtins.bool] = None,
        redshift_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        redshift_dedicated_network_acl: typing.Optional[builtins.bool] = None,
        redshift_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        redshift_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        redshift_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        redshift_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
        redshift_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
        redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
        redshift_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
        redshift_subnet_group_name: typing.Optional[builtins.str] = None,
        redshift_subnet_group_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        redshift_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
        redshift_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        redshift_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        redshift_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
        redshift_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        redshift_subnet_suffix: typing.Optional[builtins.str] = None,
        redshift_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        reuse_nat_ips: typing.Optional[builtins.bool] = None,
        secondary_cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
        single_nat_gateway: typing.Optional[builtins.bool] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        use_ipam_pool: typing.Optional[builtins.bool] = None,
        vpc_flow_log_iam_policy_name: typing.Optional[builtins.str] = None,
        vpc_flow_log_iam_policy_use_name_prefix: typing.Optional[builtins.bool] = None,
        vpc_flow_log_iam_role_name: typing.Optional[builtins.str] = None,
        vpc_flow_log_iam_role_use_name_prefix: typing.Optional[builtins.bool] = None,
        vpc_flow_log_permissions_boundary: typing.Optional[builtins.str] = None,
        vpc_flow_log_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpn_gateway_az: typing.Optional[builtins.str] = None,
        vpn_gateway_id: typing.Optional[builtins.str] = None,
        vpn_gateway_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        providers: typing.Optional[typing.Sequence[typing.Union[_cdktf_9a9027ec.TerraformProvider, typing.Union[_cdktf_9a9027ec.TerraformModuleProvider, typing.Dict[builtins.str, typing.Any]]]]] = None,
        skip_asset_creation_from_local_modules: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param amazon_side_asn: The Autonomous System Number (ASN) for the Amazon side of the gateway. By default the virtual private gateway is created with the current default Amazon ASN 64512
        :param azs: A list of availability zones names or ids in the region.
        :param cidr: (Optional) The IPv4 CIDR block for the VPC. CIDR can be explicitly set or it can be derived from IPAM using ``ipv4_netmask_length`` & ``ipv4_ipam_pool_id`` 10.0.0.0/16
        :param create_database_internet_gateway_route: Controls if an internet gateway route for public database access should be created.
        :param create_database_nat_gateway_route: Controls if a nat gateway route should be created to give internet access to the database subnets.
        :param create_database_subnet_group: Controls if database subnet group should be created (n.b. database_subnets must also be set) true.
        :param create_database_subnet_route_table: Controls if separate route table for database should be created.
        :param create_egress_only_igw: Controls if an Egress Only Internet Gateway is created and its related routes true.
        :param create_elasticache_subnet_group: Controls if elasticache subnet group should be created true.
        :param create_elasticache_subnet_route_table: Controls if separate route table for elasticache should be created.
        :param create_flow_log_cloudwatch_iam_role: Whether to create IAM role for VPC Flow Logs.
        :param create_flow_log_cloudwatch_log_group: Whether to create CloudWatch log group for VPC Flow Logs.
        :param create_igw: Controls if an Internet Gateway is created for public subnets and the related routes that connect them true.
        :param create_multiple_intra_route_tables: Indicates whether to create a separate route table for each intra subnet. Default: ``false``
        :param create_multiple_public_route_tables: Indicates whether to create a separate route table for each public subnet. Default: ``false``
        :param create_private_nat_gateway_route: Controls if a nat gateway route should be created to give internet access to the private subnets true.
        :param create_redshift_subnet_group: Controls if redshift subnet group should be created true.
        :param create_redshift_subnet_route_table: Controls if separate route table for redshift should be created.
        :param create_vpc: Controls if VPC should be created (it affects almost all resources) true.
        :param customer_gateways: Maps of Customer Gateway's attributes (BGP ASN and Gateway's Internet-routable external IP address) The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param customer_gateway_tags: Additional tags for the Customer Gateway The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param customer_owned_ipv4_pool: The customer owned IPv4 address pool. Typically used with the ``map_customer_owned_ip_on_launch`` argument. The ``outpost_arn`` argument must be specified when configured
        :param database_acl_tags: Additional tags for the database subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param database_dedicated_network_acl: Whether to use dedicated network ACL (not default) and custom rules for database subnets.
        :param database_inbound_acl_rules: Database subnets inbound network ACL rules [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param database_outbound_acl_rules: Database subnets outbound network ACL rules [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param database_route_table_tags: Additional tags for the database route tables The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param database_subnet_assign_ipv6_address_on_creation: Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. Default is ``false``
        :param database_subnet_enable_dns64: Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. Default: ``true`` true
        :param database_subnet_enable_resource_name_dns_aaaa_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records. Default: ``true`` true
        :param database_subnet_enable_resource_name_dns_a_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS A records. Default: ``false``
        :param database_subnet_group_name: Name of database subnet group.
        :param database_subnet_group_tags: Additional tags for the database subnet group The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param database_subnet_ipv6_native: Indicates whether to create an IPv6-only subnet. Default: ``false``
        :param database_subnet_ipv6_prefixes: Assigns IPv6 database subnet id based on the Amazon provided /56 prefix base 10 integer (0-256). Must be of equal length to the corresponding IPv4 subnet list
        :param database_subnet_names: Explicit values to use in the Name tag on database subnets. If empty, Name tags are generated
        :param database_subnet_private_dns_hostname_type_on_launch: The type of hostnames to assign to instances in the subnet at launch. For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        :param database_subnets: A list of database subnets inside the VPC.
        :param database_subnet_suffix: Suffix to append to database subnets name db.
        :param database_subnet_tags: Additional tags for the database subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param default_network_acl_egress: List of maps of egress rules to set on the Default Network ACL [object Object] [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param default_network_acl_ingress: List of maps of ingress rules to set on the Default Network ACL [object Object] [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param default_network_acl_name: Name to be used on the Default Network ACL.
        :param default_network_acl_tags: Additional tags for the Default Network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param default_route_table_name: Name to be used on the default route table.
        :param default_route_table_propagating_vgws: List of virtual gateways for propagation.
        :param default_route_table_routes: Configuration block of routes. See https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/default_route_table#route. The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}
        :param default_route_table_tags: Additional tags for the default route table The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param default_security_group_egress: List of maps of egress rules to set on the default security group. The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}
        :param default_security_group_ingress: List of maps of ingress rules to set on the default security group. The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}
        :param default_security_group_name: Name to be used on the default security group.
        :param default_security_group_tags: Additional tags for the default security group The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param default_vpc_enable_dns_hostnames: Should be true to enable DNS hostnames in the Default VPC true.
        :param default_vpc_enable_dns_support: Should be true to enable DNS support in the Default VPC true.
        :param default_vpc_name: Name to be used on the Default VPC.
        :param default_vpc_tags: Additional tags for the Default VPC The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param dhcp_options_domain_name: Specifies DNS name for DHCP options set (requires enable_dhcp_options set to true).
        :param dhcp_options_domain_name_servers: Specify a list of DNS server addresses for DHCP options set, default to AWS provided (requires enable_dhcp_options set to true) AmazonProvidedDNS.
        :param dhcp_options_ipv6_address_preferred_lease_time: How frequently, in seconds, a running instance with an IPv6 assigned to it goes through DHCPv6 lease renewal (requires enable_dhcp_options set to true).
        :param dhcp_options_netbios_name_servers: Specify a list of netbios servers for DHCP options set (requires enable_dhcp_options set to true).
        :param dhcp_options_netbios_node_type: Specify netbios node_type for DHCP options set (requires enable_dhcp_options set to true).
        :param dhcp_options_ntp_servers: Specify a list of NTP servers for DHCP options set (requires enable_dhcp_options set to true).
        :param dhcp_options_tags: Additional tags for the DHCP option set (requires enable_dhcp_options set to true) The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param elasticache_acl_tags: Additional tags for the elasticache subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param elasticache_dedicated_network_acl: Whether to use dedicated network ACL (not default) and custom rules for elasticache subnets.
        :param elasticache_inbound_acl_rules: Elasticache subnets inbound network ACL rules [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param elasticache_outbound_acl_rules: Elasticache subnets outbound network ACL rules [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param elasticache_route_table_tags: Additional tags for the elasticache route tables The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param elasticache_subnet_assign_ipv6_address_on_creation: Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. Default is ``false``
        :param elasticache_subnet_enable_dns64: Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. Default: ``true`` true
        :param elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records. Default: ``true`` true
        :param elasticache_subnet_enable_resource_name_dns_a_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS A records. Default: ``false``
        :param elasticache_subnet_group_name: Name of elasticache subnet group.
        :param elasticache_subnet_group_tags: Additional tags for the elasticache subnet group The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param elasticache_subnet_ipv6_native: Indicates whether to create an IPv6-only subnet. Default: ``false``
        :param elasticache_subnet_ipv6_prefixes: Assigns IPv6 elasticache subnet id based on the Amazon provided /56 prefix base 10 integer (0-256). Must be of equal length to the corresponding IPv4 subnet list
        :param elasticache_subnet_names: Explicit values to use in the Name tag on elasticache subnets. If empty, Name tags are generated
        :param elasticache_subnet_private_dns_hostname_type_on_launch: The type of hostnames to assign to instances in the subnet at launch. For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        :param elasticache_subnets: A list of elasticache subnets inside the VPC.
        :param elasticache_subnet_suffix: Suffix to append to elasticache subnets name elasticache.
        :param elasticache_subnet_tags: Additional tags for the elasticache subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param enable_dhcp_options: Should be true if you want to specify a DHCP options set with a custom domain name, DNS servers, NTP servers, netbios servers, and/or netbios server type.
        :param enable_dns_hostnames: Should be true to enable DNS hostnames in the VPC true.
        :param enable_dns_support: Should be true to enable DNS support in the VPC true.
        :param enable_flow_log: Whether or not to enable VPC Flow Logs.
        :param enable_ipv6: Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or the size of the CIDR block
        :param enable_nat_gateway: Should be true if you want to provision NAT Gateways for each of your private networks.
        :param enable_network_address_usage_metrics: Determines whether network address usage metrics are enabled for the VPC.
        :param enable_public_redshift: Controls if redshift should have public routing table.
        :param enable_vpn_gateway: Should be true if you want to create a new VPN Gateway resource and attach it to the VPC.
        :param external_nat_ip_ids: List of EIP IDs to be assigned to the NAT Gateways (used in combination with reuse_nat_ips).
        :param external_nat_ips: List of EIPs to be used for ``nat_public_ips`` output (used in combination with reuse_nat_ips and external_nat_ip_ids).
        :param flow_log_cloudwatch_iam_role_arn: The ARN for the IAM role that's used to post flow logs to a CloudWatch Logs log group. When flow_log_destination_arn is set to ARN of Cloudwatch Logs, this argument needs to be provided
        :param flow_log_cloudwatch_iam_role_conditions: Additional conditions of the CloudWatch role assumption policy.
        :param flow_log_cloudwatch_log_group_class: Specified the log class of the log group. Possible values are: STANDARD or INFREQUENT_ACCESS
        :param flow_log_cloudwatch_log_group_kms_key_id: The ARN of the KMS Key to use when encrypting log data for VPC flow logs.
        :param flow_log_cloudwatch_log_group_name_prefix: Specifies the name prefix of CloudWatch Log Group for VPC flow logs /aws/vpc-flow-log/.
        :param flow_log_cloudwatch_log_group_name_suffix: Specifies the name suffix of CloudWatch Log Group for VPC flow logs.
        :param flow_log_cloudwatch_log_group_retention_in_days: Specifies the number of days you want to retain log events in the specified log group for VPC flow logs.
        :param flow_log_cloudwatch_log_group_skip_destroy: Set to true if you do not wish the log group (and any logs it may contain) to be deleted at destroy time, and instead just remove the log group from the Terraform state.
        :param flow_log_deliver_cross_account_role: (Optional) ARN of the IAM role that allows Amazon EC2 to publish flow logs across accounts.
        :param flow_log_destination_arn: The ARN of the CloudWatch log group or S3 bucket where VPC Flow Logs will be pushed. If this ARN is a S3 bucket the appropriate permissions need to be set on that bucket's policy. When create_flow_log_cloudwatch_log_group is set to false this argument must be provided
        :param flow_log_destination_type: Type of flow log destination. Can be s3, kinesis-data-firehose or cloud-watch-logs cloud-watch-logs
        :param flow_log_file_format: (Optional) The format for the flow log. Valid values: ``plain-text``, ``parquet``
        :param flow_log_hive_compatible_partitions: (Optional) Indicates whether to use Hive-compatible prefixes for flow logs stored in Amazon S3.
        :param flow_log_log_format: The fields to include in the flow log record, in the order in which they should appear.
        :param flow_log_max_aggregation_interval: The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. Valid Values: ``60`` seconds or ``600`` seconds 600
        :param flow_log_per_hour_partition: (Optional) Indicates whether to partition the flow log per hour. This reduces the cost and response time for queries
        :param flow_log_traffic_type: The type of traffic to capture. Valid values: ACCEPT, REJECT, ALL ALL
        :param igw_tags: Additional tags for the internet gateway The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param instance_tenancy: A tenancy option for instances launched into the VPC default.
        :param intra_acl_tags: Additional tags for the intra subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param intra_dedicated_network_acl: Whether to use dedicated network ACL (not default) and custom rules for intra subnets.
        :param intra_inbound_acl_rules: Intra subnets inbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param intra_outbound_acl_rules: Intra subnets outbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param intra_route_table_tags: Additional tags for the intra route tables The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param intra_subnet_assign_ipv6_address_on_creation: Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. Default is ``false``
        :param intra_subnet_enable_dns64: Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. Default: ``true`` true
        :param intra_subnet_enable_resource_name_dns_aaaa_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records. Default: ``true`` true
        :param intra_subnet_enable_resource_name_dns_a_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS A records. Default: ``false``
        :param intra_subnet_ipv6_native: Indicates whether to create an IPv6-only subnet. Default: ``false``
        :param intra_subnet_ipv6_prefixes: Assigns IPv6 intra subnet id based on the Amazon provided /56 prefix base 10 integer (0-256). Must be of equal length to the corresponding IPv4 subnet list
        :param intra_subnet_names: Explicit values to use in the Name tag on intra subnets. If empty, Name tags are generated
        :param intra_subnet_private_dns_hostname_type_on_launch: The type of hostnames to assign to instances in the subnet at launch. For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        :param intra_subnets: A list of intra subnets inside the VPC.
        :param intra_subnet_suffix: Suffix to append to intra subnets name intra.
        :param intra_subnet_tags: Additional tags for the intra subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param ipv4_ipam_pool_id: (Optional) The ID of an IPv4 IPAM pool you want to use for allocating this VPC's CIDR.
        :param ipv4_netmask_length: (Optional) The netmask length of the IPv4 CIDR you want to allocate to this VPC. Requires specifying a ipv4_ipam_pool_id
        :param ipv6_cidr: (Optional) IPv6 CIDR block to request from an IPAM Pool. Can be set explicitly or derived from IPAM using ``ipv6_netmask_length``
        :param ipv6_cidr_block_network_border_group: By default when an IPv6 CIDR is assigned to a VPC a default ipv6_cidr_block_network_border_group will be set to the region of the VPC. This can be changed to restrict advertisement of public addresses to specific Network Border Groups such as LocalZones
        :param ipv6_ipam_pool_id: (Optional) IPAM Pool ID for a IPv6 pool. Conflicts with ``assign_generated_ipv6_cidr_block``
        :param ipv6_netmask_length: (Optional) Netmask length to request from IPAM Pool. Conflicts with ``ipv6_cidr_block``. This can be omitted if IPAM pool as a ``allocation_default_netmask_length`` set. Valid values: ``56``
        :param manage_default_network_acl: Should be true to adopt and manage Default Network ACL true.
        :param manage_default_route_table: Should be true to manage default route table true.
        :param manage_default_security_group: Should be true to adopt and manage default security group true.
        :param manage_default_vpc: Should be true to adopt and manage Default VPC.
        :param map_customer_owned_ip_on_launch: Specify true to indicate that network interfaces created in the subnet should be assigned a customer owned IP address. The ``customer_owned_ipv4_pool`` and ``outpost_arn`` arguments must be specified when set to ``true``. Default is ``false``
        :param map_public_ip_on_launch: Specify true to indicate that instances launched into the subnet should be assigned a public IP address. Default is ``false``
        :param name: Name to be used on all the resources as identifier.
        :param nat_eip_tags: Additional tags for the NAT EIP The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param nat_gateway_destination_cidr_block: Used to pass a custom destination route for private NAT Gateway. If not specified, the default 0.0.0.0/0 is used as a destination route 0.0.0.0/0
        :param nat_gateway_tags: Additional tags for the NAT gateways The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param one_nat_gateway_per_az: Should be true if you want only one NAT Gateway per availability zone. Requires ``var.azs`` to be set, and the number of ``public_subnets`` created to be greater than or equal to the number of availability zones specified in ``var.azs``
        :param outpost_acl_tags: Additional tags for the outpost subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param outpost_arn: ARN of Outpost you want to create a subnet in.
        :param outpost_az: AZ where Outpost is anchored.
        :param outpost_dedicated_network_acl: Whether to use dedicated network ACL (not default) and custom rules for outpost subnets.
        :param outpost_inbound_acl_rules: Outpost subnets inbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param outpost_outbound_acl_rules: Outpost subnets outbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param outpost_subnet_assign_ipv6_address_on_creation: Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. Default is ``false``
        :param outpost_subnet_enable_dns64: Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. Default: ``true`` true
        :param outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records. Default: ``true`` true
        :param outpost_subnet_enable_resource_name_dns_a_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS A records. Default: ``false``
        :param outpost_subnet_ipv6_native: Indicates whether to create an IPv6-only subnet. Default: ``false``
        :param outpost_subnet_ipv6_prefixes: Assigns IPv6 outpost subnet id based on the Amazon provided /56 prefix base 10 integer (0-256). Must be of equal length to the corresponding IPv4 subnet list
        :param outpost_subnet_names: Explicit values to use in the Name tag on outpost subnets. If empty, Name tags are generated
        :param outpost_subnet_private_dns_hostname_type_on_launch: The type of hostnames to assign to instances in the subnet at launch. For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        :param outpost_subnets: A list of outpost subnets inside the VPC.
        :param outpost_subnet_suffix: Suffix to append to outpost subnets name outpost.
        :param outpost_subnet_tags: Additional tags for the outpost subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param private_acl_tags: Additional tags for the private subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param private_dedicated_network_acl: Whether to use dedicated network ACL (not default) and custom rules for private subnets.
        :param private_inbound_acl_rules: Private subnets inbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param private_outbound_acl_rules: Private subnets outbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param private_route_table_tags: Additional tags for the private route tables The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param private_subnet_assign_ipv6_address_on_creation: Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. Default is ``false``
        :param private_subnet_enable_dns64: Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. Default: ``true`` true
        :param private_subnet_enable_resource_name_dns_aaaa_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records. Default: ``true`` true
        :param private_subnet_enable_resource_name_dns_a_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS A records. Default: ``false``
        :param private_subnet_ipv6_native: Indicates whether to create an IPv6-only subnet. Default: ``false``
        :param private_subnet_ipv6_prefixes: Assigns IPv6 private subnet id based on the Amazon provided /56 prefix base 10 integer (0-256). Must be of equal length to the corresponding IPv4 subnet list
        :param private_subnet_names: Explicit values to use in the Name tag on private subnets. If empty, Name tags are generated
        :param private_subnet_private_dns_hostname_type_on_launch: The type of hostnames to assign to instances in the subnet at launch. For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        :param private_subnets: A list of private subnets inside the VPC.
        :param private_subnet_suffix: Suffix to append to private subnets name private.
        :param private_subnet_tags: Additional tags for the private subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param private_subnet_tags_per_az: Additional tags for the private subnets where the primary key is the AZ The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param propagate_intra_route_tables_vgw: Should be true if you want route table propagation.
        :param propagate_private_route_tables_vgw: Should be true if you want route table propagation.
        :param propagate_public_route_tables_vgw: Should be true if you want route table propagation.
        :param public_acl_tags: Additional tags for the public subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param public_dedicated_network_acl: Whether to use dedicated network ACL (not default) and custom rules for public subnets.
        :param public_inbound_acl_rules: Public subnets inbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param public_outbound_acl_rules: Public subnets outbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param public_route_table_tags: Additional tags for the public route tables The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param public_subnet_assign_ipv6_address_on_creation: Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. Default is ``false``
        :param public_subnet_enable_dns64: Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. Default: ``true`` true
        :param public_subnet_enable_resource_name_dns_aaaa_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records. Default: ``true`` true
        :param public_subnet_enable_resource_name_dns_a_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS A records. Default: ``false``
        :param public_subnet_ipv6_native: Indicates whether to create an IPv6-only subnet. Default: ``false``
        :param public_subnet_ipv6_prefixes: Assigns IPv6 public subnet id based on the Amazon provided /56 prefix base 10 integer (0-256). Must be of equal length to the corresponding IPv4 subnet list
        :param public_subnet_names: Explicit values to use in the Name tag on public subnets. If empty, Name tags are generated
        :param public_subnet_private_dns_hostname_type_on_launch: The type of hostnames to assign to instances in the subnet at launch. For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        :param public_subnets: A list of public subnets inside the VPC.
        :param public_subnet_suffix: Suffix to append to public subnets name public.
        :param public_subnet_tags: Additional tags for the public subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param public_subnet_tags_per_az: Additional tags for the public subnets where the primary key is the AZ The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param putin_khuylo: Do you agree that Putin doesn't respect Ukrainian sovereignty and territorial integrity? More info: https://en.wikipedia.org/wiki/Putin_khuylo! true
        :param redshift_acl_tags: Additional tags for the redshift subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param redshift_dedicated_network_acl: Whether to use dedicated network ACL (not default) and custom rules for redshift subnets.
        :param redshift_inbound_acl_rules: Redshift subnets inbound network ACL rules [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param redshift_outbound_acl_rules: Redshift subnets outbound network ACL rules [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param redshift_route_table_tags: Additional tags for the redshift route tables The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param redshift_subnet_assign_ipv6_address_on_creation: Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. Default is ``false``
        :param redshift_subnet_enable_dns64: Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. Default: ``true`` true
        :param redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records. Default: ``true`` true
        :param redshift_subnet_enable_resource_name_dns_a_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS A records. Default: ``false``
        :param redshift_subnet_group_name: Name of redshift subnet group.
        :param redshift_subnet_group_tags: Additional tags for the redshift subnet group The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param redshift_subnet_ipv6_native: Indicates whether to create an IPv6-only subnet. Default: ``false``
        :param redshift_subnet_ipv6_prefixes: Assigns IPv6 redshift subnet id based on the Amazon provided /56 prefix base 10 integer (0-256). Must be of equal length to the corresponding IPv4 subnet list
        :param redshift_subnet_names: Explicit values to use in the Name tag on redshift subnets. If empty, Name tags are generated
        :param redshift_subnet_private_dns_hostname_type_on_launch: The type of hostnames to assign to instances in the subnet at launch. For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        :param redshift_subnets: A list of redshift subnets inside the VPC.
        :param redshift_subnet_suffix: Suffix to append to redshift subnets name redshift.
        :param redshift_subnet_tags: Additional tags for the redshift subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param reuse_nat_ips: Should be true if you don't want EIPs to be created for your NAT Gateways and will instead pass them in via the 'external_nat_ip_ids' variable.
        :param secondary_cidr_blocks: List of secondary CIDR blocks to associate with the VPC to extend the IP Address pool.
        :param single_nat_gateway: Should be true if you want to provision a single shared NAT Gateway across all of your private networks.
        :param tags: A map of tags to add to all resources The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param use_ipam_pool: Determines whether IPAM pool is used for CIDR allocation.
        :param vpc_flow_log_iam_policy_name: Name of the IAM policy vpc-flow-log-to-cloudwatch.
        :param vpc_flow_log_iam_policy_use_name_prefix: Determines whether the name of the IAM policy (``vpc_flow_log_iam_policy_name``) is used as a prefix true.
        :param vpc_flow_log_iam_role_name: Name to use on the VPC Flow Log IAM role created vpc-flow-log-role.
        :param vpc_flow_log_iam_role_use_name_prefix: Determines whether the IAM role name (``vpc_flow_log_iam_role_name_name``) is used as a prefix true.
        :param vpc_flow_log_permissions_boundary: The ARN of the Permissions Boundary for the VPC Flow Log IAM Role.
        :param vpc_flow_log_tags: Additional tags for the VPC Flow Logs The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param vpc_tags: Additional tags for the VPC The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param vpn_gateway_az: The Availability Zone for the VPN Gateway.
        :param vpn_gateway_id: ID of VPN Gateway to attach to the VPC.
        :param vpn_gateway_tags: Additional tags for the VPN gateway The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param depends_on: 
        :param for_each: 
        :param providers: 
        :param skip_asset_creation_from_local_modules: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36262b54abea07d1a172b2d0b5222f418075eb67faf564af87b2e528b06d12f6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = VpcConfig(
            amazon_side_asn=amazon_side_asn,
            azs=azs,
            cidr=cidr,
            create_database_internet_gateway_route=create_database_internet_gateway_route,
            create_database_nat_gateway_route=create_database_nat_gateway_route,
            create_database_subnet_group=create_database_subnet_group,
            create_database_subnet_route_table=create_database_subnet_route_table,
            create_egress_only_igw=create_egress_only_igw,
            create_elasticache_subnet_group=create_elasticache_subnet_group,
            create_elasticache_subnet_route_table=create_elasticache_subnet_route_table,
            create_flow_log_cloudwatch_iam_role=create_flow_log_cloudwatch_iam_role,
            create_flow_log_cloudwatch_log_group=create_flow_log_cloudwatch_log_group,
            create_igw=create_igw,
            create_multiple_intra_route_tables=create_multiple_intra_route_tables,
            create_multiple_public_route_tables=create_multiple_public_route_tables,
            create_private_nat_gateway_route=create_private_nat_gateway_route,
            create_redshift_subnet_group=create_redshift_subnet_group,
            create_redshift_subnet_route_table=create_redshift_subnet_route_table,
            create_vpc=create_vpc,
            customer_gateways=customer_gateways,
            customer_gateway_tags=customer_gateway_tags,
            customer_owned_ipv4_pool=customer_owned_ipv4_pool,
            database_acl_tags=database_acl_tags,
            database_dedicated_network_acl=database_dedicated_network_acl,
            database_inbound_acl_rules=database_inbound_acl_rules,
            database_outbound_acl_rules=database_outbound_acl_rules,
            database_route_table_tags=database_route_table_tags,
            database_subnet_assign_ipv6_address_on_creation=database_subnet_assign_ipv6_address_on_creation,
            database_subnet_enable_dns64=database_subnet_enable_dns64,
            database_subnet_enable_resource_name_dns_aaaa_record_on_launch=database_subnet_enable_resource_name_dns_aaaa_record_on_launch,
            database_subnet_enable_resource_name_dns_a_record_on_launch=database_subnet_enable_resource_name_dns_a_record_on_launch,
            database_subnet_group_name=database_subnet_group_name,
            database_subnet_group_tags=database_subnet_group_tags,
            database_subnet_ipv6_native=database_subnet_ipv6_native,
            database_subnet_ipv6_prefixes=database_subnet_ipv6_prefixes,
            database_subnet_names=database_subnet_names,
            database_subnet_private_dns_hostname_type_on_launch=database_subnet_private_dns_hostname_type_on_launch,
            database_subnets=database_subnets,
            database_subnet_suffix=database_subnet_suffix,
            database_subnet_tags=database_subnet_tags,
            default_network_acl_egress=default_network_acl_egress,
            default_network_acl_ingress=default_network_acl_ingress,
            default_network_acl_name=default_network_acl_name,
            default_network_acl_tags=default_network_acl_tags,
            default_route_table_name=default_route_table_name,
            default_route_table_propagating_vgws=default_route_table_propagating_vgws,
            default_route_table_routes=default_route_table_routes,
            default_route_table_tags=default_route_table_tags,
            default_security_group_egress=default_security_group_egress,
            default_security_group_ingress=default_security_group_ingress,
            default_security_group_name=default_security_group_name,
            default_security_group_tags=default_security_group_tags,
            default_vpc_enable_dns_hostnames=default_vpc_enable_dns_hostnames,
            default_vpc_enable_dns_support=default_vpc_enable_dns_support,
            default_vpc_name=default_vpc_name,
            default_vpc_tags=default_vpc_tags,
            dhcp_options_domain_name=dhcp_options_domain_name,
            dhcp_options_domain_name_servers=dhcp_options_domain_name_servers,
            dhcp_options_ipv6_address_preferred_lease_time=dhcp_options_ipv6_address_preferred_lease_time,
            dhcp_options_netbios_name_servers=dhcp_options_netbios_name_servers,
            dhcp_options_netbios_node_type=dhcp_options_netbios_node_type,
            dhcp_options_ntp_servers=dhcp_options_ntp_servers,
            dhcp_options_tags=dhcp_options_tags,
            elasticache_acl_tags=elasticache_acl_tags,
            elasticache_dedicated_network_acl=elasticache_dedicated_network_acl,
            elasticache_inbound_acl_rules=elasticache_inbound_acl_rules,
            elasticache_outbound_acl_rules=elasticache_outbound_acl_rules,
            elasticache_route_table_tags=elasticache_route_table_tags,
            elasticache_subnet_assign_ipv6_address_on_creation=elasticache_subnet_assign_ipv6_address_on_creation,
            elasticache_subnet_enable_dns64=elasticache_subnet_enable_dns64,
            elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch=elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch,
            elasticache_subnet_enable_resource_name_dns_a_record_on_launch=elasticache_subnet_enable_resource_name_dns_a_record_on_launch,
            elasticache_subnet_group_name=elasticache_subnet_group_name,
            elasticache_subnet_group_tags=elasticache_subnet_group_tags,
            elasticache_subnet_ipv6_native=elasticache_subnet_ipv6_native,
            elasticache_subnet_ipv6_prefixes=elasticache_subnet_ipv6_prefixes,
            elasticache_subnet_names=elasticache_subnet_names,
            elasticache_subnet_private_dns_hostname_type_on_launch=elasticache_subnet_private_dns_hostname_type_on_launch,
            elasticache_subnets=elasticache_subnets,
            elasticache_subnet_suffix=elasticache_subnet_suffix,
            elasticache_subnet_tags=elasticache_subnet_tags,
            enable_dhcp_options=enable_dhcp_options,
            enable_dns_hostnames=enable_dns_hostnames,
            enable_dns_support=enable_dns_support,
            enable_flow_log=enable_flow_log,
            enable_ipv6=enable_ipv6,
            enable_nat_gateway=enable_nat_gateway,
            enable_network_address_usage_metrics=enable_network_address_usage_metrics,
            enable_public_redshift=enable_public_redshift,
            enable_vpn_gateway=enable_vpn_gateway,
            external_nat_ip_ids=external_nat_ip_ids,
            external_nat_ips=external_nat_ips,
            flow_log_cloudwatch_iam_role_arn=flow_log_cloudwatch_iam_role_arn,
            flow_log_cloudwatch_iam_role_conditions=flow_log_cloudwatch_iam_role_conditions,
            flow_log_cloudwatch_log_group_class=flow_log_cloudwatch_log_group_class,
            flow_log_cloudwatch_log_group_kms_key_id=flow_log_cloudwatch_log_group_kms_key_id,
            flow_log_cloudwatch_log_group_name_prefix=flow_log_cloudwatch_log_group_name_prefix,
            flow_log_cloudwatch_log_group_name_suffix=flow_log_cloudwatch_log_group_name_suffix,
            flow_log_cloudwatch_log_group_retention_in_days=flow_log_cloudwatch_log_group_retention_in_days,
            flow_log_cloudwatch_log_group_skip_destroy=flow_log_cloudwatch_log_group_skip_destroy,
            flow_log_deliver_cross_account_role=flow_log_deliver_cross_account_role,
            flow_log_destination_arn=flow_log_destination_arn,
            flow_log_destination_type=flow_log_destination_type,
            flow_log_file_format=flow_log_file_format,
            flow_log_hive_compatible_partitions=flow_log_hive_compatible_partitions,
            flow_log_log_format=flow_log_log_format,
            flow_log_max_aggregation_interval=flow_log_max_aggregation_interval,
            flow_log_per_hour_partition=flow_log_per_hour_partition,
            flow_log_traffic_type=flow_log_traffic_type,
            igw_tags=igw_tags,
            instance_tenancy=instance_tenancy,
            intra_acl_tags=intra_acl_tags,
            intra_dedicated_network_acl=intra_dedicated_network_acl,
            intra_inbound_acl_rules=intra_inbound_acl_rules,
            intra_outbound_acl_rules=intra_outbound_acl_rules,
            intra_route_table_tags=intra_route_table_tags,
            intra_subnet_assign_ipv6_address_on_creation=intra_subnet_assign_ipv6_address_on_creation,
            intra_subnet_enable_dns64=intra_subnet_enable_dns64,
            intra_subnet_enable_resource_name_dns_aaaa_record_on_launch=intra_subnet_enable_resource_name_dns_aaaa_record_on_launch,
            intra_subnet_enable_resource_name_dns_a_record_on_launch=intra_subnet_enable_resource_name_dns_a_record_on_launch,
            intra_subnet_ipv6_native=intra_subnet_ipv6_native,
            intra_subnet_ipv6_prefixes=intra_subnet_ipv6_prefixes,
            intra_subnet_names=intra_subnet_names,
            intra_subnet_private_dns_hostname_type_on_launch=intra_subnet_private_dns_hostname_type_on_launch,
            intra_subnets=intra_subnets,
            intra_subnet_suffix=intra_subnet_suffix,
            intra_subnet_tags=intra_subnet_tags,
            ipv4_ipam_pool_id=ipv4_ipam_pool_id,
            ipv4_netmask_length=ipv4_netmask_length,
            ipv6_cidr=ipv6_cidr,
            ipv6_cidr_block_network_border_group=ipv6_cidr_block_network_border_group,
            ipv6_ipam_pool_id=ipv6_ipam_pool_id,
            ipv6_netmask_length=ipv6_netmask_length,
            manage_default_network_acl=manage_default_network_acl,
            manage_default_route_table=manage_default_route_table,
            manage_default_security_group=manage_default_security_group,
            manage_default_vpc=manage_default_vpc,
            map_customer_owned_ip_on_launch=map_customer_owned_ip_on_launch,
            map_public_ip_on_launch=map_public_ip_on_launch,
            name=name,
            nat_eip_tags=nat_eip_tags,
            nat_gateway_destination_cidr_block=nat_gateway_destination_cidr_block,
            nat_gateway_tags=nat_gateway_tags,
            one_nat_gateway_per_az=one_nat_gateway_per_az,
            outpost_acl_tags=outpost_acl_tags,
            outpost_arn=outpost_arn,
            outpost_az=outpost_az,
            outpost_dedicated_network_acl=outpost_dedicated_network_acl,
            outpost_inbound_acl_rules=outpost_inbound_acl_rules,
            outpost_outbound_acl_rules=outpost_outbound_acl_rules,
            outpost_subnet_assign_ipv6_address_on_creation=outpost_subnet_assign_ipv6_address_on_creation,
            outpost_subnet_enable_dns64=outpost_subnet_enable_dns64,
            outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch=outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch,
            outpost_subnet_enable_resource_name_dns_a_record_on_launch=outpost_subnet_enable_resource_name_dns_a_record_on_launch,
            outpost_subnet_ipv6_native=outpost_subnet_ipv6_native,
            outpost_subnet_ipv6_prefixes=outpost_subnet_ipv6_prefixes,
            outpost_subnet_names=outpost_subnet_names,
            outpost_subnet_private_dns_hostname_type_on_launch=outpost_subnet_private_dns_hostname_type_on_launch,
            outpost_subnets=outpost_subnets,
            outpost_subnet_suffix=outpost_subnet_suffix,
            outpost_subnet_tags=outpost_subnet_tags,
            private_acl_tags=private_acl_tags,
            private_dedicated_network_acl=private_dedicated_network_acl,
            private_inbound_acl_rules=private_inbound_acl_rules,
            private_outbound_acl_rules=private_outbound_acl_rules,
            private_route_table_tags=private_route_table_tags,
            private_subnet_assign_ipv6_address_on_creation=private_subnet_assign_ipv6_address_on_creation,
            private_subnet_enable_dns64=private_subnet_enable_dns64,
            private_subnet_enable_resource_name_dns_aaaa_record_on_launch=private_subnet_enable_resource_name_dns_aaaa_record_on_launch,
            private_subnet_enable_resource_name_dns_a_record_on_launch=private_subnet_enable_resource_name_dns_a_record_on_launch,
            private_subnet_ipv6_native=private_subnet_ipv6_native,
            private_subnet_ipv6_prefixes=private_subnet_ipv6_prefixes,
            private_subnet_names=private_subnet_names,
            private_subnet_private_dns_hostname_type_on_launch=private_subnet_private_dns_hostname_type_on_launch,
            private_subnets=private_subnets,
            private_subnet_suffix=private_subnet_suffix,
            private_subnet_tags=private_subnet_tags,
            private_subnet_tags_per_az=private_subnet_tags_per_az,
            propagate_intra_route_tables_vgw=propagate_intra_route_tables_vgw,
            propagate_private_route_tables_vgw=propagate_private_route_tables_vgw,
            propagate_public_route_tables_vgw=propagate_public_route_tables_vgw,
            public_acl_tags=public_acl_tags,
            public_dedicated_network_acl=public_dedicated_network_acl,
            public_inbound_acl_rules=public_inbound_acl_rules,
            public_outbound_acl_rules=public_outbound_acl_rules,
            public_route_table_tags=public_route_table_tags,
            public_subnet_assign_ipv6_address_on_creation=public_subnet_assign_ipv6_address_on_creation,
            public_subnet_enable_dns64=public_subnet_enable_dns64,
            public_subnet_enable_resource_name_dns_aaaa_record_on_launch=public_subnet_enable_resource_name_dns_aaaa_record_on_launch,
            public_subnet_enable_resource_name_dns_a_record_on_launch=public_subnet_enable_resource_name_dns_a_record_on_launch,
            public_subnet_ipv6_native=public_subnet_ipv6_native,
            public_subnet_ipv6_prefixes=public_subnet_ipv6_prefixes,
            public_subnet_names=public_subnet_names,
            public_subnet_private_dns_hostname_type_on_launch=public_subnet_private_dns_hostname_type_on_launch,
            public_subnets=public_subnets,
            public_subnet_suffix=public_subnet_suffix,
            public_subnet_tags=public_subnet_tags,
            public_subnet_tags_per_az=public_subnet_tags_per_az,
            putin_khuylo=putin_khuylo,
            redshift_acl_tags=redshift_acl_tags,
            redshift_dedicated_network_acl=redshift_dedicated_network_acl,
            redshift_inbound_acl_rules=redshift_inbound_acl_rules,
            redshift_outbound_acl_rules=redshift_outbound_acl_rules,
            redshift_route_table_tags=redshift_route_table_tags,
            redshift_subnet_assign_ipv6_address_on_creation=redshift_subnet_assign_ipv6_address_on_creation,
            redshift_subnet_enable_dns64=redshift_subnet_enable_dns64,
            redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch=redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch,
            redshift_subnet_enable_resource_name_dns_a_record_on_launch=redshift_subnet_enable_resource_name_dns_a_record_on_launch,
            redshift_subnet_group_name=redshift_subnet_group_name,
            redshift_subnet_group_tags=redshift_subnet_group_tags,
            redshift_subnet_ipv6_native=redshift_subnet_ipv6_native,
            redshift_subnet_ipv6_prefixes=redshift_subnet_ipv6_prefixes,
            redshift_subnet_names=redshift_subnet_names,
            redshift_subnet_private_dns_hostname_type_on_launch=redshift_subnet_private_dns_hostname_type_on_launch,
            redshift_subnets=redshift_subnets,
            redshift_subnet_suffix=redshift_subnet_suffix,
            redshift_subnet_tags=redshift_subnet_tags,
            reuse_nat_ips=reuse_nat_ips,
            secondary_cidr_blocks=secondary_cidr_blocks,
            single_nat_gateway=single_nat_gateway,
            tags=tags,
            use_ipam_pool=use_ipam_pool,
            vpc_flow_log_iam_policy_name=vpc_flow_log_iam_policy_name,
            vpc_flow_log_iam_policy_use_name_prefix=vpc_flow_log_iam_policy_use_name_prefix,
            vpc_flow_log_iam_role_name=vpc_flow_log_iam_role_name,
            vpc_flow_log_iam_role_use_name_prefix=vpc_flow_log_iam_role_use_name_prefix,
            vpc_flow_log_permissions_boundary=vpc_flow_log_permissions_boundary,
            vpc_flow_log_tags=vpc_flow_log_tags,
            vpc_tags=vpc_tags,
            vpn_gateway_az=vpn_gateway_az,
            vpn_gateway_id=vpn_gateway_id,
            vpn_gateway_tags=vpn_gateway_tags,
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
    @jsii.member(jsii_name="azsOutput")
    def azs_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azsOutput"))

    @builtins.property
    @jsii.member(jsii_name="cgwArnsOutput")
    def cgw_arns_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cgwArnsOutput"))

    @builtins.property
    @jsii.member(jsii_name="cgwIdsOutput")
    def cgw_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cgwIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="databaseInternetGatewayRouteIdOutput")
    def database_internet_gateway_route_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseInternetGatewayRouteIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="databaseIpv6EgressRouteIdOutput")
    def database_ipv6_egress_route_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseIpv6EgressRouteIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNatGatewayRouteIdsOutput")
    def database_nat_gateway_route_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseNatGatewayRouteIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNetworkAclArnOutput")
    def database_network_acl_arn_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseNetworkAclArnOutput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNetworkAclIdOutput")
    def database_network_acl_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseNetworkAclIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="databaseRouteTableAssociationIdsOutput")
    def database_route_table_association_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseRouteTableAssociationIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="databaseRouteTableIdsOutput")
    def database_route_table_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseRouteTableIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="databaseSubnetArnsOutput")
    def database_subnet_arns_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseSubnetArnsOutput"))

    @builtins.property
    @jsii.member(jsii_name="databaseSubnetGroupNameOutput")
    def database_subnet_group_name_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseSubnetGroupNameOutput"))

    @builtins.property
    @jsii.member(jsii_name="databaseSubnetGroupOutput")
    def database_subnet_group_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseSubnetGroupOutput"))

    @builtins.property
    @jsii.member(jsii_name="databaseSubnetObjectsOutput")
    def database_subnet_objects_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseSubnetObjectsOutput"))

    @builtins.property
    @jsii.member(jsii_name="databaseSubnetsCidrBlocksOutput")
    def database_subnets_cidr_blocks_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseSubnetsCidrBlocksOutput"))

    @builtins.property
    @jsii.member(jsii_name="databaseSubnetsIpv6CidrBlocksOutput")
    def database_subnets_ipv6_cidr_blocks_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseSubnetsIpv6CidrBlocksOutput"))

    @builtins.property
    @jsii.member(jsii_name="databaseSubnetsOutput")
    def database_subnets_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseSubnetsOutput"))

    @builtins.property
    @jsii.member(jsii_name="defaultNetworkAclIdOutput")
    def default_network_acl_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultNetworkAclIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="defaultRouteTableIdOutput")
    def default_route_table_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultRouteTableIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="defaultSecurityGroupIdOutput")
    def default_security_group_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultSecurityGroupIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="defaultVpcArnOutput")
    def default_vpc_arn_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultVpcArnOutput"))

    @builtins.property
    @jsii.member(jsii_name="defaultVpcCidrBlockOutput")
    def default_vpc_cidr_block_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultVpcCidrBlockOutput"))

    @builtins.property
    @jsii.member(jsii_name="defaultVpcDefaultNetworkAclIdOutput")
    def default_vpc_default_network_acl_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultVpcDefaultNetworkAclIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="defaultVpcDefaultRouteTableIdOutput")
    def default_vpc_default_route_table_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultVpcDefaultRouteTableIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="defaultVpcDefaultSecurityGroupIdOutput")
    def default_vpc_default_security_group_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultVpcDefaultSecurityGroupIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="defaultVpcEnableDnsHostnamesOutput")
    def default_vpc_enable_dns_hostnames_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultVpcEnableDnsHostnamesOutput"))

    @builtins.property
    @jsii.member(jsii_name="defaultVpcEnableDnsSupportOutput")
    def default_vpc_enable_dns_support_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultVpcEnableDnsSupportOutput"))

    @builtins.property
    @jsii.member(jsii_name="defaultVpcIdOutput")
    def default_vpc_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultVpcIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="defaultVpcInstanceTenancyOutput")
    def default_vpc_instance_tenancy_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultVpcInstanceTenancyOutput"))

    @builtins.property
    @jsii.member(jsii_name="defaultVpcMainRouteTableIdOutput")
    def default_vpc_main_route_table_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultVpcMainRouteTableIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="dhcpOptionsIdOutput")
    def dhcp_options_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dhcpOptionsIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="egressOnlyInternetGatewayIdOutput")
    def egress_only_internet_gateway_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "egressOnlyInternetGatewayIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="elasticacheNetworkAclArnOutput")
    def elasticache_network_acl_arn_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticacheNetworkAclArnOutput"))

    @builtins.property
    @jsii.member(jsii_name="elasticacheNetworkAclIdOutput")
    def elasticache_network_acl_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticacheNetworkAclIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="elasticacheRouteTableAssociationIdsOutput")
    def elasticache_route_table_association_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticacheRouteTableAssociationIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="elasticacheRouteTableIdsOutput")
    def elasticache_route_table_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticacheRouteTableIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnetArnsOutput")
    def elasticache_subnet_arns_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticacheSubnetArnsOutput"))

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnetGroupNameOutput")
    def elasticache_subnet_group_name_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticacheSubnetGroupNameOutput"))

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnetGroupOutput")
    def elasticache_subnet_group_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticacheSubnetGroupOutput"))

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnetObjectsOutput")
    def elasticache_subnet_objects_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticacheSubnetObjectsOutput"))

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnetsCidrBlocksOutput")
    def elasticache_subnets_cidr_blocks_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticacheSubnetsCidrBlocksOutput"))

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnetsIpv6CidrBlocksOutput")
    def elasticache_subnets_ipv6_cidr_blocks_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticacheSubnetsIpv6CidrBlocksOutput"))

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnetsOutput")
    def elasticache_subnets_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticacheSubnetsOutput"))

    @builtins.property
    @jsii.member(jsii_name="igwArnOutput")
    def igw_arn_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "igwArnOutput"))

    @builtins.property
    @jsii.member(jsii_name="igwIdOutput")
    def igw_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "igwIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="intraNetworkAclArnOutput")
    def intra_network_acl_arn_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intraNetworkAclArnOutput"))

    @builtins.property
    @jsii.member(jsii_name="intraNetworkAclIdOutput")
    def intra_network_acl_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intraNetworkAclIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="intraRouteTableAssociationIdsOutput")
    def intra_route_table_association_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intraRouteTableAssociationIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="intraRouteTableIdsOutput")
    def intra_route_table_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intraRouteTableIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="intraSubnetArnsOutput")
    def intra_subnet_arns_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intraSubnetArnsOutput"))

    @builtins.property
    @jsii.member(jsii_name="intraSubnetObjectsOutput")
    def intra_subnet_objects_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intraSubnetObjectsOutput"))

    @builtins.property
    @jsii.member(jsii_name="intraSubnetsCidrBlocksOutput")
    def intra_subnets_cidr_blocks_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intraSubnetsCidrBlocksOutput"))

    @builtins.property
    @jsii.member(jsii_name="intraSubnetsIpv6CidrBlocksOutput")
    def intra_subnets_ipv6_cidr_blocks_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intraSubnetsIpv6CidrBlocksOutput"))

    @builtins.property
    @jsii.member(jsii_name="intraSubnetsOutput")
    def intra_subnets_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intraSubnetsOutput"))

    @builtins.property
    @jsii.member(jsii_name="nameOutput")
    def name_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nameOutput"))

    @builtins.property
    @jsii.member(jsii_name="natgwIdsOutput")
    def natgw_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "natgwIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="natgwInterfaceIdsOutput")
    def natgw_interface_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "natgwInterfaceIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="natIdsOutput")
    def nat_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "natIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="natPublicIpsOutput")
    def nat_public_ips_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "natPublicIpsOutput"))

    @builtins.property
    @jsii.member(jsii_name="outpostNetworkAclArnOutput")
    def outpost_network_acl_arn_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outpostNetworkAclArnOutput"))

    @builtins.property
    @jsii.member(jsii_name="outpostNetworkAclIdOutput")
    def outpost_network_acl_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outpostNetworkAclIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="outpostSubnetArnsOutput")
    def outpost_subnet_arns_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outpostSubnetArnsOutput"))

    @builtins.property
    @jsii.member(jsii_name="outpostSubnetObjectsOutput")
    def outpost_subnet_objects_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outpostSubnetObjectsOutput"))

    @builtins.property
    @jsii.member(jsii_name="outpostSubnetsCidrBlocksOutput")
    def outpost_subnets_cidr_blocks_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outpostSubnetsCidrBlocksOutput"))

    @builtins.property
    @jsii.member(jsii_name="outpostSubnetsIpv6CidrBlocksOutput")
    def outpost_subnets_ipv6_cidr_blocks_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outpostSubnetsIpv6CidrBlocksOutput"))

    @builtins.property
    @jsii.member(jsii_name="outpostSubnetsOutput")
    def outpost_subnets_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outpostSubnetsOutput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpv6EgressRouteIdsOutput")
    def private_ipv6_egress_route_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpv6EgressRouteIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="privateNatGatewayRouteIdsOutput")
    def private_nat_gateway_route_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateNatGatewayRouteIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="privateNetworkAclArnOutput")
    def private_network_acl_arn_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateNetworkAclArnOutput"))

    @builtins.property
    @jsii.member(jsii_name="privateNetworkAclIdOutput")
    def private_network_acl_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateNetworkAclIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="privateRouteTableAssociationIdsOutput")
    def private_route_table_association_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateRouteTableAssociationIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="privateRouteTableIdsOutput")
    def private_route_table_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateRouteTableIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="privateSubnetArnsOutput")
    def private_subnet_arns_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateSubnetArnsOutput"))

    @builtins.property
    @jsii.member(jsii_name="privateSubnetObjectsOutput")
    def private_subnet_objects_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateSubnetObjectsOutput"))

    @builtins.property
    @jsii.member(jsii_name="privateSubnetsCidrBlocksOutput")
    def private_subnets_cidr_blocks_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateSubnetsCidrBlocksOutput"))

    @builtins.property
    @jsii.member(jsii_name="privateSubnetsIpv6CidrBlocksOutput")
    def private_subnets_ipv6_cidr_blocks_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateSubnetsIpv6CidrBlocksOutput"))

    @builtins.property
    @jsii.member(jsii_name="privateSubnetsOutput")
    def private_subnets_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateSubnetsOutput"))

    @builtins.property
    @jsii.member(jsii_name="publicInternetGatewayIpv6RouteIdOutput")
    def public_internet_gateway_ipv6_route_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicInternetGatewayIpv6RouteIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="publicInternetGatewayRouteIdOutput")
    def public_internet_gateway_route_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicInternetGatewayRouteIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAclArnOutput")
    def public_network_acl_arn_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicNetworkAclArnOutput"))

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAclIdOutput")
    def public_network_acl_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicNetworkAclIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="publicRouteTableAssociationIdsOutput")
    def public_route_table_association_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicRouteTableAssociationIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="publicRouteTableIdsOutput")
    def public_route_table_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicRouteTableIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="publicSubnetArnsOutput")
    def public_subnet_arns_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicSubnetArnsOutput"))

    @builtins.property
    @jsii.member(jsii_name="publicSubnetObjectsOutput")
    def public_subnet_objects_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicSubnetObjectsOutput"))

    @builtins.property
    @jsii.member(jsii_name="publicSubnetsCidrBlocksOutput")
    def public_subnets_cidr_blocks_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicSubnetsCidrBlocksOutput"))

    @builtins.property
    @jsii.member(jsii_name="publicSubnetsIpv6CidrBlocksOutput")
    def public_subnets_ipv6_cidr_blocks_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicSubnetsIpv6CidrBlocksOutput"))

    @builtins.property
    @jsii.member(jsii_name="publicSubnetsOutput")
    def public_subnets_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicSubnetsOutput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftNetworkAclArnOutput")
    def redshift_network_acl_arn_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redshiftNetworkAclArnOutput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftNetworkAclIdOutput")
    def redshift_network_acl_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redshiftNetworkAclIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftPublicRouteTableAssociationIdsOutput")
    def redshift_public_route_table_association_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redshiftPublicRouteTableAssociationIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftRouteTableAssociationIdsOutput")
    def redshift_route_table_association_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redshiftRouteTableAssociationIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftRouteTableIdsOutput")
    def redshift_route_table_ids_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redshiftRouteTableIdsOutput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftSubnetArnsOutput")
    def redshift_subnet_arns_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redshiftSubnetArnsOutput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftSubnetGroupOutput")
    def redshift_subnet_group_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redshiftSubnetGroupOutput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftSubnetObjectsOutput")
    def redshift_subnet_objects_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redshiftSubnetObjectsOutput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftSubnetsCidrBlocksOutput")
    def redshift_subnets_cidr_blocks_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redshiftSubnetsCidrBlocksOutput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftSubnetsIpv6CidrBlocksOutput")
    def redshift_subnets_ipv6_cidr_blocks_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redshiftSubnetsIpv6CidrBlocksOutput"))

    @builtins.property
    @jsii.member(jsii_name="redshiftSubnetsOutput")
    def redshift_subnets_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redshiftSubnetsOutput"))

    @builtins.property
    @jsii.member(jsii_name="thisCustomerGatewayOutput")
    def this_customer_gateway_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thisCustomerGatewayOutput"))

    @builtins.property
    @jsii.member(jsii_name="vgwArnOutput")
    def vgw_arn_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vgwArnOutput"))

    @builtins.property
    @jsii.member(jsii_name="vgwIdOutput")
    def vgw_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vgwIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="vpcArnOutput")
    def vpc_arn_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcArnOutput"))

    @builtins.property
    @jsii.member(jsii_name="vpcCidrBlockOutput")
    def vpc_cidr_block_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcCidrBlockOutput"))

    @builtins.property
    @jsii.member(jsii_name="vpcEnableDnsHostnamesOutput")
    def vpc_enable_dns_hostnames_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcEnableDnsHostnamesOutput"))

    @builtins.property
    @jsii.member(jsii_name="vpcEnableDnsSupportOutput")
    def vpc_enable_dns_support_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcEnableDnsSupportOutput"))

    @builtins.property
    @jsii.member(jsii_name="vpcFlowLogCloudwatchIamRoleArnOutput")
    def vpc_flow_log_cloudwatch_iam_role_arn_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcFlowLogCloudwatchIamRoleArnOutput"))

    @builtins.property
    @jsii.member(jsii_name="vpcFlowLogDeliverCrossAccountRoleOutput")
    def vpc_flow_log_deliver_cross_account_role_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcFlowLogDeliverCrossAccountRoleOutput"))

    @builtins.property
    @jsii.member(jsii_name="vpcFlowLogDestinationArnOutput")
    def vpc_flow_log_destination_arn_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcFlowLogDestinationArnOutput"))

    @builtins.property
    @jsii.member(jsii_name="vpcFlowLogDestinationTypeOutput")
    def vpc_flow_log_destination_type_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcFlowLogDestinationTypeOutput"))

    @builtins.property
    @jsii.member(jsii_name="vpcFlowLogIdOutput")
    def vpc_flow_log_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcFlowLogIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="vpcIdOutput")
    def vpc_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="vpcInstanceTenancyOutput")
    def vpc_instance_tenancy_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcInstanceTenancyOutput"))

    @builtins.property
    @jsii.member(jsii_name="vpcIpv6AssociationIdOutput")
    def vpc_ipv6_association_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcIpv6AssociationIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="vpcIpv6CidrBlockOutput")
    def vpc_ipv6_cidr_block_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcIpv6CidrBlockOutput"))

    @builtins.property
    @jsii.member(jsii_name="vpcMainRouteTableIdOutput")
    def vpc_main_route_table_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcMainRouteTableIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="vpcOwnerIdOutput")
    def vpc_owner_id_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcOwnerIdOutput"))

    @builtins.property
    @jsii.member(jsii_name="vpcSecondaryCidrBlocksOutput")
    def vpc_secondary_cidr_blocks_output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcSecondaryCidrBlocksOutput"))

    @builtins.property
    @jsii.member(jsii_name="flowLogCloudwatchIamRoleConditions")
    def flow_log_cloudwatch_iam_role_conditions(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "flowLogCloudwatchIamRoleConditions"))

    @flow_log_cloudwatch_iam_role_conditions.setter
    def flow_log_cloudwatch_iam_role_conditions(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae06cc41c20a8a916caa0287df54236f750c9dd0f5cfa878410891a04f755a05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowLogCloudwatchIamRoleConditions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="amazonSideAsn")
    def amazon_side_asn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "amazonSideAsn"))

    @amazon_side_asn.setter
    def amazon_side_asn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87abacfa96c4aa862e0af0807f43d0af419b01b99186ecfc0bcfa59477f93cb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amazonSideAsn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="azs")
    def azs(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "azs"))

    @azs.setter
    def azs(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e2f495405a0dfbca127193223a62470e5ced83ae0ed118e506ef7723d276a79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cidr")
    def cidr(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cidr"))

    @cidr.setter
    def cidr(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c06b3be1058a1602c68d3854df2bf2a4a0ac4249e0e7c7ec270ad412072a8d01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidr", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createDatabaseInternetGatewayRoute")
    def create_database_internet_gateway_route(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createDatabaseInternetGatewayRoute"))

    @create_database_internet_gateway_route.setter
    def create_database_internet_gateway_route(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da1bb13d5246d0a681f95aa6d3c4de26a8df28c62e8d8100c8c9dd8f760f13f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createDatabaseInternetGatewayRoute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createDatabaseNatGatewayRoute")
    def create_database_nat_gateway_route(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createDatabaseNatGatewayRoute"))

    @create_database_nat_gateway_route.setter
    def create_database_nat_gateway_route(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1ce43dfa4d0386089b4591843ae91303b528194e4612f41396c5d69fb3a72bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createDatabaseNatGatewayRoute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createDatabaseSubnetGroup")
    def create_database_subnet_group(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createDatabaseSubnetGroup"))

    @create_database_subnet_group.setter
    def create_database_subnet_group(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d945c595c24421daac63bdd224660b83d3db2dd3a365542ba60ff23b9815b615)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createDatabaseSubnetGroup", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createDatabaseSubnetRouteTable")
    def create_database_subnet_route_table(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createDatabaseSubnetRouteTable"))

    @create_database_subnet_route_table.setter
    def create_database_subnet_route_table(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c23dacff4e057dcc8dfdaf5d68f50ad6a4396016c0ef0204b1ddc8b42e5bc45a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createDatabaseSubnetRouteTable", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createEgressOnlyIgw")
    def create_egress_only_igw(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createEgressOnlyIgw"))

    @create_egress_only_igw.setter
    def create_egress_only_igw(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d78922c3d9caef7315a2fc39764449518097347e2a80192b6cba58aa3fdcdc8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createEgressOnlyIgw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createElasticacheSubnetGroup")
    def create_elasticache_subnet_group(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createElasticacheSubnetGroup"))

    @create_elasticache_subnet_group.setter
    def create_elasticache_subnet_group(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1110b4a1f56723b4d7b37c703672433202ce050d26ff6ce6d3a0fe650c6f8959)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createElasticacheSubnetGroup", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createElasticacheSubnetRouteTable")
    def create_elasticache_subnet_route_table(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createElasticacheSubnetRouteTable"))

    @create_elasticache_subnet_route_table.setter
    def create_elasticache_subnet_route_table(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b914fdb4c5835989461b5b9e47dbc56ca5b4378be8ca0965c2edaa4de5221dd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createElasticacheSubnetRouteTable", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createFlowLogCloudwatchIamRole")
    def create_flow_log_cloudwatch_iam_role(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createFlowLogCloudwatchIamRole"))

    @create_flow_log_cloudwatch_iam_role.setter
    def create_flow_log_cloudwatch_iam_role(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea1120216b43e76d68af5f9ea72c604125ff9272a4a933fd1a482cd8b7679488)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createFlowLogCloudwatchIamRole", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createFlowLogCloudwatchLogGroup")
    def create_flow_log_cloudwatch_log_group(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createFlowLogCloudwatchLogGroup"))

    @create_flow_log_cloudwatch_log_group.setter
    def create_flow_log_cloudwatch_log_group(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c319b409ba9ac51eb004582f53d89791090ccef99c160023e27deda6b01addd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createFlowLogCloudwatchLogGroup", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createIgw")
    def create_igw(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createIgw"))

    @create_igw.setter
    def create_igw(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c78dfd8a1d60795ba10f0b3b02d1cc5bbb82cec4565186e383c936e846c65ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createIgw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createMultipleIntraRouteTables")
    def create_multiple_intra_route_tables(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createMultipleIntraRouteTables"))

    @create_multiple_intra_route_tables.setter
    def create_multiple_intra_route_tables(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b164c865c4a86bf9b129b22b262498061e8549e4527869f027a36cf5d9c41c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createMultipleIntraRouteTables", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createMultiplePublicRouteTables")
    def create_multiple_public_route_tables(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createMultiplePublicRouteTables"))

    @create_multiple_public_route_tables.setter
    def create_multiple_public_route_tables(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0eebb7b3e273f39be5a181e8b5b651d33d47ad60f84a2b38310381ec9e6cf67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createMultiplePublicRouteTables", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createPrivateNatGatewayRoute")
    def create_private_nat_gateway_route(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createPrivateNatGatewayRoute"))

    @create_private_nat_gateway_route.setter
    def create_private_nat_gateway_route(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77f47ab0919ee1fcfe7b53e0ea67b7d0c3edf272cfc870443e2a6470754186a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createPrivateNatGatewayRoute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createRedshiftSubnetGroup")
    def create_redshift_subnet_group(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createRedshiftSubnetGroup"))

    @create_redshift_subnet_group.setter
    def create_redshift_subnet_group(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac52b5ed0e1526d04be7646207ad3b9b31dc2952620551b14943782a8916dfa2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createRedshiftSubnetGroup", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createRedshiftSubnetRouteTable")
    def create_redshift_subnet_route_table(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createRedshiftSubnetRouteTable"))

    @create_redshift_subnet_route_table.setter
    def create_redshift_subnet_route_table(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9237251b6f833d6281d46faf77c258974cdf1c3597c9a1944df1dfd7028732f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createRedshiftSubnetRouteTable", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="createVpc")
    def create_vpc(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "createVpc"))

    @create_vpc.setter
    def create_vpc(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe856a2a13ffa2d263770a0b1c80bf7fc65180048f6c0347ad53233f2c36881b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createVpc", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="customerGateways")
    def customer_gateways(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]], jsii.get(self, "customerGateways"))

    @customer_gateways.setter
    def customer_gateways(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__521fd2a8ce188fb97d944d84051ea1e29ffd067d9ea6aa054f3bfc0d3da82e91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerGateways", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="customerGatewayTags")
    def customer_gateway_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "customerGatewayTags"))

    @customer_gateway_tags.setter
    def customer_gateway_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86910c4f58dbb08affe58cf5e0f21ed758c35bf22ea3e91cb1965c3c7590b3f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerGatewayTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="customerOwnedIpv4Pool")
    def customer_owned_ipv4_pool(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerOwnedIpv4Pool"))

    @customer_owned_ipv4_pool.setter
    def customer_owned_ipv4_pool(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bac2ebd2b4a07d60e8608b00549b8829d553a276d3ba4664e845709c062baeac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerOwnedIpv4Pool", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseAclTags")
    def database_acl_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "databaseAclTags"))

    @database_acl_tags.setter
    def database_acl_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee401942eb0271cc09188ef90a6719d73f039ebdbb3ef68e7402c50f7ecb2b5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseAclTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseDedicatedNetworkAcl")
    def database_dedicated_network_acl(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "databaseDedicatedNetworkAcl"))

    @database_dedicated_network_acl.setter
    def database_dedicated_network_acl(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5de9c55ff98f13c69675cffc0287e12837d1d92255ced7d31f2b83c44eaf5fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseDedicatedNetworkAcl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseInboundAclRules")
    def database_inbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "databaseInboundAclRules"))

    @database_inbound_acl_rules.setter
    def database_inbound_acl_rules(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96e90d2fc9319bcf753f574c2ba2aafe4d6bc5d02fdbcf3ff62120f338c59fbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseInboundAclRules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseOutboundAclRules")
    def database_outbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "databaseOutboundAclRules"))

    @database_outbound_acl_rules.setter
    def database_outbound_acl_rules(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5a73730a00a7454ea550f9f0ab3fbbdf26ae3d9c541f27ccfd66863dd25da47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseOutboundAclRules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseRouteTableTags")
    def database_route_table_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "databaseRouteTableTags"))

    @database_route_table_tags.setter
    def database_route_table_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37acb140df1645df3aff86f4da3c84c92c128043169d0bb2ad276c2a01b4b467)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseRouteTableTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseSubnetAssignIpv6AddressOnCreation")
    def database_subnet_assign_ipv6_address_on_creation(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "databaseSubnetAssignIpv6AddressOnCreation"))

    @database_subnet_assign_ipv6_address_on_creation.setter
    def database_subnet_assign_ipv6_address_on_creation(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d4ec089a8faeac43b21fea2d3e96ce540cd7cca6eb465e665282c2f323d6f94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseSubnetAssignIpv6AddressOnCreation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseSubnetEnableDns64")
    def database_subnet_enable_dns64(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "databaseSubnetEnableDns64"))

    @database_subnet_enable_dns64.setter
    def database_subnet_enable_dns64(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27763505611da95756e2d11d8c35a7ceca1f4abb67be85b7011683f1b4ba5706)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseSubnetEnableDns64", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseSubnetEnableResourceNameDnsAaaaRecordOnLaunch")
    def database_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "databaseSubnetEnableResourceNameDnsAaaaRecordOnLaunch"))

    @database_subnet_enable_resource_name_dns_aaaa_record_on_launch.setter
    def database_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__612c0cf4d6a765eac51e7a27d4bf33b96c2c6be6df9fdbeaf99aaee69f02cd26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseSubnetEnableResourceNameDnsAaaaRecordOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseSubnetEnableResourceNameDnsARecordOnLaunch")
    def database_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "databaseSubnetEnableResourceNameDnsARecordOnLaunch"))

    @database_subnet_enable_resource_name_dns_a_record_on_launch.setter
    def database_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c51c4f56bd4719de6f2d668b6b2ace04c2bca2d17530e34f81e2d4c57f410262)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseSubnetEnableResourceNameDnsARecordOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseSubnetGroupName")
    def database_subnet_group_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseSubnetGroupName"))

    @database_subnet_group_name.setter
    def database_subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28872e66b537b08e5df30c50b8cebf4d5714d55869dc9720001ab1cdfc881c2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseSubnetGroupName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseSubnetGroupTags")
    def database_subnet_group_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "databaseSubnetGroupTags"))

    @database_subnet_group_tags.setter
    def database_subnet_group_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf1e7e5768b461793608f491e5e63422deaa208a4294bac2b2d3b79a0cc4d4a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseSubnetGroupTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseSubnetIpv6Native")
    def database_subnet_ipv6_native(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "databaseSubnetIpv6Native"))

    @database_subnet_ipv6_native.setter
    def database_subnet_ipv6_native(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73a91fb885ef0490541564f2b596e5cc7125f26448b6c4b4c3926c66dd4706a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseSubnetIpv6Native", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseSubnetIpv6Prefixes")
    def database_subnet_ipv6_prefixes(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "databaseSubnetIpv6Prefixes"))

    @database_subnet_ipv6_prefixes.setter
    def database_subnet_ipv6_prefixes(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c359b66a722f63249cf2299b8ed96948c47dc508436319dc87c8c0a6613e595)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseSubnetIpv6Prefixes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseSubnetNames")
    def database_subnet_names(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "databaseSubnetNames"))

    @database_subnet_names.setter
    def database_subnet_names(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23e8a05eafaf88daca57efb19df41ab7e3ccf69dd7122ed66565b0ee6f71eaa7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseSubnetNames", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseSubnetPrivateDnsHostnameTypeOnLaunch")
    def database_subnet_private_dns_hostname_type_on_launch(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseSubnetPrivateDnsHostnameTypeOnLaunch"))

    @database_subnet_private_dns_hostname_type_on_launch.setter
    def database_subnet_private_dns_hostname_type_on_launch(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15463b37b248b7ace797cee03eb261bb39bb7c8aa2a2e28a41a0374b909b0f17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseSubnetPrivateDnsHostnameTypeOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseSubnets")
    def database_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "databaseSubnets"))

    @database_subnets.setter
    def database_subnets(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53754c9631e7c5451e930116e87dde462b2bdd0f2348e4e72d4bbc54fdc4757c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseSubnets", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseSubnetSuffix")
    def database_subnet_suffix(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseSubnetSuffix"))

    @database_subnet_suffix.setter
    def database_subnet_suffix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c824ee67926e3b4f25fab420a3e5965739dc75a1dbd93e227b7c25447f2f9366)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseSubnetSuffix", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseSubnetTags")
    def database_subnet_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "databaseSubnetTags"))

    @database_subnet_tags.setter
    def database_subnet_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91b81620289eac4a13d49d0b3af9f7ab0b500cbfadd0cb85e483d7d5c81a03b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseSubnetTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultNetworkAclEgress")
    def default_network_acl_egress(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "defaultNetworkAclEgress"))

    @default_network_acl_egress.setter
    def default_network_acl_egress(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84830ee36db4ca5831ebdab20d40aeb873c45cd2a2eaedd5e34a0645ae1def6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultNetworkAclEgress", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultNetworkAclIngress")
    def default_network_acl_ingress(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "defaultNetworkAclIngress"))

    @default_network_acl_ingress.setter
    def default_network_acl_ingress(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3efd1667240bc49479a35c0f125ae0fcf5f2b6e9f4a6f297d4410403abe20e2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultNetworkAclIngress", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultNetworkAclName")
    def default_network_acl_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultNetworkAclName"))

    @default_network_acl_name.setter
    def default_network_acl_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7929871bb07dcf48690b87e9669466d2489187ce8c6bd537ce912b35cc95105b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultNetworkAclName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultNetworkAclTags")
    def default_network_acl_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "defaultNetworkAclTags"))

    @default_network_acl_tags.setter
    def default_network_acl_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6815250bb2c26213cda0331305f1966aa324d5afc6f861c45aa3f7634e30ef8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultNetworkAclTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultRouteTableName")
    def default_route_table_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultRouteTableName"))

    @default_route_table_name.setter
    def default_route_table_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__166adf41c5f81fb827c8a71db409d1b794a6836a85091e56ea519cbee9eed82e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultRouteTableName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultRouteTablePropagatingVgws")
    def default_route_table_propagating_vgws(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "defaultRouteTablePropagatingVgws"))

    @default_route_table_propagating_vgws.setter
    def default_route_table_propagating_vgws(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bdcedc90e5eaade2c30236b2e3554f6302d70a4fa72ec7f4ccd6f0a952f7f82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultRouteTablePropagatingVgws", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultRouteTableRoutes")
    def default_route_table_routes(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "defaultRouteTableRoutes"))

    @default_route_table_routes.setter
    def default_route_table_routes(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e56df3abf02b322d5494cd0e701711b68e4f8b28fa1f94dea43dad2557dd3071)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultRouteTableRoutes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultRouteTableTags")
    def default_route_table_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "defaultRouteTableTags"))

    @default_route_table_tags.setter
    def default_route_table_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06818ee1a6926988e93be6639b9a2de6f4cb84f21d41290bdb0b701a5b05848b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultRouteTableTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultSecurityGroupEgress")
    def default_security_group_egress(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "defaultSecurityGroupEgress"))

    @default_security_group_egress.setter
    def default_security_group_egress(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__269ba4f9870c727965b55da3a02358647be26b96dda0e6108c85aee6ddd65c67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSecurityGroupEgress", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultSecurityGroupIngress")
    def default_security_group_ingress(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "defaultSecurityGroupIngress"))

    @default_security_group_ingress.setter
    def default_security_group_ingress(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2684eaeaddb48b873e168ee392c1001fa6867ea08621dc5380ebb1527bc1bd07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSecurityGroupIngress", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultSecurityGroupName")
    def default_security_group_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSecurityGroupName"))

    @default_security_group_name.setter
    def default_security_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3a59cb5797781be39253509763d36750c27051fba87328e799fa36301ccbc5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSecurityGroupName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultSecurityGroupTags")
    def default_security_group_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "defaultSecurityGroupTags"))

    @default_security_group_tags.setter
    def default_security_group_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a8943fda4606e43559390b829fd29c0695dd0764e95b10686629d021a7dcaf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSecurityGroupTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultVpcEnableDnsHostnames")
    def default_vpc_enable_dns_hostnames(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "defaultVpcEnableDnsHostnames"))

    @default_vpc_enable_dns_hostnames.setter
    def default_vpc_enable_dns_hostnames(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a76dcd56ccd733200d31a979ac62574a596b9feea98750279f1cc4f2df269910)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultVpcEnableDnsHostnames", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultVpcEnableDnsSupport")
    def default_vpc_enable_dns_support(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "defaultVpcEnableDnsSupport"))

    @default_vpc_enable_dns_support.setter
    def default_vpc_enable_dns_support(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d353552fc482365754a527abbd647ab1c881cc2e8373fe080972526b06f80675)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultVpcEnableDnsSupport", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultVpcName")
    def default_vpc_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultVpcName"))

    @default_vpc_name.setter
    def default_vpc_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf714407292fd99b3fec70a222bf1a7cc508b3abf42f53606cebb14b868fb5cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultVpcName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultVpcTags")
    def default_vpc_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "defaultVpcTags"))

    @default_vpc_tags.setter
    def default_vpc_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87e7a314ab8ff3accc52fc790cd42b1c91eebad52c2cfb7c94c355dd03071fba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultVpcTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dhcpOptionsDomainName")
    def dhcp_options_domain_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dhcpOptionsDomainName"))

    @dhcp_options_domain_name.setter
    def dhcp_options_domain_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d66c965d027e62b92b2b7347021551b92e365cea89da4883444bef43652f5830)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dhcpOptionsDomainName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dhcpOptionsDomainNameServers")
    def dhcp_options_domain_name_servers(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dhcpOptionsDomainNameServers"))

    @dhcp_options_domain_name_servers.setter
    def dhcp_options_domain_name_servers(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b894210cfc93cb00a3b52c85c68e501002e87363ef9914ee28e3881cbb92830)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dhcpOptionsDomainNameServers", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dhcpOptionsIpv6AddressPreferredLeaseTime")
    def dhcp_options_ipv6_address_preferred_lease_time(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dhcpOptionsIpv6AddressPreferredLeaseTime"))

    @dhcp_options_ipv6_address_preferred_lease_time.setter
    def dhcp_options_ipv6_address_preferred_lease_time(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b4b16c46de1726d9113e3fb66c812292bf48e8f63a57298140af4a187ae946e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dhcpOptionsIpv6AddressPreferredLeaseTime", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dhcpOptionsNetbiosNameServers")
    def dhcp_options_netbios_name_servers(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dhcpOptionsNetbiosNameServers"))

    @dhcp_options_netbios_name_servers.setter
    def dhcp_options_netbios_name_servers(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87c28741ab8b06012b772ce7beae35390c075dae3f87c12a1e3df9d37ea42143)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dhcpOptionsNetbiosNameServers", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dhcpOptionsNetbiosNodeType")
    def dhcp_options_netbios_node_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dhcpOptionsNetbiosNodeType"))

    @dhcp_options_netbios_node_type.setter
    def dhcp_options_netbios_node_type(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__222b8e975b982e68934e077c55cfa398b80eca78317cb65dd80342111fc1be6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dhcpOptionsNetbiosNodeType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dhcpOptionsNtpServers")
    def dhcp_options_ntp_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dhcpOptionsNtpServers"))

    @dhcp_options_ntp_servers.setter
    def dhcp_options_ntp_servers(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db331367d6fcfb0643d1f50052ad4501c13900f0b9ec51600a465c801eff370b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dhcpOptionsNtpServers", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dhcpOptionsTags")
    def dhcp_options_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "dhcpOptionsTags"))

    @dhcp_options_tags.setter
    def dhcp_options_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc4c2dc5e0257d35f5fb2d108364a6552670d830d1aaa850fe60276fb0fa5c75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dhcpOptionsTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticacheAclTags")
    def elasticache_acl_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "elasticacheAclTags"))

    @elasticache_acl_tags.setter
    def elasticache_acl_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b841c8882422262e76ef370bc628f9f9a6944e3c8533f04f972bb00511e5dd55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticacheAclTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticacheDedicatedNetworkAcl")
    def elasticache_dedicated_network_acl(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "elasticacheDedicatedNetworkAcl"))

    @elasticache_dedicated_network_acl.setter
    def elasticache_dedicated_network_acl(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38261699df6d98c41f63eeeebb86d2eaafdb1caa0afbf0cb978b6c7fed53929b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticacheDedicatedNetworkAcl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticacheInboundAclRules")
    def elasticache_inbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "elasticacheInboundAclRules"))

    @elasticache_inbound_acl_rules.setter
    def elasticache_inbound_acl_rules(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__001d7b6387d3d94de25a766982829563e7c3d2a32b9b71ed448bd0ce3aa7afce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticacheInboundAclRules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticacheOutboundAclRules")
    def elasticache_outbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "elasticacheOutboundAclRules"))

    @elasticache_outbound_acl_rules.setter
    def elasticache_outbound_acl_rules(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d9c4d49f2c4357266b5cbd4bb6dc599e4ea0468dbbe6b29e2a7456a390bfd19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticacheOutboundAclRules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticacheRouteTableTags")
    def elasticache_route_table_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "elasticacheRouteTableTags"))

    @elasticache_route_table_tags.setter
    def elasticache_route_table_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__313e463ac61d17bbe9597d724df4e611706fed132ac741e91d09c26710a92ffe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticacheRouteTableTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnetAssignIpv6AddressOnCreation")
    def elasticache_subnet_assign_ipv6_address_on_creation(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "elasticacheSubnetAssignIpv6AddressOnCreation"))

    @elasticache_subnet_assign_ipv6_address_on_creation.setter
    def elasticache_subnet_assign_ipv6_address_on_creation(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__310084674dbbbf4f20266183d2456520d913e137d7dbdb3381139d9defc22406)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticacheSubnetAssignIpv6AddressOnCreation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnetEnableDns64")
    def elasticache_subnet_enable_dns64(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "elasticacheSubnetEnableDns64"))

    @elasticache_subnet_enable_dns64.setter
    def elasticache_subnet_enable_dns64(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__557128c6507c8a9441bf64961adbae8b3668e3c9ed9cbbbf0e98811bdd6250c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticacheSubnetEnableDns64", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnetEnableResourceNameDnsAaaaRecordOnLaunch")
    def elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "elasticacheSubnetEnableResourceNameDnsAaaaRecordOnLaunch"))

    @elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch.setter
    def elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50143c31efe280ed61aa36c65ea0127a57184b3de87d1216ea8e0dab8a9c0c24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticacheSubnetEnableResourceNameDnsAaaaRecordOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnetEnableResourceNameDnsARecordOnLaunch")
    def elasticache_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "elasticacheSubnetEnableResourceNameDnsARecordOnLaunch"))

    @elasticache_subnet_enable_resource_name_dns_a_record_on_launch.setter
    def elasticache_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__076b1a6e619efe2fc70ccfa58176e77bfe71683a8c01cef7085f7c873aeefac0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticacheSubnetEnableResourceNameDnsARecordOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnetGroupName")
    def elasticache_subnet_group_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "elasticacheSubnetGroupName"))

    @elasticache_subnet_group_name.setter
    def elasticache_subnet_group_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ecd53a5e24620ff355086bd9ac6042cc40ac3caec3364eb3fc8839043341fc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticacheSubnetGroupName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnetGroupTags")
    def elasticache_subnet_group_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "elasticacheSubnetGroupTags"))

    @elasticache_subnet_group_tags.setter
    def elasticache_subnet_group_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bafd78eca4790b998bede502b2bebc40c329a0c8b0d6134c72ba77f1c9381f58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticacheSubnetGroupTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnetIpv6Native")
    def elasticache_subnet_ipv6_native(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "elasticacheSubnetIpv6Native"))

    @elasticache_subnet_ipv6_native.setter
    def elasticache_subnet_ipv6_native(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1e274acbadf0686949124823efd7f83179eab8338f2fefcb39c6f7677298fb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticacheSubnetIpv6Native", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnetIpv6Prefixes")
    def elasticache_subnet_ipv6_prefixes(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "elasticacheSubnetIpv6Prefixes"))

    @elasticache_subnet_ipv6_prefixes.setter
    def elasticache_subnet_ipv6_prefixes(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__011618e74b6666f0d1cf92f59134de09036f70b3d8691333ccf813d14c77f744)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticacheSubnetIpv6Prefixes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnetNames")
    def elasticache_subnet_names(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "elasticacheSubnetNames"))

    @elasticache_subnet_names.setter
    def elasticache_subnet_names(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee69dcd15f6f17988e5e95618e6bd0f363e00c19f61827e99e2e2b1be22db539)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticacheSubnetNames", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnetPrivateDnsHostnameTypeOnLaunch")
    def elasticache_subnet_private_dns_hostname_type_on_launch(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "elasticacheSubnetPrivateDnsHostnameTypeOnLaunch"))

    @elasticache_subnet_private_dns_hostname_type_on_launch.setter
    def elasticache_subnet_private_dns_hostname_type_on_launch(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2897b0e953185529b30dd0ed8ee56c745866807ded60a9e7831e04030f06a460)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticacheSubnetPrivateDnsHostnameTypeOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnets")
    def elasticache_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "elasticacheSubnets"))

    @elasticache_subnets.setter
    def elasticache_subnets(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1990ebeec646acf740a0951b0ca7da096d254f8f90c42608456a202180f9dda3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticacheSubnets", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnetSuffix")
    def elasticache_subnet_suffix(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "elasticacheSubnetSuffix"))

    @elasticache_subnet_suffix.setter
    def elasticache_subnet_suffix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__053f122fb59f4f57721ddfafd8ab7e14d251e4d1243a6dbacbc2fce880728041)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticacheSubnetSuffix", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticacheSubnetTags")
    def elasticache_subnet_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "elasticacheSubnetTags"))

    @elasticache_subnet_tags.setter
    def elasticache_subnet_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e25175b545087947d3c43723e402a8eea585c8cf33387e6a4f53d7fe9b9640db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticacheSubnetTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enableDhcpOptions")
    def enable_dhcp_options(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enableDhcpOptions"))

    @enable_dhcp_options.setter
    def enable_dhcp_options(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ff86dbc6331a4d6a01b356e7bd5d930f9547f4c1b2594144d4e7fba6d465ee1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDhcpOptions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enableDnsHostnames")
    def enable_dns_hostnames(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enableDnsHostnames"))

    @enable_dns_hostnames.setter
    def enable_dns_hostnames(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d8b5d936aa07ab715de58f302359003cd3d4307282b4ba41ddd69d9663e78b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDnsHostnames", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enableDnsSupport")
    def enable_dns_support(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enableDnsSupport"))

    @enable_dns_support.setter
    def enable_dns_support(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33bd08d06ae5ccf49b2e7585ec691fbc483ec8ca9019876f8bc30e9605a7d3f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDnsSupport", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enableFlowLog")
    def enable_flow_log(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enableFlowLog"))

    @enable_flow_log.setter
    def enable_flow_log(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__478a3458a0140f7c94fee2c8e5962e6d67941c5e0ac274a1087655fddaf3515a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableFlowLog", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enableIpv6")
    def enable_ipv6(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enableIpv6"))

    @enable_ipv6.setter
    def enable_ipv6(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca88793b055049b39c2d0a34d167798469c5b73ddf812709c87cfbc94a9522da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableIpv6", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enableNatGateway")
    def enable_nat_gateway(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enableNatGateway"))

    @enable_nat_gateway.setter
    def enable_nat_gateway(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e344fc7a745511055af819bccd6e3a38b8019555fe76abdefd5243036cd15cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableNatGateway", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enableNetworkAddressUsageMetrics")
    def enable_network_address_usage_metrics(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enableNetworkAddressUsageMetrics"))

    @enable_network_address_usage_metrics.setter
    def enable_network_address_usage_metrics(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e2297569d5db042aa3f23a1adcc0b78eb38c23ea2dce4c1e98b8d9b1b6f88f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableNetworkAddressUsageMetrics", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enablePublicRedshift")
    def enable_public_redshift(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enablePublicRedshift"))

    @enable_public_redshift.setter
    def enable_public_redshift(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e207433146f67a36aedfefe76b075311ef8e0115b6873cdc468c5faf64863be0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablePublicRedshift", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enableVpnGateway")
    def enable_vpn_gateway(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enableVpnGateway"))

    @enable_vpn_gateway.setter
    def enable_vpn_gateway(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c80f8fb26f5b7c219057b7803f9eb03666eeeb9f7a0adfdae29132dca261cc85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableVpnGateway", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="externalNatIpIds")
    def external_nat_ip_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "externalNatIpIds"))

    @external_nat_ip_ids.setter
    def external_nat_ip_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf698b63f74810d0a2de6b4b1a75e4395735391a813a5fc38f10a0022379117b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalNatIpIds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="externalNatIps")
    def external_nat_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "externalNatIps"))

    @external_nat_ips.setter
    def external_nat_ips(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__796fbebaeb82847b48b21e88b01ea498a76bbc5a3e3daaca330f0afa8786a00a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalNatIps", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowLogCloudwatchIamRoleArn")
    def flow_log_cloudwatch_iam_role_arn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flowLogCloudwatchIamRoleArn"))

    @flow_log_cloudwatch_iam_role_arn.setter
    def flow_log_cloudwatch_iam_role_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19a9e1ba46d733493db96fb0574dc59732adacf19d84d7e99a7e3fc7f9aa75a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowLogCloudwatchIamRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowLogCloudwatchLogGroupClass")
    def flow_log_cloudwatch_log_group_class(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flowLogCloudwatchLogGroupClass"))

    @flow_log_cloudwatch_log_group_class.setter
    def flow_log_cloudwatch_log_group_class(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8075a59939cc739701ecbd09dd4516301ed7362b6e448a33bb274843efd0bba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowLogCloudwatchLogGroupClass", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowLogCloudwatchLogGroupKmsKeyId")
    def flow_log_cloudwatch_log_group_kms_key_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flowLogCloudwatchLogGroupKmsKeyId"))

    @flow_log_cloudwatch_log_group_kms_key_id.setter
    def flow_log_cloudwatch_log_group_kms_key_id(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea9aa1e8e035162e2a12f837e3a5862f361702cd30bb8fe33a11bdf1f22e8781)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowLogCloudwatchLogGroupKmsKeyId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowLogCloudwatchLogGroupNamePrefix")
    def flow_log_cloudwatch_log_group_name_prefix(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flowLogCloudwatchLogGroupNamePrefix"))

    @flow_log_cloudwatch_log_group_name_prefix.setter
    def flow_log_cloudwatch_log_group_name_prefix(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__920d1acd6786899641bbf7c6abd793c4b533dd6188442b85514dd0c59911af5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowLogCloudwatchLogGroupNamePrefix", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowLogCloudwatchLogGroupNameSuffix")
    def flow_log_cloudwatch_log_group_name_suffix(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flowLogCloudwatchLogGroupNameSuffix"))

    @flow_log_cloudwatch_log_group_name_suffix.setter
    def flow_log_cloudwatch_log_group_name_suffix(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4adc9a4b4ae1a0560531d09afd18102f98105038f059545e3ebf88262cab424)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowLogCloudwatchLogGroupNameSuffix", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowLogCloudwatchLogGroupRetentionInDays")
    def flow_log_cloudwatch_log_group_retention_in_days(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "flowLogCloudwatchLogGroupRetentionInDays"))

    @flow_log_cloudwatch_log_group_retention_in_days.setter
    def flow_log_cloudwatch_log_group_retention_in_days(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91f9ca3784663281378f37e265c79e34dd71617dc556385e823b3acd076d12fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowLogCloudwatchLogGroupRetentionInDays", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowLogCloudwatchLogGroupSkipDestroy")
    def flow_log_cloudwatch_log_group_skip_destroy(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "flowLogCloudwatchLogGroupSkipDestroy"))

    @flow_log_cloudwatch_log_group_skip_destroy.setter
    def flow_log_cloudwatch_log_group_skip_destroy(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3d248a591b9c0e3ecd5f69c1d9a087530c95898ab6c5f677ae7728232751d68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowLogCloudwatchLogGroupSkipDestroy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowLogDeliverCrossAccountRole")
    def flow_log_deliver_cross_account_role(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flowLogDeliverCrossAccountRole"))

    @flow_log_deliver_cross_account_role.setter
    def flow_log_deliver_cross_account_role(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58f26752bbbd325e1ff31c97703319a97b55a19defb47daa052d20c5dbed5f61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowLogDeliverCrossAccountRole", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowLogDestinationArn")
    def flow_log_destination_arn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flowLogDestinationArn"))

    @flow_log_destination_arn.setter
    def flow_log_destination_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b223678d15ce7dbcdabd08cabe9a4de5c3a6c8bd3cba71d41a02af0ccea60ae4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowLogDestinationArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowLogDestinationType")
    def flow_log_destination_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flowLogDestinationType"))

    @flow_log_destination_type.setter
    def flow_log_destination_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45e2671cbcfa534317bf478030758af062256307d5fa0a90d2b97b773c509ee0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowLogDestinationType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowLogFileFormat")
    def flow_log_file_format(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flowLogFileFormat"))

    @flow_log_file_format.setter
    def flow_log_file_format(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e93d2d61e20844650bfa663dad74b6e57ef40a7fa136bf360e0eda8f433e98d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowLogFileFormat", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowLogHiveCompatiblePartitions")
    def flow_log_hive_compatible_partitions(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "flowLogHiveCompatiblePartitions"))

    @flow_log_hive_compatible_partitions.setter
    def flow_log_hive_compatible_partitions(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbbf3cfba2fda64ee21692050bf59b61740fcca7973c4ce614bfe259df6efff5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowLogHiveCompatiblePartitions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowLogLogFormat")
    def flow_log_log_format(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flowLogLogFormat"))

    @flow_log_log_format.setter
    def flow_log_log_format(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__108a4f32dece40e78cc5f568b61347b95471e9efa6c8fbeb8f4f1c7641c6e751)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowLogLogFormat", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowLogMaxAggregationInterval")
    def flow_log_max_aggregation_interval(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "flowLogMaxAggregationInterval"))

    @flow_log_max_aggregation_interval.setter
    def flow_log_max_aggregation_interval(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__726e6fce20fa9aa7f8ae2df1616cab4060f88d1f906ccbed6679cf486dda9ef9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowLogMaxAggregationInterval", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowLogPerHourPartition")
    def flow_log_per_hour_partition(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "flowLogPerHourPartition"))

    @flow_log_per_hour_partition.setter
    def flow_log_per_hour_partition(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a89224b8e390c752ba27969c1e8c04bd729fa981dfad345553bfea22e2d4544)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowLogPerHourPartition", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowLogTrafficType")
    def flow_log_traffic_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flowLogTrafficType"))

    @flow_log_traffic_type.setter
    def flow_log_traffic_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4766349345d4311e4d7fd8eaf8a64d9e31e8838c80415dce7d088bca75d1a61a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowLogTrafficType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="igwTags")
    def igw_tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "igwTags"))

    @igw_tags.setter
    def igw_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dd3f77191587bd2ae046944d0d5bf90e66e51145e744b8f1cf17079eb85c928)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "igwTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="instanceTenancy")
    def instance_tenancy(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTenancy"))

    @instance_tenancy.setter
    def instance_tenancy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e84ca9b65d9c257980383158795874b631a0d5dad154d6a65cd2f0a4e19f191f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceTenancy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="intraAclTags")
    def intra_acl_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "intraAclTags"))

    @intra_acl_tags.setter
    def intra_acl_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84edec64b32293f0d2dbd6e20d2a6864b5b46abcc2b750be3ec6fe5be9accbbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intraAclTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="intraDedicatedNetworkAcl")
    def intra_dedicated_network_acl(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "intraDedicatedNetworkAcl"))

    @intra_dedicated_network_acl.setter
    def intra_dedicated_network_acl(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__398ce30a45ee4d02b2aa14fc7f2e8c80bc46980a3d9bfd82fa7c94332a1ce5e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intraDedicatedNetworkAcl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="intraInboundAclRules")
    def intra_inbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "intraInboundAclRules"))

    @intra_inbound_acl_rules.setter
    def intra_inbound_acl_rules(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3300edb1a54db6ca525f79edcc6ccafca7bd8240d9c82208e3a3b79535c2df81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intraInboundAclRules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="intraOutboundAclRules")
    def intra_outbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "intraOutboundAclRules"))

    @intra_outbound_acl_rules.setter
    def intra_outbound_acl_rules(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c4cbde4e3db469aac802cb3962aa5ee5994808f9fb5abd5ffc775d6d0e9fafa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intraOutboundAclRules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="intraRouteTableTags")
    def intra_route_table_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "intraRouteTableTags"))

    @intra_route_table_tags.setter
    def intra_route_table_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6c7569d0de94ae2933fc3c133c0ec53783ed214ad4bc0cb4458da6780e5a5c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intraRouteTableTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="intraSubnetAssignIpv6AddressOnCreation")
    def intra_subnet_assign_ipv6_address_on_creation(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "intraSubnetAssignIpv6AddressOnCreation"))

    @intra_subnet_assign_ipv6_address_on_creation.setter
    def intra_subnet_assign_ipv6_address_on_creation(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af3410bacffdfebcf39a903470b70702ecbeb0c50f39d8fc36f041bc1bf15848)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intraSubnetAssignIpv6AddressOnCreation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="intraSubnetEnableDns64")
    def intra_subnet_enable_dns64(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "intraSubnetEnableDns64"))

    @intra_subnet_enable_dns64.setter
    def intra_subnet_enable_dns64(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1fa41975ac99ebfd84dce20b141f92d9c0a005a8791235914b6955a0851c524)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intraSubnetEnableDns64", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="intraSubnetEnableResourceNameDnsAaaaRecordOnLaunch")
    def intra_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "intraSubnetEnableResourceNameDnsAaaaRecordOnLaunch"))

    @intra_subnet_enable_resource_name_dns_aaaa_record_on_launch.setter
    def intra_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b157bf7a56aa4db9d358ea2f087119e3a4382896234ed449d6d4307a4225b73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intraSubnetEnableResourceNameDnsAaaaRecordOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="intraSubnetEnableResourceNameDnsARecordOnLaunch")
    def intra_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "intraSubnetEnableResourceNameDnsARecordOnLaunch"))

    @intra_subnet_enable_resource_name_dns_a_record_on_launch.setter
    def intra_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d4ca4c27e22bf4254260d46f235cee9350f8b20a8d2d67e0fac9f79bd4fb5aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intraSubnetEnableResourceNameDnsARecordOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="intraSubnetIpv6Native")
    def intra_subnet_ipv6_native(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "intraSubnetIpv6Native"))

    @intra_subnet_ipv6_native.setter
    def intra_subnet_ipv6_native(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b93b7204dcbcfd2a73039cc3c471571f000a94b83ec06441f0e5992dd87e083)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intraSubnetIpv6Native", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="intraSubnetIpv6Prefixes")
    def intra_subnet_ipv6_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "intraSubnetIpv6Prefixes"))

    @intra_subnet_ipv6_prefixes.setter
    def intra_subnet_ipv6_prefixes(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6597e8260dae99d1269791beef323e61c5bb6cc5353d81add7367f6665e88cd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intraSubnetIpv6Prefixes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="intraSubnetNames")
    def intra_subnet_names(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "intraSubnetNames"))

    @intra_subnet_names.setter
    def intra_subnet_names(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a36031178f2a94c650f42652622604e05fa2a625bb89d7a89dab357fc2aae47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intraSubnetNames", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="intraSubnetPrivateDnsHostnameTypeOnLaunch")
    def intra_subnet_private_dns_hostname_type_on_launch(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intraSubnetPrivateDnsHostnameTypeOnLaunch"))

    @intra_subnet_private_dns_hostname_type_on_launch.setter
    def intra_subnet_private_dns_hostname_type_on_launch(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__399556e5da63bd96f9444f8fb86098fd69e8eef0cc1fbb00edd2f03f1dfc3d3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intraSubnetPrivateDnsHostnameTypeOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="intraSubnets")
    def intra_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "intraSubnets"))

    @intra_subnets.setter
    def intra_subnets(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e92f2f5a50e0dea9d680cd242269319284b51843e0357412f07523df386d90c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intraSubnets", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="intraSubnetSuffix")
    def intra_subnet_suffix(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intraSubnetSuffix"))

    @intra_subnet_suffix.setter
    def intra_subnet_suffix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__041b937728f2f6e8db0eccbfa68ac8c7bbc2f7f8edf0caeec2fcc9d3c7f26ba7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intraSubnetSuffix", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="intraSubnetTags")
    def intra_subnet_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "intraSubnetTags"))

    @intra_subnet_tags.setter
    def intra_subnet_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ace6041e64215939faad638e29090fa5906c6f01e533aaf4e9bb97d2ad36eb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intraSubnetTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipv4IpamPoolId")
    def ipv4_ipam_pool_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv4IpamPoolId"))

    @ipv4_ipam_pool_id.setter
    def ipv4_ipam_pool_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee34601531e9d1b19e9d39ef0e1ef1f4b6ceeaafc3c0099d1ab116d8628ecab3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv4IpamPoolId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipv4NetmaskLength")
    def ipv4_netmask_length(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ipv4NetmaskLength"))

    @ipv4_netmask_length.setter
    def ipv4_netmask_length(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3e5bc8ba989c9d913a731134d00d3404fb88ace9efadfb813236ff21574a83e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv4NetmaskLength", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipv6Cidr")
    def ipv6_cidr(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv6Cidr"))

    @ipv6_cidr.setter
    def ipv6_cidr(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__053af3691edcb6a33bdada50c84f58beeaead847253a9fa0d5e7875aad832d4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6Cidr", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipv6CidrBlockNetworkBorderGroup")
    def ipv6_cidr_block_network_border_group(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv6CidrBlockNetworkBorderGroup"))

    @ipv6_cidr_block_network_border_group.setter
    def ipv6_cidr_block_network_border_group(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baa50918760d03da3776281e0e691bcfa1ae858236a4213e49c1932beca6cdad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6CidrBlockNetworkBorderGroup", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipv6IpamPoolId")
    def ipv6_ipam_pool_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv6IpamPoolId"))

    @ipv6_ipam_pool_id.setter
    def ipv6_ipam_pool_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aa2e706f45e55fbe0acdeb94afd9dc60981b4188c6a0dff810179bab54e0b87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6IpamPoolId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipv6NetmaskLength")
    def ipv6_netmask_length(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ipv6NetmaskLength"))

    @ipv6_netmask_length.setter
    def ipv6_netmask_length(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e2da995c87a6aa99c3c86fffeb256e8ce88ad830b6c9799b806f039e2a682e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6NetmaskLength", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="manageDefaultNetworkAcl")
    def manage_default_network_acl(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "manageDefaultNetworkAcl"))

    @manage_default_network_acl.setter
    def manage_default_network_acl(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bf7e37ca69daa7b44eeeb7114a22c3a6b1181962469de2397c5a282d6840911)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manageDefaultNetworkAcl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="manageDefaultRouteTable")
    def manage_default_route_table(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "manageDefaultRouteTable"))

    @manage_default_route_table.setter
    def manage_default_route_table(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8bc8e61d034e30c455492fc81961c2ba032ebb9a804150111bc7f0c1ac2782a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manageDefaultRouteTable", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="manageDefaultSecurityGroup")
    def manage_default_security_group(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "manageDefaultSecurityGroup"))

    @manage_default_security_group.setter
    def manage_default_security_group(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b534a6f17cba668bf20e4f1a571cb46b183091004fa167192e70b5b1755ebd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manageDefaultSecurityGroup", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="manageDefaultVpc")
    def manage_default_vpc(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "manageDefaultVpc"))

    @manage_default_vpc.setter
    def manage_default_vpc(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a6510bbc2e317a21c4cc82510fb1ec04441a9760a46fec535a7c90833a84a38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manageDefaultVpc", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mapCustomerOwnedIpOnLaunch")
    def map_customer_owned_ip_on_launch(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "mapCustomerOwnedIpOnLaunch"))

    @map_customer_owned_ip_on_launch.setter
    def map_customer_owned_ip_on_launch(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84bf2a6779dd2572808ceb6676d77281427e0473d74f79e36aa50ed1f7e0ad82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mapCustomerOwnedIpOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mapPublicIpOnLaunch")
    def map_public_ip_on_launch(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "mapPublicIpOnLaunch"))

    @map_public_ip_on_launch.setter
    def map_public_ip_on_launch(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5b8ae6598f9ae485cc27a8e8dad462fa88a65af2ae0fcfcede3e42a054551a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mapPublicIpOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79bdcdaf09aed8a9b2b62c6243dc6760292310d8d365b1a5b08534ce40a811f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="natEipTags")
    def nat_eip_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "natEipTags"))

    @nat_eip_tags.setter
    def nat_eip_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f993f9004736b963d696e52a01f123e3618f35acfb6a215bbc23fa86e7192670)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "natEipTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="natGatewayDestinationCidrBlock")
    def nat_gateway_destination_cidr_block(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "natGatewayDestinationCidrBlock"))

    @nat_gateway_destination_cidr_block.setter
    def nat_gateway_destination_cidr_block(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce5b0659fcd074b1b400b777ab73219f2efac49be7af3c9f705434ffb2de20a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "natGatewayDestinationCidrBlock", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="natGatewayTags")
    def nat_gateway_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "natGatewayTags"))

    @nat_gateway_tags.setter
    def nat_gateway_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cd094b4b3d16ecea6ea693da3ccce21f89784684c5b429c1a8581e783f09e2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "natGatewayTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="oneNatGatewayPerAz")
    def one_nat_gateway_per_az(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "oneNatGatewayPerAz"))

    @one_nat_gateway_per_az.setter
    def one_nat_gateway_per_az(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3810ab80b87bcf31490c692e42b984cf8efc6d079fb6b205533b0051534c2839)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oneNatGatewayPerAz", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outpostAclTags")
    def outpost_acl_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "outpostAclTags"))

    @outpost_acl_tags.setter
    def outpost_acl_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e1aca22671fd3d735988b5627e89c7e947345cd9d3e3945632f6bb651d3034c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostAclTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outpostArn")
    def outpost_arn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outpostArn"))

    @outpost_arn.setter
    def outpost_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2756a27f1337d672223bb9365be7e301b50d7713529d84b0a11bc5dec4d03cc9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outpostAz")
    def outpost_az(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outpostAz"))

    @outpost_az.setter
    def outpost_az(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0864a13bd398c3440fe15f16b4956f1b4de2a202d74aac6914736d05a78287bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostAz", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outpostDedicatedNetworkAcl")
    def outpost_dedicated_network_acl(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "outpostDedicatedNetworkAcl"))

    @outpost_dedicated_network_acl.setter
    def outpost_dedicated_network_acl(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b241815eb3cab5d93f81ae50d317f0ceb1b4d208f440438af2c148473270d5c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostDedicatedNetworkAcl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outpostInboundAclRules")
    def outpost_inbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "outpostInboundAclRules"))

    @outpost_inbound_acl_rules.setter
    def outpost_inbound_acl_rules(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__106e9fd31c1f82360cb56d27132625354b826f0ac0273eceb5242c76ab8a821e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostInboundAclRules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outpostOutboundAclRules")
    def outpost_outbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "outpostOutboundAclRules"))

    @outpost_outbound_acl_rules.setter
    def outpost_outbound_acl_rules(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__350d31bd1bda7b56378692512ba11c75204362ef07f26d6eff74766e55d98836)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostOutboundAclRules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outpostSubnetAssignIpv6AddressOnCreation")
    def outpost_subnet_assign_ipv6_address_on_creation(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "outpostSubnetAssignIpv6AddressOnCreation"))

    @outpost_subnet_assign_ipv6_address_on_creation.setter
    def outpost_subnet_assign_ipv6_address_on_creation(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dcf7bc316dab6067ba11cf9c018057abe50cb1522795778b50cfd72e7e66c09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostSubnetAssignIpv6AddressOnCreation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outpostSubnetEnableDns64")
    def outpost_subnet_enable_dns64(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "outpostSubnetEnableDns64"))

    @outpost_subnet_enable_dns64.setter
    def outpost_subnet_enable_dns64(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1770effef7f97a65c7f920c9d7b13d7b3bb4796f87f0cd82eaed000d3d0532f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostSubnetEnableDns64", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outpostSubnetEnableResourceNameDnsAaaaRecordOnLaunch")
    def outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "outpostSubnetEnableResourceNameDnsAaaaRecordOnLaunch"))

    @outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch.setter
    def outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddb652febe09952f5f7b75127ac1d7425d24b68f38111dd4fb0f7b5efd73d118)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostSubnetEnableResourceNameDnsAaaaRecordOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outpostSubnetEnableResourceNameDnsARecordOnLaunch")
    def outpost_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "outpostSubnetEnableResourceNameDnsARecordOnLaunch"))

    @outpost_subnet_enable_resource_name_dns_a_record_on_launch.setter
    def outpost_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c061ea484b7a50ee7f31fb25bb4e8d1c2374f87b5fc094638aee1d46fd469157)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostSubnetEnableResourceNameDnsARecordOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outpostSubnetIpv6Native")
    def outpost_subnet_ipv6_native(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "outpostSubnetIpv6Native"))

    @outpost_subnet_ipv6_native.setter
    def outpost_subnet_ipv6_native(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__496ca4b4e63e2ca846db8b42c82fc97497f299478f8c05507c123b56653e3822)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostSubnetIpv6Native", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outpostSubnetIpv6Prefixes")
    def outpost_subnet_ipv6_prefixes(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "outpostSubnetIpv6Prefixes"))

    @outpost_subnet_ipv6_prefixes.setter
    def outpost_subnet_ipv6_prefixes(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15d0487aaf0fa26a9a17e7ff9a561301d3dc67ecac213ecc8c4500da1720ae97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostSubnetIpv6Prefixes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outpostSubnetNames")
    def outpost_subnet_names(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "outpostSubnetNames"))

    @outpost_subnet_names.setter
    def outpost_subnet_names(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__057961e32a519377c227bb6f576215bd253e03b548d9f8a6c2c073c0748a0192)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostSubnetNames", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outpostSubnetPrivateDnsHostnameTypeOnLaunch")
    def outpost_subnet_private_dns_hostname_type_on_launch(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outpostSubnetPrivateDnsHostnameTypeOnLaunch"))

    @outpost_subnet_private_dns_hostname_type_on_launch.setter
    def outpost_subnet_private_dns_hostname_type_on_launch(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9bead36c6a48eb8eeb69aa65bbacdfd060becda77b8bcbe95dd8bfbfa65f79f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostSubnetPrivateDnsHostnameTypeOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outpostSubnets")
    def outpost_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "outpostSubnets"))

    @outpost_subnets.setter
    def outpost_subnets(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7b32476efe98e2a0817e4e79fdf7d93c58f4cfddeb0e522409ca4747eda6361)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostSubnets", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outpostSubnetSuffix")
    def outpost_subnet_suffix(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outpostSubnetSuffix"))

    @outpost_subnet_suffix.setter
    def outpost_subnet_suffix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05086260e02edec212fc912c4030ed1745c81d9231028187d359eaa4ee5ddb91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostSubnetSuffix", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outpostSubnetTags")
    def outpost_subnet_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "outpostSubnetTags"))

    @outpost_subnet_tags.setter
    def outpost_subnet_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff2d331be5adbb3305410667d2715cc3ec363e8e7ac583c6dd6f6c945a06f4d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outpostSubnetTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privateAclTags")
    def private_acl_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "privateAclTags"))

    @private_acl_tags.setter
    def private_acl_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffc33b8e6048ed4e7fc6835208af109b6affb5ae9ab5c1750a31b1d8bfc088e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateAclTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privateDedicatedNetworkAcl")
    def private_dedicated_network_acl(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "privateDedicatedNetworkAcl"))

    @private_dedicated_network_acl.setter
    def private_dedicated_network_acl(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31760941123757ddc7f8632458cd731b97f19d50286aa3e0597709e226850c4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateDedicatedNetworkAcl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privateInboundAclRules")
    def private_inbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "privateInboundAclRules"))

    @private_inbound_acl_rules.setter
    def private_inbound_acl_rules(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80131791c554aaaeef2bb300a5a006fed1e7c520e8919f85494ed30002948338)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateInboundAclRules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privateOutboundAclRules")
    def private_outbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "privateOutboundAclRules"))

    @private_outbound_acl_rules.setter
    def private_outbound_acl_rules(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64193c0e68f340669c92e091af6f06bfd957813a6e9f06ea909d4667383bcb78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateOutboundAclRules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privateRouteTableTags")
    def private_route_table_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "privateRouteTableTags"))

    @private_route_table_tags.setter
    def private_route_table_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3256d4048ca41eff9b7cdeab34640d7c5572f1137ae46c342551e9ccdd6a60b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateRouteTableTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privateSubnetAssignIpv6AddressOnCreation")
    def private_subnet_assign_ipv6_address_on_creation(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "privateSubnetAssignIpv6AddressOnCreation"))

    @private_subnet_assign_ipv6_address_on_creation.setter
    def private_subnet_assign_ipv6_address_on_creation(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c812b00d56177f52f1deb8895ebf343be7f9f5d6ea9316c07f9c18fa6d353c19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateSubnetAssignIpv6AddressOnCreation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privateSubnetEnableDns64")
    def private_subnet_enable_dns64(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "privateSubnetEnableDns64"))

    @private_subnet_enable_dns64.setter
    def private_subnet_enable_dns64(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05e233eeaeef1a1dc41ef1b1e34aa23afdef8487d207436e191008db089cf297)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateSubnetEnableDns64", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privateSubnetEnableResourceNameDnsAaaaRecordOnLaunch")
    def private_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "privateSubnetEnableResourceNameDnsAaaaRecordOnLaunch"))

    @private_subnet_enable_resource_name_dns_aaaa_record_on_launch.setter
    def private_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14931e29610838a69383bf280b39281c5de0a87f97163b3797e5293ff9c6700e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateSubnetEnableResourceNameDnsAaaaRecordOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privateSubnetEnableResourceNameDnsARecordOnLaunch")
    def private_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "privateSubnetEnableResourceNameDnsARecordOnLaunch"))

    @private_subnet_enable_resource_name_dns_a_record_on_launch.setter
    def private_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fe3b27c4b11cd3cf46abceaab395d0e1738b2634ec89192e0620d22e4850c01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateSubnetEnableResourceNameDnsARecordOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privateSubnetIpv6Native")
    def private_subnet_ipv6_native(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "privateSubnetIpv6Native"))

    @private_subnet_ipv6_native.setter
    def private_subnet_ipv6_native(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__571559e8afb94db1654b131b99fc9251a23415575b06d273f0b9457436ee2f9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateSubnetIpv6Native", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privateSubnetIpv6Prefixes")
    def private_subnet_ipv6_prefixes(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "privateSubnetIpv6Prefixes"))

    @private_subnet_ipv6_prefixes.setter
    def private_subnet_ipv6_prefixes(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a1927c9a413bf4e94413632d36675c81407589dcfb7c14cf1528d5801f4e148)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateSubnetIpv6Prefixes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privateSubnetNames")
    def private_subnet_names(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "privateSubnetNames"))

    @private_subnet_names.setter
    def private_subnet_names(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f21caa57eba2f42058f57abc438e13a8d4488422b30bd64d119df5db89c38f02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateSubnetNames", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privateSubnetPrivateDnsHostnameTypeOnLaunch")
    def private_subnet_private_dns_hostname_type_on_launch(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateSubnetPrivateDnsHostnameTypeOnLaunch"))

    @private_subnet_private_dns_hostname_type_on_launch.setter
    def private_subnet_private_dns_hostname_type_on_launch(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__600cbca1a56591036e47a444ea68d9aab8a7df016f88e0c3b5ddd75f617ac063)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateSubnetPrivateDnsHostnameTypeOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privateSubnets")
    def private_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "privateSubnets"))

    @private_subnets.setter
    def private_subnets(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__911d9f6ed5111f187a9d2630e0bc6983c84d8c95531b7eae48112ea8b87077f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateSubnets", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privateSubnetSuffix")
    def private_subnet_suffix(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateSubnetSuffix"))

    @private_subnet_suffix.setter
    def private_subnet_suffix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91a705f4ab73184b6689bba963e3276199fee3e0145ade67880d950af3ae673c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateSubnetSuffix", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privateSubnetTags")
    def private_subnet_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "privateSubnetTags"))

    @private_subnet_tags.setter
    def private_subnet_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a097c4e4f8025347132ddb88ddfee71472b292cd37f370a7cb8656d503b3375)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateSubnetTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privateSubnetTagsPerAz")
    def private_subnet_tags_per_az(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "privateSubnetTagsPerAz"))

    @private_subnet_tags_per_az.setter
    def private_subnet_tags_per_az(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2a41ea842f3047e4d9067f16517fae49d9f594122d5848b94fc6e15eb65003b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateSubnetTagsPerAz", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="propagateIntraRouteTablesVgw")
    def propagate_intra_route_tables_vgw(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "propagateIntraRouteTablesVgw"))

    @propagate_intra_route_tables_vgw.setter
    def propagate_intra_route_tables_vgw(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b5429e3718ea772d4c95a546ffd57d8efb248cb4d3db76103297cdc4e9a4383)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagateIntraRouteTablesVgw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="propagatePrivateRouteTablesVgw")
    def propagate_private_route_tables_vgw(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "propagatePrivateRouteTablesVgw"))

    @propagate_private_route_tables_vgw.setter
    def propagate_private_route_tables_vgw(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d091c45179fb3ed91279840894f3d0dd5bcab64b14c0c58bdfc8441a5a0f2d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagatePrivateRouteTablesVgw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="propagatePublicRouteTablesVgw")
    def propagate_public_route_tables_vgw(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "propagatePublicRouteTablesVgw"))

    @propagate_public_route_tables_vgw.setter
    def propagate_public_route_tables_vgw(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f83e0a7fff94bac2d39081ac751cefecc432a2a157da3e7e1168ea4b94aaa32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagatePublicRouteTablesVgw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicAclTags")
    def public_acl_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "publicAclTags"))

    @public_acl_tags.setter
    def public_acl_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76990ef2189a0292944e6f98d67ed524280323ade216563800bfe46af72121ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicAclTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicDedicatedNetworkAcl")
    def public_dedicated_network_acl(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "publicDedicatedNetworkAcl"))

    @public_dedicated_network_acl.setter
    def public_dedicated_network_acl(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df557fd9d154386f943c4fa65a2b78e4e6b81f1565ad749f05b20fab10e3d26a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicDedicatedNetworkAcl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicInboundAclRules")
    def public_inbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "publicInboundAclRules"))

    @public_inbound_acl_rules.setter
    def public_inbound_acl_rules(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__558bac9bf9fea3261d8d15324036be768e2b927e0c2476dc76ec7a079c0beaa9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicInboundAclRules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicOutboundAclRules")
    def public_outbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "publicOutboundAclRules"))

    @public_outbound_acl_rules.setter
    def public_outbound_acl_rules(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3368f32241d617fec75fe7b16e6664a580606d3710b7d68af5d3fc4e4d26173)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicOutboundAclRules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicRouteTableTags")
    def public_route_table_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "publicRouteTableTags"))

    @public_route_table_tags.setter
    def public_route_table_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__339672d1779bc6aca172917c7df78bd2504bc6a6a607c13db5b489ff579d8e0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicRouteTableTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicSubnetAssignIpv6AddressOnCreation")
    def public_subnet_assign_ipv6_address_on_creation(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "publicSubnetAssignIpv6AddressOnCreation"))

    @public_subnet_assign_ipv6_address_on_creation.setter
    def public_subnet_assign_ipv6_address_on_creation(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0deedec8c161ed2b1bd6579cdcfd8ee0e0df2976a1056850d9653ca38e11e5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicSubnetAssignIpv6AddressOnCreation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicSubnetEnableDns64")
    def public_subnet_enable_dns64(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "publicSubnetEnableDns64"))

    @public_subnet_enable_dns64.setter
    def public_subnet_enable_dns64(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c587a87718b46a5cb103134a8b82fd5833a85d2915d3523acd888ff88a1b78b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicSubnetEnableDns64", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicSubnetEnableResourceNameDnsAaaaRecordOnLaunch")
    def public_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "publicSubnetEnableResourceNameDnsAaaaRecordOnLaunch"))

    @public_subnet_enable_resource_name_dns_aaaa_record_on_launch.setter
    def public_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96c423f97d564d8c5fb71ed8551a67288cfcddcae5b76bd891ee75255a97aa43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicSubnetEnableResourceNameDnsAaaaRecordOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicSubnetEnableResourceNameDnsARecordOnLaunch")
    def public_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "publicSubnetEnableResourceNameDnsARecordOnLaunch"))

    @public_subnet_enable_resource_name_dns_a_record_on_launch.setter
    def public_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f907a799fbe9efd59314c9785ab20c576a38709285dc9fbb08df3792c8e3f41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicSubnetEnableResourceNameDnsARecordOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicSubnetIpv6Native")
    def public_subnet_ipv6_native(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "publicSubnetIpv6Native"))

    @public_subnet_ipv6_native.setter
    def public_subnet_ipv6_native(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec652f1b48c3f0dffb67aa880c3d1f9cc3805d5b64aaeaec347dd742d4f6534c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicSubnetIpv6Native", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicSubnetIpv6Prefixes")
    def public_subnet_ipv6_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "publicSubnetIpv6Prefixes"))

    @public_subnet_ipv6_prefixes.setter
    def public_subnet_ipv6_prefixes(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11040abad81734974d02441e859775a7de6cc55e7da56a8a2c01a4a3f801f5a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicSubnetIpv6Prefixes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicSubnetNames")
    def public_subnet_names(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "publicSubnetNames"))

    @public_subnet_names.setter
    def public_subnet_names(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af11bfa0f75de0837ac47155fe4e5e1f5e2f8edb2fdf6aa935a3bfa8aa6649e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicSubnetNames", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicSubnetPrivateDnsHostnameTypeOnLaunch")
    def public_subnet_private_dns_hostname_type_on_launch(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicSubnetPrivateDnsHostnameTypeOnLaunch"))

    @public_subnet_private_dns_hostname_type_on_launch.setter
    def public_subnet_private_dns_hostname_type_on_launch(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90ce7a8a0e906c965d9e90c63d6e22bd429223c63cd2a7be4e408dccea576b16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicSubnetPrivateDnsHostnameTypeOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicSubnets")
    def public_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "publicSubnets"))

    @public_subnets.setter
    def public_subnets(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62ef78822c655030f526583590edf72ea7c77ca1a9905ce36ac66317d1987b05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicSubnets", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicSubnetSuffix")
    def public_subnet_suffix(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicSubnetSuffix"))

    @public_subnet_suffix.setter
    def public_subnet_suffix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1377e062da302bcffd8b87439d46c6040855f3c3c231f6c926419a446b66e598)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicSubnetSuffix", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicSubnetTags")
    def public_subnet_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "publicSubnetTags"))

    @public_subnet_tags.setter
    def public_subnet_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7798401f732de4991e8ee0e3c12bdaf5a92df225b7f5bfc2ae4b7a8a2fec9bcc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicSubnetTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicSubnetTagsPerAz")
    def public_subnet_tags_per_az(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "publicSubnetTagsPerAz"))

    @public_subnet_tags_per_az.setter
    def public_subnet_tags_per_az(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de7aa747a0497ec37fd5bbcc29185da02cdbfef3771fc2fcd252fab3a9b9227d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicSubnetTagsPerAz", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="putinKhuylo")
    def putin_khuylo(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "putinKhuylo"))

    @putin_khuylo.setter
    def putin_khuylo(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65d0ecdab60b588f6dc0fafda59770703b7fe6e1737c5b95751c971fb9d55e08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "putinKhuylo", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftAclTags")
    def redshift_acl_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "redshiftAclTags"))

    @redshift_acl_tags.setter
    def redshift_acl_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bfab94d814463999d0398a1ec28ea240f597504ec528b98fc741a8b58e39a48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftAclTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftDedicatedNetworkAcl")
    def redshift_dedicated_network_acl(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "redshiftDedicatedNetworkAcl"))

    @redshift_dedicated_network_acl.setter
    def redshift_dedicated_network_acl(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df3063e6588b53eb0f2678487e35ab76d4f885bf93eb049f7947dedb5bbd75cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftDedicatedNetworkAcl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftInboundAclRules")
    def redshift_inbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "redshiftInboundAclRules"))

    @redshift_inbound_acl_rules.setter
    def redshift_inbound_acl_rules(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3005d8b133a1baf2fc5e36f7379db9adce370d29402131ee66a1e3794bd3d5ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftInboundAclRules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftOutboundAclRules")
    def redshift_outbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "redshiftOutboundAclRules"))

    @redshift_outbound_acl_rules.setter
    def redshift_outbound_acl_rules(
        self,
        value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa0d9c253451026c97230bb226c3642a146dc092a07e7bf983837be94a021aaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftOutboundAclRules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftRouteTableTags")
    def redshift_route_table_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "redshiftRouteTableTags"))

    @redshift_route_table_tags.setter
    def redshift_route_table_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b5788ebdfe963a6960acd204dea7ebd903bf7e09d6e10a112ccf257d76643f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftRouteTableTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftSubnetAssignIpv6AddressOnCreation")
    def redshift_subnet_assign_ipv6_address_on_creation(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "redshiftSubnetAssignIpv6AddressOnCreation"))

    @redshift_subnet_assign_ipv6_address_on_creation.setter
    def redshift_subnet_assign_ipv6_address_on_creation(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98f43049959b70f5573ce02eec0ce86341789c2eaacfe9aa72a6961b8f2b6036)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftSubnetAssignIpv6AddressOnCreation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftSubnetEnableDns64")
    def redshift_subnet_enable_dns64(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "redshiftSubnetEnableDns64"))

    @redshift_subnet_enable_dns64.setter
    def redshift_subnet_enable_dns64(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cea9fe70657515ad2e75e54f220413acf2fc3de1fc1be094545c282e9c30507a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftSubnetEnableDns64", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftSubnetEnableResourceNameDnsAaaaRecordOnLaunch")
    def redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "redshiftSubnetEnableResourceNameDnsAaaaRecordOnLaunch"))

    @redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch.setter
    def redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a037288e7c7eda7103f8641012aebdfdc6a67179dd94608e36c9b9560f58615b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftSubnetEnableResourceNameDnsAaaaRecordOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftSubnetEnableResourceNameDnsARecordOnLaunch")
    def redshift_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "redshiftSubnetEnableResourceNameDnsARecordOnLaunch"))

    @redshift_subnet_enable_resource_name_dns_a_record_on_launch.setter
    def redshift_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82dfb23355ff4ac1e11451987a8387c77165b6d9ec6e349bd1ac7590850ef21b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftSubnetEnableResourceNameDnsARecordOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftSubnetGroupName")
    def redshift_subnet_group_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redshiftSubnetGroupName"))

    @redshift_subnet_group_name.setter
    def redshift_subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43c5df43796e3e5a31653616d3f648a9064d6d2fe3bf98af0bfd4fcb92234708)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftSubnetGroupName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftSubnetGroupTags")
    def redshift_subnet_group_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "redshiftSubnetGroupTags"))

    @redshift_subnet_group_tags.setter
    def redshift_subnet_group_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fdc96cdfff7fd0b4dc3d696d1a76a5ad3544e55490f4e3fca44a8f2b347f69b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftSubnetGroupTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftSubnetIpv6Native")
    def redshift_subnet_ipv6_native(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "redshiftSubnetIpv6Native"))

    @redshift_subnet_ipv6_native.setter
    def redshift_subnet_ipv6_native(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba123350849539a396f59d1544c52858975b46500e89846bb2f929f3e7ade3dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftSubnetIpv6Native", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftSubnetIpv6Prefixes")
    def redshift_subnet_ipv6_prefixes(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "redshiftSubnetIpv6Prefixes"))

    @redshift_subnet_ipv6_prefixes.setter
    def redshift_subnet_ipv6_prefixes(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff76ff403a72e3d4c53d3f7cdb9ca84a2590ebbbd952c4268698b04eb4d1dbb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftSubnetIpv6Prefixes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftSubnetNames")
    def redshift_subnet_names(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "redshiftSubnetNames"))

    @redshift_subnet_names.setter
    def redshift_subnet_names(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83cdf7ec35ec6bde09f07ae17bd037c16c85a32cc1776e2782199b9994e3893f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftSubnetNames", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftSubnetPrivateDnsHostnameTypeOnLaunch")
    def redshift_subnet_private_dns_hostname_type_on_launch(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redshiftSubnetPrivateDnsHostnameTypeOnLaunch"))

    @redshift_subnet_private_dns_hostname_type_on_launch.setter
    def redshift_subnet_private_dns_hostname_type_on_launch(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d1627fb8e7df3c0a69c6b8b0d1b3e7cf95017e4bfbe908edcb2c9909be2ca51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftSubnetPrivateDnsHostnameTypeOnLaunch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftSubnets")
    def redshift_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "redshiftSubnets"))

    @redshift_subnets.setter
    def redshift_subnets(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c28ddc7a688d2522ecde1466e84e13231d92a8386fdaa170ff677ab68d8d07d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftSubnets", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftSubnetSuffix")
    def redshift_subnet_suffix(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redshiftSubnetSuffix"))

    @redshift_subnet_suffix.setter
    def redshift_subnet_suffix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26cc47f20f5953b69e9ad499f521981a9638651227751f6d0dd4e4a21f7fbdaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftSubnetSuffix", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftSubnetTags")
    def redshift_subnet_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "redshiftSubnetTags"))

    @redshift_subnet_tags.setter
    def redshift_subnet_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d50796cf72be476ab120055bdf6930639483ac2b4ebf52436fcf308cda796d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftSubnetTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="reuseNatIps")
    def reuse_nat_ips(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "reuseNatIps"))

    @reuse_nat_ips.setter
    def reuse_nat_ips(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97b714ce66a0a87e83b57148d8da7767cc9a0081fd790828ff259b313c6f2076)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reuseNatIps", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="secondaryCidrBlocks")
    def secondary_cidr_blocks(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "secondaryCidrBlocks"))

    @secondary_cidr_blocks.setter
    def secondary_cidr_blocks(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c50ac9abfae08b36727e9a4fccf8e6c1323243eea7a8022c2d44fc2f259fc366)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secondaryCidrBlocks", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="singleNatGateway")
    def single_nat_gateway(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "singleNatGateway"))

    @single_nat_gateway.setter
    def single_nat_gateway(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e954e401e6c322260dea04550eabf7ace80b54ecd0ecbc70a7cfdca1856f5fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "singleNatGateway", value) # pyright: ignore[reportArgumentType]

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
            type_hints = typing.get_type_hints(_typecheckingstub__a919039858d54608f561e4fa34f8d3e0ca2816fce70d4a7c7416e7d2048caf16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="useIpamPool")
    def use_ipam_pool(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "useIpamPool"))

    @use_ipam_pool.setter
    def use_ipam_pool(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2161ed1de147cdc422d6e9eec1dc70e71c1cef8939894ffff4607451bf00c4f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useIpamPool", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcFlowLogIamPolicyName")
    def vpc_flow_log_iam_policy_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcFlowLogIamPolicyName"))

    @vpc_flow_log_iam_policy_name.setter
    def vpc_flow_log_iam_policy_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3842e9c0ac79c16cde7892ff492b5cea94efc1e0860ded0b90e11201e5c21c95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcFlowLogIamPolicyName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcFlowLogIamPolicyUseNamePrefix")
    def vpc_flow_log_iam_policy_use_name_prefix(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "vpcFlowLogIamPolicyUseNamePrefix"))

    @vpc_flow_log_iam_policy_use_name_prefix.setter
    def vpc_flow_log_iam_policy_use_name_prefix(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81336a57b1fd9a0a044e1d9cfcf0fceff5ebcb88cc253e8c8652eb685586f7ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcFlowLogIamPolicyUseNamePrefix", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcFlowLogIamRoleName")
    def vpc_flow_log_iam_role_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcFlowLogIamRoleName"))

    @vpc_flow_log_iam_role_name.setter
    def vpc_flow_log_iam_role_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5939785122602ea2bb40dca5db5c0f3b1a7979e99330ef6972d0db8482375bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcFlowLogIamRoleName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcFlowLogIamRoleUseNamePrefix")
    def vpc_flow_log_iam_role_use_name_prefix(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "vpcFlowLogIamRoleUseNamePrefix"))

    @vpc_flow_log_iam_role_use_name_prefix.setter
    def vpc_flow_log_iam_role_use_name_prefix(
        self,
        value: typing.Optional[builtins.bool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a98e4804e95d6a9dfc3cc2ddeda9e54ec862545009815be40621be7b1ed1c83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcFlowLogIamRoleUseNamePrefix", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcFlowLogPermissionsBoundary")
    def vpc_flow_log_permissions_boundary(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcFlowLogPermissionsBoundary"))

    @vpc_flow_log_permissions_boundary.setter
    def vpc_flow_log_permissions_boundary(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac14357e1e2bddfd641691ba0b3219cf2e088bdd89205862877b4d02ca2bae9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcFlowLogPermissionsBoundary", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcFlowLogTags")
    def vpc_flow_log_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "vpcFlowLogTags"))

    @vpc_flow_log_tags.setter
    def vpc_flow_log_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49a4d10b44ba7b9a941862098df254c9865b48b52395888bfb4e2369a161e36f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcFlowLogTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcTags")
    def vpc_tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "vpcTags"))

    @vpc_tags.setter
    def vpc_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5fedd8450b7eb1a91c68b4a2c81748fb032ec2d66f45a2f6f80dae52fd556fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpnGatewayAz")
    def vpn_gateway_az(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpnGatewayAz"))

    @vpn_gateway_az.setter
    def vpn_gateway_az(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01f3f2cf14a631c1f869eb7f617eaa135af99f64af91f5a345db57abafb3359e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnGatewayAz", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpnGatewayId")
    def vpn_gateway_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpnGatewayId"))

    @vpn_gateway_id.setter
    def vpn_gateway_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46886245cae571c3e4d51b0ecf721eae50f515d6c6e55b4e7346d42ef76270ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnGatewayId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpnGatewayTags")
    def vpn_gateway_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "vpnGatewayTags"))

    @vpn_gateway_tags.setter
    def vpn_gateway_tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__742ee9359f64a2b5e0e8d78fc9304572742c5c972de75ac81f717d59f546ced6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnGatewayTags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="vpc.VpcConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformModuleUserConfig],
    name_mapping={
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "providers": "providers",
        "skip_asset_creation_from_local_modules": "skipAssetCreationFromLocalModules",
        "amazon_side_asn": "amazonSideAsn",
        "azs": "azs",
        "cidr": "cidr",
        "create_database_internet_gateway_route": "createDatabaseInternetGatewayRoute",
        "create_database_nat_gateway_route": "createDatabaseNatGatewayRoute",
        "create_database_subnet_group": "createDatabaseSubnetGroup",
        "create_database_subnet_route_table": "createDatabaseSubnetRouteTable",
        "create_egress_only_igw": "createEgressOnlyIgw",
        "create_elasticache_subnet_group": "createElasticacheSubnetGroup",
        "create_elasticache_subnet_route_table": "createElasticacheSubnetRouteTable",
        "create_flow_log_cloudwatch_iam_role": "createFlowLogCloudwatchIamRole",
        "create_flow_log_cloudwatch_log_group": "createFlowLogCloudwatchLogGroup",
        "create_igw": "createIgw",
        "create_multiple_intra_route_tables": "createMultipleIntraRouteTables",
        "create_multiple_public_route_tables": "createMultiplePublicRouteTables",
        "create_private_nat_gateway_route": "createPrivateNatGatewayRoute",
        "create_redshift_subnet_group": "createRedshiftSubnetGroup",
        "create_redshift_subnet_route_table": "createRedshiftSubnetRouteTable",
        "create_vpc": "createVpc",
        "customer_gateways": "customerGateways",
        "customer_gateway_tags": "customerGatewayTags",
        "customer_owned_ipv4_pool": "customerOwnedIpv4Pool",
        "database_acl_tags": "databaseAclTags",
        "database_dedicated_network_acl": "databaseDedicatedNetworkAcl",
        "database_inbound_acl_rules": "databaseInboundAclRules",
        "database_outbound_acl_rules": "databaseOutboundAclRules",
        "database_route_table_tags": "databaseRouteTableTags",
        "database_subnet_assign_ipv6_address_on_creation": "databaseSubnetAssignIpv6AddressOnCreation",
        "database_subnet_enable_dns64": "databaseSubnetEnableDns64",
        "database_subnet_enable_resource_name_dns_aaaa_record_on_launch": "databaseSubnetEnableResourceNameDnsAaaaRecordOnLaunch",
        "database_subnet_enable_resource_name_dns_a_record_on_launch": "databaseSubnetEnableResourceNameDnsARecordOnLaunch",
        "database_subnet_group_name": "databaseSubnetGroupName",
        "database_subnet_group_tags": "databaseSubnetGroupTags",
        "database_subnet_ipv6_native": "databaseSubnetIpv6Native",
        "database_subnet_ipv6_prefixes": "databaseSubnetIpv6Prefixes",
        "database_subnet_names": "databaseSubnetNames",
        "database_subnet_private_dns_hostname_type_on_launch": "databaseSubnetPrivateDnsHostnameTypeOnLaunch",
        "database_subnets": "databaseSubnets",
        "database_subnet_suffix": "databaseSubnetSuffix",
        "database_subnet_tags": "databaseSubnetTags",
        "default_network_acl_egress": "defaultNetworkAclEgress",
        "default_network_acl_ingress": "defaultNetworkAclIngress",
        "default_network_acl_name": "defaultNetworkAclName",
        "default_network_acl_tags": "defaultNetworkAclTags",
        "default_route_table_name": "defaultRouteTableName",
        "default_route_table_propagating_vgws": "defaultRouteTablePropagatingVgws",
        "default_route_table_routes": "defaultRouteTableRoutes",
        "default_route_table_tags": "defaultRouteTableTags",
        "default_security_group_egress": "defaultSecurityGroupEgress",
        "default_security_group_ingress": "defaultSecurityGroupIngress",
        "default_security_group_name": "defaultSecurityGroupName",
        "default_security_group_tags": "defaultSecurityGroupTags",
        "default_vpc_enable_dns_hostnames": "defaultVpcEnableDnsHostnames",
        "default_vpc_enable_dns_support": "defaultVpcEnableDnsSupport",
        "default_vpc_name": "defaultVpcName",
        "default_vpc_tags": "defaultVpcTags",
        "dhcp_options_domain_name": "dhcpOptionsDomainName",
        "dhcp_options_domain_name_servers": "dhcpOptionsDomainNameServers",
        "dhcp_options_ipv6_address_preferred_lease_time": "dhcpOptionsIpv6AddressPreferredLeaseTime",
        "dhcp_options_netbios_name_servers": "dhcpOptionsNetbiosNameServers",
        "dhcp_options_netbios_node_type": "dhcpOptionsNetbiosNodeType",
        "dhcp_options_ntp_servers": "dhcpOptionsNtpServers",
        "dhcp_options_tags": "dhcpOptionsTags",
        "elasticache_acl_tags": "elasticacheAclTags",
        "elasticache_dedicated_network_acl": "elasticacheDedicatedNetworkAcl",
        "elasticache_inbound_acl_rules": "elasticacheInboundAclRules",
        "elasticache_outbound_acl_rules": "elasticacheOutboundAclRules",
        "elasticache_route_table_tags": "elasticacheRouteTableTags",
        "elasticache_subnet_assign_ipv6_address_on_creation": "elasticacheSubnetAssignIpv6AddressOnCreation",
        "elasticache_subnet_enable_dns64": "elasticacheSubnetEnableDns64",
        "elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch": "elasticacheSubnetEnableResourceNameDnsAaaaRecordOnLaunch",
        "elasticache_subnet_enable_resource_name_dns_a_record_on_launch": "elasticacheSubnetEnableResourceNameDnsARecordOnLaunch",
        "elasticache_subnet_group_name": "elasticacheSubnetGroupName",
        "elasticache_subnet_group_tags": "elasticacheSubnetGroupTags",
        "elasticache_subnet_ipv6_native": "elasticacheSubnetIpv6Native",
        "elasticache_subnet_ipv6_prefixes": "elasticacheSubnetIpv6Prefixes",
        "elasticache_subnet_names": "elasticacheSubnetNames",
        "elasticache_subnet_private_dns_hostname_type_on_launch": "elasticacheSubnetPrivateDnsHostnameTypeOnLaunch",
        "elasticache_subnets": "elasticacheSubnets",
        "elasticache_subnet_suffix": "elasticacheSubnetSuffix",
        "elasticache_subnet_tags": "elasticacheSubnetTags",
        "enable_dhcp_options": "enableDhcpOptions",
        "enable_dns_hostnames": "enableDnsHostnames",
        "enable_dns_support": "enableDnsSupport",
        "enable_flow_log": "enableFlowLog",
        "enable_ipv6": "enableIpv6",
        "enable_nat_gateway": "enableNatGateway",
        "enable_network_address_usage_metrics": "enableNetworkAddressUsageMetrics",
        "enable_public_redshift": "enablePublicRedshift",
        "enable_vpn_gateway": "enableVpnGateway",
        "external_nat_ip_ids": "externalNatIpIds",
        "external_nat_ips": "externalNatIps",
        "flow_log_cloudwatch_iam_role_arn": "flowLogCloudwatchIamRoleArn",
        "flow_log_cloudwatch_iam_role_conditions": "flowLogCloudwatchIamRoleConditions",
        "flow_log_cloudwatch_log_group_class": "flowLogCloudwatchLogGroupClass",
        "flow_log_cloudwatch_log_group_kms_key_id": "flowLogCloudwatchLogGroupKmsKeyId",
        "flow_log_cloudwatch_log_group_name_prefix": "flowLogCloudwatchLogGroupNamePrefix",
        "flow_log_cloudwatch_log_group_name_suffix": "flowLogCloudwatchLogGroupNameSuffix",
        "flow_log_cloudwatch_log_group_retention_in_days": "flowLogCloudwatchLogGroupRetentionInDays",
        "flow_log_cloudwatch_log_group_skip_destroy": "flowLogCloudwatchLogGroupSkipDestroy",
        "flow_log_deliver_cross_account_role": "flowLogDeliverCrossAccountRole",
        "flow_log_destination_arn": "flowLogDestinationArn",
        "flow_log_destination_type": "flowLogDestinationType",
        "flow_log_file_format": "flowLogFileFormat",
        "flow_log_hive_compatible_partitions": "flowLogHiveCompatiblePartitions",
        "flow_log_log_format": "flowLogLogFormat",
        "flow_log_max_aggregation_interval": "flowLogMaxAggregationInterval",
        "flow_log_per_hour_partition": "flowLogPerHourPartition",
        "flow_log_traffic_type": "flowLogTrafficType",
        "igw_tags": "igwTags",
        "instance_tenancy": "instanceTenancy",
        "intra_acl_tags": "intraAclTags",
        "intra_dedicated_network_acl": "intraDedicatedNetworkAcl",
        "intra_inbound_acl_rules": "intraInboundAclRules",
        "intra_outbound_acl_rules": "intraOutboundAclRules",
        "intra_route_table_tags": "intraRouteTableTags",
        "intra_subnet_assign_ipv6_address_on_creation": "intraSubnetAssignIpv6AddressOnCreation",
        "intra_subnet_enable_dns64": "intraSubnetEnableDns64",
        "intra_subnet_enable_resource_name_dns_aaaa_record_on_launch": "intraSubnetEnableResourceNameDnsAaaaRecordOnLaunch",
        "intra_subnet_enable_resource_name_dns_a_record_on_launch": "intraSubnetEnableResourceNameDnsARecordOnLaunch",
        "intra_subnet_ipv6_native": "intraSubnetIpv6Native",
        "intra_subnet_ipv6_prefixes": "intraSubnetIpv6Prefixes",
        "intra_subnet_names": "intraSubnetNames",
        "intra_subnet_private_dns_hostname_type_on_launch": "intraSubnetPrivateDnsHostnameTypeOnLaunch",
        "intra_subnets": "intraSubnets",
        "intra_subnet_suffix": "intraSubnetSuffix",
        "intra_subnet_tags": "intraSubnetTags",
        "ipv4_ipam_pool_id": "ipv4IpamPoolId",
        "ipv4_netmask_length": "ipv4NetmaskLength",
        "ipv6_cidr": "ipv6Cidr",
        "ipv6_cidr_block_network_border_group": "ipv6CidrBlockNetworkBorderGroup",
        "ipv6_ipam_pool_id": "ipv6IpamPoolId",
        "ipv6_netmask_length": "ipv6NetmaskLength",
        "manage_default_network_acl": "manageDefaultNetworkAcl",
        "manage_default_route_table": "manageDefaultRouteTable",
        "manage_default_security_group": "manageDefaultSecurityGroup",
        "manage_default_vpc": "manageDefaultVpc",
        "map_customer_owned_ip_on_launch": "mapCustomerOwnedIpOnLaunch",
        "map_public_ip_on_launch": "mapPublicIpOnLaunch",
        "name": "name",
        "nat_eip_tags": "natEipTags",
        "nat_gateway_destination_cidr_block": "natGatewayDestinationCidrBlock",
        "nat_gateway_tags": "natGatewayTags",
        "one_nat_gateway_per_az": "oneNatGatewayPerAz",
        "outpost_acl_tags": "outpostAclTags",
        "outpost_arn": "outpostArn",
        "outpost_az": "outpostAz",
        "outpost_dedicated_network_acl": "outpostDedicatedNetworkAcl",
        "outpost_inbound_acl_rules": "outpostInboundAclRules",
        "outpost_outbound_acl_rules": "outpostOutboundAclRules",
        "outpost_subnet_assign_ipv6_address_on_creation": "outpostSubnetAssignIpv6AddressOnCreation",
        "outpost_subnet_enable_dns64": "outpostSubnetEnableDns64",
        "outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch": "outpostSubnetEnableResourceNameDnsAaaaRecordOnLaunch",
        "outpost_subnet_enable_resource_name_dns_a_record_on_launch": "outpostSubnetEnableResourceNameDnsARecordOnLaunch",
        "outpost_subnet_ipv6_native": "outpostSubnetIpv6Native",
        "outpost_subnet_ipv6_prefixes": "outpostSubnetIpv6Prefixes",
        "outpost_subnet_names": "outpostSubnetNames",
        "outpost_subnet_private_dns_hostname_type_on_launch": "outpostSubnetPrivateDnsHostnameTypeOnLaunch",
        "outpost_subnets": "outpostSubnets",
        "outpost_subnet_suffix": "outpostSubnetSuffix",
        "outpost_subnet_tags": "outpostSubnetTags",
        "private_acl_tags": "privateAclTags",
        "private_dedicated_network_acl": "privateDedicatedNetworkAcl",
        "private_inbound_acl_rules": "privateInboundAclRules",
        "private_outbound_acl_rules": "privateOutboundAclRules",
        "private_route_table_tags": "privateRouteTableTags",
        "private_subnet_assign_ipv6_address_on_creation": "privateSubnetAssignIpv6AddressOnCreation",
        "private_subnet_enable_dns64": "privateSubnetEnableDns64",
        "private_subnet_enable_resource_name_dns_aaaa_record_on_launch": "privateSubnetEnableResourceNameDnsAaaaRecordOnLaunch",
        "private_subnet_enable_resource_name_dns_a_record_on_launch": "privateSubnetEnableResourceNameDnsARecordOnLaunch",
        "private_subnet_ipv6_native": "privateSubnetIpv6Native",
        "private_subnet_ipv6_prefixes": "privateSubnetIpv6Prefixes",
        "private_subnet_names": "privateSubnetNames",
        "private_subnet_private_dns_hostname_type_on_launch": "privateSubnetPrivateDnsHostnameTypeOnLaunch",
        "private_subnets": "privateSubnets",
        "private_subnet_suffix": "privateSubnetSuffix",
        "private_subnet_tags": "privateSubnetTags",
        "private_subnet_tags_per_az": "privateSubnetTagsPerAz",
        "propagate_intra_route_tables_vgw": "propagateIntraRouteTablesVgw",
        "propagate_private_route_tables_vgw": "propagatePrivateRouteTablesVgw",
        "propagate_public_route_tables_vgw": "propagatePublicRouteTablesVgw",
        "public_acl_tags": "publicAclTags",
        "public_dedicated_network_acl": "publicDedicatedNetworkAcl",
        "public_inbound_acl_rules": "publicInboundAclRules",
        "public_outbound_acl_rules": "publicOutboundAclRules",
        "public_route_table_tags": "publicRouteTableTags",
        "public_subnet_assign_ipv6_address_on_creation": "publicSubnetAssignIpv6AddressOnCreation",
        "public_subnet_enable_dns64": "publicSubnetEnableDns64",
        "public_subnet_enable_resource_name_dns_aaaa_record_on_launch": "publicSubnetEnableResourceNameDnsAaaaRecordOnLaunch",
        "public_subnet_enable_resource_name_dns_a_record_on_launch": "publicSubnetEnableResourceNameDnsARecordOnLaunch",
        "public_subnet_ipv6_native": "publicSubnetIpv6Native",
        "public_subnet_ipv6_prefixes": "publicSubnetIpv6Prefixes",
        "public_subnet_names": "publicSubnetNames",
        "public_subnet_private_dns_hostname_type_on_launch": "publicSubnetPrivateDnsHostnameTypeOnLaunch",
        "public_subnets": "publicSubnets",
        "public_subnet_suffix": "publicSubnetSuffix",
        "public_subnet_tags": "publicSubnetTags",
        "public_subnet_tags_per_az": "publicSubnetTagsPerAz",
        "putin_khuylo": "putinKhuylo",
        "redshift_acl_tags": "redshiftAclTags",
        "redshift_dedicated_network_acl": "redshiftDedicatedNetworkAcl",
        "redshift_inbound_acl_rules": "redshiftInboundAclRules",
        "redshift_outbound_acl_rules": "redshiftOutboundAclRules",
        "redshift_route_table_tags": "redshiftRouteTableTags",
        "redshift_subnet_assign_ipv6_address_on_creation": "redshiftSubnetAssignIpv6AddressOnCreation",
        "redshift_subnet_enable_dns64": "redshiftSubnetEnableDns64",
        "redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch": "redshiftSubnetEnableResourceNameDnsAaaaRecordOnLaunch",
        "redshift_subnet_enable_resource_name_dns_a_record_on_launch": "redshiftSubnetEnableResourceNameDnsARecordOnLaunch",
        "redshift_subnet_group_name": "redshiftSubnetGroupName",
        "redshift_subnet_group_tags": "redshiftSubnetGroupTags",
        "redshift_subnet_ipv6_native": "redshiftSubnetIpv6Native",
        "redshift_subnet_ipv6_prefixes": "redshiftSubnetIpv6Prefixes",
        "redshift_subnet_names": "redshiftSubnetNames",
        "redshift_subnet_private_dns_hostname_type_on_launch": "redshiftSubnetPrivateDnsHostnameTypeOnLaunch",
        "redshift_subnets": "redshiftSubnets",
        "redshift_subnet_suffix": "redshiftSubnetSuffix",
        "redshift_subnet_tags": "redshiftSubnetTags",
        "reuse_nat_ips": "reuseNatIps",
        "secondary_cidr_blocks": "secondaryCidrBlocks",
        "single_nat_gateway": "singleNatGateway",
        "tags": "tags",
        "use_ipam_pool": "useIpamPool",
        "vpc_flow_log_iam_policy_name": "vpcFlowLogIamPolicyName",
        "vpc_flow_log_iam_policy_use_name_prefix": "vpcFlowLogIamPolicyUseNamePrefix",
        "vpc_flow_log_iam_role_name": "vpcFlowLogIamRoleName",
        "vpc_flow_log_iam_role_use_name_prefix": "vpcFlowLogIamRoleUseNamePrefix",
        "vpc_flow_log_permissions_boundary": "vpcFlowLogPermissionsBoundary",
        "vpc_flow_log_tags": "vpcFlowLogTags",
        "vpc_tags": "vpcTags",
        "vpn_gateway_az": "vpnGatewayAz",
        "vpn_gateway_id": "vpnGatewayId",
        "vpn_gateway_tags": "vpnGatewayTags",
    },
)
class VpcConfig(_cdktf_9a9027ec.TerraformModuleUserConfig):
    def __init__(
        self,
        *,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        providers: typing.Optional[typing.Sequence[typing.Union[_cdktf_9a9027ec.TerraformProvider, typing.Union[_cdktf_9a9027ec.TerraformModuleProvider, typing.Dict[builtins.str, typing.Any]]]]] = None,
        skip_asset_creation_from_local_modules: typing.Optional[builtins.bool] = None,
        amazon_side_asn: typing.Optional[builtins.str] = None,
        azs: typing.Optional[typing.Sequence[builtins.str]] = None,
        cidr: typing.Optional[builtins.str] = None,
        create_database_internet_gateway_route: typing.Optional[builtins.bool] = None,
        create_database_nat_gateway_route: typing.Optional[builtins.bool] = None,
        create_database_subnet_group: typing.Optional[builtins.bool] = None,
        create_database_subnet_route_table: typing.Optional[builtins.bool] = None,
        create_egress_only_igw: typing.Optional[builtins.bool] = None,
        create_elasticache_subnet_group: typing.Optional[builtins.bool] = None,
        create_elasticache_subnet_route_table: typing.Optional[builtins.bool] = None,
        create_flow_log_cloudwatch_iam_role: typing.Optional[builtins.bool] = None,
        create_flow_log_cloudwatch_log_group: typing.Optional[builtins.bool] = None,
        create_igw: typing.Optional[builtins.bool] = None,
        create_multiple_intra_route_tables: typing.Optional[builtins.bool] = None,
        create_multiple_public_route_tables: typing.Optional[builtins.bool] = None,
        create_private_nat_gateway_route: typing.Optional[builtins.bool] = None,
        create_redshift_subnet_group: typing.Optional[builtins.bool] = None,
        create_redshift_subnet_route_table: typing.Optional[builtins.bool] = None,
        create_vpc: typing.Optional[builtins.bool] = None,
        customer_gateways: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]] = None,
        customer_gateway_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        customer_owned_ipv4_pool: typing.Optional[builtins.str] = None,
        database_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        database_dedicated_network_acl: typing.Optional[builtins.bool] = None,
        database_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        database_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        database_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        database_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
        database_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
        database_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
        database_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
        database_subnet_group_name: typing.Optional[builtins.str] = None,
        database_subnet_group_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        database_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
        database_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        database_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        database_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
        database_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        database_subnet_suffix: typing.Optional[builtins.str] = None,
        database_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        default_network_acl_egress: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        default_network_acl_ingress: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        default_network_acl_name: typing.Optional[builtins.str] = None,
        default_network_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        default_route_table_name: typing.Optional[builtins.str] = None,
        default_route_table_propagating_vgws: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_route_table_routes: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        default_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        default_security_group_egress: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        default_security_group_ingress: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        default_security_group_name: typing.Optional[builtins.str] = None,
        default_security_group_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        default_vpc_enable_dns_hostnames: typing.Optional[builtins.bool] = None,
        default_vpc_enable_dns_support: typing.Optional[builtins.bool] = None,
        default_vpc_name: typing.Optional[builtins.str] = None,
        default_vpc_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        dhcp_options_domain_name: typing.Optional[builtins.str] = None,
        dhcp_options_domain_name_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        dhcp_options_ipv6_address_preferred_lease_time: typing.Optional[jsii.Number] = None,
        dhcp_options_netbios_name_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        dhcp_options_netbios_node_type: typing.Optional[builtins.str] = None,
        dhcp_options_ntp_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        dhcp_options_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        elasticache_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        elasticache_dedicated_network_acl: typing.Optional[builtins.bool] = None,
        elasticache_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        elasticache_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        elasticache_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        elasticache_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
        elasticache_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
        elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
        elasticache_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
        elasticache_subnet_group_name: typing.Optional[builtins.str] = None,
        elasticache_subnet_group_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        elasticache_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
        elasticache_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        elasticache_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        elasticache_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
        elasticache_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        elasticache_subnet_suffix: typing.Optional[builtins.str] = None,
        elasticache_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        enable_dhcp_options: typing.Optional[builtins.bool] = None,
        enable_dns_hostnames: typing.Optional[builtins.bool] = None,
        enable_dns_support: typing.Optional[builtins.bool] = None,
        enable_flow_log: typing.Optional[builtins.bool] = None,
        enable_ipv6: typing.Optional[builtins.bool] = None,
        enable_nat_gateway: typing.Optional[builtins.bool] = None,
        enable_network_address_usage_metrics: typing.Optional[builtins.bool] = None,
        enable_public_redshift: typing.Optional[builtins.bool] = None,
        enable_vpn_gateway: typing.Optional[builtins.bool] = None,
        external_nat_ip_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        external_nat_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        flow_log_cloudwatch_iam_role_arn: typing.Optional[builtins.str] = None,
        flow_log_cloudwatch_iam_role_conditions: typing.Any = None,
        flow_log_cloudwatch_log_group_class: typing.Optional[builtins.str] = None,
        flow_log_cloudwatch_log_group_kms_key_id: typing.Optional[builtins.str] = None,
        flow_log_cloudwatch_log_group_name_prefix: typing.Optional[builtins.str] = None,
        flow_log_cloudwatch_log_group_name_suffix: typing.Optional[builtins.str] = None,
        flow_log_cloudwatch_log_group_retention_in_days: typing.Optional[jsii.Number] = None,
        flow_log_cloudwatch_log_group_skip_destroy: typing.Optional[builtins.bool] = None,
        flow_log_deliver_cross_account_role: typing.Optional[builtins.str] = None,
        flow_log_destination_arn: typing.Optional[builtins.str] = None,
        flow_log_destination_type: typing.Optional[builtins.str] = None,
        flow_log_file_format: typing.Optional[builtins.str] = None,
        flow_log_hive_compatible_partitions: typing.Optional[builtins.bool] = None,
        flow_log_log_format: typing.Optional[builtins.str] = None,
        flow_log_max_aggregation_interval: typing.Optional[jsii.Number] = None,
        flow_log_per_hour_partition: typing.Optional[builtins.bool] = None,
        flow_log_traffic_type: typing.Optional[builtins.str] = None,
        igw_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instance_tenancy: typing.Optional[builtins.str] = None,
        intra_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        intra_dedicated_network_acl: typing.Optional[builtins.bool] = None,
        intra_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        intra_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        intra_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        intra_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
        intra_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
        intra_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
        intra_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
        intra_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
        intra_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        intra_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        intra_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
        intra_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        intra_subnet_suffix: typing.Optional[builtins.str] = None,
        intra_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ipv4_ipam_pool_id: typing.Optional[builtins.str] = None,
        ipv4_netmask_length: typing.Optional[jsii.Number] = None,
        ipv6_cidr: typing.Optional[builtins.str] = None,
        ipv6_cidr_block_network_border_group: typing.Optional[builtins.str] = None,
        ipv6_ipam_pool_id: typing.Optional[builtins.str] = None,
        ipv6_netmask_length: typing.Optional[jsii.Number] = None,
        manage_default_network_acl: typing.Optional[builtins.bool] = None,
        manage_default_route_table: typing.Optional[builtins.bool] = None,
        manage_default_security_group: typing.Optional[builtins.bool] = None,
        manage_default_vpc: typing.Optional[builtins.bool] = None,
        map_customer_owned_ip_on_launch: typing.Optional[builtins.bool] = None,
        map_public_ip_on_launch: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
        nat_eip_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        nat_gateway_destination_cidr_block: typing.Optional[builtins.str] = None,
        nat_gateway_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        one_nat_gateway_per_az: typing.Optional[builtins.bool] = None,
        outpost_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        outpost_arn: typing.Optional[builtins.str] = None,
        outpost_az: typing.Optional[builtins.str] = None,
        outpost_dedicated_network_acl: typing.Optional[builtins.bool] = None,
        outpost_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        outpost_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        outpost_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
        outpost_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
        outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
        outpost_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
        outpost_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
        outpost_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        outpost_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        outpost_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
        outpost_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        outpost_subnet_suffix: typing.Optional[builtins.str] = None,
        outpost_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        private_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        private_dedicated_network_acl: typing.Optional[builtins.bool] = None,
        private_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        private_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        private_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        private_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
        private_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
        private_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
        private_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
        private_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
        private_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        private_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        private_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
        private_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        private_subnet_suffix: typing.Optional[builtins.str] = None,
        private_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        private_subnet_tags_per_az: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]] = None,
        propagate_intra_route_tables_vgw: typing.Optional[builtins.bool] = None,
        propagate_private_route_tables_vgw: typing.Optional[builtins.bool] = None,
        propagate_public_route_tables_vgw: typing.Optional[builtins.bool] = None,
        public_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        public_dedicated_network_acl: typing.Optional[builtins.bool] = None,
        public_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        public_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        public_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        public_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
        public_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
        public_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
        public_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
        public_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
        public_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        public_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        public_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
        public_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        public_subnet_suffix: typing.Optional[builtins.str] = None,
        public_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        public_subnet_tags_per_az: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]] = None,
        putin_khuylo: typing.Optional[builtins.bool] = None,
        redshift_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        redshift_dedicated_network_acl: typing.Optional[builtins.bool] = None,
        redshift_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        redshift_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
        redshift_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        redshift_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
        redshift_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
        redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
        redshift_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
        redshift_subnet_group_name: typing.Optional[builtins.str] = None,
        redshift_subnet_group_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        redshift_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
        redshift_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        redshift_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        redshift_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
        redshift_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        redshift_subnet_suffix: typing.Optional[builtins.str] = None,
        redshift_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        reuse_nat_ips: typing.Optional[builtins.bool] = None,
        secondary_cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
        single_nat_gateway: typing.Optional[builtins.bool] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        use_ipam_pool: typing.Optional[builtins.bool] = None,
        vpc_flow_log_iam_policy_name: typing.Optional[builtins.str] = None,
        vpc_flow_log_iam_policy_use_name_prefix: typing.Optional[builtins.bool] = None,
        vpc_flow_log_iam_role_name: typing.Optional[builtins.str] = None,
        vpc_flow_log_iam_role_use_name_prefix: typing.Optional[builtins.bool] = None,
        vpc_flow_log_permissions_boundary: typing.Optional[builtins.str] = None,
        vpc_flow_log_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpc_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        vpn_gateway_az: typing.Optional[builtins.str] = None,
        vpn_gateway_id: typing.Optional[builtins.str] = None,
        vpn_gateway_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param depends_on: 
        :param for_each: 
        :param providers: 
        :param skip_asset_creation_from_local_modules: 
        :param amazon_side_asn: The Autonomous System Number (ASN) for the Amazon side of the gateway. By default the virtual private gateway is created with the current default Amazon ASN 64512
        :param azs: A list of availability zones names or ids in the region.
        :param cidr: (Optional) The IPv4 CIDR block for the VPC. CIDR can be explicitly set or it can be derived from IPAM using ``ipv4_netmask_length`` & ``ipv4_ipam_pool_id`` 10.0.0.0/16
        :param create_database_internet_gateway_route: Controls if an internet gateway route for public database access should be created.
        :param create_database_nat_gateway_route: Controls if a nat gateway route should be created to give internet access to the database subnets.
        :param create_database_subnet_group: Controls if database subnet group should be created (n.b. database_subnets must also be set) true.
        :param create_database_subnet_route_table: Controls if separate route table for database should be created.
        :param create_egress_only_igw: Controls if an Egress Only Internet Gateway is created and its related routes true.
        :param create_elasticache_subnet_group: Controls if elasticache subnet group should be created true.
        :param create_elasticache_subnet_route_table: Controls if separate route table for elasticache should be created.
        :param create_flow_log_cloudwatch_iam_role: Whether to create IAM role for VPC Flow Logs.
        :param create_flow_log_cloudwatch_log_group: Whether to create CloudWatch log group for VPC Flow Logs.
        :param create_igw: Controls if an Internet Gateway is created for public subnets and the related routes that connect them true.
        :param create_multiple_intra_route_tables: Indicates whether to create a separate route table for each intra subnet. Default: ``false``
        :param create_multiple_public_route_tables: Indicates whether to create a separate route table for each public subnet. Default: ``false``
        :param create_private_nat_gateway_route: Controls if a nat gateway route should be created to give internet access to the private subnets true.
        :param create_redshift_subnet_group: Controls if redshift subnet group should be created true.
        :param create_redshift_subnet_route_table: Controls if separate route table for redshift should be created.
        :param create_vpc: Controls if VPC should be created (it affects almost all resources) true.
        :param customer_gateways: Maps of Customer Gateway's attributes (BGP ASN and Gateway's Internet-routable external IP address) The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param customer_gateway_tags: Additional tags for the Customer Gateway The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param customer_owned_ipv4_pool: The customer owned IPv4 address pool. Typically used with the ``map_customer_owned_ip_on_launch`` argument. The ``outpost_arn`` argument must be specified when configured
        :param database_acl_tags: Additional tags for the database subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param database_dedicated_network_acl: Whether to use dedicated network ACL (not default) and custom rules for database subnets.
        :param database_inbound_acl_rules: Database subnets inbound network ACL rules [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param database_outbound_acl_rules: Database subnets outbound network ACL rules [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param database_route_table_tags: Additional tags for the database route tables The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param database_subnet_assign_ipv6_address_on_creation: Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. Default is ``false``
        :param database_subnet_enable_dns64: Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. Default: ``true`` true
        :param database_subnet_enable_resource_name_dns_aaaa_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records. Default: ``true`` true
        :param database_subnet_enable_resource_name_dns_a_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS A records. Default: ``false``
        :param database_subnet_group_name: Name of database subnet group.
        :param database_subnet_group_tags: Additional tags for the database subnet group The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param database_subnet_ipv6_native: Indicates whether to create an IPv6-only subnet. Default: ``false``
        :param database_subnet_ipv6_prefixes: Assigns IPv6 database subnet id based on the Amazon provided /56 prefix base 10 integer (0-256). Must be of equal length to the corresponding IPv4 subnet list
        :param database_subnet_names: Explicit values to use in the Name tag on database subnets. If empty, Name tags are generated
        :param database_subnet_private_dns_hostname_type_on_launch: The type of hostnames to assign to instances in the subnet at launch. For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        :param database_subnets: A list of database subnets inside the VPC.
        :param database_subnet_suffix: Suffix to append to database subnets name db.
        :param database_subnet_tags: Additional tags for the database subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param default_network_acl_egress: List of maps of egress rules to set on the Default Network ACL [object Object] [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param default_network_acl_ingress: List of maps of ingress rules to set on the Default Network ACL [object Object] [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param default_network_acl_name: Name to be used on the Default Network ACL.
        :param default_network_acl_tags: Additional tags for the Default Network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param default_route_table_name: Name to be used on the default route table.
        :param default_route_table_propagating_vgws: List of virtual gateways for propagation.
        :param default_route_table_routes: Configuration block of routes. See https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/default_route_table#route. The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}
        :param default_route_table_tags: Additional tags for the default route table The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param default_security_group_egress: List of maps of egress rules to set on the default security group. The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}
        :param default_security_group_ingress: List of maps of ingress rules to set on the default security group. The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}
        :param default_security_group_name: Name to be used on the default security group.
        :param default_security_group_tags: Additional tags for the default security group The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param default_vpc_enable_dns_hostnames: Should be true to enable DNS hostnames in the Default VPC true.
        :param default_vpc_enable_dns_support: Should be true to enable DNS support in the Default VPC true.
        :param default_vpc_name: Name to be used on the Default VPC.
        :param default_vpc_tags: Additional tags for the Default VPC The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param dhcp_options_domain_name: Specifies DNS name for DHCP options set (requires enable_dhcp_options set to true).
        :param dhcp_options_domain_name_servers: Specify a list of DNS server addresses for DHCP options set, default to AWS provided (requires enable_dhcp_options set to true) AmazonProvidedDNS.
        :param dhcp_options_ipv6_address_preferred_lease_time: How frequently, in seconds, a running instance with an IPv6 assigned to it goes through DHCPv6 lease renewal (requires enable_dhcp_options set to true).
        :param dhcp_options_netbios_name_servers: Specify a list of netbios servers for DHCP options set (requires enable_dhcp_options set to true).
        :param dhcp_options_netbios_node_type: Specify netbios node_type for DHCP options set (requires enable_dhcp_options set to true).
        :param dhcp_options_ntp_servers: Specify a list of NTP servers for DHCP options set (requires enable_dhcp_options set to true).
        :param dhcp_options_tags: Additional tags for the DHCP option set (requires enable_dhcp_options set to true) The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param elasticache_acl_tags: Additional tags for the elasticache subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param elasticache_dedicated_network_acl: Whether to use dedicated network ACL (not default) and custom rules for elasticache subnets.
        :param elasticache_inbound_acl_rules: Elasticache subnets inbound network ACL rules [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param elasticache_outbound_acl_rules: Elasticache subnets outbound network ACL rules [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param elasticache_route_table_tags: Additional tags for the elasticache route tables The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param elasticache_subnet_assign_ipv6_address_on_creation: Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. Default is ``false``
        :param elasticache_subnet_enable_dns64: Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. Default: ``true`` true
        :param elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records. Default: ``true`` true
        :param elasticache_subnet_enable_resource_name_dns_a_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS A records. Default: ``false``
        :param elasticache_subnet_group_name: Name of elasticache subnet group.
        :param elasticache_subnet_group_tags: Additional tags for the elasticache subnet group The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param elasticache_subnet_ipv6_native: Indicates whether to create an IPv6-only subnet. Default: ``false``
        :param elasticache_subnet_ipv6_prefixes: Assigns IPv6 elasticache subnet id based on the Amazon provided /56 prefix base 10 integer (0-256). Must be of equal length to the corresponding IPv4 subnet list
        :param elasticache_subnet_names: Explicit values to use in the Name tag on elasticache subnets. If empty, Name tags are generated
        :param elasticache_subnet_private_dns_hostname_type_on_launch: The type of hostnames to assign to instances in the subnet at launch. For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        :param elasticache_subnets: A list of elasticache subnets inside the VPC.
        :param elasticache_subnet_suffix: Suffix to append to elasticache subnets name elasticache.
        :param elasticache_subnet_tags: Additional tags for the elasticache subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param enable_dhcp_options: Should be true if you want to specify a DHCP options set with a custom domain name, DNS servers, NTP servers, netbios servers, and/or netbios server type.
        :param enable_dns_hostnames: Should be true to enable DNS hostnames in the VPC true.
        :param enable_dns_support: Should be true to enable DNS support in the VPC true.
        :param enable_flow_log: Whether or not to enable VPC Flow Logs.
        :param enable_ipv6: Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or the size of the CIDR block
        :param enable_nat_gateway: Should be true if you want to provision NAT Gateways for each of your private networks.
        :param enable_network_address_usage_metrics: Determines whether network address usage metrics are enabled for the VPC.
        :param enable_public_redshift: Controls if redshift should have public routing table.
        :param enable_vpn_gateway: Should be true if you want to create a new VPN Gateway resource and attach it to the VPC.
        :param external_nat_ip_ids: List of EIP IDs to be assigned to the NAT Gateways (used in combination with reuse_nat_ips).
        :param external_nat_ips: List of EIPs to be used for ``nat_public_ips`` output (used in combination with reuse_nat_ips and external_nat_ip_ids).
        :param flow_log_cloudwatch_iam_role_arn: The ARN for the IAM role that's used to post flow logs to a CloudWatch Logs log group. When flow_log_destination_arn is set to ARN of Cloudwatch Logs, this argument needs to be provided
        :param flow_log_cloudwatch_iam_role_conditions: Additional conditions of the CloudWatch role assumption policy.
        :param flow_log_cloudwatch_log_group_class: Specified the log class of the log group. Possible values are: STANDARD or INFREQUENT_ACCESS
        :param flow_log_cloudwatch_log_group_kms_key_id: The ARN of the KMS Key to use when encrypting log data for VPC flow logs.
        :param flow_log_cloudwatch_log_group_name_prefix: Specifies the name prefix of CloudWatch Log Group for VPC flow logs /aws/vpc-flow-log/.
        :param flow_log_cloudwatch_log_group_name_suffix: Specifies the name suffix of CloudWatch Log Group for VPC flow logs.
        :param flow_log_cloudwatch_log_group_retention_in_days: Specifies the number of days you want to retain log events in the specified log group for VPC flow logs.
        :param flow_log_cloudwatch_log_group_skip_destroy: Set to true if you do not wish the log group (and any logs it may contain) to be deleted at destroy time, and instead just remove the log group from the Terraform state.
        :param flow_log_deliver_cross_account_role: (Optional) ARN of the IAM role that allows Amazon EC2 to publish flow logs across accounts.
        :param flow_log_destination_arn: The ARN of the CloudWatch log group or S3 bucket where VPC Flow Logs will be pushed. If this ARN is a S3 bucket the appropriate permissions need to be set on that bucket's policy. When create_flow_log_cloudwatch_log_group is set to false this argument must be provided
        :param flow_log_destination_type: Type of flow log destination. Can be s3, kinesis-data-firehose or cloud-watch-logs cloud-watch-logs
        :param flow_log_file_format: (Optional) The format for the flow log. Valid values: ``plain-text``, ``parquet``
        :param flow_log_hive_compatible_partitions: (Optional) Indicates whether to use Hive-compatible prefixes for flow logs stored in Amazon S3.
        :param flow_log_log_format: The fields to include in the flow log record, in the order in which they should appear.
        :param flow_log_max_aggregation_interval: The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. Valid Values: ``60`` seconds or ``600`` seconds 600
        :param flow_log_per_hour_partition: (Optional) Indicates whether to partition the flow log per hour. This reduces the cost and response time for queries
        :param flow_log_traffic_type: The type of traffic to capture. Valid values: ACCEPT, REJECT, ALL ALL
        :param igw_tags: Additional tags for the internet gateway The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param instance_tenancy: A tenancy option for instances launched into the VPC default.
        :param intra_acl_tags: Additional tags for the intra subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param intra_dedicated_network_acl: Whether to use dedicated network ACL (not default) and custom rules for intra subnets.
        :param intra_inbound_acl_rules: Intra subnets inbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param intra_outbound_acl_rules: Intra subnets outbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param intra_route_table_tags: Additional tags for the intra route tables The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param intra_subnet_assign_ipv6_address_on_creation: Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. Default is ``false``
        :param intra_subnet_enable_dns64: Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. Default: ``true`` true
        :param intra_subnet_enable_resource_name_dns_aaaa_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records. Default: ``true`` true
        :param intra_subnet_enable_resource_name_dns_a_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS A records. Default: ``false``
        :param intra_subnet_ipv6_native: Indicates whether to create an IPv6-only subnet. Default: ``false``
        :param intra_subnet_ipv6_prefixes: Assigns IPv6 intra subnet id based on the Amazon provided /56 prefix base 10 integer (0-256). Must be of equal length to the corresponding IPv4 subnet list
        :param intra_subnet_names: Explicit values to use in the Name tag on intra subnets. If empty, Name tags are generated
        :param intra_subnet_private_dns_hostname_type_on_launch: The type of hostnames to assign to instances in the subnet at launch. For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        :param intra_subnets: A list of intra subnets inside the VPC.
        :param intra_subnet_suffix: Suffix to append to intra subnets name intra.
        :param intra_subnet_tags: Additional tags for the intra subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param ipv4_ipam_pool_id: (Optional) The ID of an IPv4 IPAM pool you want to use for allocating this VPC's CIDR.
        :param ipv4_netmask_length: (Optional) The netmask length of the IPv4 CIDR you want to allocate to this VPC. Requires specifying a ipv4_ipam_pool_id
        :param ipv6_cidr: (Optional) IPv6 CIDR block to request from an IPAM Pool. Can be set explicitly or derived from IPAM using ``ipv6_netmask_length``
        :param ipv6_cidr_block_network_border_group: By default when an IPv6 CIDR is assigned to a VPC a default ipv6_cidr_block_network_border_group will be set to the region of the VPC. This can be changed to restrict advertisement of public addresses to specific Network Border Groups such as LocalZones
        :param ipv6_ipam_pool_id: (Optional) IPAM Pool ID for a IPv6 pool. Conflicts with ``assign_generated_ipv6_cidr_block``
        :param ipv6_netmask_length: (Optional) Netmask length to request from IPAM Pool. Conflicts with ``ipv6_cidr_block``. This can be omitted if IPAM pool as a ``allocation_default_netmask_length`` set. Valid values: ``56``
        :param manage_default_network_acl: Should be true to adopt and manage Default Network ACL true.
        :param manage_default_route_table: Should be true to manage default route table true.
        :param manage_default_security_group: Should be true to adopt and manage default security group true.
        :param manage_default_vpc: Should be true to adopt and manage Default VPC.
        :param map_customer_owned_ip_on_launch: Specify true to indicate that network interfaces created in the subnet should be assigned a customer owned IP address. The ``customer_owned_ipv4_pool`` and ``outpost_arn`` arguments must be specified when set to ``true``. Default is ``false``
        :param map_public_ip_on_launch: Specify true to indicate that instances launched into the subnet should be assigned a public IP address. Default is ``false``
        :param name: Name to be used on all the resources as identifier.
        :param nat_eip_tags: Additional tags for the NAT EIP The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param nat_gateway_destination_cidr_block: Used to pass a custom destination route for private NAT Gateway. If not specified, the default 0.0.0.0/0 is used as a destination route 0.0.0.0/0
        :param nat_gateway_tags: Additional tags for the NAT gateways The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param one_nat_gateway_per_az: Should be true if you want only one NAT Gateway per availability zone. Requires ``var.azs`` to be set, and the number of ``public_subnets`` created to be greater than or equal to the number of availability zones specified in ``var.azs``
        :param outpost_acl_tags: Additional tags for the outpost subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param outpost_arn: ARN of Outpost you want to create a subnet in.
        :param outpost_az: AZ where Outpost is anchored.
        :param outpost_dedicated_network_acl: Whether to use dedicated network ACL (not default) and custom rules for outpost subnets.
        :param outpost_inbound_acl_rules: Outpost subnets inbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param outpost_outbound_acl_rules: Outpost subnets outbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param outpost_subnet_assign_ipv6_address_on_creation: Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. Default is ``false``
        :param outpost_subnet_enable_dns64: Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. Default: ``true`` true
        :param outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records. Default: ``true`` true
        :param outpost_subnet_enable_resource_name_dns_a_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS A records. Default: ``false``
        :param outpost_subnet_ipv6_native: Indicates whether to create an IPv6-only subnet. Default: ``false``
        :param outpost_subnet_ipv6_prefixes: Assigns IPv6 outpost subnet id based on the Amazon provided /56 prefix base 10 integer (0-256). Must be of equal length to the corresponding IPv4 subnet list
        :param outpost_subnet_names: Explicit values to use in the Name tag on outpost subnets. If empty, Name tags are generated
        :param outpost_subnet_private_dns_hostname_type_on_launch: The type of hostnames to assign to instances in the subnet at launch. For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        :param outpost_subnets: A list of outpost subnets inside the VPC.
        :param outpost_subnet_suffix: Suffix to append to outpost subnets name outpost.
        :param outpost_subnet_tags: Additional tags for the outpost subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param private_acl_tags: Additional tags for the private subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param private_dedicated_network_acl: Whether to use dedicated network ACL (not default) and custom rules for private subnets.
        :param private_inbound_acl_rules: Private subnets inbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param private_outbound_acl_rules: Private subnets outbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param private_route_table_tags: Additional tags for the private route tables The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param private_subnet_assign_ipv6_address_on_creation: Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. Default is ``false``
        :param private_subnet_enable_dns64: Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. Default: ``true`` true
        :param private_subnet_enable_resource_name_dns_aaaa_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records. Default: ``true`` true
        :param private_subnet_enable_resource_name_dns_a_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS A records. Default: ``false``
        :param private_subnet_ipv6_native: Indicates whether to create an IPv6-only subnet. Default: ``false``
        :param private_subnet_ipv6_prefixes: Assigns IPv6 private subnet id based on the Amazon provided /56 prefix base 10 integer (0-256). Must be of equal length to the corresponding IPv4 subnet list
        :param private_subnet_names: Explicit values to use in the Name tag on private subnets. If empty, Name tags are generated
        :param private_subnet_private_dns_hostname_type_on_launch: The type of hostnames to assign to instances in the subnet at launch. For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        :param private_subnets: A list of private subnets inside the VPC.
        :param private_subnet_suffix: Suffix to append to private subnets name private.
        :param private_subnet_tags: Additional tags for the private subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param private_subnet_tags_per_az: Additional tags for the private subnets where the primary key is the AZ The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param propagate_intra_route_tables_vgw: Should be true if you want route table propagation.
        :param propagate_private_route_tables_vgw: Should be true if you want route table propagation.
        :param propagate_public_route_tables_vgw: Should be true if you want route table propagation.
        :param public_acl_tags: Additional tags for the public subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param public_dedicated_network_acl: Whether to use dedicated network ACL (not default) and custom rules for public subnets.
        :param public_inbound_acl_rules: Public subnets inbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param public_outbound_acl_rules: Public subnets outbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param public_route_table_tags: Additional tags for the public route tables The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param public_subnet_assign_ipv6_address_on_creation: Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. Default is ``false``
        :param public_subnet_enable_dns64: Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. Default: ``true`` true
        :param public_subnet_enable_resource_name_dns_aaaa_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records. Default: ``true`` true
        :param public_subnet_enable_resource_name_dns_a_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS A records. Default: ``false``
        :param public_subnet_ipv6_native: Indicates whether to create an IPv6-only subnet. Default: ``false``
        :param public_subnet_ipv6_prefixes: Assigns IPv6 public subnet id based on the Amazon provided /56 prefix base 10 integer (0-256). Must be of equal length to the corresponding IPv4 subnet list
        :param public_subnet_names: Explicit values to use in the Name tag on public subnets. If empty, Name tags are generated
        :param public_subnet_private_dns_hostname_type_on_launch: The type of hostnames to assign to instances in the subnet at launch. For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        :param public_subnets: A list of public subnets inside the VPC.
        :param public_subnet_suffix: Suffix to append to public subnets name public.
        :param public_subnet_tags: Additional tags for the public subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param public_subnet_tags_per_az: Additional tags for the public subnets where the primary key is the AZ The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param putin_khuylo: Do you agree that Putin doesn't respect Ukrainian sovereignty and territorial integrity? More info: https://en.wikipedia.org/wiki/Putin_khuylo! true
        :param redshift_acl_tags: Additional tags for the redshift subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param redshift_dedicated_network_acl: Whether to use dedicated network ACL (not default) and custom rules for redshift subnets.
        :param redshift_inbound_acl_rules: Redshift subnets inbound network ACL rules [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param redshift_outbound_acl_rules: Redshift subnets outbound network ACL rules [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param redshift_route_table_tags: Additional tags for the redshift route tables The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param redshift_subnet_assign_ipv6_address_on_creation: Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. Default is ``false``
        :param redshift_subnet_enable_dns64: Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. Default: ``true`` true
        :param redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records. Default: ``true`` true
        :param redshift_subnet_enable_resource_name_dns_a_record_on_launch: Indicates whether to respond to DNS queries for instance hostnames with DNS A records. Default: ``false``
        :param redshift_subnet_group_name: Name of redshift subnet group.
        :param redshift_subnet_group_tags: Additional tags for the redshift subnet group The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param redshift_subnet_ipv6_native: Indicates whether to create an IPv6-only subnet. Default: ``false``
        :param redshift_subnet_ipv6_prefixes: Assigns IPv6 redshift subnet id based on the Amazon provided /56 prefix base 10 integer (0-256). Must be of equal length to the corresponding IPv4 subnet list
        :param redshift_subnet_names: Explicit values to use in the Name tag on redshift subnets. If empty, Name tags are generated
        :param redshift_subnet_private_dns_hostname_type_on_launch: The type of hostnames to assign to instances in the subnet at launch. For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        :param redshift_subnets: A list of redshift subnets inside the VPC.
        :param redshift_subnet_suffix: Suffix to append to redshift subnets name redshift.
        :param redshift_subnet_tags: Additional tags for the redshift subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param reuse_nat_ips: Should be true if you don't want EIPs to be created for your NAT Gateways and will instead pass them in via the 'external_nat_ip_ids' variable.
        :param secondary_cidr_blocks: List of secondary CIDR blocks to associate with the VPC to extend the IP Address pool.
        :param single_nat_gateway: Should be true if you want to provision a single shared NAT Gateway across all of your private networks.
        :param tags: A map of tags to add to all resources The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param use_ipam_pool: Determines whether IPAM pool is used for CIDR allocation.
        :param vpc_flow_log_iam_policy_name: Name of the IAM policy vpc-flow-log-to-cloudwatch.
        :param vpc_flow_log_iam_policy_use_name_prefix: Determines whether the name of the IAM policy (``vpc_flow_log_iam_policy_name``) is used as a prefix true.
        :param vpc_flow_log_iam_role_name: Name to use on the VPC Flow Log IAM role created vpc-flow-log-role.
        :param vpc_flow_log_iam_role_use_name_prefix: Determines whether the IAM role name (``vpc_flow_log_iam_role_name_name``) is used as a prefix true.
        :param vpc_flow_log_permissions_boundary: The ARN of the Permissions Boundary for the VPC Flow Log IAM Role.
        :param vpc_flow_log_tags: Additional tags for the VPC Flow Logs The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param vpc_tags: Additional tags for the VPC The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        :param vpn_gateway_az: The Availability Zone for the VPN Gateway.
        :param vpn_gateway_id: ID of VPN Gateway to attach to the VPC.
        :param vpn_gateway_tags: Additional tags for the VPN gateway The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c53c03bd250cea36159fea33bf7c86f44d606c1ab37fd7d410cc66ed192cf385)
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument providers", value=providers, expected_type=type_hints["providers"])
            check_type(argname="argument skip_asset_creation_from_local_modules", value=skip_asset_creation_from_local_modules, expected_type=type_hints["skip_asset_creation_from_local_modules"])
            check_type(argname="argument amazon_side_asn", value=amazon_side_asn, expected_type=type_hints["amazon_side_asn"])
            check_type(argname="argument azs", value=azs, expected_type=type_hints["azs"])
            check_type(argname="argument cidr", value=cidr, expected_type=type_hints["cidr"])
            check_type(argname="argument create_database_internet_gateway_route", value=create_database_internet_gateway_route, expected_type=type_hints["create_database_internet_gateway_route"])
            check_type(argname="argument create_database_nat_gateway_route", value=create_database_nat_gateway_route, expected_type=type_hints["create_database_nat_gateway_route"])
            check_type(argname="argument create_database_subnet_group", value=create_database_subnet_group, expected_type=type_hints["create_database_subnet_group"])
            check_type(argname="argument create_database_subnet_route_table", value=create_database_subnet_route_table, expected_type=type_hints["create_database_subnet_route_table"])
            check_type(argname="argument create_egress_only_igw", value=create_egress_only_igw, expected_type=type_hints["create_egress_only_igw"])
            check_type(argname="argument create_elasticache_subnet_group", value=create_elasticache_subnet_group, expected_type=type_hints["create_elasticache_subnet_group"])
            check_type(argname="argument create_elasticache_subnet_route_table", value=create_elasticache_subnet_route_table, expected_type=type_hints["create_elasticache_subnet_route_table"])
            check_type(argname="argument create_flow_log_cloudwatch_iam_role", value=create_flow_log_cloudwatch_iam_role, expected_type=type_hints["create_flow_log_cloudwatch_iam_role"])
            check_type(argname="argument create_flow_log_cloudwatch_log_group", value=create_flow_log_cloudwatch_log_group, expected_type=type_hints["create_flow_log_cloudwatch_log_group"])
            check_type(argname="argument create_igw", value=create_igw, expected_type=type_hints["create_igw"])
            check_type(argname="argument create_multiple_intra_route_tables", value=create_multiple_intra_route_tables, expected_type=type_hints["create_multiple_intra_route_tables"])
            check_type(argname="argument create_multiple_public_route_tables", value=create_multiple_public_route_tables, expected_type=type_hints["create_multiple_public_route_tables"])
            check_type(argname="argument create_private_nat_gateway_route", value=create_private_nat_gateway_route, expected_type=type_hints["create_private_nat_gateway_route"])
            check_type(argname="argument create_redshift_subnet_group", value=create_redshift_subnet_group, expected_type=type_hints["create_redshift_subnet_group"])
            check_type(argname="argument create_redshift_subnet_route_table", value=create_redshift_subnet_route_table, expected_type=type_hints["create_redshift_subnet_route_table"])
            check_type(argname="argument create_vpc", value=create_vpc, expected_type=type_hints["create_vpc"])
            check_type(argname="argument customer_gateways", value=customer_gateways, expected_type=type_hints["customer_gateways"])
            check_type(argname="argument customer_gateway_tags", value=customer_gateway_tags, expected_type=type_hints["customer_gateway_tags"])
            check_type(argname="argument customer_owned_ipv4_pool", value=customer_owned_ipv4_pool, expected_type=type_hints["customer_owned_ipv4_pool"])
            check_type(argname="argument database_acl_tags", value=database_acl_tags, expected_type=type_hints["database_acl_tags"])
            check_type(argname="argument database_dedicated_network_acl", value=database_dedicated_network_acl, expected_type=type_hints["database_dedicated_network_acl"])
            check_type(argname="argument database_inbound_acl_rules", value=database_inbound_acl_rules, expected_type=type_hints["database_inbound_acl_rules"])
            check_type(argname="argument database_outbound_acl_rules", value=database_outbound_acl_rules, expected_type=type_hints["database_outbound_acl_rules"])
            check_type(argname="argument database_route_table_tags", value=database_route_table_tags, expected_type=type_hints["database_route_table_tags"])
            check_type(argname="argument database_subnet_assign_ipv6_address_on_creation", value=database_subnet_assign_ipv6_address_on_creation, expected_type=type_hints["database_subnet_assign_ipv6_address_on_creation"])
            check_type(argname="argument database_subnet_enable_dns64", value=database_subnet_enable_dns64, expected_type=type_hints["database_subnet_enable_dns64"])
            check_type(argname="argument database_subnet_enable_resource_name_dns_aaaa_record_on_launch", value=database_subnet_enable_resource_name_dns_aaaa_record_on_launch, expected_type=type_hints["database_subnet_enable_resource_name_dns_aaaa_record_on_launch"])
            check_type(argname="argument database_subnet_enable_resource_name_dns_a_record_on_launch", value=database_subnet_enable_resource_name_dns_a_record_on_launch, expected_type=type_hints["database_subnet_enable_resource_name_dns_a_record_on_launch"])
            check_type(argname="argument database_subnet_group_name", value=database_subnet_group_name, expected_type=type_hints["database_subnet_group_name"])
            check_type(argname="argument database_subnet_group_tags", value=database_subnet_group_tags, expected_type=type_hints["database_subnet_group_tags"])
            check_type(argname="argument database_subnet_ipv6_native", value=database_subnet_ipv6_native, expected_type=type_hints["database_subnet_ipv6_native"])
            check_type(argname="argument database_subnet_ipv6_prefixes", value=database_subnet_ipv6_prefixes, expected_type=type_hints["database_subnet_ipv6_prefixes"])
            check_type(argname="argument database_subnet_names", value=database_subnet_names, expected_type=type_hints["database_subnet_names"])
            check_type(argname="argument database_subnet_private_dns_hostname_type_on_launch", value=database_subnet_private_dns_hostname_type_on_launch, expected_type=type_hints["database_subnet_private_dns_hostname_type_on_launch"])
            check_type(argname="argument database_subnets", value=database_subnets, expected_type=type_hints["database_subnets"])
            check_type(argname="argument database_subnet_suffix", value=database_subnet_suffix, expected_type=type_hints["database_subnet_suffix"])
            check_type(argname="argument database_subnet_tags", value=database_subnet_tags, expected_type=type_hints["database_subnet_tags"])
            check_type(argname="argument default_network_acl_egress", value=default_network_acl_egress, expected_type=type_hints["default_network_acl_egress"])
            check_type(argname="argument default_network_acl_ingress", value=default_network_acl_ingress, expected_type=type_hints["default_network_acl_ingress"])
            check_type(argname="argument default_network_acl_name", value=default_network_acl_name, expected_type=type_hints["default_network_acl_name"])
            check_type(argname="argument default_network_acl_tags", value=default_network_acl_tags, expected_type=type_hints["default_network_acl_tags"])
            check_type(argname="argument default_route_table_name", value=default_route_table_name, expected_type=type_hints["default_route_table_name"])
            check_type(argname="argument default_route_table_propagating_vgws", value=default_route_table_propagating_vgws, expected_type=type_hints["default_route_table_propagating_vgws"])
            check_type(argname="argument default_route_table_routes", value=default_route_table_routes, expected_type=type_hints["default_route_table_routes"])
            check_type(argname="argument default_route_table_tags", value=default_route_table_tags, expected_type=type_hints["default_route_table_tags"])
            check_type(argname="argument default_security_group_egress", value=default_security_group_egress, expected_type=type_hints["default_security_group_egress"])
            check_type(argname="argument default_security_group_ingress", value=default_security_group_ingress, expected_type=type_hints["default_security_group_ingress"])
            check_type(argname="argument default_security_group_name", value=default_security_group_name, expected_type=type_hints["default_security_group_name"])
            check_type(argname="argument default_security_group_tags", value=default_security_group_tags, expected_type=type_hints["default_security_group_tags"])
            check_type(argname="argument default_vpc_enable_dns_hostnames", value=default_vpc_enable_dns_hostnames, expected_type=type_hints["default_vpc_enable_dns_hostnames"])
            check_type(argname="argument default_vpc_enable_dns_support", value=default_vpc_enable_dns_support, expected_type=type_hints["default_vpc_enable_dns_support"])
            check_type(argname="argument default_vpc_name", value=default_vpc_name, expected_type=type_hints["default_vpc_name"])
            check_type(argname="argument default_vpc_tags", value=default_vpc_tags, expected_type=type_hints["default_vpc_tags"])
            check_type(argname="argument dhcp_options_domain_name", value=dhcp_options_domain_name, expected_type=type_hints["dhcp_options_domain_name"])
            check_type(argname="argument dhcp_options_domain_name_servers", value=dhcp_options_domain_name_servers, expected_type=type_hints["dhcp_options_domain_name_servers"])
            check_type(argname="argument dhcp_options_ipv6_address_preferred_lease_time", value=dhcp_options_ipv6_address_preferred_lease_time, expected_type=type_hints["dhcp_options_ipv6_address_preferred_lease_time"])
            check_type(argname="argument dhcp_options_netbios_name_servers", value=dhcp_options_netbios_name_servers, expected_type=type_hints["dhcp_options_netbios_name_servers"])
            check_type(argname="argument dhcp_options_netbios_node_type", value=dhcp_options_netbios_node_type, expected_type=type_hints["dhcp_options_netbios_node_type"])
            check_type(argname="argument dhcp_options_ntp_servers", value=dhcp_options_ntp_servers, expected_type=type_hints["dhcp_options_ntp_servers"])
            check_type(argname="argument dhcp_options_tags", value=dhcp_options_tags, expected_type=type_hints["dhcp_options_tags"])
            check_type(argname="argument elasticache_acl_tags", value=elasticache_acl_tags, expected_type=type_hints["elasticache_acl_tags"])
            check_type(argname="argument elasticache_dedicated_network_acl", value=elasticache_dedicated_network_acl, expected_type=type_hints["elasticache_dedicated_network_acl"])
            check_type(argname="argument elasticache_inbound_acl_rules", value=elasticache_inbound_acl_rules, expected_type=type_hints["elasticache_inbound_acl_rules"])
            check_type(argname="argument elasticache_outbound_acl_rules", value=elasticache_outbound_acl_rules, expected_type=type_hints["elasticache_outbound_acl_rules"])
            check_type(argname="argument elasticache_route_table_tags", value=elasticache_route_table_tags, expected_type=type_hints["elasticache_route_table_tags"])
            check_type(argname="argument elasticache_subnet_assign_ipv6_address_on_creation", value=elasticache_subnet_assign_ipv6_address_on_creation, expected_type=type_hints["elasticache_subnet_assign_ipv6_address_on_creation"])
            check_type(argname="argument elasticache_subnet_enable_dns64", value=elasticache_subnet_enable_dns64, expected_type=type_hints["elasticache_subnet_enable_dns64"])
            check_type(argname="argument elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch", value=elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch, expected_type=type_hints["elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch"])
            check_type(argname="argument elasticache_subnet_enable_resource_name_dns_a_record_on_launch", value=elasticache_subnet_enable_resource_name_dns_a_record_on_launch, expected_type=type_hints["elasticache_subnet_enable_resource_name_dns_a_record_on_launch"])
            check_type(argname="argument elasticache_subnet_group_name", value=elasticache_subnet_group_name, expected_type=type_hints["elasticache_subnet_group_name"])
            check_type(argname="argument elasticache_subnet_group_tags", value=elasticache_subnet_group_tags, expected_type=type_hints["elasticache_subnet_group_tags"])
            check_type(argname="argument elasticache_subnet_ipv6_native", value=elasticache_subnet_ipv6_native, expected_type=type_hints["elasticache_subnet_ipv6_native"])
            check_type(argname="argument elasticache_subnet_ipv6_prefixes", value=elasticache_subnet_ipv6_prefixes, expected_type=type_hints["elasticache_subnet_ipv6_prefixes"])
            check_type(argname="argument elasticache_subnet_names", value=elasticache_subnet_names, expected_type=type_hints["elasticache_subnet_names"])
            check_type(argname="argument elasticache_subnet_private_dns_hostname_type_on_launch", value=elasticache_subnet_private_dns_hostname_type_on_launch, expected_type=type_hints["elasticache_subnet_private_dns_hostname_type_on_launch"])
            check_type(argname="argument elasticache_subnets", value=elasticache_subnets, expected_type=type_hints["elasticache_subnets"])
            check_type(argname="argument elasticache_subnet_suffix", value=elasticache_subnet_suffix, expected_type=type_hints["elasticache_subnet_suffix"])
            check_type(argname="argument elasticache_subnet_tags", value=elasticache_subnet_tags, expected_type=type_hints["elasticache_subnet_tags"])
            check_type(argname="argument enable_dhcp_options", value=enable_dhcp_options, expected_type=type_hints["enable_dhcp_options"])
            check_type(argname="argument enable_dns_hostnames", value=enable_dns_hostnames, expected_type=type_hints["enable_dns_hostnames"])
            check_type(argname="argument enable_dns_support", value=enable_dns_support, expected_type=type_hints["enable_dns_support"])
            check_type(argname="argument enable_flow_log", value=enable_flow_log, expected_type=type_hints["enable_flow_log"])
            check_type(argname="argument enable_ipv6", value=enable_ipv6, expected_type=type_hints["enable_ipv6"])
            check_type(argname="argument enable_nat_gateway", value=enable_nat_gateway, expected_type=type_hints["enable_nat_gateway"])
            check_type(argname="argument enable_network_address_usage_metrics", value=enable_network_address_usage_metrics, expected_type=type_hints["enable_network_address_usage_metrics"])
            check_type(argname="argument enable_public_redshift", value=enable_public_redshift, expected_type=type_hints["enable_public_redshift"])
            check_type(argname="argument enable_vpn_gateway", value=enable_vpn_gateway, expected_type=type_hints["enable_vpn_gateway"])
            check_type(argname="argument external_nat_ip_ids", value=external_nat_ip_ids, expected_type=type_hints["external_nat_ip_ids"])
            check_type(argname="argument external_nat_ips", value=external_nat_ips, expected_type=type_hints["external_nat_ips"])
            check_type(argname="argument flow_log_cloudwatch_iam_role_arn", value=flow_log_cloudwatch_iam_role_arn, expected_type=type_hints["flow_log_cloudwatch_iam_role_arn"])
            check_type(argname="argument flow_log_cloudwatch_iam_role_conditions", value=flow_log_cloudwatch_iam_role_conditions, expected_type=type_hints["flow_log_cloudwatch_iam_role_conditions"])
            check_type(argname="argument flow_log_cloudwatch_log_group_class", value=flow_log_cloudwatch_log_group_class, expected_type=type_hints["flow_log_cloudwatch_log_group_class"])
            check_type(argname="argument flow_log_cloudwatch_log_group_kms_key_id", value=flow_log_cloudwatch_log_group_kms_key_id, expected_type=type_hints["flow_log_cloudwatch_log_group_kms_key_id"])
            check_type(argname="argument flow_log_cloudwatch_log_group_name_prefix", value=flow_log_cloudwatch_log_group_name_prefix, expected_type=type_hints["flow_log_cloudwatch_log_group_name_prefix"])
            check_type(argname="argument flow_log_cloudwatch_log_group_name_suffix", value=flow_log_cloudwatch_log_group_name_suffix, expected_type=type_hints["flow_log_cloudwatch_log_group_name_suffix"])
            check_type(argname="argument flow_log_cloudwatch_log_group_retention_in_days", value=flow_log_cloudwatch_log_group_retention_in_days, expected_type=type_hints["flow_log_cloudwatch_log_group_retention_in_days"])
            check_type(argname="argument flow_log_cloudwatch_log_group_skip_destroy", value=flow_log_cloudwatch_log_group_skip_destroy, expected_type=type_hints["flow_log_cloudwatch_log_group_skip_destroy"])
            check_type(argname="argument flow_log_deliver_cross_account_role", value=flow_log_deliver_cross_account_role, expected_type=type_hints["flow_log_deliver_cross_account_role"])
            check_type(argname="argument flow_log_destination_arn", value=flow_log_destination_arn, expected_type=type_hints["flow_log_destination_arn"])
            check_type(argname="argument flow_log_destination_type", value=flow_log_destination_type, expected_type=type_hints["flow_log_destination_type"])
            check_type(argname="argument flow_log_file_format", value=flow_log_file_format, expected_type=type_hints["flow_log_file_format"])
            check_type(argname="argument flow_log_hive_compatible_partitions", value=flow_log_hive_compatible_partitions, expected_type=type_hints["flow_log_hive_compatible_partitions"])
            check_type(argname="argument flow_log_log_format", value=flow_log_log_format, expected_type=type_hints["flow_log_log_format"])
            check_type(argname="argument flow_log_max_aggregation_interval", value=flow_log_max_aggregation_interval, expected_type=type_hints["flow_log_max_aggregation_interval"])
            check_type(argname="argument flow_log_per_hour_partition", value=flow_log_per_hour_partition, expected_type=type_hints["flow_log_per_hour_partition"])
            check_type(argname="argument flow_log_traffic_type", value=flow_log_traffic_type, expected_type=type_hints["flow_log_traffic_type"])
            check_type(argname="argument igw_tags", value=igw_tags, expected_type=type_hints["igw_tags"])
            check_type(argname="argument instance_tenancy", value=instance_tenancy, expected_type=type_hints["instance_tenancy"])
            check_type(argname="argument intra_acl_tags", value=intra_acl_tags, expected_type=type_hints["intra_acl_tags"])
            check_type(argname="argument intra_dedicated_network_acl", value=intra_dedicated_network_acl, expected_type=type_hints["intra_dedicated_network_acl"])
            check_type(argname="argument intra_inbound_acl_rules", value=intra_inbound_acl_rules, expected_type=type_hints["intra_inbound_acl_rules"])
            check_type(argname="argument intra_outbound_acl_rules", value=intra_outbound_acl_rules, expected_type=type_hints["intra_outbound_acl_rules"])
            check_type(argname="argument intra_route_table_tags", value=intra_route_table_tags, expected_type=type_hints["intra_route_table_tags"])
            check_type(argname="argument intra_subnet_assign_ipv6_address_on_creation", value=intra_subnet_assign_ipv6_address_on_creation, expected_type=type_hints["intra_subnet_assign_ipv6_address_on_creation"])
            check_type(argname="argument intra_subnet_enable_dns64", value=intra_subnet_enable_dns64, expected_type=type_hints["intra_subnet_enable_dns64"])
            check_type(argname="argument intra_subnet_enable_resource_name_dns_aaaa_record_on_launch", value=intra_subnet_enable_resource_name_dns_aaaa_record_on_launch, expected_type=type_hints["intra_subnet_enable_resource_name_dns_aaaa_record_on_launch"])
            check_type(argname="argument intra_subnet_enable_resource_name_dns_a_record_on_launch", value=intra_subnet_enable_resource_name_dns_a_record_on_launch, expected_type=type_hints["intra_subnet_enable_resource_name_dns_a_record_on_launch"])
            check_type(argname="argument intra_subnet_ipv6_native", value=intra_subnet_ipv6_native, expected_type=type_hints["intra_subnet_ipv6_native"])
            check_type(argname="argument intra_subnet_ipv6_prefixes", value=intra_subnet_ipv6_prefixes, expected_type=type_hints["intra_subnet_ipv6_prefixes"])
            check_type(argname="argument intra_subnet_names", value=intra_subnet_names, expected_type=type_hints["intra_subnet_names"])
            check_type(argname="argument intra_subnet_private_dns_hostname_type_on_launch", value=intra_subnet_private_dns_hostname_type_on_launch, expected_type=type_hints["intra_subnet_private_dns_hostname_type_on_launch"])
            check_type(argname="argument intra_subnets", value=intra_subnets, expected_type=type_hints["intra_subnets"])
            check_type(argname="argument intra_subnet_suffix", value=intra_subnet_suffix, expected_type=type_hints["intra_subnet_suffix"])
            check_type(argname="argument intra_subnet_tags", value=intra_subnet_tags, expected_type=type_hints["intra_subnet_tags"])
            check_type(argname="argument ipv4_ipam_pool_id", value=ipv4_ipam_pool_id, expected_type=type_hints["ipv4_ipam_pool_id"])
            check_type(argname="argument ipv4_netmask_length", value=ipv4_netmask_length, expected_type=type_hints["ipv4_netmask_length"])
            check_type(argname="argument ipv6_cidr", value=ipv6_cidr, expected_type=type_hints["ipv6_cidr"])
            check_type(argname="argument ipv6_cidr_block_network_border_group", value=ipv6_cidr_block_network_border_group, expected_type=type_hints["ipv6_cidr_block_network_border_group"])
            check_type(argname="argument ipv6_ipam_pool_id", value=ipv6_ipam_pool_id, expected_type=type_hints["ipv6_ipam_pool_id"])
            check_type(argname="argument ipv6_netmask_length", value=ipv6_netmask_length, expected_type=type_hints["ipv6_netmask_length"])
            check_type(argname="argument manage_default_network_acl", value=manage_default_network_acl, expected_type=type_hints["manage_default_network_acl"])
            check_type(argname="argument manage_default_route_table", value=manage_default_route_table, expected_type=type_hints["manage_default_route_table"])
            check_type(argname="argument manage_default_security_group", value=manage_default_security_group, expected_type=type_hints["manage_default_security_group"])
            check_type(argname="argument manage_default_vpc", value=manage_default_vpc, expected_type=type_hints["manage_default_vpc"])
            check_type(argname="argument map_customer_owned_ip_on_launch", value=map_customer_owned_ip_on_launch, expected_type=type_hints["map_customer_owned_ip_on_launch"])
            check_type(argname="argument map_public_ip_on_launch", value=map_public_ip_on_launch, expected_type=type_hints["map_public_ip_on_launch"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument nat_eip_tags", value=nat_eip_tags, expected_type=type_hints["nat_eip_tags"])
            check_type(argname="argument nat_gateway_destination_cidr_block", value=nat_gateway_destination_cidr_block, expected_type=type_hints["nat_gateway_destination_cidr_block"])
            check_type(argname="argument nat_gateway_tags", value=nat_gateway_tags, expected_type=type_hints["nat_gateway_tags"])
            check_type(argname="argument one_nat_gateway_per_az", value=one_nat_gateway_per_az, expected_type=type_hints["one_nat_gateway_per_az"])
            check_type(argname="argument outpost_acl_tags", value=outpost_acl_tags, expected_type=type_hints["outpost_acl_tags"])
            check_type(argname="argument outpost_arn", value=outpost_arn, expected_type=type_hints["outpost_arn"])
            check_type(argname="argument outpost_az", value=outpost_az, expected_type=type_hints["outpost_az"])
            check_type(argname="argument outpost_dedicated_network_acl", value=outpost_dedicated_network_acl, expected_type=type_hints["outpost_dedicated_network_acl"])
            check_type(argname="argument outpost_inbound_acl_rules", value=outpost_inbound_acl_rules, expected_type=type_hints["outpost_inbound_acl_rules"])
            check_type(argname="argument outpost_outbound_acl_rules", value=outpost_outbound_acl_rules, expected_type=type_hints["outpost_outbound_acl_rules"])
            check_type(argname="argument outpost_subnet_assign_ipv6_address_on_creation", value=outpost_subnet_assign_ipv6_address_on_creation, expected_type=type_hints["outpost_subnet_assign_ipv6_address_on_creation"])
            check_type(argname="argument outpost_subnet_enable_dns64", value=outpost_subnet_enable_dns64, expected_type=type_hints["outpost_subnet_enable_dns64"])
            check_type(argname="argument outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch", value=outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch, expected_type=type_hints["outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch"])
            check_type(argname="argument outpost_subnet_enable_resource_name_dns_a_record_on_launch", value=outpost_subnet_enable_resource_name_dns_a_record_on_launch, expected_type=type_hints["outpost_subnet_enable_resource_name_dns_a_record_on_launch"])
            check_type(argname="argument outpost_subnet_ipv6_native", value=outpost_subnet_ipv6_native, expected_type=type_hints["outpost_subnet_ipv6_native"])
            check_type(argname="argument outpost_subnet_ipv6_prefixes", value=outpost_subnet_ipv6_prefixes, expected_type=type_hints["outpost_subnet_ipv6_prefixes"])
            check_type(argname="argument outpost_subnet_names", value=outpost_subnet_names, expected_type=type_hints["outpost_subnet_names"])
            check_type(argname="argument outpost_subnet_private_dns_hostname_type_on_launch", value=outpost_subnet_private_dns_hostname_type_on_launch, expected_type=type_hints["outpost_subnet_private_dns_hostname_type_on_launch"])
            check_type(argname="argument outpost_subnets", value=outpost_subnets, expected_type=type_hints["outpost_subnets"])
            check_type(argname="argument outpost_subnet_suffix", value=outpost_subnet_suffix, expected_type=type_hints["outpost_subnet_suffix"])
            check_type(argname="argument outpost_subnet_tags", value=outpost_subnet_tags, expected_type=type_hints["outpost_subnet_tags"])
            check_type(argname="argument private_acl_tags", value=private_acl_tags, expected_type=type_hints["private_acl_tags"])
            check_type(argname="argument private_dedicated_network_acl", value=private_dedicated_network_acl, expected_type=type_hints["private_dedicated_network_acl"])
            check_type(argname="argument private_inbound_acl_rules", value=private_inbound_acl_rules, expected_type=type_hints["private_inbound_acl_rules"])
            check_type(argname="argument private_outbound_acl_rules", value=private_outbound_acl_rules, expected_type=type_hints["private_outbound_acl_rules"])
            check_type(argname="argument private_route_table_tags", value=private_route_table_tags, expected_type=type_hints["private_route_table_tags"])
            check_type(argname="argument private_subnet_assign_ipv6_address_on_creation", value=private_subnet_assign_ipv6_address_on_creation, expected_type=type_hints["private_subnet_assign_ipv6_address_on_creation"])
            check_type(argname="argument private_subnet_enable_dns64", value=private_subnet_enable_dns64, expected_type=type_hints["private_subnet_enable_dns64"])
            check_type(argname="argument private_subnet_enable_resource_name_dns_aaaa_record_on_launch", value=private_subnet_enable_resource_name_dns_aaaa_record_on_launch, expected_type=type_hints["private_subnet_enable_resource_name_dns_aaaa_record_on_launch"])
            check_type(argname="argument private_subnet_enable_resource_name_dns_a_record_on_launch", value=private_subnet_enable_resource_name_dns_a_record_on_launch, expected_type=type_hints["private_subnet_enable_resource_name_dns_a_record_on_launch"])
            check_type(argname="argument private_subnet_ipv6_native", value=private_subnet_ipv6_native, expected_type=type_hints["private_subnet_ipv6_native"])
            check_type(argname="argument private_subnet_ipv6_prefixes", value=private_subnet_ipv6_prefixes, expected_type=type_hints["private_subnet_ipv6_prefixes"])
            check_type(argname="argument private_subnet_names", value=private_subnet_names, expected_type=type_hints["private_subnet_names"])
            check_type(argname="argument private_subnet_private_dns_hostname_type_on_launch", value=private_subnet_private_dns_hostname_type_on_launch, expected_type=type_hints["private_subnet_private_dns_hostname_type_on_launch"])
            check_type(argname="argument private_subnets", value=private_subnets, expected_type=type_hints["private_subnets"])
            check_type(argname="argument private_subnet_suffix", value=private_subnet_suffix, expected_type=type_hints["private_subnet_suffix"])
            check_type(argname="argument private_subnet_tags", value=private_subnet_tags, expected_type=type_hints["private_subnet_tags"])
            check_type(argname="argument private_subnet_tags_per_az", value=private_subnet_tags_per_az, expected_type=type_hints["private_subnet_tags_per_az"])
            check_type(argname="argument propagate_intra_route_tables_vgw", value=propagate_intra_route_tables_vgw, expected_type=type_hints["propagate_intra_route_tables_vgw"])
            check_type(argname="argument propagate_private_route_tables_vgw", value=propagate_private_route_tables_vgw, expected_type=type_hints["propagate_private_route_tables_vgw"])
            check_type(argname="argument propagate_public_route_tables_vgw", value=propagate_public_route_tables_vgw, expected_type=type_hints["propagate_public_route_tables_vgw"])
            check_type(argname="argument public_acl_tags", value=public_acl_tags, expected_type=type_hints["public_acl_tags"])
            check_type(argname="argument public_dedicated_network_acl", value=public_dedicated_network_acl, expected_type=type_hints["public_dedicated_network_acl"])
            check_type(argname="argument public_inbound_acl_rules", value=public_inbound_acl_rules, expected_type=type_hints["public_inbound_acl_rules"])
            check_type(argname="argument public_outbound_acl_rules", value=public_outbound_acl_rules, expected_type=type_hints["public_outbound_acl_rules"])
            check_type(argname="argument public_route_table_tags", value=public_route_table_tags, expected_type=type_hints["public_route_table_tags"])
            check_type(argname="argument public_subnet_assign_ipv6_address_on_creation", value=public_subnet_assign_ipv6_address_on_creation, expected_type=type_hints["public_subnet_assign_ipv6_address_on_creation"])
            check_type(argname="argument public_subnet_enable_dns64", value=public_subnet_enable_dns64, expected_type=type_hints["public_subnet_enable_dns64"])
            check_type(argname="argument public_subnet_enable_resource_name_dns_aaaa_record_on_launch", value=public_subnet_enable_resource_name_dns_aaaa_record_on_launch, expected_type=type_hints["public_subnet_enable_resource_name_dns_aaaa_record_on_launch"])
            check_type(argname="argument public_subnet_enable_resource_name_dns_a_record_on_launch", value=public_subnet_enable_resource_name_dns_a_record_on_launch, expected_type=type_hints["public_subnet_enable_resource_name_dns_a_record_on_launch"])
            check_type(argname="argument public_subnet_ipv6_native", value=public_subnet_ipv6_native, expected_type=type_hints["public_subnet_ipv6_native"])
            check_type(argname="argument public_subnet_ipv6_prefixes", value=public_subnet_ipv6_prefixes, expected_type=type_hints["public_subnet_ipv6_prefixes"])
            check_type(argname="argument public_subnet_names", value=public_subnet_names, expected_type=type_hints["public_subnet_names"])
            check_type(argname="argument public_subnet_private_dns_hostname_type_on_launch", value=public_subnet_private_dns_hostname_type_on_launch, expected_type=type_hints["public_subnet_private_dns_hostname_type_on_launch"])
            check_type(argname="argument public_subnets", value=public_subnets, expected_type=type_hints["public_subnets"])
            check_type(argname="argument public_subnet_suffix", value=public_subnet_suffix, expected_type=type_hints["public_subnet_suffix"])
            check_type(argname="argument public_subnet_tags", value=public_subnet_tags, expected_type=type_hints["public_subnet_tags"])
            check_type(argname="argument public_subnet_tags_per_az", value=public_subnet_tags_per_az, expected_type=type_hints["public_subnet_tags_per_az"])
            check_type(argname="argument putin_khuylo", value=putin_khuylo, expected_type=type_hints["putin_khuylo"])
            check_type(argname="argument redshift_acl_tags", value=redshift_acl_tags, expected_type=type_hints["redshift_acl_tags"])
            check_type(argname="argument redshift_dedicated_network_acl", value=redshift_dedicated_network_acl, expected_type=type_hints["redshift_dedicated_network_acl"])
            check_type(argname="argument redshift_inbound_acl_rules", value=redshift_inbound_acl_rules, expected_type=type_hints["redshift_inbound_acl_rules"])
            check_type(argname="argument redshift_outbound_acl_rules", value=redshift_outbound_acl_rules, expected_type=type_hints["redshift_outbound_acl_rules"])
            check_type(argname="argument redshift_route_table_tags", value=redshift_route_table_tags, expected_type=type_hints["redshift_route_table_tags"])
            check_type(argname="argument redshift_subnet_assign_ipv6_address_on_creation", value=redshift_subnet_assign_ipv6_address_on_creation, expected_type=type_hints["redshift_subnet_assign_ipv6_address_on_creation"])
            check_type(argname="argument redshift_subnet_enable_dns64", value=redshift_subnet_enable_dns64, expected_type=type_hints["redshift_subnet_enable_dns64"])
            check_type(argname="argument redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch", value=redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch, expected_type=type_hints["redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch"])
            check_type(argname="argument redshift_subnet_enable_resource_name_dns_a_record_on_launch", value=redshift_subnet_enable_resource_name_dns_a_record_on_launch, expected_type=type_hints["redshift_subnet_enable_resource_name_dns_a_record_on_launch"])
            check_type(argname="argument redshift_subnet_group_name", value=redshift_subnet_group_name, expected_type=type_hints["redshift_subnet_group_name"])
            check_type(argname="argument redshift_subnet_group_tags", value=redshift_subnet_group_tags, expected_type=type_hints["redshift_subnet_group_tags"])
            check_type(argname="argument redshift_subnet_ipv6_native", value=redshift_subnet_ipv6_native, expected_type=type_hints["redshift_subnet_ipv6_native"])
            check_type(argname="argument redshift_subnet_ipv6_prefixes", value=redshift_subnet_ipv6_prefixes, expected_type=type_hints["redshift_subnet_ipv6_prefixes"])
            check_type(argname="argument redshift_subnet_names", value=redshift_subnet_names, expected_type=type_hints["redshift_subnet_names"])
            check_type(argname="argument redshift_subnet_private_dns_hostname_type_on_launch", value=redshift_subnet_private_dns_hostname_type_on_launch, expected_type=type_hints["redshift_subnet_private_dns_hostname_type_on_launch"])
            check_type(argname="argument redshift_subnets", value=redshift_subnets, expected_type=type_hints["redshift_subnets"])
            check_type(argname="argument redshift_subnet_suffix", value=redshift_subnet_suffix, expected_type=type_hints["redshift_subnet_suffix"])
            check_type(argname="argument redshift_subnet_tags", value=redshift_subnet_tags, expected_type=type_hints["redshift_subnet_tags"])
            check_type(argname="argument reuse_nat_ips", value=reuse_nat_ips, expected_type=type_hints["reuse_nat_ips"])
            check_type(argname="argument secondary_cidr_blocks", value=secondary_cidr_blocks, expected_type=type_hints["secondary_cidr_blocks"])
            check_type(argname="argument single_nat_gateway", value=single_nat_gateway, expected_type=type_hints["single_nat_gateway"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument use_ipam_pool", value=use_ipam_pool, expected_type=type_hints["use_ipam_pool"])
            check_type(argname="argument vpc_flow_log_iam_policy_name", value=vpc_flow_log_iam_policy_name, expected_type=type_hints["vpc_flow_log_iam_policy_name"])
            check_type(argname="argument vpc_flow_log_iam_policy_use_name_prefix", value=vpc_flow_log_iam_policy_use_name_prefix, expected_type=type_hints["vpc_flow_log_iam_policy_use_name_prefix"])
            check_type(argname="argument vpc_flow_log_iam_role_name", value=vpc_flow_log_iam_role_name, expected_type=type_hints["vpc_flow_log_iam_role_name"])
            check_type(argname="argument vpc_flow_log_iam_role_use_name_prefix", value=vpc_flow_log_iam_role_use_name_prefix, expected_type=type_hints["vpc_flow_log_iam_role_use_name_prefix"])
            check_type(argname="argument vpc_flow_log_permissions_boundary", value=vpc_flow_log_permissions_boundary, expected_type=type_hints["vpc_flow_log_permissions_boundary"])
            check_type(argname="argument vpc_flow_log_tags", value=vpc_flow_log_tags, expected_type=type_hints["vpc_flow_log_tags"])
            check_type(argname="argument vpc_tags", value=vpc_tags, expected_type=type_hints["vpc_tags"])
            check_type(argname="argument vpn_gateway_az", value=vpn_gateway_az, expected_type=type_hints["vpn_gateway_az"])
            check_type(argname="argument vpn_gateway_id", value=vpn_gateway_id, expected_type=type_hints["vpn_gateway_id"])
            check_type(argname="argument vpn_gateway_tags", value=vpn_gateway_tags, expected_type=type_hints["vpn_gateway_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if providers is not None:
            self._values["providers"] = providers
        if skip_asset_creation_from_local_modules is not None:
            self._values["skip_asset_creation_from_local_modules"] = skip_asset_creation_from_local_modules
        if amazon_side_asn is not None:
            self._values["amazon_side_asn"] = amazon_side_asn
        if azs is not None:
            self._values["azs"] = azs
        if cidr is not None:
            self._values["cidr"] = cidr
        if create_database_internet_gateway_route is not None:
            self._values["create_database_internet_gateway_route"] = create_database_internet_gateway_route
        if create_database_nat_gateway_route is not None:
            self._values["create_database_nat_gateway_route"] = create_database_nat_gateway_route
        if create_database_subnet_group is not None:
            self._values["create_database_subnet_group"] = create_database_subnet_group
        if create_database_subnet_route_table is not None:
            self._values["create_database_subnet_route_table"] = create_database_subnet_route_table
        if create_egress_only_igw is not None:
            self._values["create_egress_only_igw"] = create_egress_only_igw
        if create_elasticache_subnet_group is not None:
            self._values["create_elasticache_subnet_group"] = create_elasticache_subnet_group
        if create_elasticache_subnet_route_table is not None:
            self._values["create_elasticache_subnet_route_table"] = create_elasticache_subnet_route_table
        if create_flow_log_cloudwatch_iam_role is not None:
            self._values["create_flow_log_cloudwatch_iam_role"] = create_flow_log_cloudwatch_iam_role
        if create_flow_log_cloudwatch_log_group is not None:
            self._values["create_flow_log_cloudwatch_log_group"] = create_flow_log_cloudwatch_log_group
        if create_igw is not None:
            self._values["create_igw"] = create_igw
        if create_multiple_intra_route_tables is not None:
            self._values["create_multiple_intra_route_tables"] = create_multiple_intra_route_tables
        if create_multiple_public_route_tables is not None:
            self._values["create_multiple_public_route_tables"] = create_multiple_public_route_tables
        if create_private_nat_gateway_route is not None:
            self._values["create_private_nat_gateway_route"] = create_private_nat_gateway_route
        if create_redshift_subnet_group is not None:
            self._values["create_redshift_subnet_group"] = create_redshift_subnet_group
        if create_redshift_subnet_route_table is not None:
            self._values["create_redshift_subnet_route_table"] = create_redshift_subnet_route_table
        if create_vpc is not None:
            self._values["create_vpc"] = create_vpc
        if customer_gateways is not None:
            self._values["customer_gateways"] = customer_gateways
        if customer_gateway_tags is not None:
            self._values["customer_gateway_tags"] = customer_gateway_tags
        if customer_owned_ipv4_pool is not None:
            self._values["customer_owned_ipv4_pool"] = customer_owned_ipv4_pool
        if database_acl_tags is not None:
            self._values["database_acl_tags"] = database_acl_tags
        if database_dedicated_network_acl is not None:
            self._values["database_dedicated_network_acl"] = database_dedicated_network_acl
        if database_inbound_acl_rules is not None:
            self._values["database_inbound_acl_rules"] = database_inbound_acl_rules
        if database_outbound_acl_rules is not None:
            self._values["database_outbound_acl_rules"] = database_outbound_acl_rules
        if database_route_table_tags is not None:
            self._values["database_route_table_tags"] = database_route_table_tags
        if database_subnet_assign_ipv6_address_on_creation is not None:
            self._values["database_subnet_assign_ipv6_address_on_creation"] = database_subnet_assign_ipv6_address_on_creation
        if database_subnet_enable_dns64 is not None:
            self._values["database_subnet_enable_dns64"] = database_subnet_enable_dns64
        if database_subnet_enable_resource_name_dns_aaaa_record_on_launch is not None:
            self._values["database_subnet_enable_resource_name_dns_aaaa_record_on_launch"] = database_subnet_enable_resource_name_dns_aaaa_record_on_launch
        if database_subnet_enable_resource_name_dns_a_record_on_launch is not None:
            self._values["database_subnet_enable_resource_name_dns_a_record_on_launch"] = database_subnet_enable_resource_name_dns_a_record_on_launch
        if database_subnet_group_name is not None:
            self._values["database_subnet_group_name"] = database_subnet_group_name
        if database_subnet_group_tags is not None:
            self._values["database_subnet_group_tags"] = database_subnet_group_tags
        if database_subnet_ipv6_native is not None:
            self._values["database_subnet_ipv6_native"] = database_subnet_ipv6_native
        if database_subnet_ipv6_prefixes is not None:
            self._values["database_subnet_ipv6_prefixes"] = database_subnet_ipv6_prefixes
        if database_subnet_names is not None:
            self._values["database_subnet_names"] = database_subnet_names
        if database_subnet_private_dns_hostname_type_on_launch is not None:
            self._values["database_subnet_private_dns_hostname_type_on_launch"] = database_subnet_private_dns_hostname_type_on_launch
        if database_subnets is not None:
            self._values["database_subnets"] = database_subnets
        if database_subnet_suffix is not None:
            self._values["database_subnet_suffix"] = database_subnet_suffix
        if database_subnet_tags is not None:
            self._values["database_subnet_tags"] = database_subnet_tags
        if default_network_acl_egress is not None:
            self._values["default_network_acl_egress"] = default_network_acl_egress
        if default_network_acl_ingress is not None:
            self._values["default_network_acl_ingress"] = default_network_acl_ingress
        if default_network_acl_name is not None:
            self._values["default_network_acl_name"] = default_network_acl_name
        if default_network_acl_tags is not None:
            self._values["default_network_acl_tags"] = default_network_acl_tags
        if default_route_table_name is not None:
            self._values["default_route_table_name"] = default_route_table_name
        if default_route_table_propagating_vgws is not None:
            self._values["default_route_table_propagating_vgws"] = default_route_table_propagating_vgws
        if default_route_table_routes is not None:
            self._values["default_route_table_routes"] = default_route_table_routes
        if default_route_table_tags is not None:
            self._values["default_route_table_tags"] = default_route_table_tags
        if default_security_group_egress is not None:
            self._values["default_security_group_egress"] = default_security_group_egress
        if default_security_group_ingress is not None:
            self._values["default_security_group_ingress"] = default_security_group_ingress
        if default_security_group_name is not None:
            self._values["default_security_group_name"] = default_security_group_name
        if default_security_group_tags is not None:
            self._values["default_security_group_tags"] = default_security_group_tags
        if default_vpc_enable_dns_hostnames is not None:
            self._values["default_vpc_enable_dns_hostnames"] = default_vpc_enable_dns_hostnames
        if default_vpc_enable_dns_support is not None:
            self._values["default_vpc_enable_dns_support"] = default_vpc_enable_dns_support
        if default_vpc_name is not None:
            self._values["default_vpc_name"] = default_vpc_name
        if default_vpc_tags is not None:
            self._values["default_vpc_tags"] = default_vpc_tags
        if dhcp_options_domain_name is not None:
            self._values["dhcp_options_domain_name"] = dhcp_options_domain_name
        if dhcp_options_domain_name_servers is not None:
            self._values["dhcp_options_domain_name_servers"] = dhcp_options_domain_name_servers
        if dhcp_options_ipv6_address_preferred_lease_time is not None:
            self._values["dhcp_options_ipv6_address_preferred_lease_time"] = dhcp_options_ipv6_address_preferred_lease_time
        if dhcp_options_netbios_name_servers is not None:
            self._values["dhcp_options_netbios_name_servers"] = dhcp_options_netbios_name_servers
        if dhcp_options_netbios_node_type is not None:
            self._values["dhcp_options_netbios_node_type"] = dhcp_options_netbios_node_type
        if dhcp_options_ntp_servers is not None:
            self._values["dhcp_options_ntp_servers"] = dhcp_options_ntp_servers
        if dhcp_options_tags is not None:
            self._values["dhcp_options_tags"] = dhcp_options_tags
        if elasticache_acl_tags is not None:
            self._values["elasticache_acl_tags"] = elasticache_acl_tags
        if elasticache_dedicated_network_acl is not None:
            self._values["elasticache_dedicated_network_acl"] = elasticache_dedicated_network_acl
        if elasticache_inbound_acl_rules is not None:
            self._values["elasticache_inbound_acl_rules"] = elasticache_inbound_acl_rules
        if elasticache_outbound_acl_rules is not None:
            self._values["elasticache_outbound_acl_rules"] = elasticache_outbound_acl_rules
        if elasticache_route_table_tags is not None:
            self._values["elasticache_route_table_tags"] = elasticache_route_table_tags
        if elasticache_subnet_assign_ipv6_address_on_creation is not None:
            self._values["elasticache_subnet_assign_ipv6_address_on_creation"] = elasticache_subnet_assign_ipv6_address_on_creation
        if elasticache_subnet_enable_dns64 is not None:
            self._values["elasticache_subnet_enable_dns64"] = elasticache_subnet_enable_dns64
        if elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch is not None:
            self._values["elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch"] = elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch
        if elasticache_subnet_enable_resource_name_dns_a_record_on_launch is not None:
            self._values["elasticache_subnet_enable_resource_name_dns_a_record_on_launch"] = elasticache_subnet_enable_resource_name_dns_a_record_on_launch
        if elasticache_subnet_group_name is not None:
            self._values["elasticache_subnet_group_name"] = elasticache_subnet_group_name
        if elasticache_subnet_group_tags is not None:
            self._values["elasticache_subnet_group_tags"] = elasticache_subnet_group_tags
        if elasticache_subnet_ipv6_native is not None:
            self._values["elasticache_subnet_ipv6_native"] = elasticache_subnet_ipv6_native
        if elasticache_subnet_ipv6_prefixes is not None:
            self._values["elasticache_subnet_ipv6_prefixes"] = elasticache_subnet_ipv6_prefixes
        if elasticache_subnet_names is not None:
            self._values["elasticache_subnet_names"] = elasticache_subnet_names
        if elasticache_subnet_private_dns_hostname_type_on_launch is not None:
            self._values["elasticache_subnet_private_dns_hostname_type_on_launch"] = elasticache_subnet_private_dns_hostname_type_on_launch
        if elasticache_subnets is not None:
            self._values["elasticache_subnets"] = elasticache_subnets
        if elasticache_subnet_suffix is not None:
            self._values["elasticache_subnet_suffix"] = elasticache_subnet_suffix
        if elasticache_subnet_tags is not None:
            self._values["elasticache_subnet_tags"] = elasticache_subnet_tags
        if enable_dhcp_options is not None:
            self._values["enable_dhcp_options"] = enable_dhcp_options
        if enable_dns_hostnames is not None:
            self._values["enable_dns_hostnames"] = enable_dns_hostnames
        if enable_dns_support is not None:
            self._values["enable_dns_support"] = enable_dns_support
        if enable_flow_log is not None:
            self._values["enable_flow_log"] = enable_flow_log
        if enable_ipv6 is not None:
            self._values["enable_ipv6"] = enable_ipv6
        if enable_nat_gateway is not None:
            self._values["enable_nat_gateway"] = enable_nat_gateway
        if enable_network_address_usage_metrics is not None:
            self._values["enable_network_address_usage_metrics"] = enable_network_address_usage_metrics
        if enable_public_redshift is not None:
            self._values["enable_public_redshift"] = enable_public_redshift
        if enable_vpn_gateway is not None:
            self._values["enable_vpn_gateway"] = enable_vpn_gateway
        if external_nat_ip_ids is not None:
            self._values["external_nat_ip_ids"] = external_nat_ip_ids
        if external_nat_ips is not None:
            self._values["external_nat_ips"] = external_nat_ips
        if flow_log_cloudwatch_iam_role_arn is not None:
            self._values["flow_log_cloudwatch_iam_role_arn"] = flow_log_cloudwatch_iam_role_arn
        if flow_log_cloudwatch_iam_role_conditions is not None:
            self._values["flow_log_cloudwatch_iam_role_conditions"] = flow_log_cloudwatch_iam_role_conditions
        if flow_log_cloudwatch_log_group_class is not None:
            self._values["flow_log_cloudwatch_log_group_class"] = flow_log_cloudwatch_log_group_class
        if flow_log_cloudwatch_log_group_kms_key_id is not None:
            self._values["flow_log_cloudwatch_log_group_kms_key_id"] = flow_log_cloudwatch_log_group_kms_key_id
        if flow_log_cloudwatch_log_group_name_prefix is not None:
            self._values["flow_log_cloudwatch_log_group_name_prefix"] = flow_log_cloudwatch_log_group_name_prefix
        if flow_log_cloudwatch_log_group_name_suffix is not None:
            self._values["flow_log_cloudwatch_log_group_name_suffix"] = flow_log_cloudwatch_log_group_name_suffix
        if flow_log_cloudwatch_log_group_retention_in_days is not None:
            self._values["flow_log_cloudwatch_log_group_retention_in_days"] = flow_log_cloudwatch_log_group_retention_in_days
        if flow_log_cloudwatch_log_group_skip_destroy is not None:
            self._values["flow_log_cloudwatch_log_group_skip_destroy"] = flow_log_cloudwatch_log_group_skip_destroy
        if flow_log_deliver_cross_account_role is not None:
            self._values["flow_log_deliver_cross_account_role"] = flow_log_deliver_cross_account_role
        if flow_log_destination_arn is not None:
            self._values["flow_log_destination_arn"] = flow_log_destination_arn
        if flow_log_destination_type is not None:
            self._values["flow_log_destination_type"] = flow_log_destination_type
        if flow_log_file_format is not None:
            self._values["flow_log_file_format"] = flow_log_file_format
        if flow_log_hive_compatible_partitions is not None:
            self._values["flow_log_hive_compatible_partitions"] = flow_log_hive_compatible_partitions
        if flow_log_log_format is not None:
            self._values["flow_log_log_format"] = flow_log_log_format
        if flow_log_max_aggregation_interval is not None:
            self._values["flow_log_max_aggregation_interval"] = flow_log_max_aggregation_interval
        if flow_log_per_hour_partition is not None:
            self._values["flow_log_per_hour_partition"] = flow_log_per_hour_partition
        if flow_log_traffic_type is not None:
            self._values["flow_log_traffic_type"] = flow_log_traffic_type
        if igw_tags is not None:
            self._values["igw_tags"] = igw_tags
        if instance_tenancy is not None:
            self._values["instance_tenancy"] = instance_tenancy
        if intra_acl_tags is not None:
            self._values["intra_acl_tags"] = intra_acl_tags
        if intra_dedicated_network_acl is not None:
            self._values["intra_dedicated_network_acl"] = intra_dedicated_network_acl
        if intra_inbound_acl_rules is not None:
            self._values["intra_inbound_acl_rules"] = intra_inbound_acl_rules
        if intra_outbound_acl_rules is not None:
            self._values["intra_outbound_acl_rules"] = intra_outbound_acl_rules
        if intra_route_table_tags is not None:
            self._values["intra_route_table_tags"] = intra_route_table_tags
        if intra_subnet_assign_ipv6_address_on_creation is not None:
            self._values["intra_subnet_assign_ipv6_address_on_creation"] = intra_subnet_assign_ipv6_address_on_creation
        if intra_subnet_enable_dns64 is not None:
            self._values["intra_subnet_enable_dns64"] = intra_subnet_enable_dns64
        if intra_subnet_enable_resource_name_dns_aaaa_record_on_launch is not None:
            self._values["intra_subnet_enable_resource_name_dns_aaaa_record_on_launch"] = intra_subnet_enable_resource_name_dns_aaaa_record_on_launch
        if intra_subnet_enable_resource_name_dns_a_record_on_launch is not None:
            self._values["intra_subnet_enable_resource_name_dns_a_record_on_launch"] = intra_subnet_enable_resource_name_dns_a_record_on_launch
        if intra_subnet_ipv6_native is not None:
            self._values["intra_subnet_ipv6_native"] = intra_subnet_ipv6_native
        if intra_subnet_ipv6_prefixes is not None:
            self._values["intra_subnet_ipv6_prefixes"] = intra_subnet_ipv6_prefixes
        if intra_subnet_names is not None:
            self._values["intra_subnet_names"] = intra_subnet_names
        if intra_subnet_private_dns_hostname_type_on_launch is not None:
            self._values["intra_subnet_private_dns_hostname_type_on_launch"] = intra_subnet_private_dns_hostname_type_on_launch
        if intra_subnets is not None:
            self._values["intra_subnets"] = intra_subnets
        if intra_subnet_suffix is not None:
            self._values["intra_subnet_suffix"] = intra_subnet_suffix
        if intra_subnet_tags is not None:
            self._values["intra_subnet_tags"] = intra_subnet_tags
        if ipv4_ipam_pool_id is not None:
            self._values["ipv4_ipam_pool_id"] = ipv4_ipam_pool_id
        if ipv4_netmask_length is not None:
            self._values["ipv4_netmask_length"] = ipv4_netmask_length
        if ipv6_cidr is not None:
            self._values["ipv6_cidr"] = ipv6_cidr
        if ipv6_cidr_block_network_border_group is not None:
            self._values["ipv6_cidr_block_network_border_group"] = ipv6_cidr_block_network_border_group
        if ipv6_ipam_pool_id is not None:
            self._values["ipv6_ipam_pool_id"] = ipv6_ipam_pool_id
        if ipv6_netmask_length is not None:
            self._values["ipv6_netmask_length"] = ipv6_netmask_length
        if manage_default_network_acl is not None:
            self._values["manage_default_network_acl"] = manage_default_network_acl
        if manage_default_route_table is not None:
            self._values["manage_default_route_table"] = manage_default_route_table
        if manage_default_security_group is not None:
            self._values["manage_default_security_group"] = manage_default_security_group
        if manage_default_vpc is not None:
            self._values["manage_default_vpc"] = manage_default_vpc
        if map_customer_owned_ip_on_launch is not None:
            self._values["map_customer_owned_ip_on_launch"] = map_customer_owned_ip_on_launch
        if map_public_ip_on_launch is not None:
            self._values["map_public_ip_on_launch"] = map_public_ip_on_launch
        if name is not None:
            self._values["name"] = name
        if nat_eip_tags is not None:
            self._values["nat_eip_tags"] = nat_eip_tags
        if nat_gateway_destination_cidr_block is not None:
            self._values["nat_gateway_destination_cidr_block"] = nat_gateway_destination_cidr_block
        if nat_gateway_tags is not None:
            self._values["nat_gateway_tags"] = nat_gateway_tags
        if one_nat_gateway_per_az is not None:
            self._values["one_nat_gateway_per_az"] = one_nat_gateway_per_az
        if outpost_acl_tags is not None:
            self._values["outpost_acl_tags"] = outpost_acl_tags
        if outpost_arn is not None:
            self._values["outpost_arn"] = outpost_arn
        if outpost_az is not None:
            self._values["outpost_az"] = outpost_az
        if outpost_dedicated_network_acl is not None:
            self._values["outpost_dedicated_network_acl"] = outpost_dedicated_network_acl
        if outpost_inbound_acl_rules is not None:
            self._values["outpost_inbound_acl_rules"] = outpost_inbound_acl_rules
        if outpost_outbound_acl_rules is not None:
            self._values["outpost_outbound_acl_rules"] = outpost_outbound_acl_rules
        if outpost_subnet_assign_ipv6_address_on_creation is not None:
            self._values["outpost_subnet_assign_ipv6_address_on_creation"] = outpost_subnet_assign_ipv6_address_on_creation
        if outpost_subnet_enable_dns64 is not None:
            self._values["outpost_subnet_enable_dns64"] = outpost_subnet_enable_dns64
        if outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch is not None:
            self._values["outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch"] = outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch
        if outpost_subnet_enable_resource_name_dns_a_record_on_launch is not None:
            self._values["outpost_subnet_enable_resource_name_dns_a_record_on_launch"] = outpost_subnet_enable_resource_name_dns_a_record_on_launch
        if outpost_subnet_ipv6_native is not None:
            self._values["outpost_subnet_ipv6_native"] = outpost_subnet_ipv6_native
        if outpost_subnet_ipv6_prefixes is not None:
            self._values["outpost_subnet_ipv6_prefixes"] = outpost_subnet_ipv6_prefixes
        if outpost_subnet_names is not None:
            self._values["outpost_subnet_names"] = outpost_subnet_names
        if outpost_subnet_private_dns_hostname_type_on_launch is not None:
            self._values["outpost_subnet_private_dns_hostname_type_on_launch"] = outpost_subnet_private_dns_hostname_type_on_launch
        if outpost_subnets is not None:
            self._values["outpost_subnets"] = outpost_subnets
        if outpost_subnet_suffix is not None:
            self._values["outpost_subnet_suffix"] = outpost_subnet_suffix
        if outpost_subnet_tags is not None:
            self._values["outpost_subnet_tags"] = outpost_subnet_tags
        if private_acl_tags is not None:
            self._values["private_acl_tags"] = private_acl_tags
        if private_dedicated_network_acl is not None:
            self._values["private_dedicated_network_acl"] = private_dedicated_network_acl
        if private_inbound_acl_rules is not None:
            self._values["private_inbound_acl_rules"] = private_inbound_acl_rules
        if private_outbound_acl_rules is not None:
            self._values["private_outbound_acl_rules"] = private_outbound_acl_rules
        if private_route_table_tags is not None:
            self._values["private_route_table_tags"] = private_route_table_tags
        if private_subnet_assign_ipv6_address_on_creation is not None:
            self._values["private_subnet_assign_ipv6_address_on_creation"] = private_subnet_assign_ipv6_address_on_creation
        if private_subnet_enable_dns64 is not None:
            self._values["private_subnet_enable_dns64"] = private_subnet_enable_dns64
        if private_subnet_enable_resource_name_dns_aaaa_record_on_launch is not None:
            self._values["private_subnet_enable_resource_name_dns_aaaa_record_on_launch"] = private_subnet_enable_resource_name_dns_aaaa_record_on_launch
        if private_subnet_enable_resource_name_dns_a_record_on_launch is not None:
            self._values["private_subnet_enable_resource_name_dns_a_record_on_launch"] = private_subnet_enable_resource_name_dns_a_record_on_launch
        if private_subnet_ipv6_native is not None:
            self._values["private_subnet_ipv6_native"] = private_subnet_ipv6_native
        if private_subnet_ipv6_prefixes is not None:
            self._values["private_subnet_ipv6_prefixes"] = private_subnet_ipv6_prefixes
        if private_subnet_names is not None:
            self._values["private_subnet_names"] = private_subnet_names
        if private_subnet_private_dns_hostname_type_on_launch is not None:
            self._values["private_subnet_private_dns_hostname_type_on_launch"] = private_subnet_private_dns_hostname_type_on_launch
        if private_subnets is not None:
            self._values["private_subnets"] = private_subnets
        if private_subnet_suffix is not None:
            self._values["private_subnet_suffix"] = private_subnet_suffix
        if private_subnet_tags is not None:
            self._values["private_subnet_tags"] = private_subnet_tags
        if private_subnet_tags_per_az is not None:
            self._values["private_subnet_tags_per_az"] = private_subnet_tags_per_az
        if propagate_intra_route_tables_vgw is not None:
            self._values["propagate_intra_route_tables_vgw"] = propagate_intra_route_tables_vgw
        if propagate_private_route_tables_vgw is not None:
            self._values["propagate_private_route_tables_vgw"] = propagate_private_route_tables_vgw
        if propagate_public_route_tables_vgw is not None:
            self._values["propagate_public_route_tables_vgw"] = propagate_public_route_tables_vgw
        if public_acl_tags is not None:
            self._values["public_acl_tags"] = public_acl_tags
        if public_dedicated_network_acl is not None:
            self._values["public_dedicated_network_acl"] = public_dedicated_network_acl
        if public_inbound_acl_rules is not None:
            self._values["public_inbound_acl_rules"] = public_inbound_acl_rules
        if public_outbound_acl_rules is not None:
            self._values["public_outbound_acl_rules"] = public_outbound_acl_rules
        if public_route_table_tags is not None:
            self._values["public_route_table_tags"] = public_route_table_tags
        if public_subnet_assign_ipv6_address_on_creation is not None:
            self._values["public_subnet_assign_ipv6_address_on_creation"] = public_subnet_assign_ipv6_address_on_creation
        if public_subnet_enable_dns64 is not None:
            self._values["public_subnet_enable_dns64"] = public_subnet_enable_dns64
        if public_subnet_enable_resource_name_dns_aaaa_record_on_launch is not None:
            self._values["public_subnet_enable_resource_name_dns_aaaa_record_on_launch"] = public_subnet_enable_resource_name_dns_aaaa_record_on_launch
        if public_subnet_enable_resource_name_dns_a_record_on_launch is not None:
            self._values["public_subnet_enable_resource_name_dns_a_record_on_launch"] = public_subnet_enable_resource_name_dns_a_record_on_launch
        if public_subnet_ipv6_native is not None:
            self._values["public_subnet_ipv6_native"] = public_subnet_ipv6_native
        if public_subnet_ipv6_prefixes is not None:
            self._values["public_subnet_ipv6_prefixes"] = public_subnet_ipv6_prefixes
        if public_subnet_names is not None:
            self._values["public_subnet_names"] = public_subnet_names
        if public_subnet_private_dns_hostname_type_on_launch is not None:
            self._values["public_subnet_private_dns_hostname_type_on_launch"] = public_subnet_private_dns_hostname_type_on_launch
        if public_subnets is not None:
            self._values["public_subnets"] = public_subnets
        if public_subnet_suffix is not None:
            self._values["public_subnet_suffix"] = public_subnet_suffix
        if public_subnet_tags is not None:
            self._values["public_subnet_tags"] = public_subnet_tags
        if public_subnet_tags_per_az is not None:
            self._values["public_subnet_tags_per_az"] = public_subnet_tags_per_az
        if putin_khuylo is not None:
            self._values["putin_khuylo"] = putin_khuylo
        if redshift_acl_tags is not None:
            self._values["redshift_acl_tags"] = redshift_acl_tags
        if redshift_dedicated_network_acl is not None:
            self._values["redshift_dedicated_network_acl"] = redshift_dedicated_network_acl
        if redshift_inbound_acl_rules is not None:
            self._values["redshift_inbound_acl_rules"] = redshift_inbound_acl_rules
        if redshift_outbound_acl_rules is not None:
            self._values["redshift_outbound_acl_rules"] = redshift_outbound_acl_rules
        if redshift_route_table_tags is not None:
            self._values["redshift_route_table_tags"] = redshift_route_table_tags
        if redshift_subnet_assign_ipv6_address_on_creation is not None:
            self._values["redshift_subnet_assign_ipv6_address_on_creation"] = redshift_subnet_assign_ipv6_address_on_creation
        if redshift_subnet_enable_dns64 is not None:
            self._values["redshift_subnet_enable_dns64"] = redshift_subnet_enable_dns64
        if redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch is not None:
            self._values["redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch"] = redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch
        if redshift_subnet_enable_resource_name_dns_a_record_on_launch is not None:
            self._values["redshift_subnet_enable_resource_name_dns_a_record_on_launch"] = redshift_subnet_enable_resource_name_dns_a_record_on_launch
        if redshift_subnet_group_name is not None:
            self._values["redshift_subnet_group_name"] = redshift_subnet_group_name
        if redshift_subnet_group_tags is not None:
            self._values["redshift_subnet_group_tags"] = redshift_subnet_group_tags
        if redshift_subnet_ipv6_native is not None:
            self._values["redshift_subnet_ipv6_native"] = redshift_subnet_ipv6_native
        if redshift_subnet_ipv6_prefixes is not None:
            self._values["redshift_subnet_ipv6_prefixes"] = redshift_subnet_ipv6_prefixes
        if redshift_subnet_names is not None:
            self._values["redshift_subnet_names"] = redshift_subnet_names
        if redshift_subnet_private_dns_hostname_type_on_launch is not None:
            self._values["redshift_subnet_private_dns_hostname_type_on_launch"] = redshift_subnet_private_dns_hostname_type_on_launch
        if redshift_subnets is not None:
            self._values["redshift_subnets"] = redshift_subnets
        if redshift_subnet_suffix is not None:
            self._values["redshift_subnet_suffix"] = redshift_subnet_suffix
        if redshift_subnet_tags is not None:
            self._values["redshift_subnet_tags"] = redshift_subnet_tags
        if reuse_nat_ips is not None:
            self._values["reuse_nat_ips"] = reuse_nat_ips
        if secondary_cidr_blocks is not None:
            self._values["secondary_cidr_blocks"] = secondary_cidr_blocks
        if single_nat_gateway is not None:
            self._values["single_nat_gateway"] = single_nat_gateway
        if tags is not None:
            self._values["tags"] = tags
        if use_ipam_pool is not None:
            self._values["use_ipam_pool"] = use_ipam_pool
        if vpc_flow_log_iam_policy_name is not None:
            self._values["vpc_flow_log_iam_policy_name"] = vpc_flow_log_iam_policy_name
        if vpc_flow_log_iam_policy_use_name_prefix is not None:
            self._values["vpc_flow_log_iam_policy_use_name_prefix"] = vpc_flow_log_iam_policy_use_name_prefix
        if vpc_flow_log_iam_role_name is not None:
            self._values["vpc_flow_log_iam_role_name"] = vpc_flow_log_iam_role_name
        if vpc_flow_log_iam_role_use_name_prefix is not None:
            self._values["vpc_flow_log_iam_role_use_name_prefix"] = vpc_flow_log_iam_role_use_name_prefix
        if vpc_flow_log_permissions_boundary is not None:
            self._values["vpc_flow_log_permissions_boundary"] = vpc_flow_log_permissions_boundary
        if vpc_flow_log_tags is not None:
            self._values["vpc_flow_log_tags"] = vpc_flow_log_tags
        if vpc_tags is not None:
            self._values["vpc_tags"] = vpc_tags
        if vpn_gateway_az is not None:
            self._values["vpn_gateway_az"] = vpn_gateway_az
        if vpn_gateway_id is not None:
            self._values["vpn_gateway_id"] = vpn_gateway_id
        if vpn_gateway_tags is not None:
            self._values["vpn_gateway_tags"] = vpn_gateway_tags

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
    def amazon_side_asn(self) -> typing.Optional[builtins.str]:
        '''The Autonomous System Number (ASN) for the Amazon side of the gateway.

        By default the virtual private gateway is created with the current default Amazon ASN
        64512
        '''
        result = self._values.get("amazon_side_asn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def azs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of availability zones names or ids in the region.'''
        result = self._values.get("azs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cidr(self) -> typing.Optional[builtins.str]:
        '''(Optional) The IPv4 CIDR block for the VPC.

        CIDR can be explicitly set or it can be derived from IPAM using ``ipv4_netmask_length`` & ``ipv4_ipam_pool_id``
        10.0.0.0/16
        '''
        result = self._values.get("cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def create_database_internet_gateway_route(self) -> typing.Optional[builtins.bool]:
        '''Controls if an internet gateway route for public database access should be created.'''
        result = self._values.get("create_database_internet_gateway_route")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_database_nat_gateway_route(self) -> typing.Optional[builtins.bool]:
        '''Controls if a nat gateway route should be created to give internet access to the database subnets.'''
        result = self._values.get("create_database_nat_gateway_route")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_database_subnet_group(self) -> typing.Optional[builtins.bool]:
        '''Controls if database subnet group should be created (n.b. database_subnets must also be set) true.'''
        result = self._values.get("create_database_subnet_group")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_database_subnet_route_table(self) -> typing.Optional[builtins.bool]:
        '''Controls if separate route table for database should be created.'''
        result = self._values.get("create_database_subnet_route_table")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_egress_only_igw(self) -> typing.Optional[builtins.bool]:
        '''Controls if an Egress Only Internet Gateway is created and its related routes true.'''
        result = self._values.get("create_egress_only_igw")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_elasticache_subnet_group(self) -> typing.Optional[builtins.bool]:
        '''Controls if elasticache subnet group should be created true.'''
        result = self._values.get("create_elasticache_subnet_group")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_elasticache_subnet_route_table(self) -> typing.Optional[builtins.bool]:
        '''Controls if separate route table for elasticache should be created.'''
        result = self._values.get("create_elasticache_subnet_route_table")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_flow_log_cloudwatch_iam_role(self) -> typing.Optional[builtins.bool]:
        '''Whether to create IAM role for VPC Flow Logs.'''
        result = self._values.get("create_flow_log_cloudwatch_iam_role")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_flow_log_cloudwatch_log_group(self) -> typing.Optional[builtins.bool]:
        '''Whether to create CloudWatch log group for VPC Flow Logs.'''
        result = self._values.get("create_flow_log_cloudwatch_log_group")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_igw(self) -> typing.Optional[builtins.bool]:
        '''Controls if an Internet Gateway is created for public subnets and the related routes that connect them true.'''
        result = self._values.get("create_igw")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_multiple_intra_route_tables(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether to create a separate route table for each intra subnet.

        Default: ``false``
        '''
        result = self._values.get("create_multiple_intra_route_tables")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_multiple_public_route_tables(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether to create a separate route table for each public subnet.

        Default: ``false``
        '''
        result = self._values.get("create_multiple_public_route_tables")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_private_nat_gateway_route(self) -> typing.Optional[builtins.bool]:
        '''Controls if a nat gateway route should be created to give internet access to the private subnets true.'''
        result = self._values.get("create_private_nat_gateway_route")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_redshift_subnet_group(self) -> typing.Optional[builtins.bool]:
        '''Controls if redshift subnet group should be created true.'''
        result = self._values.get("create_redshift_subnet_group")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_redshift_subnet_route_table(self) -> typing.Optional[builtins.bool]:
        '''Controls if separate route table for redshift should be created.'''
        result = self._values.get("create_redshift_subnet_route_table")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def create_vpc(self) -> typing.Optional[builtins.bool]:
        '''Controls if VPC should be created (it affects almost all resources) true.'''
        result = self._values.get("create_vpc")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def customer_gateways(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]]:
        '''Maps of Customer Gateway's attributes (BGP ASN and Gateway's Internet-routable external IP address) The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("customer_gateways")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]], result)

    @builtins.property
    def customer_gateway_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the Customer Gateway The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("customer_gateway_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def customer_owned_ipv4_pool(self) -> typing.Optional[builtins.str]:
        '''The customer owned IPv4 address pool.

        Typically used with the ``map_customer_owned_ip_on_launch`` argument. The ``outpost_arn`` argument must be specified when configured
        '''
        result = self._values.get("customer_owned_ipv4_pool")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_acl_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the database subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("database_acl_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def database_dedicated_network_acl(self) -> typing.Optional[builtins.bool]:
        '''Whether to use dedicated network ACL (not default) and custom rules for database subnets.'''
        result = self._values.get("database_dedicated_network_acl")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def database_inbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''Database subnets inbound network ACL rules [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("database_inbound_acl_rules")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def database_outbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''Database subnets outbound network ACL rules [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("database_outbound_acl_rules")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def database_route_table_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the database route tables The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("database_route_table_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def database_subnet_assign_ipv6_address_on_creation(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address.

        Default is ``false``
        '''
        result = self._values.get("database_subnet_assign_ipv6_address_on_creation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def database_subnet_enable_dns64(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations.

        Default: ``true``
        true
        '''
        result = self._values.get("database_subnet_enable_dns64")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def database_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.

        Default: ``true``
        true
        '''
        result = self._values.get("database_subnet_enable_resource_name_dns_aaaa_record_on_launch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def database_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Indicates whether to respond to DNS queries for instance hostnames with DNS A records.

        Default: ``false``
        '''
        result = self._values.get("database_subnet_enable_resource_name_dns_a_record_on_launch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def database_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''Name of database subnet group.'''
        result = self._values.get("database_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_subnet_group_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the database subnet group The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("database_subnet_group_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def database_subnet_ipv6_native(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether to create an IPv6-only subnet.

        Default: ``false``
        '''
        result = self._values.get("database_subnet_ipv6_native")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def database_subnet_ipv6_prefixes(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Assigns IPv6 database subnet id based on the Amazon provided /56 prefix base 10 integer (0-256).

        Must be of equal length to the corresponding IPv4 subnet list
        '''
        result = self._values.get("database_subnet_ipv6_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def database_subnet_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Explicit values to use in the Name tag on database subnets.

        If empty, Name tags are generated
        '''
        result = self._values.get("database_subnet_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def database_subnet_private_dns_hostname_type_on_launch(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The type of hostnames to assign to instances in the subnet at launch.

        For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        '''
        result = self._values.get("database_subnet_private_dns_hostname_type_on_launch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of database subnets inside the VPC.'''
        result = self._values.get("database_subnets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def database_subnet_suffix(self) -> typing.Optional[builtins.str]:
        '''Suffix to append to database subnets name db.'''
        result = self._values.get("database_subnet_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_subnet_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the database subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("database_subnet_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def default_network_acl_egress(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''List of maps of egress rules to set on the Default Network ACL [object Object] [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("default_network_acl_egress")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def default_network_acl_ingress(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''List of maps of ingress rules to set on the Default Network ACL [object Object] [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("default_network_acl_ingress")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def default_network_acl_name(self) -> typing.Optional[builtins.str]:
        '''Name to be used on the Default Network ACL.'''
        result = self._values.get("default_network_acl_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_network_acl_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the Default Network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("default_network_acl_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def default_route_table_name(self) -> typing.Optional[builtins.str]:
        '''Name to be used on the default route table.'''
        result = self._values.get("default_route_table_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_route_table_propagating_vgws(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''List of virtual gateways for propagation.'''
        result = self._values.get("default_route_table_propagating_vgws")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def default_route_table_routes(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''Configuration block of routes. See https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/default_route_table#route.

        The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}
        '''
        result = self._values.get("default_route_table_routes")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def default_route_table_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the default route table The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("default_route_table_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def default_security_group_egress(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''List of maps of egress rules to set on the default security group.

        The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}
        '''
        result = self._values.get("default_security_group_egress")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def default_security_group_ingress(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''List of maps of ingress rules to set on the default security group.

        The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}
        '''
        result = self._values.get("default_security_group_ingress")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def default_security_group_name(self) -> typing.Optional[builtins.str]:
        '''Name to be used on the default security group.'''
        result = self._values.get("default_security_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_security_group_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the default security group The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("default_security_group_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def default_vpc_enable_dns_hostnames(self) -> typing.Optional[builtins.bool]:
        '''Should be true to enable DNS hostnames in the Default VPC true.'''
        result = self._values.get("default_vpc_enable_dns_hostnames")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def default_vpc_enable_dns_support(self) -> typing.Optional[builtins.bool]:
        '''Should be true to enable DNS support in the Default VPC true.'''
        result = self._values.get("default_vpc_enable_dns_support")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def default_vpc_name(self) -> typing.Optional[builtins.str]:
        '''Name to be used on the Default VPC.'''
        result = self._values.get("default_vpc_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_vpc_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the Default VPC The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("default_vpc_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def dhcp_options_domain_name(self) -> typing.Optional[builtins.str]:
        '''Specifies DNS name for DHCP options set (requires enable_dhcp_options set to true).'''
        result = self._values.get("dhcp_options_domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dhcp_options_domain_name_servers(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify a list of DNS server addresses for DHCP options set, default to AWS provided (requires enable_dhcp_options set to true) AmazonProvidedDNS.'''
        result = self._values.get("dhcp_options_domain_name_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def dhcp_options_ipv6_address_preferred_lease_time(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''How frequently, in seconds, a running instance with an IPv6 assigned to it goes through DHCPv6 lease renewal (requires enable_dhcp_options set to true).'''
        result = self._values.get("dhcp_options_ipv6_address_preferred_lease_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dhcp_options_netbios_name_servers(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify a list of netbios servers for DHCP options set (requires enable_dhcp_options set to true).'''
        result = self._values.get("dhcp_options_netbios_name_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def dhcp_options_netbios_node_type(self) -> typing.Optional[builtins.str]:
        '''Specify netbios node_type for DHCP options set (requires enable_dhcp_options set to true).'''
        result = self._values.get("dhcp_options_netbios_node_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dhcp_options_ntp_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify a list of NTP servers for DHCP options set (requires enable_dhcp_options set to true).'''
        result = self._values.get("dhcp_options_ntp_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def dhcp_options_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the DHCP option set (requires enable_dhcp_options set to true) The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("dhcp_options_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def elasticache_acl_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the elasticache subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("elasticache_acl_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def elasticache_dedicated_network_acl(self) -> typing.Optional[builtins.bool]:
        '''Whether to use dedicated network ACL (not default) and custom rules for elasticache subnets.'''
        result = self._values.get("elasticache_dedicated_network_acl")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def elasticache_inbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''Elasticache subnets inbound network ACL rules [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("elasticache_inbound_acl_rules")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def elasticache_outbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''Elasticache subnets outbound network ACL rules [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("elasticache_outbound_acl_rules")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def elasticache_route_table_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the elasticache route tables The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("elasticache_route_table_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def elasticache_subnet_assign_ipv6_address_on_creation(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address.

        Default is ``false``
        '''
        result = self._values.get("elasticache_subnet_assign_ipv6_address_on_creation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def elasticache_subnet_enable_dns64(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations.

        Default: ``true``
        true
        '''
        result = self._values.get("elasticache_subnet_enable_dns64")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.

        Default: ``true``
        true
        '''
        result = self._values.get("elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def elasticache_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Indicates whether to respond to DNS queries for instance hostnames with DNS A records.

        Default: ``false``
        '''
        result = self._values.get("elasticache_subnet_enable_resource_name_dns_a_record_on_launch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def elasticache_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''Name of elasticache subnet group.'''
        result = self._values.get("elasticache_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elasticache_subnet_group_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the elasticache subnet group The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("elasticache_subnet_group_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def elasticache_subnet_ipv6_native(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether to create an IPv6-only subnet.

        Default: ``false``
        '''
        result = self._values.get("elasticache_subnet_ipv6_native")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def elasticache_subnet_ipv6_prefixes(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Assigns IPv6 elasticache subnet id based on the Amazon provided /56 prefix base 10 integer (0-256).

        Must be of equal length to the corresponding IPv4 subnet list
        '''
        result = self._values.get("elasticache_subnet_ipv6_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def elasticache_subnet_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Explicit values to use in the Name tag on elasticache subnets.

        If empty, Name tags are generated
        '''
        result = self._values.get("elasticache_subnet_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def elasticache_subnet_private_dns_hostname_type_on_launch(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The type of hostnames to assign to instances in the subnet at launch.

        For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        '''
        result = self._values.get("elasticache_subnet_private_dns_hostname_type_on_launch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elasticache_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of elasticache subnets inside the VPC.'''
        result = self._values.get("elasticache_subnets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def elasticache_subnet_suffix(self) -> typing.Optional[builtins.str]:
        '''Suffix to append to elasticache subnets name elasticache.'''
        result = self._values.get("elasticache_subnet_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elasticache_subnet_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the elasticache subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("elasticache_subnet_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def enable_dhcp_options(self) -> typing.Optional[builtins.bool]:
        '''Should be true if you want to specify a DHCP options set with a custom domain name, DNS servers, NTP servers, netbios servers, and/or netbios server type.'''
        result = self._values.get("enable_dhcp_options")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_dns_hostnames(self) -> typing.Optional[builtins.bool]:
        '''Should be true to enable DNS hostnames in the VPC true.'''
        result = self._values.get("enable_dns_hostnames")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_dns_support(self) -> typing.Optional[builtins.bool]:
        '''Should be true to enable DNS support in the VPC true.'''
        result = self._values.get("enable_dns_support")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_flow_log(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to enable VPC Flow Logs.'''
        result = self._values.get("enable_flow_log")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_ipv6(self) -> typing.Optional[builtins.bool]:
        '''Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC.

        You cannot specify the range of IP addresses, or the size of the CIDR block
        '''
        result = self._values.get("enable_ipv6")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_nat_gateway(self) -> typing.Optional[builtins.bool]:
        '''Should be true if you want to provision NAT Gateways for each of your private networks.'''
        result = self._values.get("enable_nat_gateway")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_network_address_usage_metrics(self) -> typing.Optional[builtins.bool]:
        '''Determines whether network address usage metrics are enabled for the VPC.'''
        result = self._values.get("enable_network_address_usage_metrics")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_public_redshift(self) -> typing.Optional[builtins.bool]:
        '''Controls if redshift should have public routing table.'''
        result = self._values.get("enable_public_redshift")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_vpn_gateway(self) -> typing.Optional[builtins.bool]:
        '''Should be true if you want to create a new VPN Gateway resource and attach it to the VPC.'''
        result = self._values.get("enable_vpn_gateway")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def external_nat_ip_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of EIP IDs to be assigned to the NAT Gateways (used in combination with reuse_nat_ips).'''
        result = self._values.get("external_nat_ip_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def external_nat_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of EIPs to be used for ``nat_public_ips`` output (used in combination with reuse_nat_ips and external_nat_ip_ids).'''
        result = self._values.get("external_nat_ips")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def flow_log_cloudwatch_iam_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN for the IAM role that's used to post flow logs to a CloudWatch Logs log group.

        When flow_log_destination_arn is set to ARN of Cloudwatch Logs, this argument needs to be provided
        '''
        result = self._values.get("flow_log_cloudwatch_iam_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flow_log_cloudwatch_iam_role_conditions(self) -> typing.Any:
        '''Additional conditions of the CloudWatch role assumption policy.'''
        result = self._values.get("flow_log_cloudwatch_iam_role_conditions")
        return typing.cast(typing.Any, result)

    @builtins.property
    def flow_log_cloudwatch_log_group_class(self) -> typing.Optional[builtins.str]:
        '''Specified the log class of the log group.

        Possible values are: STANDARD or INFREQUENT_ACCESS
        '''
        result = self._values.get("flow_log_cloudwatch_log_group_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flow_log_cloudwatch_log_group_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ARN of the KMS Key to use when encrypting log data for VPC flow logs.'''
        result = self._values.get("flow_log_cloudwatch_log_group_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flow_log_cloudwatch_log_group_name_prefix(
        self,
    ) -> typing.Optional[builtins.str]:
        '''Specifies the name prefix of CloudWatch Log Group for VPC flow logs /aws/vpc-flow-log/.'''
        result = self._values.get("flow_log_cloudwatch_log_group_name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flow_log_cloudwatch_log_group_name_suffix(
        self,
    ) -> typing.Optional[builtins.str]:
        '''Specifies the name suffix of CloudWatch Log Group for VPC flow logs.'''
        result = self._values.get("flow_log_cloudwatch_log_group_name_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flow_log_cloudwatch_log_group_retention_in_days(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Specifies the number of days you want to retain log events in the specified log group for VPC flow logs.'''
        result = self._values.get("flow_log_cloudwatch_log_group_retention_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def flow_log_cloudwatch_log_group_skip_destroy(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Set to true if you do not wish the log group (and any logs it may contain) to be deleted at destroy time, and instead just remove the log group from the Terraform state.'''
        result = self._values.get("flow_log_cloudwatch_log_group_skip_destroy")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def flow_log_deliver_cross_account_role(self) -> typing.Optional[builtins.str]:
        '''(Optional) ARN of the IAM role that allows Amazon EC2 to publish flow logs across accounts.'''
        result = self._values.get("flow_log_deliver_cross_account_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flow_log_destination_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the CloudWatch log group or S3 bucket where VPC Flow Logs will be pushed.

        If this ARN is a S3 bucket the appropriate permissions need to be set on that bucket's policy. When create_flow_log_cloudwatch_log_group is set to false this argument must be provided
        '''
        result = self._values.get("flow_log_destination_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flow_log_destination_type(self) -> typing.Optional[builtins.str]:
        '''Type of flow log destination.

        Can be s3, kinesis-data-firehose or cloud-watch-logs
        cloud-watch-logs
        '''
        result = self._values.get("flow_log_destination_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flow_log_file_format(self) -> typing.Optional[builtins.str]:
        '''(Optional) The format for the flow log.

        Valid values: ``plain-text``, ``parquet``
        '''
        result = self._values.get("flow_log_file_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flow_log_hive_compatible_partitions(self) -> typing.Optional[builtins.bool]:
        '''(Optional) Indicates whether to use Hive-compatible prefixes for flow logs stored in Amazon S3.'''
        result = self._values.get("flow_log_hive_compatible_partitions")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def flow_log_log_format(self) -> typing.Optional[builtins.str]:
        '''The fields to include in the flow log record, in the order in which they should appear.'''
        result = self._values.get("flow_log_log_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flow_log_max_aggregation_interval(self) -> typing.Optional[jsii.Number]:
        '''The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record.

        Valid Values: ``60`` seconds or ``600`` seconds
        600
        '''
        result = self._values.get("flow_log_max_aggregation_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def flow_log_per_hour_partition(self) -> typing.Optional[builtins.bool]:
        '''(Optional) Indicates whether to partition the flow log per hour.

        This reduces the cost and response time for queries
        '''
        result = self._values.get("flow_log_per_hour_partition")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def flow_log_traffic_type(self) -> typing.Optional[builtins.str]:
        '''The type of traffic to capture.

        Valid values: ACCEPT, REJECT, ALL
        ALL
        '''
        result = self._values.get("flow_log_traffic_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def igw_tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the internet gateway The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("igw_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def instance_tenancy(self) -> typing.Optional[builtins.str]:
        '''A tenancy option for instances launched into the VPC default.'''
        result = self._values.get("instance_tenancy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def intra_acl_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the intra subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("intra_acl_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def intra_dedicated_network_acl(self) -> typing.Optional[builtins.bool]:
        '''Whether to use dedicated network ACL (not default) and custom rules for intra subnets.'''
        result = self._values.get("intra_dedicated_network_acl")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def intra_inbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''Intra subnets inbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("intra_inbound_acl_rules")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def intra_outbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''Intra subnets outbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("intra_outbound_acl_rules")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def intra_route_table_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the intra route tables The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("intra_route_table_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def intra_subnet_assign_ipv6_address_on_creation(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address.

        Default is ``false``
        '''
        result = self._values.get("intra_subnet_assign_ipv6_address_on_creation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def intra_subnet_enable_dns64(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations.

        Default: ``true``
        true
        '''
        result = self._values.get("intra_subnet_enable_dns64")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def intra_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.

        Default: ``true``
        true
        '''
        result = self._values.get("intra_subnet_enable_resource_name_dns_aaaa_record_on_launch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def intra_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Indicates whether to respond to DNS queries for instance hostnames with DNS A records.

        Default: ``false``
        '''
        result = self._values.get("intra_subnet_enable_resource_name_dns_a_record_on_launch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def intra_subnet_ipv6_native(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether to create an IPv6-only subnet.

        Default: ``false``
        '''
        result = self._values.get("intra_subnet_ipv6_native")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def intra_subnet_ipv6_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Assigns IPv6 intra subnet id based on the Amazon provided /56 prefix base 10 integer (0-256).

        Must be of equal length to the corresponding IPv4 subnet list
        '''
        result = self._values.get("intra_subnet_ipv6_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def intra_subnet_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Explicit values to use in the Name tag on intra subnets.

        If empty, Name tags are generated
        '''
        result = self._values.get("intra_subnet_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def intra_subnet_private_dns_hostname_type_on_launch(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The type of hostnames to assign to instances in the subnet at launch.

        For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        '''
        result = self._values.get("intra_subnet_private_dns_hostname_type_on_launch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def intra_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of intra subnets inside the VPC.'''
        result = self._values.get("intra_subnets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def intra_subnet_suffix(self) -> typing.Optional[builtins.str]:
        '''Suffix to append to intra subnets name intra.'''
        result = self._values.get("intra_subnet_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def intra_subnet_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the intra subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("intra_subnet_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def ipv4_ipam_pool_id(self) -> typing.Optional[builtins.str]:
        '''(Optional) The ID of an IPv4 IPAM pool you want to use for allocating this VPC's CIDR.'''
        result = self._values.get("ipv4_ipam_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv4_netmask_length(self) -> typing.Optional[jsii.Number]:
        '''(Optional) The netmask length of the IPv4 CIDR you want to allocate to this VPC.

        Requires specifying a ipv4_ipam_pool_id
        '''
        result = self._values.get("ipv4_netmask_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ipv6_cidr(self) -> typing.Optional[builtins.str]:
        '''(Optional) IPv6 CIDR block to request from an IPAM Pool.

        Can be set explicitly or derived from IPAM using ``ipv6_netmask_length``
        '''
        result = self._values.get("ipv6_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv6_cidr_block_network_border_group(self) -> typing.Optional[builtins.str]:
        '''By default when an IPv6 CIDR is assigned to a VPC a default ipv6_cidr_block_network_border_group will be set to the region of the VPC.

        This can be changed to restrict advertisement of public addresses to specific Network Border Groups such as LocalZones
        '''
        result = self._values.get("ipv6_cidr_block_network_border_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv6_ipam_pool_id(self) -> typing.Optional[builtins.str]:
        '''(Optional) IPAM Pool ID for a IPv6 pool.

        Conflicts with ``assign_generated_ipv6_cidr_block``
        '''
        result = self._values.get("ipv6_ipam_pool_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv6_netmask_length(self) -> typing.Optional[jsii.Number]:
        '''(Optional) Netmask length to request from IPAM Pool.

        Conflicts with ``ipv6_cidr_block``. This can be omitted if IPAM pool as a ``allocation_default_netmask_length`` set. Valid values: ``56``
        '''
        result = self._values.get("ipv6_netmask_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def manage_default_network_acl(self) -> typing.Optional[builtins.bool]:
        '''Should be true to adopt and manage Default Network ACL true.'''
        result = self._values.get("manage_default_network_acl")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def manage_default_route_table(self) -> typing.Optional[builtins.bool]:
        '''Should be true to manage default route table true.'''
        result = self._values.get("manage_default_route_table")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def manage_default_security_group(self) -> typing.Optional[builtins.bool]:
        '''Should be true to adopt and manage default security group true.'''
        result = self._values.get("manage_default_security_group")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def manage_default_vpc(self) -> typing.Optional[builtins.bool]:
        '''Should be true to adopt and manage Default VPC.'''
        result = self._values.get("manage_default_vpc")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def map_customer_owned_ip_on_launch(self) -> typing.Optional[builtins.bool]:
        '''Specify true to indicate that network interfaces created in the subnet should be assigned a customer owned IP address.

        The ``customer_owned_ipv4_pool`` and ``outpost_arn`` arguments must be specified when set to ``true``. Default is ``false``
        '''
        result = self._values.get("map_customer_owned_ip_on_launch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def map_public_ip_on_launch(self) -> typing.Optional[builtins.bool]:
        '''Specify true to indicate that instances launched into the subnet should be assigned a public IP address.

        Default is ``false``
        '''
        result = self._values.get("map_public_ip_on_launch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name to be used on all the resources as identifier.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nat_eip_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the NAT EIP The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("nat_eip_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def nat_gateway_destination_cidr_block(self) -> typing.Optional[builtins.str]:
        '''Used to pass a custom destination route for private NAT Gateway.

        If not specified, the default 0.0.0.0/0 is used as a destination route
        0.0.0.0/0
        '''
        result = self._values.get("nat_gateway_destination_cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nat_gateway_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the NAT gateways The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("nat_gateway_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def one_nat_gateway_per_az(self) -> typing.Optional[builtins.bool]:
        '''Should be true if you want only one NAT Gateway per availability zone.

        Requires ``var.azs`` to be set, and the number of ``public_subnets`` created to be greater than or equal to the number of availability zones specified in ``var.azs``
        '''
        result = self._values.get("one_nat_gateway_per_az")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def outpost_acl_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the outpost subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("outpost_acl_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def outpost_arn(self) -> typing.Optional[builtins.str]:
        '''ARN of Outpost you want to create a subnet in.'''
        result = self._values.get("outpost_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def outpost_az(self) -> typing.Optional[builtins.str]:
        '''AZ where Outpost is anchored.'''
        result = self._values.get("outpost_az")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def outpost_dedicated_network_acl(self) -> typing.Optional[builtins.bool]:
        '''Whether to use dedicated network ACL (not default) and custom rules for outpost subnets.'''
        result = self._values.get("outpost_dedicated_network_acl")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def outpost_inbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''Outpost subnets inbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("outpost_inbound_acl_rules")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def outpost_outbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''Outpost subnets outbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("outpost_outbound_acl_rules")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def outpost_subnet_assign_ipv6_address_on_creation(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address.

        Default is ``false``
        '''
        result = self._values.get("outpost_subnet_assign_ipv6_address_on_creation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def outpost_subnet_enable_dns64(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations.

        Default: ``true``
        true
        '''
        result = self._values.get("outpost_subnet_enable_dns64")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.

        Default: ``true``
        true
        '''
        result = self._values.get("outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def outpost_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Indicates whether to respond to DNS queries for instance hostnames with DNS A records.

        Default: ``false``
        '''
        result = self._values.get("outpost_subnet_enable_resource_name_dns_a_record_on_launch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def outpost_subnet_ipv6_native(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether to create an IPv6-only subnet.

        Default: ``false``
        '''
        result = self._values.get("outpost_subnet_ipv6_native")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def outpost_subnet_ipv6_prefixes(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Assigns IPv6 outpost subnet id based on the Amazon provided /56 prefix base 10 integer (0-256).

        Must be of equal length to the corresponding IPv4 subnet list
        '''
        result = self._values.get("outpost_subnet_ipv6_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def outpost_subnet_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Explicit values to use in the Name tag on outpost subnets.

        If empty, Name tags are generated
        '''
        result = self._values.get("outpost_subnet_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def outpost_subnet_private_dns_hostname_type_on_launch(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The type of hostnames to assign to instances in the subnet at launch.

        For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        '''
        result = self._values.get("outpost_subnet_private_dns_hostname_type_on_launch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def outpost_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of outpost subnets inside the VPC.'''
        result = self._values.get("outpost_subnets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def outpost_subnet_suffix(self) -> typing.Optional[builtins.str]:
        '''Suffix to append to outpost subnets name outpost.'''
        result = self._values.get("outpost_subnet_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def outpost_subnet_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the outpost subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("outpost_subnet_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def private_acl_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the private subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("private_acl_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def private_dedicated_network_acl(self) -> typing.Optional[builtins.bool]:
        '''Whether to use dedicated network ACL (not default) and custom rules for private subnets.'''
        result = self._values.get("private_dedicated_network_acl")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def private_inbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''Private subnets inbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("private_inbound_acl_rules")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def private_outbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''Private subnets outbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("private_outbound_acl_rules")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def private_route_table_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the private route tables The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("private_route_table_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def private_subnet_assign_ipv6_address_on_creation(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address.

        Default is ``false``
        '''
        result = self._values.get("private_subnet_assign_ipv6_address_on_creation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def private_subnet_enable_dns64(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations.

        Default: ``true``
        true
        '''
        result = self._values.get("private_subnet_enable_dns64")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def private_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.

        Default: ``true``
        true
        '''
        result = self._values.get("private_subnet_enable_resource_name_dns_aaaa_record_on_launch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def private_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Indicates whether to respond to DNS queries for instance hostnames with DNS A records.

        Default: ``false``
        '''
        result = self._values.get("private_subnet_enable_resource_name_dns_a_record_on_launch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def private_subnet_ipv6_native(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether to create an IPv6-only subnet.

        Default: ``false``
        '''
        result = self._values.get("private_subnet_ipv6_native")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def private_subnet_ipv6_prefixes(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Assigns IPv6 private subnet id based on the Amazon provided /56 prefix base 10 integer (0-256).

        Must be of equal length to the corresponding IPv4 subnet list
        '''
        result = self._values.get("private_subnet_ipv6_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def private_subnet_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Explicit values to use in the Name tag on private subnets.

        If empty, Name tags are generated
        '''
        result = self._values.get("private_subnet_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def private_subnet_private_dns_hostname_type_on_launch(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The type of hostnames to assign to instances in the subnet at launch.

        For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        '''
        result = self._values.get("private_subnet_private_dns_hostname_type_on_launch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of private subnets inside the VPC.'''
        result = self._values.get("private_subnets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def private_subnet_suffix(self) -> typing.Optional[builtins.str]:
        '''Suffix to append to private subnets name private.'''
        result = self._values.get("private_subnet_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_subnet_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the private subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("private_subnet_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def private_subnet_tags_per_az(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]]:
        '''Additional tags for the private subnets where the primary key is the AZ The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("private_subnet_tags_per_az")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def propagate_intra_route_tables_vgw(self) -> typing.Optional[builtins.bool]:
        '''Should be true if you want route table propagation.'''
        result = self._values.get("propagate_intra_route_tables_vgw")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def propagate_private_route_tables_vgw(self) -> typing.Optional[builtins.bool]:
        '''Should be true if you want route table propagation.'''
        result = self._values.get("propagate_private_route_tables_vgw")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def propagate_public_route_tables_vgw(self) -> typing.Optional[builtins.bool]:
        '''Should be true if you want route table propagation.'''
        result = self._values.get("propagate_public_route_tables_vgw")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def public_acl_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the public subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("public_acl_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def public_dedicated_network_acl(self) -> typing.Optional[builtins.bool]:
        '''Whether to use dedicated network ACL (not default) and custom rules for public subnets.'''
        result = self._values.get("public_dedicated_network_acl")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def public_inbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''Public subnets inbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("public_inbound_acl_rules")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def public_outbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''Public subnets outbound network ACLs [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("public_outbound_acl_rules")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def public_route_table_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the public route tables The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("public_route_table_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def public_subnet_assign_ipv6_address_on_creation(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address.

        Default is ``false``
        '''
        result = self._values.get("public_subnet_assign_ipv6_address_on_creation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def public_subnet_enable_dns64(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations.

        Default: ``true``
        true
        '''
        result = self._values.get("public_subnet_enable_dns64")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def public_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.

        Default: ``true``
        true
        '''
        result = self._values.get("public_subnet_enable_resource_name_dns_aaaa_record_on_launch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def public_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Indicates whether to respond to DNS queries for instance hostnames with DNS A records.

        Default: ``false``
        '''
        result = self._values.get("public_subnet_enable_resource_name_dns_a_record_on_launch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def public_subnet_ipv6_native(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether to create an IPv6-only subnet.

        Default: ``false``
        '''
        result = self._values.get("public_subnet_ipv6_native")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def public_subnet_ipv6_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Assigns IPv6 public subnet id based on the Amazon provided /56 prefix base 10 integer (0-256).

        Must be of equal length to the corresponding IPv4 subnet list
        '''
        result = self._values.get("public_subnet_ipv6_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def public_subnet_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Explicit values to use in the Name tag on public subnets.

        If empty, Name tags are generated
        '''
        result = self._values.get("public_subnet_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def public_subnet_private_dns_hostname_type_on_launch(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The type of hostnames to assign to instances in the subnet at launch.

        For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        '''
        result = self._values.get("public_subnet_private_dns_hostname_type_on_launch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of public subnets inside the VPC.'''
        result = self._values.get("public_subnets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def public_subnet_suffix(self) -> typing.Optional[builtins.str]:
        '''Suffix to append to public subnets name public.'''
        result = self._values.get("public_subnet_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_subnet_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the public subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("public_subnet_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def public_subnet_tags_per_az(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]]:
        '''Additional tags for the public subnets where the primary key is the AZ The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("public_subnet_tags_per_az")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def putin_khuylo(self) -> typing.Optional[builtins.bool]:
        '''Do you agree that Putin doesn't respect Ukrainian sovereignty and territorial integrity?

        More info: https://en.wikipedia.org/wiki/Putin_khuylo!
        true
        '''
        result = self._values.get("putin_khuylo")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def redshift_acl_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the redshift subnets network ACL The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("redshift_acl_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def redshift_dedicated_network_acl(self) -> typing.Optional[builtins.bool]:
        '''Whether to use dedicated network ACL (not default) and custom rules for redshift subnets.'''
        result = self._values.get("redshift_dedicated_network_acl")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def redshift_inbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''Redshift subnets inbound network ACL rules [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("redshift_inbound_acl_rules")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def redshift_outbound_acl_rules(
        self,
    ) -> typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        '''Redshift subnets outbound network ACL rules [object Object] The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("redshift_outbound_acl_rules")
        return typing.cast(typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def redshift_route_table_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the redshift route tables The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("redshift_route_table_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def redshift_subnet_assign_ipv6_address_on_creation(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Specify true to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address.

        Default is ``false``
        '''
        result = self._values.get("redshift_subnet_assign_ipv6_address_on_creation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def redshift_subnet_enable_dns64(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations.

        Default: ``true``
        true
        '''
        result = self._values.get("redshift_subnet_enable_dns64")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.

        Default: ``true``
        true
        '''
        result = self._values.get("redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def redshift_subnet_enable_resource_name_dns_a_record_on_launch(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Indicates whether to respond to DNS queries for instance hostnames with DNS A records.

        Default: ``false``
        '''
        result = self._values.get("redshift_subnet_enable_resource_name_dns_a_record_on_launch")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def redshift_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''Name of redshift subnet group.'''
        result = self._values.get("redshift_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redshift_subnet_group_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the redshift subnet group The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("redshift_subnet_group_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def redshift_subnet_ipv6_native(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether to create an IPv6-only subnet.

        Default: ``false``
        '''
        result = self._values.get("redshift_subnet_ipv6_native")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def redshift_subnet_ipv6_prefixes(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Assigns IPv6 redshift subnet id based on the Amazon provided /56 prefix base 10 integer (0-256).

        Must be of equal length to the corresponding IPv4 subnet list
        '''
        result = self._values.get("redshift_subnet_ipv6_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def redshift_subnet_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Explicit values to use in the Name tag on redshift subnets.

        If empty, Name tags are generated
        '''
        result = self._values.get("redshift_subnet_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def redshift_subnet_private_dns_hostname_type_on_launch(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The type of hostnames to assign to instances in the subnet at launch.

        For IPv6-only subnets, an instance DNS name must be based on the instance ID. For dual-stack and IPv4-only subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID. Valid values: ``ip-name``, ``resource-name``
        '''
        result = self._values.get("redshift_subnet_private_dns_hostname_type_on_launch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redshift_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of redshift subnets inside the VPC.'''
        result = self._values.get("redshift_subnets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def redshift_subnet_suffix(self) -> typing.Optional[builtins.str]:
        '''Suffix to append to redshift subnets name redshift.'''
        result = self._values.get("redshift_subnet_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redshift_subnet_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the redshift subnets The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("redshift_subnet_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def reuse_nat_ips(self) -> typing.Optional[builtins.bool]:
        '''Should be true if you don't want EIPs to be created for your NAT Gateways and will instead pass them in via the 'external_nat_ip_ids' variable.'''
        result = self._values.get("reuse_nat_ips")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def secondary_cidr_blocks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of secondary CIDR blocks to associate with the VPC to extend the IP Address pool.'''
        result = self._values.get("secondary_cidr_blocks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def single_nat_gateway(self) -> typing.Optional[builtins.bool]:
        '''Should be true if you want to provision a single shared NAT Gateway across all of your private networks.'''
        result = self._values.get("single_nat_gateway")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of tags to add to all resources The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def use_ipam_pool(self) -> typing.Optional[builtins.bool]:
        '''Determines whether IPAM pool is used for CIDR allocation.'''
        result = self._values.get("use_ipam_pool")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def vpc_flow_log_iam_policy_name(self) -> typing.Optional[builtins.str]:
        '''Name of the IAM policy vpc-flow-log-to-cloudwatch.'''
        result = self._values.get("vpc_flow_log_iam_policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_flow_log_iam_policy_use_name_prefix(self) -> typing.Optional[builtins.bool]:
        '''Determines whether the name of the IAM policy (``vpc_flow_log_iam_policy_name``) is used as a prefix true.'''
        result = self._values.get("vpc_flow_log_iam_policy_use_name_prefix")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def vpc_flow_log_iam_role_name(self) -> typing.Optional[builtins.str]:
        '''Name to use on the VPC Flow Log IAM role created vpc-flow-log-role.'''
        result = self._values.get("vpc_flow_log_iam_role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_flow_log_iam_role_use_name_prefix(self) -> typing.Optional[builtins.bool]:
        '''Determines whether the IAM role name (``vpc_flow_log_iam_role_name_name``) is used as a prefix true.'''
        result = self._values.get("vpc_flow_log_iam_role_use_name_prefix")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def vpc_flow_log_permissions_boundary(self) -> typing.Optional[builtins.str]:
        '''The ARN of the Permissions Boundary for the VPC Flow Log IAM Role.'''
        result = self._values.get("vpc_flow_log_permissions_boundary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_flow_log_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the VPC Flow Logs The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("vpc_flow_log_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def vpc_tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the VPC The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("vpc_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def vpn_gateway_az(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone for the VPN Gateway.'''
        result = self._values.get("vpn_gateway_az")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpn_gateway_id(self) -> typing.Optional[builtins.str]:
        '''ID of VPN Gateway to attach to the VPC.'''
        result = self._values.get("vpn_gateway_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpn_gateway_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional tags for the VPN gateway The property type contains a map, they have special handling, please see {@link cdk.tf /module-map-inputs the docs}.'''
        result = self._values.get("vpn_gateway_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Vpc",
    "VpcConfig",
]

publication.publish()

def _typecheckingstub__36262b54abea07d1a172b2d0b5222f418075eb67faf564af87b2e528b06d12f6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    amazon_side_asn: typing.Optional[builtins.str] = None,
    azs: typing.Optional[typing.Sequence[builtins.str]] = None,
    cidr: typing.Optional[builtins.str] = None,
    create_database_internet_gateway_route: typing.Optional[builtins.bool] = None,
    create_database_nat_gateway_route: typing.Optional[builtins.bool] = None,
    create_database_subnet_group: typing.Optional[builtins.bool] = None,
    create_database_subnet_route_table: typing.Optional[builtins.bool] = None,
    create_egress_only_igw: typing.Optional[builtins.bool] = None,
    create_elasticache_subnet_group: typing.Optional[builtins.bool] = None,
    create_elasticache_subnet_route_table: typing.Optional[builtins.bool] = None,
    create_flow_log_cloudwatch_iam_role: typing.Optional[builtins.bool] = None,
    create_flow_log_cloudwatch_log_group: typing.Optional[builtins.bool] = None,
    create_igw: typing.Optional[builtins.bool] = None,
    create_multiple_intra_route_tables: typing.Optional[builtins.bool] = None,
    create_multiple_public_route_tables: typing.Optional[builtins.bool] = None,
    create_private_nat_gateway_route: typing.Optional[builtins.bool] = None,
    create_redshift_subnet_group: typing.Optional[builtins.bool] = None,
    create_redshift_subnet_route_table: typing.Optional[builtins.bool] = None,
    create_vpc: typing.Optional[builtins.bool] = None,
    customer_gateways: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]] = None,
    customer_gateway_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    customer_owned_ipv4_pool: typing.Optional[builtins.str] = None,
    database_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    database_dedicated_network_acl: typing.Optional[builtins.bool] = None,
    database_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    database_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    database_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    database_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
    database_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
    database_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
    database_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
    database_subnet_group_name: typing.Optional[builtins.str] = None,
    database_subnet_group_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    database_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
    database_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    database_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    database_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
    database_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    database_subnet_suffix: typing.Optional[builtins.str] = None,
    database_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    default_network_acl_egress: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    default_network_acl_ingress: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    default_network_acl_name: typing.Optional[builtins.str] = None,
    default_network_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    default_route_table_name: typing.Optional[builtins.str] = None,
    default_route_table_propagating_vgws: typing.Optional[typing.Sequence[builtins.str]] = None,
    default_route_table_routes: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    default_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    default_security_group_egress: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    default_security_group_ingress: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    default_security_group_name: typing.Optional[builtins.str] = None,
    default_security_group_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    default_vpc_enable_dns_hostnames: typing.Optional[builtins.bool] = None,
    default_vpc_enable_dns_support: typing.Optional[builtins.bool] = None,
    default_vpc_name: typing.Optional[builtins.str] = None,
    default_vpc_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    dhcp_options_domain_name: typing.Optional[builtins.str] = None,
    dhcp_options_domain_name_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    dhcp_options_ipv6_address_preferred_lease_time: typing.Optional[jsii.Number] = None,
    dhcp_options_netbios_name_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    dhcp_options_netbios_node_type: typing.Optional[builtins.str] = None,
    dhcp_options_ntp_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    dhcp_options_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    elasticache_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    elasticache_dedicated_network_acl: typing.Optional[builtins.bool] = None,
    elasticache_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    elasticache_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    elasticache_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    elasticache_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
    elasticache_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
    elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
    elasticache_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
    elasticache_subnet_group_name: typing.Optional[builtins.str] = None,
    elasticache_subnet_group_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    elasticache_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
    elasticache_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    elasticache_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    elasticache_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
    elasticache_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    elasticache_subnet_suffix: typing.Optional[builtins.str] = None,
    elasticache_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    enable_dhcp_options: typing.Optional[builtins.bool] = None,
    enable_dns_hostnames: typing.Optional[builtins.bool] = None,
    enable_dns_support: typing.Optional[builtins.bool] = None,
    enable_flow_log: typing.Optional[builtins.bool] = None,
    enable_ipv6: typing.Optional[builtins.bool] = None,
    enable_nat_gateway: typing.Optional[builtins.bool] = None,
    enable_network_address_usage_metrics: typing.Optional[builtins.bool] = None,
    enable_public_redshift: typing.Optional[builtins.bool] = None,
    enable_vpn_gateway: typing.Optional[builtins.bool] = None,
    external_nat_ip_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    external_nat_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
    flow_log_cloudwatch_iam_role_arn: typing.Optional[builtins.str] = None,
    flow_log_cloudwatch_iam_role_conditions: typing.Any = None,
    flow_log_cloudwatch_log_group_class: typing.Optional[builtins.str] = None,
    flow_log_cloudwatch_log_group_kms_key_id: typing.Optional[builtins.str] = None,
    flow_log_cloudwatch_log_group_name_prefix: typing.Optional[builtins.str] = None,
    flow_log_cloudwatch_log_group_name_suffix: typing.Optional[builtins.str] = None,
    flow_log_cloudwatch_log_group_retention_in_days: typing.Optional[jsii.Number] = None,
    flow_log_cloudwatch_log_group_skip_destroy: typing.Optional[builtins.bool] = None,
    flow_log_deliver_cross_account_role: typing.Optional[builtins.str] = None,
    flow_log_destination_arn: typing.Optional[builtins.str] = None,
    flow_log_destination_type: typing.Optional[builtins.str] = None,
    flow_log_file_format: typing.Optional[builtins.str] = None,
    flow_log_hive_compatible_partitions: typing.Optional[builtins.bool] = None,
    flow_log_log_format: typing.Optional[builtins.str] = None,
    flow_log_max_aggregation_interval: typing.Optional[jsii.Number] = None,
    flow_log_per_hour_partition: typing.Optional[builtins.bool] = None,
    flow_log_traffic_type: typing.Optional[builtins.str] = None,
    igw_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    instance_tenancy: typing.Optional[builtins.str] = None,
    intra_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    intra_dedicated_network_acl: typing.Optional[builtins.bool] = None,
    intra_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    intra_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    intra_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    intra_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
    intra_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
    intra_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
    intra_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
    intra_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
    intra_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    intra_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    intra_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
    intra_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    intra_subnet_suffix: typing.Optional[builtins.str] = None,
    intra_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ipv4_ipam_pool_id: typing.Optional[builtins.str] = None,
    ipv4_netmask_length: typing.Optional[jsii.Number] = None,
    ipv6_cidr: typing.Optional[builtins.str] = None,
    ipv6_cidr_block_network_border_group: typing.Optional[builtins.str] = None,
    ipv6_ipam_pool_id: typing.Optional[builtins.str] = None,
    ipv6_netmask_length: typing.Optional[jsii.Number] = None,
    manage_default_network_acl: typing.Optional[builtins.bool] = None,
    manage_default_route_table: typing.Optional[builtins.bool] = None,
    manage_default_security_group: typing.Optional[builtins.bool] = None,
    manage_default_vpc: typing.Optional[builtins.bool] = None,
    map_customer_owned_ip_on_launch: typing.Optional[builtins.bool] = None,
    map_public_ip_on_launch: typing.Optional[builtins.bool] = None,
    name: typing.Optional[builtins.str] = None,
    nat_eip_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    nat_gateway_destination_cidr_block: typing.Optional[builtins.str] = None,
    nat_gateway_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    one_nat_gateway_per_az: typing.Optional[builtins.bool] = None,
    outpost_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    outpost_arn: typing.Optional[builtins.str] = None,
    outpost_az: typing.Optional[builtins.str] = None,
    outpost_dedicated_network_acl: typing.Optional[builtins.bool] = None,
    outpost_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    outpost_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    outpost_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
    outpost_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
    outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
    outpost_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
    outpost_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
    outpost_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    outpost_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    outpost_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
    outpost_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    outpost_subnet_suffix: typing.Optional[builtins.str] = None,
    outpost_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    private_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    private_dedicated_network_acl: typing.Optional[builtins.bool] = None,
    private_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    private_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    private_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    private_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
    private_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
    private_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
    private_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
    private_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
    private_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    private_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    private_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
    private_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    private_subnet_suffix: typing.Optional[builtins.str] = None,
    private_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    private_subnet_tags_per_az: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]] = None,
    propagate_intra_route_tables_vgw: typing.Optional[builtins.bool] = None,
    propagate_private_route_tables_vgw: typing.Optional[builtins.bool] = None,
    propagate_public_route_tables_vgw: typing.Optional[builtins.bool] = None,
    public_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    public_dedicated_network_acl: typing.Optional[builtins.bool] = None,
    public_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    public_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    public_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    public_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
    public_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
    public_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
    public_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
    public_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
    public_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    public_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    public_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
    public_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    public_subnet_suffix: typing.Optional[builtins.str] = None,
    public_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    public_subnet_tags_per_az: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]] = None,
    putin_khuylo: typing.Optional[builtins.bool] = None,
    redshift_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    redshift_dedicated_network_acl: typing.Optional[builtins.bool] = None,
    redshift_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    redshift_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    redshift_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    redshift_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
    redshift_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
    redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
    redshift_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
    redshift_subnet_group_name: typing.Optional[builtins.str] = None,
    redshift_subnet_group_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    redshift_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
    redshift_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    redshift_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    redshift_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
    redshift_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    redshift_subnet_suffix: typing.Optional[builtins.str] = None,
    redshift_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    reuse_nat_ips: typing.Optional[builtins.bool] = None,
    secondary_cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
    single_nat_gateway: typing.Optional[builtins.bool] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    use_ipam_pool: typing.Optional[builtins.bool] = None,
    vpc_flow_log_iam_policy_name: typing.Optional[builtins.str] = None,
    vpc_flow_log_iam_policy_use_name_prefix: typing.Optional[builtins.bool] = None,
    vpc_flow_log_iam_role_name: typing.Optional[builtins.str] = None,
    vpc_flow_log_iam_role_use_name_prefix: typing.Optional[builtins.bool] = None,
    vpc_flow_log_permissions_boundary: typing.Optional[builtins.str] = None,
    vpc_flow_log_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpn_gateway_az: typing.Optional[builtins.str] = None,
    vpn_gateway_id: typing.Optional[builtins.str] = None,
    vpn_gateway_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    providers: typing.Optional[typing.Sequence[typing.Union[_cdktf_9a9027ec.TerraformProvider, typing.Union[_cdktf_9a9027ec.TerraformModuleProvider, typing.Dict[builtins.str, typing.Any]]]]] = None,
    skip_asset_creation_from_local_modules: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae06cc41c20a8a916caa0287df54236f750c9dd0f5cfa878410891a04f755a05(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87abacfa96c4aa862e0af0807f43d0af419b01b99186ecfc0bcfa59477f93cb3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e2f495405a0dfbca127193223a62470e5ced83ae0ed118e506ef7723d276a79(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c06b3be1058a1602c68d3854df2bf2a4a0ac4249e0e7c7ec270ad412072a8d01(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da1bb13d5246d0a681f95aa6d3c4de26a8df28c62e8d8100c8c9dd8f760f13f8(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1ce43dfa4d0386089b4591843ae91303b528194e4612f41396c5d69fb3a72bf(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d945c595c24421daac63bdd224660b83d3db2dd3a365542ba60ff23b9815b615(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c23dacff4e057dcc8dfdaf5d68f50ad6a4396016c0ef0204b1ddc8b42e5bc45a(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d78922c3d9caef7315a2fc39764449518097347e2a80192b6cba58aa3fdcdc8f(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1110b4a1f56723b4d7b37c703672433202ce050d26ff6ce6d3a0fe650c6f8959(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b914fdb4c5835989461b5b9e47dbc56ca5b4378be8ca0965c2edaa4de5221dd0(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea1120216b43e76d68af5f9ea72c604125ff9272a4a933fd1a482cd8b7679488(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c319b409ba9ac51eb004582f53d89791090ccef99c160023e27deda6b01addd4(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c78dfd8a1d60795ba10f0b3b02d1cc5bbb82cec4565186e383c936e846c65ae(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b164c865c4a86bf9b129b22b262498061e8549e4527869f027a36cf5d9c41c1(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0eebb7b3e273f39be5a181e8b5b651d33d47ad60f84a2b38310381ec9e6cf67(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77f47ab0919ee1fcfe7b53e0ea67b7d0c3edf272cfc870443e2a6470754186a8(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac52b5ed0e1526d04be7646207ad3b9b31dc2952620551b14943782a8916dfa2(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9237251b6f833d6281d46faf77c258974cdf1c3597c9a1944df1dfd7028732f9(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe856a2a13ffa2d263770a0b1c80bf7fc65180048f6c0347ad53233f2c36881b(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__521fd2a8ce188fb97d944d84051ea1e29ffd067d9ea6aa054f3bfc0d3da82e91(
    value: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86910c4f58dbb08affe58cf5e0f21ed758c35bf22ea3e91cb1965c3c7590b3f0(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bac2ebd2b4a07d60e8608b00549b8829d553a276d3ba4664e845709c062baeac(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee401942eb0271cc09188ef90a6719d73f039ebdbb3ef68e7402c50f7ecb2b5a(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5de9c55ff98f13c69675cffc0287e12837d1d92255ced7d31f2b83c44eaf5fe(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96e90d2fc9319bcf753f574c2ba2aafe4d6bc5d02fdbcf3ff62120f338c59fbb(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5a73730a00a7454ea550f9f0ab3fbbdf26ae3d9c541f27ccfd66863dd25da47(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37acb140df1645df3aff86f4da3c84c92c128043169d0bb2ad276c2a01b4b467(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d4ec089a8faeac43b21fea2d3e96ce540cd7cca6eb465e665282c2f323d6f94(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27763505611da95756e2d11d8c35a7ceca1f4abb67be85b7011683f1b4ba5706(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__612c0cf4d6a765eac51e7a27d4bf33b96c2c6be6df9fdbeaf99aaee69f02cd26(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c51c4f56bd4719de6f2d668b6b2ace04c2bca2d17530e34f81e2d4c57f410262(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28872e66b537b08e5df30c50b8cebf4d5714d55869dc9720001ab1cdfc881c2b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf1e7e5768b461793608f491e5e63422deaa208a4294bac2b2d3b79a0cc4d4a7(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73a91fb885ef0490541564f2b596e5cc7125f26448b6c4b4c3926c66dd4706a0(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c359b66a722f63249cf2299b8ed96948c47dc508436319dc87c8c0a6613e595(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23e8a05eafaf88daca57efb19df41ab7e3ccf69dd7122ed66565b0ee6f71eaa7(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15463b37b248b7ace797cee03eb261bb39bb7c8aa2a2e28a41a0374b909b0f17(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53754c9631e7c5451e930116e87dde462b2bdd0f2348e4e72d4bbc54fdc4757c(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c824ee67926e3b4f25fab420a3e5965739dc75a1dbd93e227b7c25447f2f9366(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91b81620289eac4a13d49d0b3af9f7ab0b500cbfadd0cb85e483d7d5c81a03b3(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84830ee36db4ca5831ebdab20d40aeb873c45cd2a2eaedd5e34a0645ae1def6f(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3efd1667240bc49479a35c0f125ae0fcf5f2b6e9f4a6f297d4410403abe20e2f(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7929871bb07dcf48690b87e9669466d2489187ce8c6bd537ce912b35cc95105b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6815250bb2c26213cda0331305f1966aa324d5afc6f861c45aa3f7634e30ef8c(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__166adf41c5f81fb827c8a71db409d1b794a6836a85091e56ea519cbee9eed82e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bdcedc90e5eaade2c30236b2e3554f6302d70a4fa72ec7f4ccd6f0a952f7f82(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e56df3abf02b322d5494cd0e701711b68e4f8b28fa1f94dea43dad2557dd3071(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06818ee1a6926988e93be6639b9a2de6f4cb84f21d41290bdb0b701a5b05848b(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__269ba4f9870c727965b55da3a02358647be26b96dda0e6108c85aee6ddd65c67(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2684eaeaddb48b873e168ee392c1001fa6867ea08621dc5380ebb1527bc1bd07(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3a59cb5797781be39253509763d36750c27051fba87328e799fa36301ccbc5a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a8943fda4606e43559390b829fd29c0695dd0764e95b10686629d021a7dcaf8(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a76dcd56ccd733200d31a979ac62574a596b9feea98750279f1cc4f2df269910(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d353552fc482365754a527abbd647ab1c881cc2e8373fe080972526b06f80675(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf714407292fd99b3fec70a222bf1a7cc508b3abf42f53606cebb14b868fb5cb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87e7a314ab8ff3accc52fc790cd42b1c91eebad52c2cfb7c94c355dd03071fba(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d66c965d027e62b92b2b7347021551b92e365cea89da4883444bef43652f5830(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b894210cfc93cb00a3b52c85c68e501002e87363ef9914ee28e3881cbb92830(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b4b16c46de1726d9113e3fb66c812292bf48e8f63a57298140af4a187ae946e(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87c28741ab8b06012b772ce7beae35390c075dae3f87c12a1e3df9d37ea42143(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__222b8e975b982e68934e077c55cfa398b80eca78317cb65dd80342111fc1be6b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db331367d6fcfb0643d1f50052ad4501c13900f0b9ec51600a465c801eff370b(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc4c2dc5e0257d35f5fb2d108364a6552670d830d1aaa850fe60276fb0fa5c75(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b841c8882422262e76ef370bc628f9f9a6944e3c8533f04f972bb00511e5dd55(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38261699df6d98c41f63eeeebb86d2eaafdb1caa0afbf0cb978b6c7fed53929b(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__001d7b6387d3d94de25a766982829563e7c3d2a32b9b71ed448bd0ce3aa7afce(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d9c4d49f2c4357266b5cbd4bb6dc599e4ea0468dbbe6b29e2a7456a390bfd19(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__313e463ac61d17bbe9597d724df4e611706fed132ac741e91d09c26710a92ffe(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__310084674dbbbf4f20266183d2456520d913e137d7dbdb3381139d9defc22406(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__557128c6507c8a9441bf64961adbae8b3668e3c9ed9cbbbf0e98811bdd6250c1(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50143c31efe280ed61aa36c65ea0127a57184b3de87d1216ea8e0dab8a9c0c24(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__076b1a6e619efe2fc70ccfa58176e77bfe71683a8c01cef7085f7c873aeefac0(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ecd53a5e24620ff355086bd9ac6042cc40ac3caec3364eb3fc8839043341fc3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bafd78eca4790b998bede502b2bebc40c329a0c8b0d6134c72ba77f1c9381f58(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1e274acbadf0686949124823efd7f83179eab8338f2fefcb39c6f7677298fb7(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__011618e74b6666f0d1cf92f59134de09036f70b3d8691333ccf813d14c77f744(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee69dcd15f6f17988e5e95618e6bd0f363e00c19f61827e99e2e2b1be22db539(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2897b0e953185529b30dd0ed8ee56c745866807ded60a9e7831e04030f06a460(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1990ebeec646acf740a0951b0ca7da096d254f8f90c42608456a202180f9dda3(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__053f122fb59f4f57721ddfafd8ab7e14d251e4d1243a6dbacbc2fce880728041(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e25175b545087947d3c43723e402a8eea585c8cf33387e6a4f53d7fe9b9640db(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ff86dbc6331a4d6a01b356e7bd5d930f9547f4c1b2594144d4e7fba6d465ee1(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d8b5d936aa07ab715de58f302359003cd3d4307282b4ba41ddd69d9663e78b2(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33bd08d06ae5ccf49b2e7585ec691fbc483ec8ca9019876f8bc30e9605a7d3f2(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__478a3458a0140f7c94fee2c8e5962e6d67941c5e0ac274a1087655fddaf3515a(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca88793b055049b39c2d0a34d167798469c5b73ddf812709c87cfbc94a9522da(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e344fc7a745511055af819bccd6e3a38b8019555fe76abdefd5243036cd15cd(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e2297569d5db042aa3f23a1adcc0b78eb38c23ea2dce4c1e98b8d9b1b6f88f9(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e207433146f67a36aedfefe76b075311ef8e0115b6873cdc468c5faf64863be0(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c80f8fb26f5b7c219057b7803f9eb03666eeeb9f7a0adfdae29132dca261cc85(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf698b63f74810d0a2de6b4b1a75e4395735391a813a5fc38f10a0022379117b(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__796fbebaeb82847b48b21e88b01ea498a76bbc5a3e3daaca330f0afa8786a00a(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19a9e1ba46d733493db96fb0574dc59732adacf19d84d7e99a7e3fc7f9aa75a9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8075a59939cc739701ecbd09dd4516301ed7362b6e448a33bb274843efd0bba(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea9aa1e8e035162e2a12f837e3a5862f361702cd30bb8fe33a11bdf1f22e8781(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__920d1acd6786899641bbf7c6abd793c4b533dd6188442b85514dd0c59911af5d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4adc9a4b4ae1a0560531d09afd18102f98105038f059545e3ebf88262cab424(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91f9ca3784663281378f37e265c79e34dd71617dc556385e823b3acd076d12fc(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3d248a591b9c0e3ecd5f69c1d9a087530c95898ab6c5f677ae7728232751d68(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58f26752bbbd325e1ff31c97703319a97b55a19defb47daa052d20c5dbed5f61(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b223678d15ce7dbcdabd08cabe9a4de5c3a6c8bd3cba71d41a02af0ccea60ae4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45e2671cbcfa534317bf478030758af062256307d5fa0a90d2b97b773c509ee0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e93d2d61e20844650bfa663dad74b6e57ef40a7fa136bf360e0eda8f433e98d8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbbf3cfba2fda64ee21692050bf59b61740fcca7973c4ce614bfe259df6efff5(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__108a4f32dece40e78cc5f568b61347b95471e9efa6c8fbeb8f4f1c7641c6e751(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__726e6fce20fa9aa7f8ae2df1616cab4060f88d1f906ccbed6679cf486dda9ef9(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a89224b8e390c752ba27969c1e8c04bd729fa981dfad345553bfea22e2d4544(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4766349345d4311e4d7fd8eaf8a64d9e31e8838c80415dce7d088bca75d1a61a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dd3f77191587bd2ae046944d0d5bf90e66e51145e744b8f1cf17079eb85c928(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e84ca9b65d9c257980383158795874b631a0d5dad154d6a65cd2f0a4e19f191f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84edec64b32293f0d2dbd6e20d2a6864b5b46abcc2b750be3ec6fe5be9accbbc(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__398ce30a45ee4d02b2aa14fc7f2e8c80bc46980a3d9bfd82fa7c94332a1ce5e0(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3300edb1a54db6ca525f79edcc6ccafca7bd8240d9c82208e3a3b79535c2df81(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c4cbde4e3db469aac802cb3962aa5ee5994808f9fb5abd5ffc775d6d0e9fafa(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6c7569d0de94ae2933fc3c133c0ec53783ed214ad4bc0cb4458da6780e5a5c8(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af3410bacffdfebcf39a903470b70702ecbeb0c50f39d8fc36f041bc1bf15848(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1fa41975ac99ebfd84dce20b141f92d9c0a005a8791235914b6955a0851c524(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b157bf7a56aa4db9d358ea2f087119e3a4382896234ed449d6d4307a4225b73(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d4ca4c27e22bf4254260d46f235cee9350f8b20a8d2d67e0fac9f79bd4fb5aa(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b93b7204dcbcfd2a73039cc3c471571f000a94b83ec06441f0e5992dd87e083(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6597e8260dae99d1269791beef323e61c5bb6cc5353d81add7367f6665e88cd8(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a36031178f2a94c650f42652622604e05fa2a625bb89d7a89dab357fc2aae47(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__399556e5da63bd96f9444f8fb86098fd69e8eef0cc1fbb00edd2f03f1dfc3d3a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e92f2f5a50e0dea9d680cd242269319284b51843e0357412f07523df386d90c(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__041b937728f2f6e8db0eccbfa68ac8c7bbc2f7f8edf0caeec2fcc9d3c7f26ba7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ace6041e64215939faad638e29090fa5906c6f01e533aaf4e9bb97d2ad36eb7(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee34601531e9d1b19e9d39ef0e1ef1f4b6ceeaafc3c0099d1ab116d8628ecab3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3e5bc8ba989c9d913a731134d00d3404fb88ace9efadfb813236ff21574a83e(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__053af3691edcb6a33bdada50c84f58beeaead847253a9fa0d5e7875aad832d4c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baa50918760d03da3776281e0e691bcfa1ae858236a4213e49c1932beca6cdad(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aa2e706f45e55fbe0acdeb94afd9dc60981b4188c6a0dff810179bab54e0b87(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e2da995c87a6aa99c3c86fffeb256e8ce88ad830b6c9799b806f039e2a682e2(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bf7e37ca69daa7b44eeeb7114a22c3a6b1181962469de2397c5a282d6840911(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8bc8e61d034e30c455492fc81961c2ba032ebb9a804150111bc7f0c1ac2782a(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b534a6f17cba668bf20e4f1a571cb46b183091004fa167192e70b5b1755ebd4(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a6510bbc2e317a21c4cc82510fb1ec04441a9760a46fec535a7c90833a84a38(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84bf2a6779dd2572808ceb6676d77281427e0473d74f79e36aa50ed1f7e0ad82(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5b8ae6598f9ae485cc27a8e8dad462fa88a65af2ae0fcfcede3e42a054551a6(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79bdcdaf09aed8a9b2b62c6243dc6760292310d8d365b1a5b08534ce40a811f9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f993f9004736b963d696e52a01f123e3618f35acfb6a215bbc23fa86e7192670(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce5b0659fcd074b1b400b777ab73219f2efac49be7af3c9f705434ffb2de20a7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cd094b4b3d16ecea6ea693da3ccce21f89784684c5b429c1a8581e783f09e2b(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3810ab80b87bcf31490c692e42b984cf8efc6d079fb6b205533b0051534c2839(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e1aca22671fd3d735988b5627e89c7e947345cd9d3e3945632f6bb651d3034c(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2756a27f1337d672223bb9365be7e301b50d7713529d84b0a11bc5dec4d03cc9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0864a13bd398c3440fe15f16b4956f1b4de2a202d74aac6914736d05a78287bc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b241815eb3cab5d93f81ae50d317f0ceb1b4d208f440438af2c148473270d5c9(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__106e9fd31c1f82360cb56d27132625354b826f0ac0273eceb5242c76ab8a821e(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__350d31bd1bda7b56378692512ba11c75204362ef07f26d6eff74766e55d98836(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dcf7bc316dab6067ba11cf9c018057abe50cb1522795778b50cfd72e7e66c09(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1770effef7f97a65c7f920c9d7b13d7b3bb4796f87f0cd82eaed000d3d0532f(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddb652febe09952f5f7b75127ac1d7425d24b68f38111dd4fb0f7b5efd73d118(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c061ea484b7a50ee7f31fb25bb4e8d1c2374f87b5fc094638aee1d46fd469157(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__496ca4b4e63e2ca846db8b42c82fc97497f299478f8c05507c123b56653e3822(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15d0487aaf0fa26a9a17e7ff9a561301d3dc67ecac213ecc8c4500da1720ae97(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__057961e32a519377c227bb6f576215bd253e03b548d9f8a6c2c073c0748a0192(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9bead36c6a48eb8eeb69aa65bbacdfd060becda77b8bcbe95dd8bfbfa65f79f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7b32476efe98e2a0817e4e79fdf7d93c58f4cfddeb0e522409ca4747eda6361(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05086260e02edec212fc912c4030ed1745c81d9231028187d359eaa4ee5ddb91(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff2d331be5adbb3305410667d2715cc3ec363e8e7ac583c6dd6f6c945a06f4d0(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffc33b8e6048ed4e7fc6835208af109b6affb5ae9ab5c1750a31b1d8bfc088e9(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31760941123757ddc7f8632458cd731b97f19d50286aa3e0597709e226850c4a(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80131791c554aaaeef2bb300a5a006fed1e7c520e8919f85494ed30002948338(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64193c0e68f340669c92e091af6f06bfd957813a6e9f06ea909d4667383bcb78(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3256d4048ca41eff9b7cdeab34640d7c5572f1137ae46c342551e9ccdd6a60b8(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c812b00d56177f52f1deb8895ebf343be7f9f5d6ea9316c07f9c18fa6d353c19(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05e233eeaeef1a1dc41ef1b1e34aa23afdef8487d207436e191008db089cf297(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14931e29610838a69383bf280b39281c5de0a87f97163b3797e5293ff9c6700e(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fe3b27c4b11cd3cf46abceaab395d0e1738b2634ec89192e0620d22e4850c01(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__571559e8afb94db1654b131b99fc9251a23415575b06d273f0b9457436ee2f9b(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a1927c9a413bf4e94413632d36675c81407589dcfb7c14cf1528d5801f4e148(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f21caa57eba2f42058f57abc438e13a8d4488422b30bd64d119df5db89c38f02(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__600cbca1a56591036e47a444ea68d9aab8a7df016f88e0c3b5ddd75f617ac063(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__911d9f6ed5111f187a9d2630e0bc6983c84d8c95531b7eae48112ea8b87077f8(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91a705f4ab73184b6689bba963e3276199fee3e0145ade67880d950af3ae673c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a097c4e4f8025347132ddb88ddfee71472b292cd37f370a7cb8656d503b3375(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2a41ea842f3047e4d9067f16517fae49d9f594122d5848b94fc6e15eb65003b(
    value: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b5429e3718ea772d4c95a546ffd57d8efb248cb4d3db76103297cdc4e9a4383(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d091c45179fb3ed91279840894f3d0dd5bcab64b14c0c58bdfc8441a5a0f2d5(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f83e0a7fff94bac2d39081ac751cefecc432a2a157da3e7e1168ea4b94aaa32(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76990ef2189a0292944e6f98d67ed524280323ade216563800bfe46af72121ea(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df557fd9d154386f943c4fa65a2b78e4e6b81f1565ad749f05b20fab10e3d26a(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__558bac9bf9fea3261d8d15324036be768e2b927e0c2476dc76ec7a079c0beaa9(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3368f32241d617fec75fe7b16e6664a580606d3710b7d68af5d3fc4e4d26173(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__339672d1779bc6aca172917c7df78bd2504bc6a6a607c13db5b489ff579d8e0a(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0deedec8c161ed2b1bd6579cdcfd8ee0e0df2976a1056850d9653ca38e11e5f(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c587a87718b46a5cb103134a8b82fd5833a85d2915d3523acd888ff88a1b78b4(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96c423f97d564d8c5fb71ed8551a67288cfcddcae5b76bd891ee75255a97aa43(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f907a799fbe9efd59314c9785ab20c576a38709285dc9fbb08df3792c8e3f41(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec652f1b48c3f0dffb67aa880c3d1f9cc3805d5b64aaeaec347dd742d4f6534c(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11040abad81734974d02441e859775a7de6cc55e7da56a8a2c01a4a3f801f5a4(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af11bfa0f75de0837ac47155fe4e5e1f5e2f8edb2fdf6aa935a3bfa8aa6649e6(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90ce7a8a0e906c965d9e90c63d6e22bd429223c63cd2a7be4e408dccea576b16(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62ef78822c655030f526583590edf72ea7c77ca1a9905ce36ac66317d1987b05(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1377e062da302bcffd8b87439d46c6040855f3c3c231f6c926419a446b66e598(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7798401f732de4991e8ee0e3c12bdaf5a92df225b7f5bfc2ae4b7a8a2fec9bcc(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de7aa747a0497ec37fd5bbcc29185da02cdbfef3771fc2fcd252fab3a9b9227d(
    value: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65d0ecdab60b588f6dc0fafda59770703b7fe6e1737c5b95751c971fb9d55e08(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bfab94d814463999d0398a1ec28ea240f597504ec528b98fc741a8b58e39a48(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df3063e6588b53eb0f2678487e35ab76d4f885bf93eb049f7947dedb5bbd75cb(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3005d8b133a1baf2fc5e36f7379db9adce370d29402131ee66a1e3794bd3d5ea(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa0d9c253451026c97230bb226c3642a146dc092a07e7bf983837be94a021aaf(
    value: typing.Optional[typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b5788ebdfe963a6960acd204dea7ebd903bf7e09d6e10a112ccf257d76643f2(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98f43049959b70f5573ce02eec0ce86341789c2eaacfe9aa72a6961b8f2b6036(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cea9fe70657515ad2e75e54f220413acf2fc3de1fc1be094545c282e9c30507a(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a037288e7c7eda7103f8641012aebdfdc6a67179dd94608e36c9b9560f58615b(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82dfb23355ff4ac1e11451987a8387c77165b6d9ec6e349bd1ac7590850ef21b(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43c5df43796e3e5a31653616d3f648a9064d6d2fe3bf98af0bfd4fcb92234708(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fdc96cdfff7fd0b4dc3d696d1a76a5ad3544e55490f4e3fca44a8f2b347f69b(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba123350849539a396f59d1544c52858975b46500e89846bb2f929f3e7ade3dc(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff76ff403a72e3d4c53d3f7cdb9ca84a2590ebbbd952c4268698b04eb4d1dbb7(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83cdf7ec35ec6bde09f07ae17bd037c16c85a32cc1776e2782199b9994e3893f(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d1627fb8e7df3c0a69c6b8b0d1b3e7cf95017e4bfbe908edcb2c9909be2ca51(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c28ddc7a688d2522ecde1466e84e13231d92a8386fdaa170ff677ab68d8d07d5(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26cc47f20f5953b69e9ad499f521981a9638651227751f6d0dd4e4a21f7fbdaa(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d50796cf72be476ab120055bdf6930639483ac2b4ebf52436fcf308cda796d0(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97b714ce66a0a87e83b57148d8da7767cc9a0081fd790828ff259b313c6f2076(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c50ac9abfae08b36727e9a4fccf8e6c1323243eea7a8022c2d44fc2f259fc366(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e954e401e6c322260dea04550eabf7ace80b54ecd0ecbc70a7cfdca1856f5fa(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a919039858d54608f561e4fa34f8d3e0ca2816fce70d4a7c7416e7d2048caf16(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2161ed1de147cdc422d6e9eec1dc70e71c1cef8939894ffff4607451bf00c4f7(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3842e9c0ac79c16cde7892ff492b5cea94efc1e0860ded0b90e11201e5c21c95(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81336a57b1fd9a0a044e1d9cfcf0fceff5ebcb88cc253e8c8652eb685586f7ee(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5939785122602ea2bb40dca5db5c0f3b1a7979e99330ef6972d0db8482375bb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a98e4804e95d6a9dfc3cc2ddeda9e54ec862545009815be40621be7b1ed1c83(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac14357e1e2bddfd641691ba0b3219cf2e088bdd89205862877b4d02ca2bae9b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49a4d10b44ba7b9a941862098df254c9865b48b52395888bfb4e2369a161e36f(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5fedd8450b7eb1a91c68b4a2c81748fb032ec2d66f45a2f6f80dae52fd556fe(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01f3f2cf14a631c1f869eb7f617eaa135af99f64af91f5a345db57abafb3359e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46886245cae571c3e4d51b0ecf721eae50f515d6c6e55b4e7346d42ef76270ce(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__742ee9359f64a2b5e0e8d78fc9304572742c5c972de75ac81f717d59f546ced6(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c53c03bd250cea36159fea33bf7c86f44d606c1ab37fd7d410cc66ed192cf385(
    *,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    providers: typing.Optional[typing.Sequence[typing.Union[_cdktf_9a9027ec.TerraformProvider, typing.Union[_cdktf_9a9027ec.TerraformModuleProvider, typing.Dict[builtins.str, typing.Any]]]]] = None,
    skip_asset_creation_from_local_modules: typing.Optional[builtins.bool] = None,
    amazon_side_asn: typing.Optional[builtins.str] = None,
    azs: typing.Optional[typing.Sequence[builtins.str]] = None,
    cidr: typing.Optional[builtins.str] = None,
    create_database_internet_gateway_route: typing.Optional[builtins.bool] = None,
    create_database_nat_gateway_route: typing.Optional[builtins.bool] = None,
    create_database_subnet_group: typing.Optional[builtins.bool] = None,
    create_database_subnet_route_table: typing.Optional[builtins.bool] = None,
    create_egress_only_igw: typing.Optional[builtins.bool] = None,
    create_elasticache_subnet_group: typing.Optional[builtins.bool] = None,
    create_elasticache_subnet_route_table: typing.Optional[builtins.bool] = None,
    create_flow_log_cloudwatch_iam_role: typing.Optional[builtins.bool] = None,
    create_flow_log_cloudwatch_log_group: typing.Optional[builtins.bool] = None,
    create_igw: typing.Optional[builtins.bool] = None,
    create_multiple_intra_route_tables: typing.Optional[builtins.bool] = None,
    create_multiple_public_route_tables: typing.Optional[builtins.bool] = None,
    create_private_nat_gateway_route: typing.Optional[builtins.bool] = None,
    create_redshift_subnet_group: typing.Optional[builtins.bool] = None,
    create_redshift_subnet_route_table: typing.Optional[builtins.bool] = None,
    create_vpc: typing.Optional[builtins.bool] = None,
    customer_gateways: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]] = None,
    customer_gateway_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    customer_owned_ipv4_pool: typing.Optional[builtins.str] = None,
    database_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    database_dedicated_network_acl: typing.Optional[builtins.bool] = None,
    database_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    database_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    database_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    database_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
    database_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
    database_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
    database_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
    database_subnet_group_name: typing.Optional[builtins.str] = None,
    database_subnet_group_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    database_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
    database_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    database_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    database_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
    database_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    database_subnet_suffix: typing.Optional[builtins.str] = None,
    database_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    default_network_acl_egress: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    default_network_acl_ingress: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    default_network_acl_name: typing.Optional[builtins.str] = None,
    default_network_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    default_route_table_name: typing.Optional[builtins.str] = None,
    default_route_table_propagating_vgws: typing.Optional[typing.Sequence[builtins.str]] = None,
    default_route_table_routes: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    default_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    default_security_group_egress: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    default_security_group_ingress: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    default_security_group_name: typing.Optional[builtins.str] = None,
    default_security_group_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    default_vpc_enable_dns_hostnames: typing.Optional[builtins.bool] = None,
    default_vpc_enable_dns_support: typing.Optional[builtins.bool] = None,
    default_vpc_name: typing.Optional[builtins.str] = None,
    default_vpc_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    dhcp_options_domain_name: typing.Optional[builtins.str] = None,
    dhcp_options_domain_name_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    dhcp_options_ipv6_address_preferred_lease_time: typing.Optional[jsii.Number] = None,
    dhcp_options_netbios_name_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    dhcp_options_netbios_node_type: typing.Optional[builtins.str] = None,
    dhcp_options_ntp_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
    dhcp_options_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    elasticache_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    elasticache_dedicated_network_acl: typing.Optional[builtins.bool] = None,
    elasticache_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    elasticache_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    elasticache_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    elasticache_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
    elasticache_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
    elasticache_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
    elasticache_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
    elasticache_subnet_group_name: typing.Optional[builtins.str] = None,
    elasticache_subnet_group_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    elasticache_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
    elasticache_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    elasticache_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    elasticache_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
    elasticache_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    elasticache_subnet_suffix: typing.Optional[builtins.str] = None,
    elasticache_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    enable_dhcp_options: typing.Optional[builtins.bool] = None,
    enable_dns_hostnames: typing.Optional[builtins.bool] = None,
    enable_dns_support: typing.Optional[builtins.bool] = None,
    enable_flow_log: typing.Optional[builtins.bool] = None,
    enable_ipv6: typing.Optional[builtins.bool] = None,
    enable_nat_gateway: typing.Optional[builtins.bool] = None,
    enable_network_address_usage_metrics: typing.Optional[builtins.bool] = None,
    enable_public_redshift: typing.Optional[builtins.bool] = None,
    enable_vpn_gateway: typing.Optional[builtins.bool] = None,
    external_nat_ip_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    external_nat_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
    flow_log_cloudwatch_iam_role_arn: typing.Optional[builtins.str] = None,
    flow_log_cloudwatch_iam_role_conditions: typing.Any = None,
    flow_log_cloudwatch_log_group_class: typing.Optional[builtins.str] = None,
    flow_log_cloudwatch_log_group_kms_key_id: typing.Optional[builtins.str] = None,
    flow_log_cloudwatch_log_group_name_prefix: typing.Optional[builtins.str] = None,
    flow_log_cloudwatch_log_group_name_suffix: typing.Optional[builtins.str] = None,
    flow_log_cloudwatch_log_group_retention_in_days: typing.Optional[jsii.Number] = None,
    flow_log_cloudwatch_log_group_skip_destroy: typing.Optional[builtins.bool] = None,
    flow_log_deliver_cross_account_role: typing.Optional[builtins.str] = None,
    flow_log_destination_arn: typing.Optional[builtins.str] = None,
    flow_log_destination_type: typing.Optional[builtins.str] = None,
    flow_log_file_format: typing.Optional[builtins.str] = None,
    flow_log_hive_compatible_partitions: typing.Optional[builtins.bool] = None,
    flow_log_log_format: typing.Optional[builtins.str] = None,
    flow_log_max_aggregation_interval: typing.Optional[jsii.Number] = None,
    flow_log_per_hour_partition: typing.Optional[builtins.bool] = None,
    flow_log_traffic_type: typing.Optional[builtins.str] = None,
    igw_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    instance_tenancy: typing.Optional[builtins.str] = None,
    intra_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    intra_dedicated_network_acl: typing.Optional[builtins.bool] = None,
    intra_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    intra_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    intra_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    intra_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
    intra_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
    intra_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
    intra_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
    intra_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
    intra_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    intra_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    intra_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
    intra_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    intra_subnet_suffix: typing.Optional[builtins.str] = None,
    intra_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ipv4_ipam_pool_id: typing.Optional[builtins.str] = None,
    ipv4_netmask_length: typing.Optional[jsii.Number] = None,
    ipv6_cidr: typing.Optional[builtins.str] = None,
    ipv6_cidr_block_network_border_group: typing.Optional[builtins.str] = None,
    ipv6_ipam_pool_id: typing.Optional[builtins.str] = None,
    ipv6_netmask_length: typing.Optional[jsii.Number] = None,
    manage_default_network_acl: typing.Optional[builtins.bool] = None,
    manage_default_route_table: typing.Optional[builtins.bool] = None,
    manage_default_security_group: typing.Optional[builtins.bool] = None,
    manage_default_vpc: typing.Optional[builtins.bool] = None,
    map_customer_owned_ip_on_launch: typing.Optional[builtins.bool] = None,
    map_public_ip_on_launch: typing.Optional[builtins.bool] = None,
    name: typing.Optional[builtins.str] = None,
    nat_eip_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    nat_gateway_destination_cidr_block: typing.Optional[builtins.str] = None,
    nat_gateway_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    one_nat_gateway_per_az: typing.Optional[builtins.bool] = None,
    outpost_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    outpost_arn: typing.Optional[builtins.str] = None,
    outpost_az: typing.Optional[builtins.str] = None,
    outpost_dedicated_network_acl: typing.Optional[builtins.bool] = None,
    outpost_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    outpost_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    outpost_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
    outpost_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
    outpost_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
    outpost_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
    outpost_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
    outpost_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    outpost_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    outpost_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
    outpost_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    outpost_subnet_suffix: typing.Optional[builtins.str] = None,
    outpost_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    private_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    private_dedicated_network_acl: typing.Optional[builtins.bool] = None,
    private_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    private_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    private_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    private_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
    private_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
    private_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
    private_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
    private_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
    private_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    private_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    private_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
    private_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    private_subnet_suffix: typing.Optional[builtins.str] = None,
    private_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    private_subnet_tags_per_az: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]] = None,
    propagate_intra_route_tables_vgw: typing.Optional[builtins.bool] = None,
    propagate_private_route_tables_vgw: typing.Optional[builtins.bool] = None,
    propagate_public_route_tables_vgw: typing.Optional[builtins.bool] = None,
    public_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    public_dedicated_network_acl: typing.Optional[builtins.bool] = None,
    public_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    public_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    public_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    public_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
    public_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
    public_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
    public_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
    public_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
    public_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    public_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    public_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
    public_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    public_subnet_suffix: typing.Optional[builtins.str] = None,
    public_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    public_subnet_tags_per_az: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, builtins.str]]] = None,
    putin_khuylo: typing.Optional[builtins.bool] = None,
    redshift_acl_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    redshift_dedicated_network_acl: typing.Optional[builtins.bool] = None,
    redshift_inbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    redshift_outbound_acl_rules: typing.Optional[typing.Sequence[typing.Mapping[builtins.str, builtins.str]]] = None,
    redshift_route_table_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    redshift_subnet_assign_ipv6_address_on_creation: typing.Optional[builtins.bool] = None,
    redshift_subnet_enable_dns64: typing.Optional[builtins.bool] = None,
    redshift_subnet_enable_resource_name_dns_aaaa_record_on_launch: typing.Optional[builtins.bool] = None,
    redshift_subnet_enable_resource_name_dns_a_record_on_launch: typing.Optional[builtins.bool] = None,
    redshift_subnet_group_name: typing.Optional[builtins.str] = None,
    redshift_subnet_group_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    redshift_subnet_ipv6_native: typing.Optional[builtins.bool] = None,
    redshift_subnet_ipv6_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    redshift_subnet_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    redshift_subnet_private_dns_hostname_type_on_launch: typing.Optional[builtins.str] = None,
    redshift_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    redshift_subnet_suffix: typing.Optional[builtins.str] = None,
    redshift_subnet_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    reuse_nat_ips: typing.Optional[builtins.bool] = None,
    secondary_cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
    single_nat_gateway: typing.Optional[builtins.bool] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    use_ipam_pool: typing.Optional[builtins.bool] = None,
    vpc_flow_log_iam_policy_name: typing.Optional[builtins.str] = None,
    vpc_flow_log_iam_policy_use_name_prefix: typing.Optional[builtins.bool] = None,
    vpc_flow_log_iam_role_name: typing.Optional[builtins.str] = None,
    vpc_flow_log_iam_role_use_name_prefix: typing.Optional[builtins.bool] = None,
    vpc_flow_log_permissions_boundary: typing.Optional[builtins.str] = None,
    vpc_flow_log_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpc_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    vpn_gateway_az: typing.Optional[builtins.str] = None,
    vpn_gateway_id: typing.Optional[builtins.str] = None,
    vpn_gateway_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
