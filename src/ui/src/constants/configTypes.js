// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

/**
 * Configuration type constants.
 *
 * These constants define the valid configuration types used throughout the system.
 * Use these instead of hardcoded strings to ensure consistency with backend.
 *
 * IMPORTANT: These must match the values in:
 * lib/idp_common_pkg/idp_common/config/constants.py
 */

// Configuration Types
export const CONFIG_TYPE_SCHEMA = 'Schema';
export const CONFIG_TYPE_DEFAULT = 'Default';
export const CONFIG_TYPE_CUSTOM = 'Custom';

// All valid configuration types
export const VALID_CONFIG_TYPES = [CONFIG_TYPE_SCHEMA, CONFIG_TYPE_DEFAULT, CONFIG_TYPE_CUSTOM];

// Service Tier Constants
export const SERVICE_TIER_PRIORITY = 'priority';
export const SERVICE_TIER_STANDARD = 'standard';
export const SERVICE_TIER_FLEX = 'flex';

export const SERVICE_TIER_OPTIONS = [
  { label: 'Standard (Default)', value: SERVICE_TIER_STANDARD },
  { label: 'Priority (Fastest)', value: SERVICE_TIER_PRIORITY },
  { label: 'Flex (Cost-Effective)', value: SERVICE_TIER_FLEX },
];

export const SERVICE_TIER_OPERATION_OPTIONS = [
  { label: 'Use Global Default', value: null },
  { label: 'Priority (Fastest)', value: SERVICE_TIER_PRIORITY },
  { label: 'Standard', value: SERVICE_TIER_STANDARD },
  { label: 'Flex (Cost-Effective)', value: SERVICE_TIER_FLEX },
];

export const SERVICE_TIER_HELP_TEXT = {
  global:
    'Choose the default service tier for all Bedrock API calls. Priority offers fastest response times at premium pricing, Standard provides consistent performance, and Flex offers cost savings with longer latency.',
  operation:
    'Override the global service tier for this specific operation. Select "Use Global Default" to inherit the global setting.',
};
