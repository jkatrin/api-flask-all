variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "instance_name" {
  type    = string
  default = "api-devsecops"
}

variable "instance_type" {
  type    = string
  default = "t2.micro"
}

variable "ami_id" {
  type    = string
  description = "AMI ID for Ubuntu (ex: ami-0c02fb55956c7d316 for us-east-1)"
}

variable "key_name" {
  type    = string
  description = "Nome da chave pública SSH cadastrada na AWS"
}

variable "subnet_id" {
  type = string
}

variable "security_group" {
  type = string
}
