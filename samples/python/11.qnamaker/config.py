#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "22eb2d3f-2613-4c2e-81eb-6d8008fb2261")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "adb330b7-64dc-4361-bf69-ec854044e17c")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "6faa9b50-a19c-4416-9aca-69f7bdca8f42")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://qnasaptest.azurewebsites.net/qnamaker")
