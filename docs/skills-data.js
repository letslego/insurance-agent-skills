window.UNDERWRITER_SKILLS = [
  {
    "id": "agent-coaching",
    "name": "Agent Coaching",
    "command": "/agent-coaching",
    "pack": "knowledge",
    "blurb": "Turn an insurance case into coaching for agents or adjusters.",
    "when": "Reviewing a mishandled file or teaching a better pattern.",
    "output": "the learner has a practiceable behavior change, not just feedback adjectives."
  },
  {
    "id": "ask-insurance",
    "name": "Ask Insurance",
    "command": "/ask-insurance",
    "pack": "knowledge",
    "blurb": "Router for all insurance desk skills.",
    "when": "Unsure which insurance skill to run across underwriting, claims, customer, compliance, or analytics.",
    "output": "the user has a clear next skill."
  },
  {
    "id": "guideline-cite",
    "name": "Guideline Cite",
    "command": "/guideline-cite",
    "pack": "knowledge",
    "blurb": "Answer from insurance guidelines/manuals with citations.",
    "when": "Looking up UW, claims, or servicing rules and you need cited answers.",
    "output": "every normative statement has a citation or is marked unknown."
  },
  {
    "id": "handoff-brief",
    "name": "Handoff Brief",
    "command": "/handoff-brief",
    "pack": "knowledge",
    "blurb": "Compact an insurance case into a handoff brief across teams.",
    "when": "Transferring between UW, claims, retention, SIU, or supervisors.",
    "output": "the receiving team does not need to re-discover the thread."
  },
  {
    "id": "ask-underwriter",
    "name": "Ask Underwriter",
    "command": "/ask-underwriter",
    "pack": "underwriting",
    "blurb": "Router for insurance underwriting skills.",
    "when": "The user is unsure which underwriting workflow to run, or asks what skill fits a submission, renewal, referral, pricing, or decline question.",
    "output": "the user has a clear next skill and knows what to provide."
  },
  {
    "id": "broker-rfi",
    "name": "Broker RFI",
    "command": "/broker-rfi",
    "pack": "underwriting",
    "blurb": "Draft broker RFIs and missing-information requests for underwriting.",
    "when": "The submission is incomplete or clarification is needed before quoting.",
    "output": "every blocker question is answerable with a document or a yes/no, and the broker knows what unlocks a quote."
  },
  {
    "id": "coverage-terms-review",
    "name": "Coverage Terms Review",
    "command": "/coverage-terms-review",
    "pack": "underwriting",
    "blurb": "Review insurance coverage terms, forms, limits, and gaps.",
    "when": "Checking policy structure, endorsements, exclusions, deductibles, or comparing requested vs recommended wording.",
    "output": "a coherent terms sheet exists and every material gap has a recommendation or an explicit accept risk."
  },
  {
    "id": "financial-strength-review",
    "name": "Financial Strength Review",
    "command": "/financial-strength-review",
    "pack": "underwriting",
    "blurb": "Review insured financial strength for underwriting.",
    "when": "Analyzing financials, credit risk, bankruptcy risk, or ability to fund retentions and risk control.",
    "output": "posture and structure implications are explicit, with numbers cited from the file."
  },
  {
    "id": "hazard-exposure-analysis",
    "name": "Hazard & Exposure Analysis",
    "command": "/hazard-exposure-analysis",
    "pack": "underwriting",
    "blurb": "Analyze insurance hazards and exposures (COPE, CAT, operations).",
    "when": "Reviewing property schedules, locations, occupancy, protection, or casualty operations hazards.",
    "output": "the largest loss drivers are named and each has a concrete UW response."
  },
  {
    "id": "loss-history-triage",
    "name": "Loss History Triage",
    "command": "/loss-history-triage",
    "pack": "underwriting",
    "blurb": "Triage insurance loss runs and claims history.",
    "when": "Analyzing frequency, severity, large losses, trends, or open claims for underwriting.",
    "output": "the loss story can explain the last 3\u20135 years and each material implication has a recommended term or price response."
  },
  {
    "id": "pricing-rationale",
    "name": "Pricing Rationale",
    "command": "/pricing-rationale",
    "pack": "underwriting",
    "blurb": "Build insurance pricing and rating rationale.",
    "when": "Explaining rate, credits and debits, technical vs market premium, or competitive positioning on a quote.",
    "output": "another underwriter can see why this price is not a round number pulled from air."
  },
  {
    "id": "referral-authority",
    "name": "Referral & Authority",
    "command": "/referral-authority",
    "pack": "underwriting",
    "blurb": "Check underwriting authority and referral triggers.",
    "when": "Deciding if a file needs referral, exceeds desk authority, or can be bound within authority.",
    "output": "authority status is binary-clear and any referral has a crisp ask."
  },
  {
    "id": "renewal-comparison",
    "name": "Renewal Comparison",
    "command": "/renewal-comparison",
    "pack": "underwriting",
    "blurb": "Compare expiring insurance terms to renewal proposal.",
    "when": "Renewing an account, explaining rate change, or checking coverage drift year over year.",
    "output": "premium change is decomposed and coverage drift is explicit."
  },
  {
    "id": "risk-appetite-check",
    "name": "Risk Appetite Check",
    "command": "/risk-appetite-check",
    "pack": "underwriting",
    "blurb": "Check a risk against underwriting appetite and guidelines.",
    "when": "Asking if a class, industry, geography, or account is in appetite, prohibited, or referral-only.",
    "output": "every material appetite attribute is classified and the overall posture is unambiguous."
  },
  {
    "id": "underwrite-submission",
    "name": "Underwrite Submission",
    "command": "/underwrite-submission",
    "pack": "underwriting",
    "blurb": "End-to-end insurance submission underwriting.",
    "when": "Reviewing a new or renewal submission, binding a quote package, or walking a risk from intake through decision.",
    "output": "the user has a decision recommendation, key drivers, subjectivities/RFIs, and whether referral is required."
  },
  {
    "id": "underwriting-decision-memo",
    "name": "Underwriting Decision Memo",
    "command": "/underwriting-decision-memo",
    "pack": "underwriting",
    "blurb": "Write an underwriting decision memo (quote, modify, decline, refer).",
    "when": "Documenting rationale, subjectivities, or communicating a UW decision.",
    "output": "a peer can defend the same decision from the memo alone without re-reading the full submission."
  },
  {
    "id": "claims-status-update",
    "name": "Claims Status Update",
    "command": "/claims-status-update",
    "pack": "claims",
    "blurb": "Draft clear claim status updates for customers or diaries.",
    "when": "Writing status notes, customer emails, or next-step explanations.",
    "output": "both versions are consistent and the customer knows the next concrete step."
  },
  {
    "id": "coverage-determination",
    "name": "Coverage Determination",
    "command": "/coverage-determination",
    "pack": "claims",
    "blurb": "Map claim facts to policy coverage language.",
    "when": "Deciding if a loss is covered, excluded, limited, or needs reservation of rights / coverage counsel.",
    "output": "every material coverage question has a conclusion or a precise fact gap."
  },
  {
    "id": "fnol-intake",
    "name": "FNOL Intake",
    "command": "/fnol-intake",
    "pack": "claims",
    "blurb": "Structure first notice of loss (FNOL) intake.",
    "when": "Capturing a new claim, missing FNOL facts, or turning a messy call/chat into a complete loss notice.",
    "output": "another adjuster can open the claim without re-asking the basics already provided."
  },
  {
    "id": "fraud-red-flags",
    "name": "Fraud Red Flags (SIU Screen)",
    "command": "/fraud-red-flags",
    "pack": "claims",
    "blurb": "Screen claims for SIU / fraud referral indicators.",
    "when": "Patterns look staged, inconsistent, or organized \u2014 without accusing the customer.",
    "output": "a clear refer/monitor/clear decision exists with factual support."
  },
  {
    "id": "intake-and-triage",
    "name": "Intake and Triage",
    "command": "/intake-and-triage",
    "pack": "claims",
    "blurb": "End-to-end claim intake and triage agent.",
    "when": "Opening a new claim, stitching FNOL intake with coverage verification, fraud screening, and route/escalate decisions.",
    "output": "the claim has a coverage posture, fraud posture, handling track, and a named next owner (or a blocker list that explains why triage cannot finish)."
  },
  {
    "id": "liability-assessment",
    "name": "Liability Assessment",
    "command": "/liability-assessment",
    "pack": "claims",
    "blurb": "Assess liability and comparative negligence on auto/property claims.",
    "when": "Evaluating fault, evidence gaps, or settlement posture.",
    "output": "liability posture is explicit and every contested point has an evidence status."
  },
  {
    "id": "severity-triage",
    "name": "Severity Triage",
    "command": "/severity-triage",
    "pack": "claims",
    "blurb": "Triage claim severity: repair vs total loss, rental, and handling track.",
    "when": "Estimating severity, assigning appraiser/DRP, or spotting complex claims.",
    "output": "the claim has a clear next operational path within 24\u201348 hours."
  },
  {
    "id": "subrogation-scan",
    "name": "Subrogation Opportunity Scan",
    "command": "/subrogation-scan",
    "pack": "claims",
    "blurb": "Scan a claim for subrogation / recovery opportunity.",
    "when": "Another party, product, or carrier may be liable for recovery.",
    "output": "subro either has a pursuit plan or a documented reason not to pursue."
  },
  {
    "id": "complaint-escalation",
    "name": "Complaint & Escalation Handling",
    "command": "/complaint-escalation",
    "pack": "customer",
    "blurb": "Handle customer complaints and escalations with clear issue framing.",
    "when": "A customer is upset, files a complaint, or asks for a supervisor.",
    "output": "the customer has a next step and ownership is clear."
  },
  {
    "id": "coverage-counseling",
    "name": "Coverage Counseling",
    "command": "/coverage-counseling",
    "pack": "customer",
    "blurb": "Counsel customers on personal lines coverage choices and tradeoffs.",
    "when": "Helping choose limits, deductibles, or optional coverages.",
    "output": "the customer can state what they chose and what they declined."
  },
  {
    "id": "endorsement-impact",
    "name": "Endorsement Impact",
    "command": "/endorsement-impact",
    "pack": "customer",
    "blurb": "Explain the impact of policy endorsement changes.",
    "when": "Adding/removing a driver, vehicle, address, or coverage mid-term.",
    "output": "the customer knows what happens if the change is processed today."
  },
  {
    "id": "quote-explanation",
    "name": "Quote Explanation",
    "command": "/quote-explanation",
    "pack": "customer",
    "blurb": "Explain an insurance quote or premium change in plain language.",
    "when": "A customer asks why the price is what it is or why it changed.",
    "output": "a non-expert understands the \u201cwhy\u201d without feeling gaslit."
  },
  {
    "id": "retention-save",
    "name": "Retention Save",
    "command": "/retention-save",
    "pack": "customer",
    "blurb": "Run a retention / save conversation within guidelines.",
    "when": "A customer wants to cancel or shop away.",
    "output": "either a compliant save path is offered or a clean cancel handoff is prepared."
  },
  {
    "id": "household-risk",
    "name": "Household Risk",
    "command": "/household-risk",
    "pack": "personal-lines",
    "blurb": "Assess household / multi-policy personal lines risk.",
    "when": "Bundling auto/home/renters or reviewing multi-driver households.",
    "output": "the household story is coherent across lines."
  },
  {
    "id": "mvr-clue-review",
    "name": "MVR / CLUE Review",
    "command": "/mvr-clue-review",
    "pack": "personal-lines",
    "blurb": "Interpret MVR and CLUE / claims-history reports for personal lines underwriting.",
    "when": "Reviewing violations, accidents, or prior claims.",
    "output": "every report item has a disposition tied to a rule or an explicit gap."
  },
  {
    "id": "nonrenew-rationale",
    "name": "Non-Renew Rationale",
    "command": "/nonrenew-rationale",
    "pack": "personal-lines",
    "blurb": "Draft renewal non-renewal or adverse action rationale.",
    "when": "Explaining why a personal lines policy is being non-renewed or restricted.",
    "output": "the action can be defended from the cited facts and rules alone."
  },
  {
    "id": "telematics-review",
    "name": "Telematics Review",
    "command": "/telematics-review",
    "pack": "personal-lines",
    "blurb": "Review telematics / usage-based insurance signals for underwriting or customer explanation.",
    "when": "Discussing driving scores, trips, or UBI discounts.",
    "output": "customer or UW knows what the data implies and what can change next term."
  },
  {
    "id": "fair-claims-check",
    "name": "Fair Claims Process Check",
    "command": "/fair-claims-check",
    "pack": "compliance",
    "blurb": "Run a fair-claims / unfair-practices process checklist.",
    "when": "Auditing claim handling for delays, communication gaps, or compliance risk.",
    "output": "every checklist duty is pass/fail/unknown with a cure if fail."
  },
  {
    "id": "interaction-qa-scoring",
    "name": "Interaction QA Scoring",
    "command": "/interaction-qa-scoring",
    "pack": "compliance",
    "blurb": "Score call or chat interactions against QA and compliance rubrics.",
    "when": "Reviewing agent/adjuster conversations for coaching or audit.",
    "output": "another QA reviewer could reach a similar score from the same evidence."
  },
  {
    "id": "regulatory-complaint-response",
    "name": "Regulatory Complaint Response",
    "command": "/regulatory-complaint-response",
    "pack": "compliance",
    "blurb": "Draft responses to regulatory / DOI-style insurance complaints.",
    "when": "Preparing regulator correspondence or complaint files.",
    "output": "a reviewer can send or escalate the draft with exhibits mapped."
  },
  {
    "id": "repair-network-qa",
    "name": "Repair Network QA",
    "command": "/repair-network-qa",
    "pack": "compliance",
    "blurb": "QA repair network / body shop estimates against standards.",
    "when": "Reviewing DRP estimates, supplements, or shop disputes.",
    "output": "the estimate decision is evidence-linked and communicable."
  },
  {
    "id": "catastrophe-event-brief",
    "name": "Catastrophe Event Brief",
    "command": "/catastrophe-event-brief",
    "pack": "analytics",
    "blurb": "Produce catastrophe event operating briefs.",
    "when": "A CAT is approaching or has hit and teams need exposure, claims surge, and playbook actions.",
    "output": "claims, UW, and CX leaders can act from one page."
  },
  {
    "id": "loss-ratio-investigation",
    "name": "Loss Ratio Investigation",
    "command": "/loss-ratio-investigation",
    "pack": "analytics",
    "blurb": "Investigate loss ratio deterioration by segment.",
    "when": "LR worsens and you need drivers and next analyses.",
    "output": "leadership knows the top 3 drivers and the next analytical move."
  },
  {
    "id": "rate-filing-narrative",
    "name": "Rate Filing Narrative",
    "command": "/rate-filing-narrative",
    "pack": "analytics",
    "blurb": "Draft plain-language rate filing narratives from exhibits.",
    "when": "Explaining indicated rate need, support, or filing talking points.",
    "output": "a non-actuary can explain the filing without the spreadsheet open."
  }
];
