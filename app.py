#!/usr/bin/env python3
import aws_cdk as cdk

from aws.example_rest_api.infrastructure import ExampleRestAPI

app = cdk.App()

ExampleRestAPI(app, 'ExampleRestAPIStack')

app.synth()
