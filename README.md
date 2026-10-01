# GitHub Actions Backend

This repository contains GitHub Actions workflows for cloud operations and developer automation, along with Terraform configuration for provisioning an AWS EC2 instance. Operational workflows are manually triggered and can be used directly in GitHub Actions or integrated with Port.

## Repository contents

- `.github/workflows/` — dispatchable workflows and sample CI workflows.
- `.github/templates/` — JSON templates used by IAM permission workflows.
- `main.tf`, `variables.tf`, `outputs.tf` — Terraform configuration for an EC2 instance and its outputs.

## Workflow catalog

### AWS

- **EC2:** provision, start, reboot, or terminate an instance.
- **ECS:** check service health, restart, scale, update a task definition, roll back a deployment, or delete a service.
- **Auto Scaling:** scale an Auto Scaling Group or resize its capacity.
- **SQS:** delete or purge a queue, or redrive dead-letter queue messages.
- **RDS:** reboot or delete an instance.
- **ACM:** request, renew, or delete a certificate.
- **IAM:** create or delete resource permissions.
- **Resource tags:** add tags to an ECR repository or S3 bucket.

### Azure

- Start, restart, or deallocate a virtual machine.
- Start, restart, or stop a web app.

### Developer automation

- Trigger Claude Code or Gemini Code Assistant.
- Assign an issue to Copilot.
- Manage a pull request or add a pull request comment.

The `ci_workflow_*` files are sample workflows that run on pushes and pull requests. For a workflow's exact inputs and behavior, see its YAML file in `.github/workflows/`.

## Run a workflow

1. Open the repository's **Actions** tab and select a workflow.
2. Select **Run workflow**, provide its required inputs, and start the run.
3. Review the run logs for results.

Most operational workflows use `workflow_dispatch`. Workflows integrated with Port may require a `port_context` input containing the selected entity context. Check the workflow definition before running it.

## Configure repository secrets

Add only the secrets needed by the workflows you intend to run under **Settings → Secrets and variables → Actions**. The workflows reference these secrets:

| Secret | Used for |
| --- | --- |
| `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`, `AWS_SESSION_TOKEN` | AWS workflows, including EC2, ECS, RDS, SQS, ACM, and resource tagging |
| `PORT_AWS_ACCESS_KEY_ID`, `PORT_AWS_SECRET_ACCESS_KEY`, `AWS_ACCOUNT_ID` | IAM permission workflows |
| `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`, `AZURE_TENANT_ID` | Azure workflows |
| `PORT_CLIENT_ID`, `PORT_CLIENT_SECRET` | Workflows that update entities or action-run status in Port |
| `PORT_GITHUB_TOKEN` | Claude and Gemini workflows that check out and update another repository |
| `ANTHROPIC_API_KEY` | Claude Code workflow |
| `GEMINI_API_KEY` | Gemini Code Assistant workflow |
| `GH_TOKEN` | Pull request management workflow |
| `COMMENT_ON_PR_TOKEN` | Pull request comment workflow |

Use appropriately scoped credentials and follow your organization's secret-management policies. Not every workflow needs every secret.

## Provision an EC2 instance

The **Provision AN EC2 Instance** workflow runs Terraform from the repository root. It requires AWS credentials and the AWS region secrets above, plus the following workflow inputs:

- `ec2_name` — instance name tag (defaults to `App Server`).
- `ec2_instance_type` — instance type (defaults to `t3.micro`).
- `pem_key_name` — existing EC2 key pair name.

The Terraform configuration selects the latest matching Ubuntu 20.04 AMI published by Canonical. The workflow applies the configuration and publishes the instance details to Port, so `PORT_CLIENT_ID` and `PORT_CLIENT_SECRET` must also be configured for the workflow to complete.

To provision locally, install Terraform and configure AWS credentials, then provide the required Terraform variables:

```sh
export TF_VAR_ec2_name="App Server"
export TF_VAR_pem_key_name="your-key-pair-name"
export TF_VAR_aws_region="us-east-1"
export TF_VAR_ec2_instance_type="t3.micro"

terraform init
terraform validate
terraform plan
terraform apply
```

Terraform state is local by default. Protect the state file and avoid sharing it; it can contain sensitive infrastructure details.
