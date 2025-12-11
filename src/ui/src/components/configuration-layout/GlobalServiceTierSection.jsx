// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

import React from 'react';
import PropTypes from 'prop-types';
import { FormField, Select } from '@cloudscape-design/components';
import { SERVICE_TIER_OPTIONS, SERVICE_TIER_HELP_TEXT } from '../../constants/configTypes';

/**
 * Global Service Tier Configuration Section
 *
 * Allows users to set the default service tier for all Bedrock API calls.
 * Can be overridden at the operation level (classification, extraction, etc.)
 */
const GlobalServiceTierSection = ({ configuration, onConfigChange }) => {
  const currentTier = configuration?.service_tier || 'standard';

  const handleServiceTierChange = ({ detail }) => {
    onConfigChange({
      ...configuration,
      service_tier: detail.selectedOption.value,
    });
  };

  return (
    <FormField
      label="Service Tier (Global Default)"
      description={SERVICE_TIER_HELP_TEXT.global}
      info={
        <a
          href="https://docs.aws.amazon.com/bedrock/latest/userguide/service-tiers-inference.html"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn more about service tiers
        </a>
      }
    >
      <Select
        selectedOption={SERVICE_TIER_OPTIONS.find((opt) => opt.value === currentTier)}
        onChange={handleServiceTierChange}
        options={SERVICE_TIER_OPTIONS}
        placeholder="Select service tier"
      />
    </FormField>
  );
};

GlobalServiceTierSection.propTypes = {
  configuration: PropTypes.shape({
    service_tier: PropTypes.string,
  }).isRequired,
  onConfigChange: PropTypes.func.isRequired,
};

export default GlobalServiceTierSection;
