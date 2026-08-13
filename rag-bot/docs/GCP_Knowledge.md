
# GCP Knowledge Guide: Cloud DNS & Cloud Load Balancing

## 1. GCP Cloud DNS

Google Cloud DNS is a high-performance, resilient, global DNS service that translates domain names into IP addresses with low latency.

### Core Concepts & Zones

| Concept | Description | Typical Use Case |
| :--- | :--- | :--- |
| **Public Zone** | Managed DNS zone visible to the global internet. | Domain mapping for public web applications. |
| **Private Zone** | DNS zone restricted to one or more internal VPC networks. | Internal microservice discovery and private IP mapping. |
| **Forwarding Zone** | Routes DNS queries to on-premises or third-party DNS servers. | Hybrid cloud network connectivity via Cloud VPN / Interconnect. |
| **Peering Zone** | Shares DNS resolution across separate GCP organizations or VPCs. | Multi-tenant or multi-project infrastructure design. |

---

## 2. GCP Cloud Load Balancing Overview

Google Cloud offers external and internal load balancers designed for global, regional, HTTP(S), TCP, and UDP traffic.

### Load Balancer Types Matrix
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