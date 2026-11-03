# Interaction completeness

Read when implementing controls or changing a workflow. Scope states to the actual
task; a text-only section does not need artificial loading states.

## Controls

Use native link/button semantics and clear outcomes. Supply default, hover where
supported, focus-visible, pressed, disabled, and pending states when relevant.
Focus remains visible while hovered. Disabled appearance must match behavior;
explain restrictions when their reason is unclear. Read-only data stays copyable.

During submission keep a meaningful label, stable width, and protection against
duplicate submissions. Show success after the operation succeeds. On failure,
restore a useful retry path. Color or a spinner alone is insufficient feedback.

## Inputs

Provide persistent labels; distinguish required, optional, disabled, and read-only.
Place helper/error text beside the field and connect it with `aria-describedby`.
Use `aria-invalid` for invalid values, native types, and appropriate autocomplete.

Choose validation timing to fit the form. Usually check on blur/submit and revalidate
corrections without trapping the person in an error. Preserve entered data after
failure. Client validation improves feedback; real submissions still require server
checks. A frontend simulation cannot prove an email was delivered or data secured.

## Async regions

| State | Behavior |
| --- | --- |
| Loading | Identify the pending operation and preserve surrounding layout. |
| Empty | Distinguish no data yet from no results; give a useful next action. |
| Error | Name the failed operation, retain useful data, and offer recovery. |
| Success | Confirm completion without repeated announcements. |
| Partial/stale | Keep known data usable and explain what failed to refresh. |

Use polite announcements and `aria-busy` where appropriate. Do not move keyboard
focus to every status message. Dialogs need a name, focus management, dismissal,
and focus return. Verify behavior rather than relying on visual resemblance.

Respect reduced motion, touch, zoom, and long labels. Phone controls cannot depend
on hover. Apply the system's control dimensions and suitable touch targets rather
than treating a small visible icon as the entire hit area.
