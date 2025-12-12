# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Integration tests for BedrockClient serviceTier parameter with real AWS API calls."""

import pytest
from idp_common.bedrock.client import BedrockClient


@pytest.mark.integration
class TestBedrockClientServiceTierIntegration:
    """Integration tests for service tier with real Bedrock API calls."""

    @pytest.fixture
    def bedrock_client(self):
        """Create BedrockClient instance for us-west-2."""
        return BedrockClient(region="us-west-2", metrics_enabled=False)

    def test_flex_service_tier_with_nova_2_lite(self, bedrock_client):
        """Test Flex service tier with Nova 2 Lite model."""
        response = bedrock_client.invoke_model(
            model_id="us.amazon.nova-2-lite-v1:0",
            system_prompt="You are a helpful assistant.",
            content=[{"text": "What is 2+2? Answer in one word."}],
            service_tier="flex",
            max_tokens=10,
        )

        assert response is not None
        assert "output" in response
        assert "message" in response["output"]
        assert "content" in response["output"]["message"]
        assert len(response["output"]["message"]["content"]) > 0
        assert "text" in response["output"]["message"]["content"][0]

    def test_priority_service_tier_with_nova_2_lite(self, bedrock_client):
        """Test Priority service tier with Nova 2 Lite model."""
        response = bedrock_client.invoke_model(
            model_id="us.amazon.nova-2-lite-v1:0",
            system_prompt="You are a helpful assistant.",
            content=[{"text": "Say 'hello' in one word."}],
            service_tier="priority",
            max_tokens=5,
        )

        assert response is not None
        assert "output" in response

    def test_standard_service_tier_with_nova_2_lite(self, bedrock_client):
        """Test Standard service tier (normalized to default) with Nova 2 Lite model."""
        response = bedrock_client.invoke_model(
            model_id="us.amazon.nova-2-lite-v1:0",
            system_prompt="You are a helpful assistant.",
            content=[{"text": "Count to 3."}],
            service_tier="standard",
            max_tokens=20,
        )

        assert response is not None
        assert "output" in response

    def test_no_service_tier_with_nova_2_lite(self, bedrock_client):
        """Test without service tier (default behavior) with Nova 2 Lite model."""
        response = bedrock_client.invoke_model(
            model_id="us.amazon.nova-2-lite-v1:0",
            system_prompt="You are a helpful assistant.",
            content=[{"text": "Say yes or no."}],
            max_tokens=5,
        )

        assert response is not None
        assert "output" in response
