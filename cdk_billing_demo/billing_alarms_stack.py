from aws_cdk import (
    Stack,
    aws_budgets as budgets,
    CfnOutput
)
from constructs import Construct

class BillingAlarmsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, email_address: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        budget_amounts = [25, 50, 100]
        
        budgets_created = []
        
        for amount in budget_amounts:
            budget = budgets.CfnBudget(
                self, f"Budget{amount}USD",
                budget=budgets.CfnBudget.BudgetDataProperty(
                    budget_name=f"Monthly-Budget-{amount}USD",
                    budget_type="COST",
                    time_unit="MONTHLY",
                    budget_limit=budgets.CfnBudget.SpendProperty(
                        amount=amount,
                        unit="USD"
                    )
                ),
                notifications_with_subscribers=[
                    budgets.CfnBudget.NotificationWithSubscribersProperty(
                        notification=budgets.CfnBudget.NotificationProperty(
                            comparison_operator="GREATER_THAN",
                            notification_type="ACTUAL",
                            threshold=80,
                            threshold_type="PERCENTAGE"
                        ),
                        subscribers=[
                            budgets.CfnBudget.SubscriberProperty(
                                address=email_address,
                                subscription_type="EMAIL"
                            )
                        ]
                    ),
                    budgets.CfnBudget.NotificationWithSubscribersProperty(
                        notification=budgets.CfnBudget.NotificationProperty(
                            comparison_operator="GREATER_THAN",
                            notification_type="ACTUAL",
                            threshold=100,
                            threshold_type="PERCENTAGE"
                        ),
                        subscribers=[
                            budgets.CfnBudget.SubscriberProperty(
                                address=email_address,
                                subscription_type="EMAIL"
                            )
                        ]
                    ),
                    budgets.CfnBudget.NotificationWithSubscribersProperty(
                        notification=budgets.CfnBudget.NotificationProperty(
                            comparison_operator="GREATER_THAN",
                            notification_type="FORECASTED",
                            threshold=100,
                            threshold_type="PERCENTAGE"
                        ),
                        subscribers=[
                            budgets.CfnBudget.SubscriberProperty(
                                address=email_address,
                                subscription_type="EMAIL"
                            )
                        ]
                    )
                ]
            )
            budgets_created.append(f"${amount}")
        
        CfnOutput(
            self, "BudgetsCreated",
            value=f"Created budgets for: {', '.join(budgets_created)}",
            description="Budget thresholds that were created"
        )
        
        CfnOutput(
            self, "NotificationEmail",
            value=email_address,
            description="Email address that will receive budget alerts"
        )