# Matching Algorithm Design

## Purpose
Pairs anonymous submissions with reviewers in a fair, unbiased way while respecting configurable constraints.

## Architecture
- **Isolated Rust microservice** (containerized)
- Exposes simple HTTP endpoint: `POST /match`
- Stateless - takes input, returns assignments, no storage
- Called by C# API after anonymization is complete

## Input
```json
{
  "submissions": [
    {
      "id": "anon-sub-001",
      "skillLevel": 2,
      "metadata": {}
    }
  ],
  "reviewers": [
    {
      "id": "user-456",
      "availableSlots": 3,
      "reputation": 4.2,
      "skillLevel": 2
    }
  ],
  "config": {
    "reviewsPerSubmission": 3,
    "reviewsPerReviewer": 3,
    "skillMatching": "Any",  // "Similar", "Mixed", "Any"
    "distributeQuality": false,
    "allowRepeatPairings": false
  }
}
```

## Output
```json
{
  "assignments": [
    {
      "submissionId": "anon-sub-001",
      "reviewers": ["user-456", "user-789", "user-321"]
    }
  ],
  "unassigned": [],
  "errors": []
}
```

## Algorithm (Sprint 1 - Greedy Approach)

### Pseudocode
```
1. Shuffle submissions randomly (ensures fairness)
2. For each submission:
   a. Find reviewers with available capacity
   b. Filter out invalid reviewers:
      - Can't review their own submission
      - Already at capacity
      - Violates config constraints
   c. Select R reviewers randomly from valid pool
   d. Decrement their available slots
   e. Record assignment
3. Flag any submissions that couldn't get full reviews
4. Return assignments + errors
```

### Constraints

**Hard (must satisfy):**
- Reviewers can't review their own work
- Can't exceed reviewer capacity
- Must assign exactly `reviewsPerSubmission` reviewers (or flag as error)

**Soft (optimize for, Sprint 2):**
- Balance workload evenly across reviewers
- Distribute high-reputation reviewers fairly
- Match skill levels per config
- Prevent gaming/patterns

## Sprint 2 Enhancement (If Time)
Upgrade to **bipartite graph matching** using `petgraph` crate:
- Model as graph (submissions ↔ reviewers)
- Use Hungarian algorithm for optimal assignment
- Better handles edge cases and constraint optimization

## Edge Cases to Handle
- Not enough reviewers (10 submissions, 5 reviewers)
- Uneven numbers (31 submissions × 3 reviews each)
- Small cohorts (everyone would review everyone)
- Conflicting constraints (impossible to satisfy config)

## Why Rust?
- Performance matters (potentially hundreds of submissions)
- Isolated, pure function (clean inputs/outputs)
- Good learning opportunity for algorithms + systems programming
- Easy to test independently of main API

## Integration
C# API calls matcher after anonymization:
```csharp
var matcherResponse = await httpClient.PostAsync(
    "http://matcher:8080/match", 
    new StringContent(JsonSerializer.Serialize(matcherInput))
);
```

Matcher doesn't know real identities - just IDs and metadata.

## Fallback Plan
If Rust implementation falls behind, can rewrite same algorithm in C# over a weekend. Interface stays identical.
