window.UNDERWRITER_SKILLS = [
  {
    id: "ask-underwriter",
    name: "Ask Underwriter",
    command: "/ask-underwriter",
    blurb: "Router that picks the smallest skill for the job.",
    when: "You are unsure which underwriting workflow to run, or want a quick pointer before diving into a file.",
    output: "One primary skill, optional follow-on, and the minimum inputs to gather next."
  },
  {
    id: "underwrite-submission",
    name: "Underwrite Submission",
    command: "/underwrite-submission",
    blurb: "End-to-end submission workflow from intake to decision package.",
    when: "New or renewal submissions when you want a full disciplined file read.",
    output: "Decision recommendation, key drivers, subjectivities/RFIs, and authority/referral status."
  },
  {
    id: "risk-appetite-check",
    name: "Risk Appetite Check",
    command: "/risk-appetite-check",
    blurb: "Maps the risk against appetite and guideline hard stops.",
    when: "Class, industry, geography, or account size may be prohibited, preferred, or referral-only.",
    output: "Pursue / modify / refer / decline / need-info verdict with cited drivers."
  },
  {
    id: "loss-history-triage",
    name: "Loss History Triage",
    command: "/loss-history-triage",
    blurb: "Turns loss runs into frequency, severity, and large-loss story.",
    when: "You have loss runs or claims history and need UW implications, not a dump of numbers.",
    output: "Year table, trend, top causes, open-claim risk, and term/price responses."
  },
  {
    id: "financial-strength-review",
    name: "Financial Strength Review",
    command: "/financial-strength-review",
    blurb: "Assesses whether the insured can support the retention and structure.",
    when: "Credit-sensitive covers, high SIRs, long-tail casualty, or thin balance sheets.",
    output: "Strength posture, retention affordability, and structure implications."
  },
  {
    id: "hazard-exposure-analysis",
    name: "Hazard & Exposure Analysis",
    command: "/hazard-exposure-analysis",
    blurb: "Builds an exposure map: COPE, CAT, ops hazards, concentrations.",
    when: "Property schedules, multi-location risk, or casualty operations need a clear loss-driver list.",
    output: "Exposure summary, top hazard drivers, and concrete UW responses."
  },
  {
    id: "coverage-terms-review",
    name: "Coverage Terms Review",
    command: "/coverage-terms-review",
    blurb: "Designs or critiques limits, forms, gaps, and endorsements.",
    when: "Broker asks for wording, or you need to tighten grants before quoting.",
    output: "Terms sheet with requested vs recommended, gaps, and subjectivities."
  },
  {
    id: "pricing-rationale",
    name: "Pricing Rationale",
    command: "/pricing-rationale",
    blurb: "Separates technical indication, target quote, and walk-away.",
    when: "You need a defensible rate story with credits, debits, and sensitivities.",
    output: "Price bands, key mods, and what moves the number most."
  },
  {
    id: "referral-authority",
    name: "Referral & Authority",
    command: "/referral-authority",
    blurb: "Checks desk authority against referral triggers.",
    when: "Limits, class, CAT, or financials may exceed your stamp.",
    output: "Within authority / refer / cannot bind, plus a crisp referral ask."
  },
  {
    id: "underwriting-decision-memo",
    name: "Underwriting Decision Memo",
    command: "/underwriting-decision-memo",
    blurb: "File-ready quote, modify, decline, or refer memo.",
    when: "You need something another UW, auditor, or referral desk can follow.",
    output: "Abstract, drivers, terms/price, subjectivities, authority, next actions."
  },
  {
    id: "broker-rfi",
    name: "Broker RFI",
    command: "/broker-rfi",
    blurb: "Minimum missing-info questions that unblock a decision.",
    when: "The submission is incomplete and you refuse to invent facts.",
    output: "Blocker / material / nice-to-have questions and a clear quote condition."
  },
  {
    id: "renewal-comparison",
    name: "Renewal Comparison",
    command: "/renewal-comparison",
    blurb: "Explains expiring vs proposed: rate change and coverage drift.",
    when: "Renewals where premium swung or forms quietly changed.",
    output: "Delta table, exposure-adjusted rate change, and renew / push / remarket stance."
  }
];
