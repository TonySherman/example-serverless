python_sources()

python_aws_lambda_function(
    name="get_item_lambda",
    runtime="python3.11",
    handler="get_item.py:lambda_handler",
    dependencies=["!!//:root#aws-lambda-powertools"],
)


python_aws_lambda_function(
    name="manage_items_lambda",
    runtime="python3.11",
    handler="manage_items.py:lambda_handler",
    dependencies=["!!//:root#aws-lambda-powertools"],
)


python_aws_lambda_layer(
    name="dependency_layer",
    runtime="python3.11",
    dependencies=["//:root#aws-lambda-powertools"],
    include_sources=False,
)
