from aws_cdk import Stack, CfnOutput
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class ExampleRestAPI(Stack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, id, **kwargs)

        get_item_lambda = _lambda.Function(
            self,
            "getFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.handler",
            code=_lambda.Code.from_asset(
                "./dist/aws.example_rest_api.api/get_item_lambda.zip"
            ),
        )

        manage_items_lambda = _lambda.Function(
            self,
            "manageFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.handler",
            code=_lambda.Code.from_asset(
                "./dist/aws.example_rest_api.api/manage_items_lambda.zip"
            ),
        )

        get_url = get_item_lambda.add_function_url(auth_type=_lambda.FunctionUrlAuthType.NONE)
        manage_url = manage_items_lambda.add_function_url(auth_type=_lambda.FunctionUrlAuthType.NONE)

        CfnOutput(self, "get_item_url", value=get_url.url)
        CfnOutput(self, "manage_items_url", value=manage_url.url)
