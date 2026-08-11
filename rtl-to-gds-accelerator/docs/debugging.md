# Physical-design debugging

The surviving project record confirms that DRC/LVS issues were resolved, but the exact violations and fixes were lost. Inventing rule names or a timing-closure sequence would be misleading.

For new reruns, record real cases in this format:

### Problem
Exact violation/timing/congestion symptom and affected stage.

### Root cause
Specific geometry, connectivity, constraint, fanout, placement, or routing cause supported by a report/layout view.

### Diagnosis
Tool/report command and a compact evidence excerpt.

### Fix
Concrete RTL/constraint/floorplan/placement/routing change.

### Regression prevention
The sign-off or automated report check that catches recurrence.
