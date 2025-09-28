# CDK Billing Demo

This AWS CDK application creates three AWS Budget alerts to help monitor your AWS spending. It sets up budget thresholds at $25, $50, and $100 with email notifications when you approach or exceed these limits.

## Features

- Creates three monthly cost budgets ($25, $50, $100)
- Sends email alerts at:
  - 80% of budget threshold (warning)
  - 100% of budget threshold (exceeded)
  - When forecasted to exceed 100% of budget
- Deploys to us-west-2 (required for AWS Budgets)
- Easy deployment via AWS CloudShell

## Prerequisites

- AWS Account with appropriate permissions to create budgets
- AWS CloudShell access (or local AWS CLI configured)
- Valid email address for receiving budget alerts

## Deployment Instructions for AWS CloudShell

### Step 1: Open AWS CloudShell

1. Log into the AWS Management Console
2. Click on the CloudShell icon in the top navigation bar (terminal icon)
3. Wait for the CloudShell environment to initialize

### Step 2: Clone the Repository

```bash
# Clone the repository (replace with your actual repository URL)
git clone https://github.com/andrewkrug/cdk_billing_demo.git

# Navigate to the project directory
cd cdk_billing_demo
```

### Step 3: Set Up Python Virtual Environment

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip
```

### Step 4: Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt
```

### Step 5: Bootstrap CDK (First Time Only)

If this is your first time using CDK in this AWS account/region:

```bash
# Bootstrap the CDK (creates necessary resources for CDK deployments)
cdk bootstrap aws://ACCOUNT-ID/us-west-2

# Note: Replace ACCOUNT-ID with your actual AWS account ID
# You can find your account ID by running:
aws sts get-caller-identity --query Account --output text
```

### Step 6: Deploy the Stack

```bash
# Deploy the stack with your email address
cdk deploy -c email=your-email@example.com

# Replace 'your-email@example.com' with your actual email address
```

You will be prompted to confirm the deployment. Type 'y' and press Enter to proceed.

### Step 7: Verify Deployment

After successful deployment, you will see output similar to:

```
Outputs:
BillingAlarmsStack.BudgetsCreated = Created budgets for: $25, $50, $100
BillingAlarmsStack.NotificationEmail = your-email@example.com
```

### Step 8: Confirm Email Subscription

**Important:** Check your email inbox for AWS Budget notification confirmation emails. You must confirm each subscription to receive budget alerts.

## Verifying the Budgets

To verify your budgets were created:

1. Navigate to the AWS Billing Dashboard
2. Click on "Budgets" in the left sidebar
3. You should see three budgets:
   - Monthly-Budget-25USD
   - Monthly-Budget-50USD
   - Monthly-Budget-100USD

## Updating the Stack

To update email address or modify budgets:

```bash
# Make your changes to the code, then:
cdk diff -c email=your-email@example.com  # Preview changes
cdk deploy -c email=your-email@example.com # Deploy changes
```

## Destroying the Stack

To remove all budgets and clean up:

```bash
cdk destroy -c email=your-email@example.com
```

## Project Structure

```
cdk-billing-demo/
├── app.py                                  # CDK application entry point
├── cdk_billing_demo/
│   ├── __init__.py
│   └── billing_alarms_stack.py           # Stack definition with budget configurations
├── requirements.txt                       # Python dependencies
├── cdk.json                              # CDK configuration
├── LICENSE                               # MIT License
└── README.md                             # This file
```

## Customization

### Modifying Budget Amounts

To change the budget thresholds, edit the `budget_amounts` list in `cdk_billing_demo/billing_alarms_stack.py`:

```python
budget_amounts = [25, 50, 100]  # Change these values as needed
```

### Modifying Alert Thresholds

To change when alerts are sent, modify the `threshold` values in the `NotificationProperty` configurations.

## Troubleshooting

### Common Issues

1. **Permission Denied**: Ensure your AWS user/role has permissions to:
   - Create and manage AWS Budgets
   - Deploy CloudFormation stacks
   - Create IAM roles (for CDK bootstrap)

2. **Email Not Receiving Alerts**: 
   - Check spam/junk folder
   - Ensure you confirmed the email subscription
   - Verify the email address is correct

3. **CDK Bootstrap Error**: 
   - Ensure you're in the correct AWS account
   - Check you have AdministratorAccess or appropriate permissions

4. **Region Error**: 
   - AWS Budgets must be deployed to us-west-2
   - The stack automatically deploys to us-west-2

## Cost Considerations

- AWS Budgets: First two budgets are free, additional budgets cost $0.02 per day
- This demo creates three budgets, so the third budget will incur charges
- Email notifications are free

## Security Best Practices

- Never commit AWS credentials to the repository
- Use AWS CloudShell or IAM roles for authentication
- Regularly review and update budget thresholds
- Monitor the email address receiving notifications

## Support

For issues or questions:
1. Check the [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/)
2. Review [AWS Budgets Documentation](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
3. Open an issue in the GitHub repository

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.