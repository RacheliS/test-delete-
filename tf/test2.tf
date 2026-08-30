# AWS Provider Configuration
provider "aws" {
  region = "us-east-1"
}

# Misconfiguration 1: Unencrypted S3 bucket with public access
resource "aws_s3_bucket" "vulnerable_bucket" {
  bucket = "my-public-test-bucket-12345"
}

resource "aws_s3_bucket_public_access_block" "public_access" {
  bucket = aws_s3_bucket.vulnerable_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

# Misconfiguration 2: Security Group open to the world
resource "aws_security_group" "allow_all" {
  name        = "allow_all_traffic"
  description = "Vulnerable security group"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # SSH exposed to 0.0.0.0/0
  }
}
