## Scenario 1

### Asset

- The daily CSV report containing customer account balances
### Entry Point

- Analysts access the file for their analysis     
### Weak Spot

- Access is over supplied, analysts are able to see information they shouldn't be able to
### Damage

- Personal information is accessible by people who shouldn't have access to. The reports contain other balance information that should've been kept confidential. This increases the risk of protected data being leaked.

## Scenario 2

### Asset

- The linux config file
### Entry Point

- The linux service that reads the config file
### Weak Spot

- Permissions are incorrectly applied, are elevated without a time constraint. 
### Damage

- Poorly configured config files cause environment to not have the right configuration, enabling features in some and not in others.

## Scenario 3

### Asset

- The data pipeline that produces files for downstream processes.
### Entry Point
- 
### Weak Spot
### Damage