terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  required_version = ">= 1.3.0"
}

provider "aws" {
  region = var.aws_region
}

module "ec2" {
  source         = "./modules/ec2"
  instance_name  = var.instance_name
  instance_type  = var.instance_type
  ami_id         = var.ami_id
  key_name       = var.key_name
  subnet_id      = var.subnet_id
  security_group = var.security_group
}
