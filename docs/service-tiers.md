# Amazon Bedrock Service Tiers

The GenAI IDP solution supports Amazon Bedrock service tiers, allowing you to optimize for performance and cost by selecting different service tiers for model inference operations.

## Overview

Amazon Bedrock offers three service tiers for on-demand inference:

| Tier | Performance | Cost | Best For |
|------|-------------|------|----------|
| **Priority** | Fastest response times | Premium pricing (~25% more) | Customer-facing workflows, real-time interactions |
| **Standard** | Consistent performance | Regular pricing | Everyday AI tasks, content generation |
| **Flex** | Variable latency | Discounted pricing | Batch processing, evaluations, non-urgent workloads |

## Configuration

### Global Service Tier

Set a default service tier for all operations in your configuration:

```yaml
# Global default applies to all operations
service_tier: "standard"
```

### Operation-Specific Overrides

Override the global setting for specific operations:

```yaml
# Global default
service_tier: "standard"

# Operation-specific overrides
classification:
  service_tier: "priority"  # Fast classification for real-time workflows
  model: "us.amazon.nova-pro-v1:0"
  # ... other settings

extraction:
  service_tier: "flex"  # Cost-effective extraction for batch processing
  model: "us.amazon.nova-pro-v1:0"
  # ... other settings

assessment:
  service_tier: null  # null = use global default (standard)
  # ... other settings

summarization:
  service_tier: "flex"  # Summarization can tolerate longer latency
  # ... other settings
```

### Valid Values

- `"priority"` - Fastest response times, premium pricing
- `"standard"` - Default tier, consistent performance (also accepts `"default"`)
- `"flex"` - Cost-effective, longer latency
- `null` or omitted - Uses global default or "standard" if no global set

## Web UI Configuration

### Global Service Tier

1. Navigate to the Configuration page
2. Find the "Service Tier (Global Default)" dropdown near the top
3. Select your preferred tier:
   - **Standard (Default)** - Consistent performance
   - **Priority (Fastest)** - Premium speed
   - **Flex (Cost-Effective)** - Budget-friendly
4. Changes save automatically

### Operation-Specific Overrides

Within each operation section (Classification, Extraction, Assessment, Summarization):

1. Find the "Service Tier Override" dropdown
2. Select an option:
   - **Use Global Default** - Inherit global setting
   - **Priority (Fastest)** - Override with priority
   - **Standard** - Override with standard
   - **Flex (Cost-Effective)** - Override with flex
3. The UI shows the current effective tier

## CLI Usage

### Deployment

Specify service tier during stack deployment:

```bash
idp-cli deploy \
    --stack-name my-idp-stack \
    --pattern pattern-2 \
    --admin-email user@example.com \
    --service-tier flex
```

### Batch Processing

Override service tier for a specific batch:

```bash
idp-cli run-inference \
    --stack-name my-idp-stack \
    --dir ./documents/ \
    --service-tier priority \
    --monitor
```

**Note:** CLI service tier parameter sets the global default in configuration. For operation-specific control, use configuration files or the Web UI.

## Use Case Recommendations

### Priority Tier

**When to use:**
- Customer-facing chat assistants
- Real-time document processing
- Interactive AI applications
- Time-sensitive workflows

**Example configuration:**
```yaml
service_tier: "priority"  # All operations use priority
```

### Standard Tier

**When to use:**
- General document processing
- Content generation
- Text analysis
- Routine workflows

**Example configuration:**
```yaml
service_tier: "standard"  # Default, no configuration needed
```

### Flex Tier

**When to use:**
- Batch document processing
- Model evaluations
- Content summarization
- Non-urgent workflows
- Cost optimization

**Example configuration:**
```yaml
service_tier: "flex"  # All operations use flex

# Or mixed approach
service_tier: "standard"  # Global default
classification:
  service_tier: "priority"  # Fast classification
extraction:
  service_tier: "flex"  # Cost-effective extraction
```

## Mixed Tier Strategy

Optimize cost and performance by using different tiers for different operations:

```yaml
# Global default for most operations
service_tier: "standard"

# Fast classification for real-time user experience
classification:
  service_tier: "priority"
  model: "us.amazon.nova-pro-v1:0"

# Standard extraction (inherit global)
extraction:
  service_tier: null  # Uses global "standard"
  model: "us.amazon.nova-pro-v1:0"

# Cost-effective assessment (can tolerate latency)
assessment:
  service_tier: "flex"
  model: "us.amazon.nova-lite-v1:0"

# Cost-effective summarization (non-critical)
summarization:
  service_tier: "flex"
  model: "us.amazon.nova-premier-v1:0"
```

## Performance Expectations

### Priority Tier
- Up to 25% better output tokens per second (OTPS) latency vs standard
- Requests prioritized over other tiers
- Best for latency-sensitive applications

### Standard Tier
- Consistent baseline performance
- Suitable for most workloads
- Balanced cost and performance

### Flex Tier
- Variable latency (longer than standard)
- Pricing discount over standard
- Suitable for batch and background processing

## Cost Implications

- **Priority**: ~25% premium over standard pricing
- **Standard**: Regular on-demand pricing (baseline)
- **Flex**: Discounted pricing (varies by model)

Use the [AWS Pricing Calculator](https://calculator.aws/#/createCalculator/bedrock) to estimate costs for different service tiers.

## Monitoring

### CloudWatch Metrics

Service tier usage is tracked in CloudWatch metrics:
- Dimension: `ServiceTier` shows requested tier
- Dimension: `ResolvedServiceTier` shows actual tier that served the request

### CloudWatch Logs

Service tier information appears in Lambda function logs:
```
Using service tier: default
```

Look for this log message in:
- OCR function logs
- Classification function logs
- Extraction function logs
- Assessment function logs
- Summarization function logs

## Model Support

Not all models support all service tiers. Check the [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/service-tiers-inference.html) for current model support.

**Supported models include:**
- Amazon Nova models (Pro, Lite, Premier)
- Anthropic Claude models
- OpenAI models
- Qwen models
- DeepSeek models

## Troubleshooting

### Service Tier Not Applied

**Symptom:** Logs don't show service tier being used

**Solutions:**
1. Verify service_tier is set in configuration
2. Check for typos in tier name (must be: priority, standard, or flex)
3. Ensure configuration is saved and loaded correctly
4. Check CloudWatch logs for validation warnings

### Invalid Service Tier Warning

**Symptom:** Log shows "Invalid service_tier value"

**Solutions:**
1. Use only valid values: priority, standard, flex
2. Check for extra spaces or incorrect casing
3. Verify YAML syntax is correct

### Model Not Supported

**Symptom:** Bedrock API returns error about unsupported service tier

**Solutions:**
1. Check model supports the selected tier
2. Refer to AWS documentation for model support matrix
3. Fall back to standard tier for unsupported models

## Best Practices

1. **Start with Standard**: Use standard tier as baseline, then optimize
2. **Monitor Costs**: Track usage by tier in CloudWatch and AWS Cost Explorer
3. **Test Performance**: Compare latency across tiers for your workload
4. **Mixed Strategy**: Use priority for critical paths, flex for batch operations
5. **Document Decisions**: Note why specific tiers chosen for each operation

## Additional Resources

- [Amazon Bedrock Service Tiers User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/service-tiers-inference.html)
- [Service Tiers API Reference](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ServiceTier.html)
- [AWS Blog: Service Tiers Announcement](https://aws.amazon.com/blogs/aws/new-amazon-bedrock-service-tiers-help-you-match-ai-workload-performance-with-cost/)
- [AWS Pricing Calculator](https://calculator.aws/#/createCalculator/bedrock)
