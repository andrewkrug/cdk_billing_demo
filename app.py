#!/usr/bin/env python3
import os
import aws_cdk as cdk
from cdk_billing_demo.billing_alarms_stack import BillingAlarmsStack

app = cdk.App()

email = app.node.try_get_context("email")
if not email:
    raise ValueError("Please provide an email address using: cdk deploy -c email=your-email@example.com")

BillingAlarmsStack(app, "BillingAlarmsStack",
    email_address=email,
    env=cdk.Environment(
        account=os.getenv('CDK_DEFAULT_ACCOUNT'),
        region='us-east-1'  # Budgets must be in us-east-1
    ),
    description="Stack that creates AWS Budget alerts for $25, $50, and $100 thresholds"
)

app.synth()