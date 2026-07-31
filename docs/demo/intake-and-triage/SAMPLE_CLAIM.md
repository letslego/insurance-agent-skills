# Sample claim packet — intake-and-triage demo

Use this fictional file when recording the demo. **Not a real claim.**

## Call notes (messy intake)

```text
Caller: Jordan Lee, policyholder
Policy: PA-4482910-22 (personal auto)
Phone: 555-0148
Loss date: Saturday ~9:40pm
Location: parking lot behind Metro Grocery, 1800 Harbor St

Says another car backed into their 2022 Honda Civic while they were inside the store.
Came out, other driver was there — dark gray SUV, maybe Toyota. Other driver gave name
"Chris Morgan", phone number on a napkin, no insurance card photo. License plate
partially remembered: state unknown, starts with "7X".

Front bumper cover cracked, left headlight out, airbags did NOT deploy. Civic is
driveable but headlight is dark. No police called. No injuries reported.
Caller wants a rental "just in case" and asked how fast glass/body work happens.

Odd notes from CSR:
- Caller first said loss was Friday, then corrected to Saturday
- Same phone number appears on a glass claim from 3 weeks ago under a different
  policyholder name in another state (flag from internal search — verify)
- Photos were promised "tonight" but not received yet
```

## Policy snapshot (excerpt)

```text
Named insured: Jordan Lee
Policy period: 01/01/2026 – 01/01/2027
Vehicle: 2022 Honda Civic, VIN demo-only
Coverages:
  - Liability BI/PD: 100/300/100
  - Comprehensive: $500 ded
  - Collision: $1,000 ded
  - Rental reimbursement: $30/day, 30-day max
  - Roadside: included
Endorsements on file: none for business use
Territory: in-state
```

## Demo prompt to paste after install

```text
/intake-and-triage

Use the sample claim in docs/demo/intake-and-triage/SAMPLE_CLAIM.md.
Walk the full intake-and-triage workflow:
1) collect claim details
2) verify coverage
3) detect fraud signals
4) route / escalate
Show which skill you are using at each step. Do not invent policy language beyond the excerpt.
```
