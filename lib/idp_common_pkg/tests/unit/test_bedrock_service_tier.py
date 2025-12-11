# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Unit tests for BedrockClient service_tier functionality."""

from unittest.mock import MagicMock

import pytest
from idp_common.bedrock.client import BedrockClient


@pytest.mark.unit
class TestBedrockClientServiceTier:
    """Test service tier parameter handling in BedrockClient."""

    @pytest.fixture
    def mock_bedrock_response(self):
        """Mock Bedrock API response."""
        return {
            "output": {"message": {"content": [{"text": "test response"}]}},
            "usage": {
                "inputTokens": 100,
                "outputTokens": 50,
                "totalTokens": 150,
            },
        }

    @pytest.fixture
    def bedrock_client(self):
        """Create BedrockClient instance with mocked boto3 client."""
        client = BedrockClient(region="us-west-2", metrics_enabled=False)
        # Pre-initialize the client with a mock
        client._client = MagicMock()
        return client

    def test_service_tier_priority(self, bedrock_client, mock_bedrock_response):
        """Test priority service tier is passed to API."""
        bedrock_client._client.converse.return_value = mock_bedrock_response

        bedrock_client.invoke_model(
            model_id="us.amazon.nova-pro-v1:0",
            system_prompt="test",
            content=[{"text": "test"}],
            service_tier="priority",
        )

        # Verify serviceTier was passed to API
        call_args = bedrock_client._client.converse.call_args
        assert "serviceTier" in call_args.kwargs
        assert call_args.kwargs["serviceTier"] == "priority"

    def test_service_tier_standard_normalized(
        self, bedrock_client, mock_bedrock_response
    ):
        """Test standard is normalized to default for API."""
        bedrock_client._client.converse.return_value = mock_bedrock_response

        bedrock_client.invoke_model(
            model_id="us.amazon.nova-pro-v1:0",
            system_prompt="test",
            content=[{"text": "test"}],
            service_tier="standard",
        )

        # Verify serviceTier was normalized to "default"
        call_args = bedrock_client._client.converse.call_args
        assert "serviceTier" in call_args.kwargs
        assert call_args.kwargs["serviceTier"] == "default"

    def test_service_tier_flex(self, bedrock_client, mock_bedrock_response):
        """Test flex service tier is passed to API."""
        bedrock_client._client.converse.return_value = mock_bedrock_response

        bedrock_client.invoke_model(
            model_id="us.amazon.nova-pro-v1:0",
            system_prompt="test",
            content=[{"text": "test"}],
            service_tier="flex",
        )

        # Verify serviceTier was passed to API
        call_args = bedrock_client._client.converse.call_args
        assert "serviceTier" in call_args.kwargs
        assert call_args.kwargs["serviceTier"] == "flex"

    def test_service_tier_none(self, bedrock_client, mock_bedrock_response):
        """Test None service tier is not passed to API."""
        bedrock_client._client.converse.return_value = mock_bedrock_response

        bedrock_client.invoke_model(
            model_id="us.amazon.nova-pro-v1:0",
            system_prompt="test",
            content=[{"text": "test"}],
            service_tier=None,
        )

        # Verify serviceTier was not passed to API
        call_args = bedrock_client._client.converse.call_args
        assert "serviceTier" not in call_args.kwargs

    def test_service_tier_invalid(self, bedrock_client, mock_bedrock_response):
        """Test invalid service tier is rejected with warning."""
        bedrock_client._client.converse.return_value = mock_bedrock_response

        bedrock_client.invoke_model(
            model_id="us.amazon.nova-pro-v1:0",
            system_prompt="test",
            content=[{"text": "test"}],
            service_tier="invalid",
        )

        # Verify serviceTier was not passed to API (invalid value)
        call_args = bedrock_client._client.converse.call_args
        assert "serviceTier" not in call_args.kwargs

    def test_service_tier_case_insensitive(self, bedrock_client, mock_bedrock_response):
        """Test service tier is case-insensitive."""
        bedrock_client._client.converse.return_value = mock_bedrock_response

        bedrock_client.invoke_model(
            model_id="us.amazon.nova-pro-v1:0",
            system_prompt="test",
            content=[{"text": "test"}],
            service_tier="PRIORITY",
        )

        # Verify serviceTier was normalized to lowercase
        call_args = bedrock_client._client.converse.call_args
        assert call_args.kwargs["serviceTier"] == "priority"

    def test_service_tier_default_alias(self, bedrock_client, mock_bedrock_response):
        """Test 'default' is accepted as alias for 'standard'."""
        bedrock_client._client.converse.return_value = mock_bedrock_response

        bedrock_client.invoke_model(
            model_id="us.amazon.nova-pro-v1:0",
            system_prompt="test",
            content=[{"text": "test"}],
            service_tier="default",
        )

        # Verify serviceTier was passed as "default"
        call_args = bedrock_client._client.converse.call_args
        assert call_args.kwargs["serviceTier"] == "default"
