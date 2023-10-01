terraform {
  required_providers {
    kind = {
      source  = "tehcyx/kind"
      version = "0.0.15"
    }
    minio = {
      # ATTENTION: use the current version here!
      version = "1.18.0"
      source  = "aminueza/minio"
    }
  }
}

# Configure the provider for Kind
provider "kind" {}

# Create the infrastructure cluster
resource "kind_cluster" "infrastructure" {
  name = "infrastructure"
}

# Create the application cluster
resource "kind_cluster" "application" {
  name = "application"
}
