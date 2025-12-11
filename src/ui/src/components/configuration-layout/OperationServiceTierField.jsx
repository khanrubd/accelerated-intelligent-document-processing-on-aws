// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

import React from 'react';
import { FormField, Select } from '@cloudscape-design/components';
import { SERVICE_TIER_OPERATION_OPTIONS, SERVICE_TIER_HELP_TEXT } from '../../constants/configTypes';

/**
 * Operation-Specific Service Tier Field
 *
 * Allows users to override the global service tier for a specific operation.
 * Null value means "use global default".
 */
const OperationServiceTierField = ({ value, onChange, globalTier = 'standard' }) => {
  const effectiveTier = value || globalTier;

  const handleChange = ({ detail }) => {
    onChange(detail.selectedOption.value);
  };

  return (
    <FormField
      label="Service Tier Override"
      description={`${SERVICE_TIER_HELP_TEXT.operation} Current effective tier: ${effectiveTier}`}
    >
      <Select
        selectedOption={SERVICE_TIER_OPERATION_OPTIONS.find((opt) => opt.value === value)}
        onChange={handleChange}
        options={SERVICE_TIER_OPERATION_OPTIONS}
        placeholder="Select service tier override"
      />
    </FormField>
  );
};

export default OperationServiceTierField;
