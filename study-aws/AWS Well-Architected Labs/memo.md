

AWS Well-Architected Labs
https://wellarchitectedlabs.com/

AWS Well-Architected フレームワーク
https://docs.aws.amazon.com/ja_jp/wellarchitected/latest/framework/welcome.html




AWSコンソール
https://ap-northeast-1.console.aws.amazon.com/console/home?region=ap-northeast-1#


## Automating Operetaions with Playbooks and Runbooks

### サンプルアプリケーションのビルド

bash ./build_application.sh $AWS_REGION $(aws sts get-caller-identity --query Account --output text) \
      <sysops@domain.com> <owner@domain.com>



DNS名
walab-op-ALB-Qp4ccygfiw3o-409431045.us-west-2.elb.amazonaws.com

ALBEndpoint="walab-op-ALB-Qp4ccygfiw3o-409431045.us-west-2.elb.amazonaws.com"

curl --header "Content-Type: application/json" --request POST --data '{"Name":"Bob","Text":"Run your operations as code"}' $ALBEndpoint/encrypt

{"Message":"Data encrypted and stored, keep your key save","Key":"e3e13fb7-9e86-4ae5-94cf-70d0d7dca694"}s


curl --header "Content-Type: application/json" --request GET --data '{"Name":"Bob","Key":"e3e13fb7-9e86-4ae5-94cf-70d0d7dca694"}' $ALBEndpoint/decrypt


bash simulate_request.sh walab-op-ALB-Qp4ccygfiw3o-409431045.us-west-2.elb.amazonaws.com


AutomationRole ARN
arn:aws:iam::246262167857:role/AutomationRole


  aws cloudformation create-stack --stack-name waopslab-playbook-gather-resources \
                                  --parameters ParameterKey=PlaybookIAMRole,ParameterValue=arn:aws:iam::246262167857:role/AutomationRole \
                                  --template-body file://playbook_gather_resources.yml 



Output Payload
{
  "Payload": {
    "CanaryEndpoint": "walab-op-ALB-Qp4ccygfiw3o-409431045.us-west-2.elb.amazonaws.com",
    "ApplicationStackResources": "[{\"PhysicalResourceId\": \"walab-ops-sample-application\", \"Type\": \"AWS::ECR::Repository\"}, {\"PhysicalResourceId\": \"igw-041c571be174850cd\", \"Type\": \"AWS::EC2::InternetGateway\"}, {\"PhysicalResourceId\": \"IGW|vpc-059ccdb7ec5370604\", \"Type\": \"AWS::EC2::VPCGatewayAttachment\"}, {\"PhysicalResourceId\": \"nat-0923234925e194b81\", \"Type\": \"AWS::EC2::NatGateway\"}, {\"PhysicalResourceId\": \"44.237.158.87\", \"Type\": \"AWS::EC2::EIP\"}, {\"PhysicalResourceId\": \"rtb-0a501a65044760db4|0.0.0.0/0\", \"Type\": \"AWS::EC2::Route\"}, {\"PhysicalResourceId\": \"rtb-0b83b81c98a63c154|0.0.0.0/0\", \"Type\": \"AWS::EC2::Route\"}, {\"PhysicalResourceId\": \"rtb-0a501a65044760db4\", \"Type\": \"AWS::EC2::RouteTable\"}, {\"PhysicalResourceId\": \"rtb-0b83b81c98a63c154\", \"Type\": \"AWS::EC2::RouteTable\"}, {\"PhysicalResourceId\": \"subnet-0c57e6f2fd76bd23a\", \"Type\": \"AWS::EC2::Subnet\"}, {\"PhysicalResourceId\": \"rtbassoc-068c57e02028772c5\", \"Type\": \"AWS::EC2::SubnetRouteTableAssociation\"}, {\"PhysicalResourceId\": \"rtbassoc-0751c5a6353dcc287\", \"Type\": \"AWS::EC2::SubnetRouteTableAssociation\"}, {\"PhysicalResourceId\": \"subnet-0078c7cbb1321e8ca\", \"Type\": \"AWS::EC2::Subnet\"}, {\"PhysicalResourceId\": \"rtb-0eb178ed72e990aac|0.0.0.0/0\", \"Type\": \"AWS::EC2::Route\"}, {\"PhysicalResourceId\": \"rtb-0a86a60fe2287f1e2|0.0.0.0/0\", \"Type\": \"AWS::EC2::Route\"}, {\"PhysicalResourceId\": \"rtb-0eb178ed72e990aac\", \"Type\": \"AWS::EC2::RouteTable\"}, {\"PhysicalResourceId\": \"rtb-0a86a60fe2287f1e2\", \"Type\": \"AWS::EC2::RouteTable\"}, {\"PhysicalResourceId\": \"subnet-073ad0879592ef4cc\", \"Type\": \"AWS::EC2::Subnet\"}, {\"PhysicalResourceId\": \"rtbassoc-008f811cfc309b074\", \"Type\": \"AWS::EC2::SubnetRouteTableAssociation\"}, {\"PhysicalResourceId\": \"rtbassoc-09e30c9fa6091e0ee\", \"Type\": \"AWS::EC2::SubnetRouteTableAssociation\"}, {\"PhysicalResourceId\": \"subnet-0675d6dda4c7582c9\", \"Type\": \"AWS::EC2::Subnet\"}, {\"PhysicalResourceId\": \"vpc-059ccdb7ec5370604\", \"Type\": \"AWS::EC2::VPC\"}]"
  }
}


Reources
[
  {
    "PhysicalResourceId": "walab-ops-sample-application",
    "Type": "AWS::ECR::Repository"
  },
  {
    "PhysicalResourceId": "igw-041c571be174850cd",
    "Type": "AWS::EC2::InternetGateway"
  },
  {
    "PhysicalResourceId": "IGW|vpc-059ccdb7ec5370604",
    "Type": "AWS::EC2::VPCGatewayAttachment"
  },
  {
    "PhysicalResourceId": "nat-0923234925e194b81",
    "Type": "AWS::EC2::NatGateway"
  },
  {
    "PhysicalResourceId": "44.237.158.87",
    "Type": "AWS::EC2::EIP"
  },
  {
    "PhysicalResourceId": "rtb-0a501a65044760db4|0.0.0.0/0",
    "Type": "AWS::EC2::Route"
  },
  {
    "PhysicalResourceId": "rtb-0b83b81c98a63c154|0.0.0.0/0",
    "Type": "AWS::EC2::Route"
  },
  {
    "PhysicalResourceId": "rtb-0a501a65044760db4",
    "Type": "AWS::EC2::RouteTable"
  },
  {
    "PhysicalResourceId": "rtb-0b83b81c98a63c154",
    "Type": "AWS::EC2::RouteTable"
  },
  {
    "PhysicalResourceId": "subnet-0c57e6f2fd76bd23a",
    "Type": "AWS::EC2::Subnet"
  },
  {
    "PhysicalResourceId": "rtbassoc-068c57e02028772c5",
    "Type": "AWS::EC2::SubnetRouteTableAssociation"
  },
  {
    "PhysicalResourceId": "rtbassoc-0751c5a6353dcc287",
    "Type": "AWS::EC2::SubnetRouteTableAssociation"
  },
  {
    "PhysicalResourceId": "subnet-0078c7cbb1321e8ca",
    "Type": "AWS::EC2::Subnet"
  },
  {
    "PhysicalResourceId": "rtb-0eb178ed72e990aac|0.0.0.0/0",
    "Type": "AWS::EC2::Route"
  },
  {
    "PhysicalResourceId": "rtb-0a86a60fe2287f1e2|0.0.0.0/0",
    "Type": "AWS::EC2::Route"
  },
  {
    "PhysicalResourceId": "rtb-0eb178ed72e990aac",
    "Type": "AWS::EC2::RouteTable"
  },
  {
    "PhysicalResourceId": "rtb-0a86a60fe2287f1e2",
    "Type": "AWS::EC2::RouteTable"
  },
  {
    "PhysicalResourceId": "subnet-073ad0879592ef4cc",
    "Type": "AWS::EC2::Subnet"
  },
  {
    "PhysicalResourceId": "rtbassoc-008f811cfc309b074",
    "Type": "AWS::EC2::SubnetRouteTableAssociation"
  },
  {
    "PhysicalResourceId": "rtbassoc-09e30c9fa6091e0ee",
    "Type": "AWS::EC2::SubnetRouteTableAssociation"
  },
  {
    "PhysicalResourceId": "subnet-0675d6dda4c7582c9",
    "Type": "AWS::EC2::Subnet"
  },
  {
    "PhysicalResourceId": "vpc-059ccdb7ec5370604",
    "Type": "AWS::EC2::VPC"
  }
]



aws cloudformation create-stack --stack-name waopslab-playbook-investigate-resources \
                                --parameters ParameterKey=PlaybookIAMRole,ParameterValue=arn:aws:iam::246262167857:role/AutomationRole \
                                --template-body file://playbook_investigate_application_resources.yml 


Playbook-Investigate-Application-Resourcesで以下のエラー。
RDSの情報を見つけようとしてエラーになっている気がする。
ResourcesリストにRDSの情報がないことが原因のような気もするが、提供されているPlaybookのデバッグになりそう。
時間切れ、中止。


Traceback (most recent call last):
  File "/tmp/66d84801-7863-4670-8717-4be13eaf5c02-2025-09-22-02-32-03/customer_script.py", line 84, in handler
    rdsconfig = get_rds_config(rdsrsname)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/66d84801-7863-4670-8717-4be13eaf5c02-2025-09-22-02-32-03/customer_script.py", line 34, in get_rds_config
    res = rdsclient.describe_db_instances(
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/var/lang/lib/python3.11/site-packages/botocore/client.py", line 602, in _api_call
    return self._make_api_call(operation_name, kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/var/lang/lib/python3.11/site-packages/botocore/context.py", line 123, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/var/lang/lib/python3.11/site-packages/botocore/client.py", line 1035, in _make_api_call
    request_dict = self._convert_to_request_dict(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/var/lang/lib/python3.11/site-packages/botocore/client.py", line 1102, in _convert_to_request_dict
    request_dict = self._serializer.serialize_to_request(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/var/lang/lib/python3.11/site-packages/botocore/validate.py", line 381, in serialize_to_request
    raise ParamValidationError(report=report.generate_report())
botocore.exceptions.ParamValidationError: Parameter validation failed:
Invalid type for parameter DBInstanceIdentifier, value: None, type: <class 'NoneType'>, valid types: <class 'str'>

ParamValidationError - Parameter validation failed:
Invalid type for parameter DBInstanceIdentifier, value: None, type: <class 'NoneType'>, valid types: <class 'str'>