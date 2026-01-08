## Scenario 1

### Asset

- The daily CSV report containing customer account balances.

### Entry Point

- Staff members download the report from the shared directory for support questions.

### Weak Spot

- Access is over supplied, analysts are able to see information they shouldn't be able to
### Damage

- Personal information is accessible by people who shouldn't have access to. The reports contain other balance information that should've been kept confidential. This increases the risk of protected data being leaked. 

### CIA: 

- Confidentiality 

## Scenario 2

### Asset

- The linux config file
### Entry Point

- The linux service that reads the config file
### Weak Spot

- The configuration directory permissions allow write access to non-admin users.

### Damage

- Poorly configured config files cause environment to not have the right configuration, enabling features in some and not in others.

## Scenario 3

### Asset

- The deprecated pipeline binary.

### Entry Point

- The scheduled validation task executes the binary.

### Weak Spot

- The deprecated pipeline binary exists on the host file system.

### Damage

- Transformed values show discrepancies compared to expected output.

### CIA: 

- Integrity