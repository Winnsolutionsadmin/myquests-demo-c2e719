# myquests-demo (public web demo)

## UPSTREAM SOURCE OF TRUTH
This repo is a PUBLIC, backend-free static build (GitHub Pages) of the MyQuests
family chore-RPG. It is a DOWNSTREAM MIRROR — the canonical source auto-loads via
the operator's local ~/.claude registry and is deliberately not committed here
because this repo is public. Do not edit built assets here by hand.

The demo runs entirely client-side (VITE_DEMO): a seeded in-memory store backs a
fetch shim, so there is NO backend and NO real family data — the three heroes
(Robin/Sky/Sage) are fictional. State is ephemeral and resets on reload.
