# Insurance Agent Skills — Narration Script

## 000_title

Welcome to Insurance Agent Skills. This video walks through all thirty-nine skills: when to use each one, and how to pair it with other skills on a real insurance desk.

## 001_install

To install in Claude Code, add the letslego insurance-agent-skills marketplace, install the insurance-agent-skills plugin, and reload plugins. In Codex or Cursor, run npx skills latest add letslego insurance-agent-skills. After install, start with ask-insurance.

## 002_pack_knowledge

Next, Knowledge & routing. 4 skills. These skills help you route work, cite manuals, coach people, and hand off cases cleanly.

## 003_agent-coaching

Agent Coaching. Use this when reviewing a mishandled file or teaching a better pattern. Turn an insurance case into coaching for agents or adjusters.  Pair it with interaction-qa-scoring, handoff-brief, complaint-escalation.

## 004_ask-insurance

Ask Insurance. Use this when unsure which insurance skill to run across underwriting, claims, customer, compliance, or analytics. Router for all insurance desk skills.  Pair it with ask-underwriter, fnol-intake, quote-explanation.

## 005_guideline-cite

Guideline Cite. Use this when looking up UW, claims, or servicing rules and you need cited answers. Answer from insurance guidelines/manuals with citations.  Pair it with ask-insurance, risk-appetite-check, fair-claims-check.

## 006_handoff-brief

Handoff Brief. Use this when transferring between UW, claims, retention, SIU, or supervisors. Compact an insurance case into a handoff brief across teams.  Pair it with underwrite-submission, fnol-intake, complaint-escalation.

## 007_pack_underwriting

Next, Underwriting. 12 skills. These skills walk a submission from appetite and exposure through price, authority, and a written decision.

## 008_ask-underwriter

Ask Underwriter. Use this when the user is unsure which underwriting workflow to run, or asks what skill fits a submission, renewal, referral, pricing, or decline question. Router for insurance underwriting skills.  Pair it with underwrite-submission, ask-insurance.

## 009_broker-rfi

Broker RFI. Use this when the submission is incomplete or clarification is needed before quoting. Draft broker RFIs and missing-information requests for underwriting.  Pair it with underwrite-submission, coverage-terms-review.

## 010_coverage-terms-review

Coverage Terms Review. Use this when checking policy structure, endorsements, exclusions, deductibles, or comparing requested vs recommended wording. Review insurance coverage terms, forms, limits, and gaps.  Pair it with pricing-rationale, underwriting-decision-memo, broker-rfi.

## 011_financial-strength-review

Financial Strength Review. Use this when analyzing financials, credit risk, bankruptcy risk, or ability to fund retentions and risk control. Review insured financial strength for underwriting.  Pair it with coverage-terms-review, underwrite-submission.

## 012_hazard-exposure-analysis

Hazard & Exposure Analysis. Use this when reviewing property schedules, locations, occupancy, protection, or casualty operations hazards. Analyze insurance hazards and exposures (COPE, CAT, operations).  Pair it with coverage-terms-review, pricing-rationale, catastrophe-event-brief.

## 013_loss-history-triage

Loss History Triage. Use this when analyzing frequency, severity, large losses, trends, or open claims for underwriting. Triage insurance loss runs and claims history.  Pair it with pricing-rationale, underwrite-submission, hazard-exposure-analysis.

## 014_pricing-rationale

Pricing Rationale. Use this when explaining rate, credits and debits, technical vs market premium, or competitive positioning on a quote. Build insurance pricing and rating rationale.  Pair it with renewal-comparison, underwriting-decision-memo, risk-appetite-check.

## 015_referral-authority

Referral & Authority. Use this when deciding if a file needs referral, exceeds desk authority, or can be bound within authority. Check underwriting authority and referral triggers.  Pair it with underwriting-decision-memo, handoff-brief.

## 016_renewal-comparison

Renewal Comparison. Use this when renewing an account, explaining rate change, or checking coverage drift year over year. Compare expiring insurance terms to renewal proposal.  Pair it with pricing-rationale, coverage-terms-review, nonrenew-rationale.

## 017_risk-appetite-check

Risk Appetite Check. Use this when asking if a class, industry, geography, or account is in appetite, prohibited, or referral-only. Check a risk against underwriting appetite and guidelines.  Pair it with underwrite-submission, referral-authority, guideline-cite.

## 018_underwrite-submission

Underwrite Submission. Use this when reviewing a new or renewal submission, binding a quote package, or walking a risk from intake through decision. End-to-end insurance submission underwriting.  Pair it with risk-appetite-check, loss-history-triage, pricing-rationale.

## 019_underwriting-decision-memo

Underwriting Decision Memo. Use this when documenting rationale, subjectivities, or communicating a UW decision. Write an underwriting decision memo (quote, modify, decline, refer).  Pair it with broker-rfi, referral-authority, underwrite-submission.

## 020_pack_claims

Next, Claims. 7 skills. These skills cover intake, coverage, liability, severity, fraud screening, recovery, and customer updates.

## 021_claims-status-update

Claims Status Update. Use this when writing status notes, customer emails, or next-step explanations. Draft clear claim status updates for customers or diaries.  Pair it with complaint-escalation, coverage-determination.

## 022_coverage-determination

Coverage Determination. Use this when deciding if a loss is covered, excluded, limited, or needs reservation of rights / coverage counsel. Map claim facts to policy coverage language.  Pair it with liability-assessment, claims-status-update, guideline-cite.

## 023_fnol-intake

FNOL Intake. Use this when capturing a new claim, missing FNOL facts, or turning a messy call/chat into a complete loss notice. Structure first notice of loss (FNOL) intake.  Pair it with coverage-determination, severity-triage, fraud-red-flags.

## 024_fraud-red-flags

Fraud Red Flags (SIU Screen). Use this when patterns look staged, inconsistent, or organized — without accusing the customer. Screen claims for SIU / fraud referral indicators.  Pair it with handoff-brief, fnol-intake, liability-assessment.

## 025_liability-assessment

Liability Assessment. Use this when evaluating fault, evidence gaps, or settlement posture. Assess liability and comparative negligence on auto/property claims.  Pair it with subrogation-scan, severity-triage, claims-status-update.

## 026_severity-triage

Severity Triage. Use this when estimating severity, assigning appraiser/DRP, or spotting complex claims. Triage claim severity: repair vs total loss, rental, and handling track.  Pair it with repair-network-qa, claims-status-update, fnol-intake.

## 027_subrogation-scan

Subrogation Opportunity Scan. Use this when another party, product, or carrier may be liable for recovery. Scan a claim for subrogation / recovery opportunity.  Pair it with liability-assessment, handoff-brief.

## 028_pack_customer

Next, Customer & sales. 5 skills. These skills help explain price, counsel on coverages, handle endorsements, de-escalate complaints, and save policies.

## 029_complaint-escalation

Complaint & Escalation Handling. Use this when a customer is upset, files a complaint, or asks for a supervisor. Handle customer complaints and escalations with clear issue framing.  Pair it with claims-status-update, retention-save, regulatory-complaint-response.

## 030_coverage-counseling

Coverage Counseling. Use this when helping choose limits, deductibles, or optional coverages. Counsel customers on personal lines coverage choices and tradeoffs.  Pair it with quote-explanation, endorsement-impact, household-risk.

## 031_endorsement-impact

Endorsement Impact. Use this when adding/removing a driver, vehicle, address, or coverage mid-term. Explain the impact of policy endorsement changes.  Pair it with mvr-clue-review, quote-explanation, risk-appetite-check.

## 032_quote-explanation

Quote Explanation. Use this when a customer asks why the price is what it is or why it changed. Explain an insurance quote or premium change in plain language.  Pair it with coverage-counseling, retention-save, endorsement-impact.

## 033_retention-save

Retention Save. Use this when a customer wants to cancel or shop away. Run a retention / save conversation within guidelines.  Pair it with quote-explanation, coverage-counseling, handoff-brief.

## 034_pack_personal-lines

Next, Personal lines. 4 skills. These skills interpret reports, telematics, household risk, and non-renewal rationale.

## 035_household-risk

Household Risk. Use this when bundling auto/home/renters or reviewing multi-driver households. Assess household / multi-policy personal lines risk.  Pair it with coverage-counseling, underwrite-submission, retention-save.

## 036_mvr-clue-review

MVR / CLUE Review. Use this when reviewing violations, accidents, or prior claims. Interpret MVR and CLUE / claims-history reports for personal lines underwriting.  Pair it with risk-appetite-check, nonrenew-rationale, telematics-review.

## 037_nonrenew-rationale

Non-Renew Rationale. Use this when explaining why a personal lines policy is being non-renewed or restricted. Draft renewal non-renewal or adverse action rationale.  Pair it with renewal-comparison, mvr-clue-review, guideline-cite.

## 038_telematics-review

Telematics Review. Use this when discussing driving scores, trips, or UBI discounts. Review telematics / usage-based insurance signals for underwriting or customer explanation.  Pair it with quote-explanation, mvr-clue-review, pricing-rationale.

## 039_pack_compliance

Next, Compliance & QA. 4 skills. These skills support regulator responses, fair-claims audits, repair-network QA, and interaction scoring.

## 040_fair-claims-check

Fair Claims Process Check. Use this when auditing claim handling for delays, communication gaps, or compliance risk. Run a fair-claims / unfair-practices process checklist.  Pair it with claims-status-update, regulatory-complaint-response.

## 041_interaction-qa-scoring

Interaction QA Scoring. Use this when reviewing agent/adjuster conversations for coaching or audit. Score call or chat interactions against QA and compliance rubrics.  Pair it with agent-coaching, complaint-escalation.

## 042_regulatory-complaint-response

Regulatory Complaint Response. Use this when preparing regulator correspondence or complaint files. Draft responses to regulatory / DOI-style insurance complaints.  Pair it with fair-claims-check, complaint-escalation, handoff-brief.

## 043_repair-network-qa

Repair Network QA. Use this when reviewing DRP estimates, supplements, or shop disputes. QA repair network / body shop estimates against standards.  Pair it with severity-triage, claims-status-update.

## 044_pack_analytics

Next, Analytics & ops. 3 skills. These skills turn exhibits and results into filing narratives, loss-ratio diagnosis, and catastrophe briefs.

## 045_catastrophe-event-brief

Catastrophe Event Brief. Use this when a CAT is approaching or has hit and teams need exposure, claims surge, and playbook actions. Produce catastrophe event operating briefs.  Pair it with fnol-intake, hazard-exposure-analysis, claims-status-update.

## 046_loss-ratio-investigation

Loss Ratio Investigation. Use this when lR worsens and you need drivers and next analyses. Investigate loss ratio deterioration by segment.  Pair it with rate-filing-narrative, pricing-rationale, catastrophe-event-brief.

## 047_rate-filing-narrative

Rate Filing Narrative. Use this when explaining indicated rate need, support, or filing talking points. Draft plain-language rate filing narratives from exhibits.  Pair it with loss-ratio-investigation, guideline-cite.

## 999_closing

That is the full Insurance Agent Skills pack. Start with ask-insurance, keep your carrier guidelines in context, and chain focused skills instead of one giant prompt. Documentation lives at letslego dot github dot i o slash insurance-agent-skills.
