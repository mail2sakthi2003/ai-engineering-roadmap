# AWS Knowledge Guide: Networking & Serverless Execution

## 1. AWS Networking Fundamentals

Amazon Virtual Private Cloud (VPC) provides an isolated virtual network environment within the AWS Cloud. Key networking components include VPCs, subnets, route tables, internet gateways, NAT gateways, Security Groups, and Network Access Control Lists (NACLs).

### Core Components Summary

| Component | Level | Stateful / Stateless | Primary Function |
| :--- | :--- | :--- | :--- |
| **VPC** | Regional | N/A | Logically isolated virtual network across Availability Zones. |
| **Subnet** | Availability Zone | N/A | IPv4/IPv6 CIDR block segment within a VPC (Public or Private). |
| **Internet Gateway (IGW)** | VPC | Stateless | Horizontal, highly available gateway for public internet access. |
| **NAT Gateway** | Subnet | Stateful | Allows private subnet instances to access the internet outbound without inbound access. |
| **Security Group (SG)** | Instance / ENI | Stateful | Virtual firewall operating at the network interface layer. |
| **Network ACL (NACL)** | Subnet | Stateless | Subnet-level boundary layer evaluating inbound and outbound rules sequentially. |

---

## 2. AWS Lambda Architecture & Integration

AWS Lambda is an event-driven, serverless compute service that runs code in response to events without requiring infrastructure management.

### Execution Lifecycle & Networking Setup

### Key Differences: Standard vs. VPC-Enabled Lambda

* **Standard Mode:** Functions run in an AWS-managed secure network. They have direct access to public internet APIs and AWS endpoints, but cannot access private VPC resources directly.
* **VPC-Attached Mode:** Functions associate with target private subnets and Security Groups via AWS Hyperplane ENIs (Elastic Network Interfaces). This allows secure access to RDS databases, Internal Load Balancers, and ElastiCache clusters. Outbound internet access in this mode requires routing through a NAT Gateway or using VPC Endpoints (AWS PrivateLink).

---

## 3. Reference Infrastructure: Lambda inside VPC with Terraform

```hcl
# Security Group for Lambda Function
resource "aws_security_group" "lambda_sg" {
  name        = "demo-lambda-sg"
  description = "Security group for AWS Lambda function"
  vpc_id      = var.vpc_id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

# AWS Lambda Function Definition
resource "aws_lambda_function" "demo_lambda" {
  filename      = "lambda_function_payload.zip"
  function_name = "demo_vpc_lambda"
  role          = aws_iam_role.lambda_exec_role.arn
  handler       = "index.handler"
  runtime       = "nodejs18.x"

  vpc_config {
    subnet_ids         = var.private_subnet_ids
    security_group_ids = [aws_security_group.lambda_sg.id]
  }

  environment {
    variables = {
      ENV = "Production"
    }
  }
}

---

### Key Differences: Standard vs. VPC-Enabled Lambda

* **Standard Mode:** Functions run in an AWS-managed secure network. They have direct access to public internet APIs and AWS endpoints, but cannot access private VPC resources directly.
* **VPC-Attached Mode:** Functions associate with target private subnets and Security Groups via AWS Hyperplane ENIs (Elastic Network Interfaces). This allows secure access to RDS databases, Internal Load Balancers, and ElastiCache clusters. Outbound internet access in this mode requires routing through a NAT Gateway or using VPC Endpoints (AWS PrivateLink).

---

## 3. Reference Infrastructure: Lambda inside VPC with Terraform

```hcl
# Security Group for Lambda Function
resource "aws_security_group" "lambda_sg" {
  name        = "demo-lambda-sg"
  description = "Security group for AWS Lambda function"
  vpc_id      = var.vpc_id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

# AWS Lambda Function Definition
resource "aws_lambda_function" "demo_lambda" {
  filename      = "lambda_function_payload.zip"
  function_name = "demo_vpc_lambda"
  role          = aws_iam_role.lambda_exec_role.arn
  handler       = "index.handler"
  runtime       = "nodejs18.x"

  vpc_config {
    subnet_ids         = var.private_subnet_ids
    security_group_ids = [aws_security_group.lambda_sg.id]
  }

  environment {
    variables = {
      ENV = "Production"
    }
  }
}