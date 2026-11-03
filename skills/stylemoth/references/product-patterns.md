# Product structure and journeys

## Match structure to the job

| Surface | Decisions to resolve |
| --- | --- |
| Marketing page | Offer, audience, credible evidence, useful next action, unanswered objections. |
| Dashboard | Main recurring task, useful summary, data depth, filters, navigation, drill-down. |
| Search or collection | Query, refinements, result identity, comparison, detail, no-results recovery. |
| Settings | Current values, edit scope, save semantics, validation, destructive boundaries. |
| Pricing | Comparable offer, billing period, inclusions, limits, actual purchase destination. |
| Form | Minimum necessary data, labels, help, validation timing, submission, recovery. |

These are questions, not mandatory sections. A pricing concept does not justify
inventing a paid plan. A dashboard demo does not justify fabricated business
results. Preserve the user's source content and disclose example data.

## Map state transitions

For a multi-step task, note:

```text
Entry: where the person starts and what is already known.
Decision: the choice or input needed now.
Response: immediate feedback and any pending operation.
Failure: what remains saved and how the person retries or goes back.
Completion: the confirmed result and next useful destination.
```

Use the fewest steps that keep decisions understandable. A step number is useful
for a real sequence, not decoration on unrelated features. Show progress when it
helps the person predict effort. Preserve input when moving backward or recovering
from failure. Explain consequences near irreversible actions.

Authentication, payment, sharing, and destructive operations need real service
behavior to be called complete. A prototype can demonstrate the sequence using
explicit simulation, but cannot pretend that sign-in, a charge, or deletion occurred.

## Content stays beside its decision

Put price changes beside quantity or billing controls. Put validation beside its
field. Place selection context beside the action operating on it. Avoid sending
people between distant panels to understand a single choice.

One primary action per decision is a useful starting point, not a ban on secondary
actions. Keep escape, back, cancel, and recovery paths discoverable. Use labels
that predict the outcome and keep the action name consistent across its states.

## Adapt to mobile without losing the task

Reorder by meaningful reading and interaction order. Keep essential actions and
values. Convert independent table records into labeled items when suitable; retain
contained scrolling where cross-column comparison matters. Do not hide required
controls because they are inconvenient at small widths.

Test long labels, no data, validation messages, and slow responses when those
states are relevant. For review from a single image, distinguish visible evidence
from behaviors that need implementation or testing to assess.
