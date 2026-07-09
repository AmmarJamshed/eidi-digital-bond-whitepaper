# Eidi Digital Bond Program (EDBP)
## White Paper: Trend Analysis, Policy Framework & Implementation Roadmap

**Document Type:** Policy & Innovation White Paper  
**Version:** 1.1  
**Date:** July 2026  
**Classification:** Public — For Policy, Banking, Research & Implementation Use  

**Author:** Muhammad Ammar Jamshed — [LinkedIn](https://www.linkedin.com/in/goto-resumemuhammad-ammar-jamshed-029280145/)  
**Capacity:** Independent researcher and policy author  

**Prepared for:** State Bank of Pakistan, Ministry of Finance, Commercial Banks, Fintechs, Academia & Development Partners *(as prospective stakeholders — not as affiliated institutions)*

> **Independence notice:** This white paper is the independent work of the author named above. It is **not** produced, commissioned, endorsed, or reviewed by the State Bank of Pakistan, the Government of Pakistan, any bank, fintech, or other organisation referenced herein. All views, estimates, and recommendations are the author's own.

---

## Document Control

| Field | Detail |
|-------|--------|
| **Author** | Muhammad Ammar Jamshed ([LinkedIn](https://www.linkedin.com/in/goto-resumemuhammad-ammar-jamshed-029280145/)) |
| **Author capacity** | Independent — no organisational affiliation |
| **Program Name** | Eidi Digital Bond Program (EDBP) |
| **Instrument** | Eidi Digital Bond (EDB) |
| **Proposed Issuer** | Government of Pakistan (via SBP / CDNS) |
| **Settlement Rail** | RAAST (Pakistan Instant Payment System) |
| **Distribution** | Banks, EMI wallets (JazzCash, Easypaisa), digital banks (SadaPay, NayaPay, Raqami) |
| **Denomination Ladder** | PKR 100 · 500 · 1,000 · 5,000 |

---

## 1. The Problem We Are Solving

Before describing any solution, this paper establishes the core problem: **Pakistan's Eid season triggers a massive, predictable, and largely unmanaged extraction of money from the formal financial system — driven by the cultural practice of giving cash Eidi — with lasting costs for families, institutions, and the economy.**

### 1.1 What Happens Every Eid — A Predictable Cash Shock

Each year, in the weeks before Eid-ul-Fitr and Eid-ul-Adha, millions of Pakistani households follow the same pattern:

1. **Withdraw** large sums of cash from banks and ATMs
2. **Obtain** fresh currency notes (via branches, the SBP 8877 SMS service, or informal markets)
3. **Distribute** cash as Eidi to children, relatives, workers, and community members
4. **Spend** remaining cash on Eid consumer purchases — clothing, food, gifts, livestock (Eid-ul-Adha)

This is not a marginal behaviour. Historical reporting places the scale at:

| Indicator | Reported Scale | Year / Source |
|-----------|---------------|---------------|
| Fresh currency notes disbursed (single Eid cycle) | Up to **PKR 380 billion** | 2017 — [Dawn](https://www.dawn.com/news/1341892) |
| SBP 8877 SMS fresh-note service | ~**PKR 30 billion** | 2017 — Dawn (SBP spokesperson) |
| Commercial bank counter + ATM allocation | ~**PKR 340 billion** | 2017 — Dawn |
| Pre-Eid cash withdrawals | ~**PKR 250 billion** (estimated) | 2017 — Banking sector reports via Dawn |
| Remittance inflows earmarked for Eid spending | ~**$1.8 billion** (~PKR 191B) | 2016–17 est. — Dawn |

*Note: SBP does not publish a real-time official Eid withdrawal series. Figures reflect historical press and research estimates and should be re-baselined during a pilot.*

The result is **ATM congestion**, **branch overcrowding**, **accelerated banknote printing**, **informal premium trading of fresh notes**, and **seasonal liquidity pressure** on banks — documented in academic research on Ramadan/Eid deposit volatility in Pakistan ([Limodio, UZH](https://www.phd-finance.uzh.ch/dam/jcr:1c25e3b4-75d7-441f-9078-4b71e63e613c/seminar_contract_theory_paper_Limodio.pdf)).

### 1.2 The Behavioural Problem — Cash Leaves the Formal System

The problem is not only logistical. It is **behavioural and structural**:

**Step 1 — Deliberate withdrawal from banks.** Around Eid, many account holders withdraw cash *specifically* to give Eidi — not because they lack digital alternatives, but because cash is the culturally default medium for the ritual. Bankers consistently report sharp pre-Eid withdrawal spikes ([Dawn, 2025](https://www.dawn.com/news/1916220)).

**Step 2 — Exit from the formal financial system.** Once withdrawn, Eidi cash sits outside bank accounts, EMI wallets, and savings products. It is held in homes, pockets, and envelopes — unrecorded, uninsured, and invisible to the financial system.

**Step 3 — Consumption, not retention.** Eidi cash is overwhelmingly spent, not saved. Children and recipients use it for immediate purchases — snacks, toys, clothes, outings — or hand it to parents for household Eid spending. Very little converts into formal savings, investment, or account balances. The money **enters the retail economy as cash** and rarely returns to the banking system as deposits.

**Step 4 — A missed financial-inclusion moment.** Eid is the one occasion each year when virtually every Pakistani child receives money — yet the default delivery mechanism (cash) provides **no account opening, no savings pathway, no financial literacy hook, and no KYC linkage**. Pakistan's NFIS 2024–28 identifies persistent "preference for cash embedded in the culture" as a core barrier ([Business Recorder, Jan 2025](https://www.brecorder.com/news/40342500)) — and Eid is the single largest annual reinforcement of that preference.

```
  BANK ACCOUNT                    CASH IN HAND                 RETAIL / INFORMAL
  ┌──────────────┐   Withdraw    ┌──────────────┐   Spend      ┌──────────────┐
  │ Formal       │ ────────────▶ │ Eidi cash    │ ──────────▶  │ Consumer     │
  │ deposits     │   (pre-Eid)   │ (outside     │   (Eid week) │ purchases    │
  │              │               │  banking)    │              │ (no return)  │
  └──────────────┘               └──────────────┘              └──────────────┘
        ▲                              │                              │
        │                              │                              │
        └──────── No savings loop ─────┴──────────────────────────────┘
```

**This is the problem EDBP targets:** not the tradition of Eidi, but the **cash pipeline** that strips value from the formal system at the exact moment when digital onboarding would be most culturally acceptable.

### 1.3 Systemic Costs of the Status Quo

| Cost Category | Impact |
|--------------|--------|
| **Currency printing & logistics** | PKR 8–10B/year on PKR 10 notes alone; seasonal Eid spikes add pressure across denominations ([Tribune, 2025](https://tribune.com.pk/story/2594680/10-rupee-coins-could-save-billions-new-report-recommends)) |
| **Bank liquidity stress** | Seasonal deposit outflows during Ramadan/Eid reduce banks' lending capacity ([Limodio](https://www.phd-finance.uzh.ch/dam/jcr:1c25e3b4-75d7-441f-9078-4b71e63e613c/seminar_contract_theory_paper_Limodio.pdf)) |
| **Financial exclusion** | 36% of adults remain unbanked (64% inclusion, 2023); Eid reinforces cash habit instead of converting recipients ([NFIS 2024–28](https://www.brecorder.com/news/40342500)) |
| **Informal economy** | Fresh-note premiums, undocumented transfers, theft/loss risk — especially for children |
| **Diaspora friction** | Overseas Pakistanis send remittances for Eid, but recipients still convert to cash for Eidi distribution |
| **Lost sovereign float** | Billions exit deposits pre-Eid that could temporarily fund government securities if retained digitally |

### 1.4 Why Current Approaches Do Not Solve This

| Approach | Limitation |
|----------|-----------|
| **RAAST P2P transfers** | Technically capable, but not framed as "Eidi" — no cultural packaging, no child recipient workflow, no savings option |
| **ATM fresh-note programmes** | Reinforces cash habit; costs SBP PKR billions in printing and logistics |
| **Financial literacy campaigns** | Generic messaging fights cultural cash preference; Eid-specific product absent |
| **Standard remittance channels** | Money arrives in accounts but is withdrawn as cash for Eidi within days |
| **Digital Prize Bonds** | Long-term investment product — not designed for seasonal gifting or instant Eid redemption |

**No existing instrument combines:** cultural Eidi framing + government guarantee + instant digital delivery + child recipient onboarding + diaspora purchase capability + optional savings conversion.

---

## 2. Executive Summary

Having established the problem above, this paper proposes the **Eidi Digital Bond Program (EDBP)** — a culturally resonant, technically feasible, and fiscally disciplined alternative: **small-denomination, government-guaranteed digital bonds** purchased before Eid, gifted digitally, and cashed out instantly on Eid via RAAST-linked accounts.

**This is not monetary expansion.** Citizens purchase bonds using existing digital money. The State Bank receives upfront liquidity. Redemption releases funds already in the system. No new currency is printed.

### Why Now — Five Converging Trends (2024–2026)

| Trend | Signal | Relevance to EDBP |
|-------|--------|-------------------|
| **RAAST scale-up** | 1.27B transactions / PKR 29.6T in FY25; 45M Raast IDs | Instant Eidi cash-out infrastructure exists |
| **Financial inclusion push** | NFIS 2024–28 target: 75% adult account ownership by 2028 | Eidi is a natural onboarding event |
| **Digital government savings** | Digital Prize Bonds Rules 2024 notified; CDNS scripless transition | Regulatory & technical precedent established |
| **Fintech distribution depth** | 80M+ wallet accounts; JazzCash + Easypaisa dominate retail | Last-mile delivery channel ready |
| **Global tokenized retail bonds** | Philippines GBonds via GCash; World Bank DTB pilots | International proof-of-concept for wallet-distributed sovereign instruments |

### Estimated Impact (Conservative)

| Metric | Estimate | Basis |
|--------|----------|-------|
| Seasonal fresh-note demand displaced | PKR 50–150 billion per Eid cycle | Historical SBP fresh-note disbursement data |
| Avoidable printing & logistics costs | PKR 7–15 billion annually | PSPC cost benchmarks; Eid share of seasonal printing |
| New digital account openings (pilot) | 2–5 million per Eid season | Conversion of cash-Eidi recipients |
| Temporary government financing | PKR 30–80 billion float (pre-Eid purchase window) | Closed-loop purchase-to-redemption cycle |

### Recommendation

Launch EDBP as a **regulated pilot** under SBP supervision in partnership with CDNS, integrated with RAAST and distributed through licensed banks and EMIs — timed to Ramadan/Eid 2027. Scale nationally upon KPI validation.

---

## Table of Contents

1. [The Problem We Are Solving](#1-the-problem-we-are-solving)
2. [Executive Summary](#2-executive-summary)
3. [Introduction & Cultural-Economic Context](#3-introduction--cultural-economic-context)
4. [Problem Deep-Dive: Data & Behavioural Economics](#4-problem-deep-dive-data--behavioural-economics)
5. [Global & Regional Trend Analysis](#5-global--regional-trend-analysis)
6. [Pakistan Macro Trends & Policy Alignment](#6-pakistan-macro-trends--policy-alignment)
7. [Who Benefits — Stakeholder Value Propositions](#7-who-benefits--stakeholder-value-propositions)
8. [The Eidi Digital Bond — Instrument Design](#8-the-eidi-digital-bond--instrument-design)
9. [Program Architecture & User Journey](#9-program-architecture--user-journey)
10. [Overseas Pakistanis & Diaspora Eidi](#10-overseas-pakistanis--diaspora-eidi)
11. [Economic & Fiscal Analysis](#11-economic--fiscal-analysis)
12. [Monetary Policy & Inflation Safeguards](#12-monetary-policy--inflation-safeguards)
13. [Regulatory & Legal Framework](#13-regulatory--legal-framework)
14. [Technology & Interoperability](#14-technology--interoperability)
15. [Stakeholder Roles & Commercial Model](#15-stakeholder-roles--commercial-model)
16. [Risk Assessment & Mitigation](#16-risk-assessment--mitigation)
17. [Implementation Roadmap (18 Months)](#17-implementation-roadmap-18-months)
18. [KPIs, Monitoring & Research Agenda](#18-kpis-monitoring--research-agenda)
19. [Optional Product Extensions](#19-optional-product-extensions)
20. [Policy Recommendations](#20-policy-recommendations)
21. [Conclusion](#21-conclusion)
22. [Data Sources & Methodology](#22-data-sources--methodology)
23. [Annexes](#annexes)
24. [References & Sources](#references--sources)

---

## 3. Introduction & Cultural-Economic Context

### 3.1 What Is Eidi?

**Eidi** (عیدی) is a cherished Islamic cultural practice of giving cash gifts to children, younger relatives, domestic workers, and community members during Eid celebrations. In Pakistan, Eidi is not discretionary spending — it is a **social obligation** embedded in family, religious, and community norms. The practice cuts across income classes, geographies, and urban-rural divides.

This cultural universality makes Eidi a uniquely powerful **financial inclusion lever**: every household participates; every child is a potential recipient; every adult is a potential sender.

### 3.2 The Missed Opportunity

Pakistan has invested heavily since 2019 in digital payments infrastructure — RAAST, Asaan Digital Accounts, digital banks, EMI regulation, and the National Financial Inclusion Strategy (NFIS). Yet during the exact weeks when digital adoption campaigns would be most culturally acceptable, the financial system **defaults to cash**:

- Citizens queue at bank branches for fresh notes
- ATMs are pre-loaded with high-denomination notes
- Informal markets trade new notes at premiums
- Children receive cash with no pathway to savings or accounts

EDBP reframes Eidi from a **cash logistics problem** into a **national financial capability moment**.

### 3.3 Program Thesis

> **Replace the medium of Eidi — not the tradition of Eidi.**

An Eidi Digital Bond preserves the ritual of giving while routing value through regulated digital rails, creating traceability, safety, optional savings, and temporary sovereign financing — without expanding money supply.

---

## 4. Problem Deep-Dive: Data & Behavioural Economics

This section supplements §1 with additional data and behavioural analysis. The core problem — cash extraction, informal circulation, and consumption rather than savings — is established upfront in Section 1.

### 4.1 Seasonal Cash Demand — Historical Data

Pakistan's Eid economy generates substantial, predictable cash extraction from the banking system:

| Indicator | Reported Scale | Source Context |
|-----------|---------------|----------------|
| Fresh currency notes disbursed (single Eid cycle) | Up to **PKR 380 billion** (2017 peak) | SBP / commercial bank allocation |
| SBP SMS service fresh notes | ~**PKR 30 billion** | 8877 service disbursement |
| Commercial bank counter + ATM allocation | ~**PKR 340 billion** | Pre-Eid loading |
| Pre-Eid cash withdrawals | ~**PKR 250 billion** (2017 est.) | Banking sector reports |
| Eid-related spending (mid-estimate) | ~**PKR 190 billion** | Derived from fresh-note flows |

*Note: SBP does not publish real-time Eid-specific withdrawal series; figures reflect historical press and research estimates. A pilot should establish baseline telemetry.*

### 4.2 Operational Strain on Infrastructure

The Eid cash shock creates systemic friction:

1. **ATM congestion** — Long queues, out-of-cash events, urban branch overcrowding
2. **Bank liquidity pressure** — Seasonal deposit volatility (documented in academic research on Pakistan's Ramadan/Eid deposit cycles)
3. **Currency printing surge** — PSPC must accelerate production of low-denomination notes with short lifespans (6–9 months for PKR 10 notes)
4. **Informal premium economy** — Illegal trading of fresh notes; weak economic documentation
5. **Security risk** — Cash handling, theft, loss — especially for children

### 4.3 Behavioural Economics of Eid Cash

Research and market observation confirm a consistent behavioural loop:

| Stage | Behaviour | Consequence |
|-------|-----------|-------------|
| **Pre-Eid (Ramadan)** | Account holders withdraw cash specifically for Eidi envelopes | Bank deposits fall; ATM demand spikes |
| **Eid day** | Cash handed to children, workers, relatives | Money exits formal system; no KYC on recipient side |
| **Post-Eid week** | Recipients spend on consumer goods (food, clothing, toys) | Cash enters retail/MFI economy; rarely returns as savings |
| **Long-term** | Children associate Eidi with cash, not accounts | Reinforces generational cash preference |

Academic evidence from Pakistan shows that Ramadan and Eid cause measurable deposit volatility at banks, with institutions more exposed to Sunni-majority areas experiencing larger seasonal outflows ([Limodio](https://www.phd-finance.uzh.ch/dam/jcr:1c25e3b4-75d7-441f-9078-4b71e63e613c/seminar_contract_theory_paper_Limodio.pdf)). The NFIS 2024–28 explicitly names cultural cash preference as a persistent inclusion barrier ([Business Recorder, 2025](https://www.brecorder.com/news/40342500)).

**EDBP interrupts this loop** by keeping Eidi value inside regulated digital wallets until the recipient chooses to cash out or save — converting a consumption event into a potential **inclusion and savings event**.

### 4.4 Currency Management Cost Context

Pakistan's currency management costs are material and rising:

- **PKR 10 note printing alone:** PKR 8–10 billion annually (~35% of all notes printed)
- **10-year coin transition savings potential:** PKR 40–50 billion (SBP/PSPC committee report, 2026)
- **Total currency in circulation:** ~PKR 11 trillion (2026 est.)

EDBP does not replace denomination reform — it **complements** it by reducing seasonal demand for physical notes across all denominations used in Eidi (PKR 50–5,000).

### 4.5 Financial Inclusion Gap

Despite progress (16% → 64% bank account ownership, 2015–2023), Pakistan's NFIS 2024–28 acknowledges a persistent barrier:

> *"General preference for cash embedded in the culture."*  
> — NFIS 2024–28 Strategy Document

Eidi is the exception where **digital giving can be socially encouraged** without fighting cultural cash preference — because the sender wants convenience and the receiver wants instant value.

---

## 5. Global & Regional Trend Analysis

### 5.1 Trend 1 — Tokenized Government Bonds for Retail Investors

**Status:** Accelerating globally; emerging markets leapfrogging legacy bond market infrastructure.

| Jurisdiction | Initiative | Key Feature | Lesson for Pakistan |
|-------------|-----------|-------------|---------------------|
| **Philippines** | GBonds via GCash + PDAX | Min. PHP 500 (~$9); blockchain registry | Wallet-native sovereign instrument distribution |
| **World Bank / IFC** | Digital Tokenized Bonds (DTBs) | $3.7B issued globally in 2024; $22B projected by 2030 | Development finance institutions will support pilots |
| **Thailand, Brazil, Hong Kong** | Regulatory sandboxes for tokenized securities | Institutional → retail progression | Phased rollout model |

The Philippines model is the closest analog: **94 million GCash users** can access government bonds from PHP 500 through an app they already use. Pakistan's JazzCash (40M+ users) and Easypaisa (35M+ active) provide equivalent distribution scale.

**Strategic insight:** EDBP is not experimental in a global vacuum — it is a **localized, seasonal, micro-denomination variant** of a validated policy trend.

### 5.2 Trend 2 — Digital Vouchers & Purpose-Bound Money

| Jurisdiction | Program | Mechanism |
|-------------|---------|-----------|
| **India** | e-RUPI | NPCI/UPI prepaid voucher; person + purpose specific |
| **South Korea** | BOK digital voucher pilot | Tokenized deposit-based; welfare/culture/education |
| **Philippines** | BSP Christmas e-cash campaign | Central bank advocacy for digital aguinaldo (cash gifts) |
| **Bangladesh** | Prepaid Instrument Guidelines 2024 | Regulated gift cards, wallets, cash vouchers |

**Common thread:** Central banks distinguish between **CBDC (money creation)** and **digital vouchers/bonds (existing money, programmed use)**. EDBP falls in the latter category — a critical distinction for SBP monetary policy credibility.

### 5.3 Trend 3 — Instant Payment Rails as National Infrastructure

Pakistan's RAAST places the country among leading instant-payment adopters:

| Metric | RAAST Performance |
|--------|-------------------|
| Cumulative transactions (inception–Jun 2025) | 1.9 billion |
| Cumulative value | PKR 44.3 trillion |
| FY 2024–25 alone | 1.27B txns / PKR 29.6T |
| Registered Raast IDs | 45 million |
| Transaction cost to end-user | Zero (policy mandate) |
| Per-transaction limit | PKR 250,000 |

RAAST's **Bulk Payments** module — already identified by CDNS for profit payments and investment encashment — is the natural settlement backbone for EDBP redemption.

### 5.4 Trend 4 — Mobile Wallets as Primary Bank for the Masses

| Platform | Scale | Strategic Role in EDBP |
|----------|-------|------------------------|
| JazzCash | 40M+ accounts; 20.6M MAU; PKR 3.9T GTV (2025) | Urban + rural distribution; 80%+ of Raast P2M value |
| Easypaisa | 35M+ active; 170K agent network | Rural/semi-urban last mile; digital bank license |
| SadaPay, NayaPay, others | Growing EMI/DRB segment | Youth-oriented UX; innovation sandbox |
| Digital banks (Mashreq NEO, Raqami) | Newly licensed 2025–26 | Shariah-compliant Eidi savings variant |

**Trend conclusion:** Pakistan has achieved **distribution scale** before achieving **cultural cash displacement**. EDBP targets the cultural moment.

### 5.5 Trend 5 — Scripless Government Savings (Domestic Precedent)

Pakistan is already transitioning government savings instruments to digital:

- **Digital Prize Bonds (Registered) Rules, 2024** — Notified by Finance Division
- **CDNS mobile app** — Purchase, portfolio management, redemption to linked IBAN
- **CDC partnership** — Scripless National Savings Certificates
- **CDNS + RAAST integration** — Under active consideration for profit payments

EDBP should be architected as a **sibling instrument** to Digital Prize Bonds — not a competing silo — sharing KYC, registry, and settlement infrastructure.

---

## 6. Pakistan Macro Trends & Policy Alignment

### 6.1 NFIS 2024–28 Alignment Matrix

| NFIS Goal | EDBP Contribution |
|-----------|-------------------|
| 75% financial inclusion by 2028 | Mass onboarding via Eidi recipients (children/youth) |
| Gender gap reduction (34% → 25%) | Digital Eidi to girls/women; supervised child wallets |
| Digital payments promotion | Seasonal spike in P2P digital transactions |
| Underserved geography focus | EMI agent networks in rural areas |
| SME/agriculture finance | Indirect — reduces bank liquidity stress during Eid |
| Consumer protection & literacy | Structured teachable moment for families |

### 6.2 SBP "Go Cashless" & Financial Literacy Week

SBP Deputy Governor Saleem Ullah's 2025 "Go Cashless" drive explicitly targets behavioral shift from cash to digital. EDBP provides a **concrete product** for that campaign — not just awareness messaging.

### 6.3 Currency Reform Complementarity

The 2026 SBP/PSPC recommendation to replace PKR 10 notes with coins (saving PKR 40–50B over 10 years) addresses **structural** note cost. EDBP addresses **seasonal** note demand. Together, they form a coherent currency modernization agenda.

### 6.4 Political Economy Considerations

EDBP is politically viable because it:

- Respects Islamic cultural practice (not a "war on cash")
- Benefits families (convenience, child safety)
- Supports government finances (temporary float)
- Aligns with IMF-adjacent fiscal discipline narratives (no money printing)
- Creates visible digitization wins for government

---

## 7. Who Benefits — Stakeholder Value Propositions

EDBP creates value across the entire financial ecosystem. This section details **how each stakeholder benefits** — not just **that** they benefit.

### 7.1 Children & Eidi Recipients

| Benefit | Detail |
|---------|--------|
| **Safety** | No cash to lose, steal, or damage; digital record of gift |
| **First account moment** | Receiving an EDB can auto-provision a supervised child wallet (B-Form + guardian CNIC) — first step into formal finance |
| **Savings option** | "Eidi Savings Mode" lets recipients hold bonds past Eid and earn profit — converting consumption impulse into savings habit |
| **Financial literacy** | Age-appropriate app experience teaches that Eidi can be saved, not only spent |
| **Equal access** | Girls and boys receive digital Eidi equally — supports NFIS gender gap reduction (34% → 25%) |

### 7.2 Families (Senders & Households)

| Benefit | Detail |
|---------|--------|
| **Convenience** | No ATM queues, no fresh-note hunting, no envelope preparation |
| **Reach** | Send Eidi to children in another city instantly via Raast ID / phone number |
| **Cost** | Zero transaction fees (consistent with RAAST policy) |
| **Transparency** | Parents see when Eidi was received; guardians can approve cash-out for minors |
| **Family pools** | Multiple relatives contribute to one digital Eidi gift (Family Group Eidi) |
| **Cultural preservation** | Ritual of giving unchanged — only the medium modernises |

### 7.3 Overseas Pakistanis (Diaspora)

| Benefit | Detail |
|---------|--------|
| **Direct Eidi delivery** | Purchase EDB from abroad and assign to relative's CNIC — no cash handoff needed |
| **Remittance alignment** | Use RDA/NRP accounts or remittance partners to fund bond purchase in PKR |
| **Emotional connection** | Digital Eidi card with personalised message delivered on Eid morning in Pakistan |
| **Cost reduction** | Avoid hawala/informal channels for small Eidi gifts; fully documented transfer |
| **Scale** | ~9–10 million overseas Pakistanis; ~$30B annual remittances — even 5% Eidi allocation = significant volume ([SBP remittance data](https://www.sbp.org.pk)) |
| **See §10** for full diaspora workflow |

### 7.4 Government of Pakistan

| Benefit | Detail |
|---------|--------|
| **Reduced printing costs** | Estimated PKR 7–15B/year avoided in printing, ATM logistics, and cash handling (see §11) |
| **Temporary financing** | PKR 30–80B seasonal float from pre-Eid purchases (1:1 reserve-backed, not deficit financing) |
| **Economic documentation** | Eidi flows become traceable — supports tax base and AML objectives |
| **NFIS milestone** | Visible, measurable progress toward 75% inclusion by 2028 |
| **No inflation risk** | Closed-loop design — no new money printed (see §12) |
| **Political capital** | Culturally respectful digitisation win — not a "war on cash" |

### 7.5 State Bank of Pakistan & Financial System

| Benefit | Detail |
|---------|--------|
| **Deposit retention** | Reduces pre-Eid withdrawal spikes that stress bank liquidity ([Limodio](https://www.phd-finance.uzh.ch/dam/jcr:1c25e3b4-75d7-441f-9078-4b71e63e613c/seminar_contract_theory_paper_Limodio.pdf)) |
| **RAAST utilisation** | High-volume seasonal use case for Bulk Payments module |
| **Monetary stability** | Lower seasonal currency-in-circulation spikes |
| **Supervisory data** | Transaction-level visibility for AML/CFT monitoring |
| **Payment systems KPI** | Adds Eid-season metrics to Quarterly Payment Systems Review |

### 7.6 Banks, EMIs & Fintechs

| Benefit | Detail |
|---------|--------|
| **New accounts** | 2–5M recipient onboarding per Eid season (pilot estimate) |
| **CASA deposits** | Post-redemption wallet balances remain in system |
| **Transaction revenue** | Interchange fees (0.1–0.25% from government) |
| **Cross-sell** | Savings, insurance, nano-loans at moment of Eidi receipt |
| **Merchant volume** | Digital cash-out flows to P2M merchants (838K+ on RAAST) |
| **Brand** | Culturally resonant "Send Eidi" campaigns drive MAU growth |

### 7.7 Broader Economy

| Benefit | Detail |
|---------|--------|
| **Retail digitisation** | Eidi spent via wallets increases digital merchant transactions |
| **Savings rate** | Optional bond-hold past Eid increases national savings pool |
| **Remittance formalisation** | Diaspora Eidi via EDB channels flows through formal rails |
| **Research value** | Natural experiment for financial inclusion, gender, and seasonal liquidity studies |
| **Regional model** | Exportable to Bangladesh, Afghanistan, Indonesia — similar Eid economies |

---

## 8. The Eidi Digital Bond — Instrument Design

### 8.1 Definition

An **Eidi Digital Bond (EDB)** is a **short-duration, scripless, government-guaranteed digital savings instrument** issued specifically for Eid gifting, denominated in Pakistani Rupees, transferable between KYC-verified wallets, and redeemable at par during designated Eid windows via RAAST.

### 8.2 Core Properties

| Property | Specification |
|----------|--------------|
| **Legal form** | Registered digital security under Public Debt Act, 1944 (amended rules) |
| **Issuer** | Government of Pakistan via CDNS (operational) / SBP (oversight) |
| **Denominations** | PKR 100, 500, 1,000, 5,000 |
| **Purchase window** | 1st of Ramadan → 2 days before Eid |
| **Gifting window** | Open throughout purchase window + Eid day |
| **Redemption window** | Eid day → 7 days post-Eid (configurable) |
| **Transferability** | P2P between verified wallets; non-transferable after redemption |
| **Profit/coupon** | Zero in base variant; optional "Eidi Savings Mode" (see §19) |
| **Guarantee** | Full faith and credit of Government of Pakistan |
| **KYC requirement** | CNIC/B-Form; guardian-linked for minors |

### 8.3 What EDB Is — and Is Not

| EDB **Is** | EDB **Is Not** |
|-----------|---------------|
| A digital gifting instrument | A cryptocurrency or stablecoin |
| A closed-loop seasonal program | A permanent monetary expansion tool |
| A financial inclusion product | A replacement for all cash Eidi (initially) |
| A source of temporary government financing | A prize-draw lottery bond |
| Existing money, digitally routed | Newly printed currency |

### 8.4 Comparison to Adjacent Instruments

| Feature | EDB | Digital Prize Bond | RAAST P2P Transfer | Prepaid Gift Card |
|---------|-----|-------------------|-------------------|-------------------|
| Government backed | ✓ | ✓ | N/A (bank money) | ✗ |
| Seasonal/programmed | ✓ | ✗ | ✗ | Partial |
| Prize draw | ✗ | ✓ | ✗ | ✗ |
| Teaches savings/bonds | ✓ | ✓ | ✗ | ✗ |
| Temporary sovereign float | ✓ | ✓ | ✗ | ✗ |
| Cultural Eidi framing | ✓ | ✗ | Partial | ✗ |

---

## 9. Program Architecture & User Journey

### 9.1 Three-Step Flow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  1. BUY     │────▶│  2. GIFT    │────▶│  3. CASH OUT│
│  (Pre-Eid)  │     │  (Digital)  │     │  (Eid Day)  │
└─────────────┘     └─────────────┘     └─────────────┘
     │                    │                    │
  Bank/EMI           P2P transfer          RAAST credit
  wallet debit       to recipient          to IBAN/wallet
  → EDB minted       CNIC-linked           par redemption
```

### 9.2 Detailed User Journey — "Ali & Sara"

| Step | Actor | Action | Backend Event |
|------|-------|--------|---------------|
| 1 | Ali (sender) | Opens JazzCash → "Eidi Bond" → selects PKR 1,000 | Wallet debited; EDB minted in Ali's bond wallet |
| 2 | Ali | Enters Sara's Raast ID / phone → "Send Eidi" | Bond ownership transferred; SMS/push to Sara |
| 3 | Sara (recipient) | Receives notification; views animated Eidi card in app | Minor KYC check; bond in Sara's wallet |
| 4 | Sara (Eid day) | Taps "Cash Out" → PKR 1,000 credited | RAAST bulk redemption; bond burned |
| 5 | Optional | Sara selects "Save" instead → PKR 1,000 + profit | Bond rolls to CDNS savings product |

**Total time:** < 60 seconds per transaction. **No ATM. No branch. No cash handling.**

### 9.3 Distribution Channel Architecture

```
                    ┌──────────────────────┐
                    │   SBP / CDNS Core    │
                    │  Bond Registry &     │
                    │  Redemption Engine   │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │   RAAST IPS Layer    │
                    │  (Bulk Payments)     │
                    └──────────┬───────────┘
           ┌───────────────────┼───────────────────┐
           │                   │                   │
    ┌──────▼──────┐    ┌──────▼──────┐    ┌──────▼──────┐
    │   Banks     │    │    EMIs     │    │ Digital Banks│
    │ (HBL, UBL,  │    │ (JazzCash,  │    │ (SadaPay,    │
    │  MCB, etc.) │    │  Easypaisa) │    │  Raqami)     │
    └──────┬──────┘    └──────┬──────┘    └──────┬──────┘
           │                   │                   │
           └───────────────────┼───────────────────┘
                               │
                    ┌──────────▼───────────┐
                    │   Citizens (250M)    │
                    │  Senders & Recipients│
                    └──────────────────────┘
```

### 9.4 Child & Minor Wallet Framework

| Age Group | Account Type | Requirements |
|-----------|-------------|--------------|
| 0–4 | Guardian custodial wallet | Parent CNIC; no independent cash-out |
| 5–17 | Supervised Child Eidi Wallet | B-Form; guardian approval for cash-out > PKR 500/day |
| 18+ | Standard wallet / bank account | Full CNIC KYC |

This structure supports NFIS youth inclusion goals and creates **first account at first Eidi** — a lifelong financial services entry point.

---

## 10. Overseas Pakistanis & Diaspora Eidi

A significant share of Eidi in Pakistan is funded by **overseas Pakistanis** — approximately **9–10 million** Pakistanis live abroad, sending **$30+ billion** in annual remittances ([SBP](https://www.sbp.org.pk)). Historical reporting suggests that **60% of Ramadan remittance inflows** (~$1.8B in 2016–17) enter the market for Eid spending ([Dawn, 2017](https://www.dawn.com/news/1341892)). Today, diaspora senders typically remit to a family bank account — which is then **withdrawn as cash** for Eidi distribution, repeating the behavioural loop described in §1.

EDBP extends the program to overseas Pakistanis, making diaspora Eidi a **first-class use case** rather than an afterthought.

### 10.1 Diaspora User Journey — "Ahmed in Dubai → Niece Sara in Lahore"

| Step | Actor | Action | Backend Event |
|------|-------|--------|---------------|
| 1 | Ahmed (overseas Pakistani) | Opens bank app (RDA/NRP) or EMI partner abroad → "Send Eidi Bond" | PKR funded via RDA account, remittance partner, or FX conversion |
| 2 | Ahmed | Enters recipient **CNIC** or **B-Form** + name + relationship | NADRA verification; recipient matched in CDNS registry |
| 3 | Ahmed | Selects denomination (PKR 1,000) + optional Eid message | EDB minted; held in escrow until Eid window |
| 4 | System | Notifies Sara's guardian via SMS/app: *"Ahmed sent you Eidi!"* | Push notification with digital Eidi card |
| 5 | Sara (Eid day) | Taps "Open Eidi" → cash out or save | RAAST credit to wallet; bond burned |

**No cash handoff. No hawala. No dependency on a relative visiting from abroad with physical notes.**

### 10.2 Identity-Linked Assignment

Overseas senders assign bonds using the recipient's **official identity**:

| Recipient Type | Required Identifier | Guardian Rule |
|---------------|--------------------|--------------------|
| Adult (18+) | CNIC number + name match | Self-redeem |
| Minor (5–17) | B-Form + name match | Guardian CNIC linked; co-approval for cash-out |
| Minor (0–4) | B-Form + guardian CNIC | Bond held in custodial wallet |

NADRA e-KYC APIs verify identity at assignment time, preventing misdirected gifts and enabling AML compliance.

### 10.3 Funding Channels for Overseas Pakistanis

| Channel | Mechanism | Status |
|---------|-----------|--------|
| **RDA (Roshan Digital Account)** | Overseas Pakistani holds PKR account; purchases EDB directly | Existing SBP framework; banks like HBL, MCB, UBL ([SBP RDA](https://www.sbp.org.pk/rda)) |
| **NRP accounts** | Non-Resident Pakistani accounts at participating banks | Mashreq NEO, Standard Chartered, others |
| **Remittance partners** | MoneyGram, Wise, Remitly → EDB purchase at destination | Requires API integration (Phase 2) |
| **EMI diaspora apps** | JazzCash/Easypaisa international remittance → EDB | JazzCash already processes diaspora flows |

### 10.4 Regulatory Considerations

- Overseas purchasers must complete **KYC** under SBP RDA/NRP rules (already required for account holders)
- EDB assignment to a third-party CNIC is a **gift**, not a remittance — simplifies regulatory treatment vs. cross-border P2P transfers
- **FX conversion** occurs at purchase; recipient receives PKR at par — no exchange risk for child
- SBP AML/CFT rules apply to sender; recipient verification via NADRA

### 10.5 Diaspora Impact Estimate

| Scenario | Assumption | Volume |
|----------|-----------|--------|
| Conservative | 5% of diaspora households send Eidi via EDB | ~450K bonds |
| Moderate | 10% adoption; avg PKR 2,000/bond | PKR 18–20B per Eid |
| Ambitious | 20% adoption; avg PKR 3,000/bond | PKR 54–60B per Eid |

Diaspora Eidi alone could make EDBP one of the **largest seasonal digital payment events** in Pakistan's history.

### 10.6 Comparison — Diaspora Eidi Today vs. EDBP

| | Today (Cash/Hawala) | EDBP (Digital Bond) |
|--|---------------------|---------------------|
| **Sender experience** | Remit to account → relative withdraws cash | Direct Eidi assignment by CNIC |
| **Recipient experience** | Cash envelope | Digital Eidi card + optional savings |
| **Documentation** | Partial (remittance record only) | Full (sender, recipient, amount, timestamp) |
| **Cost** | Remittance fee + cash withdrawal | Remittance fee + zero EDB transfer fee |
| **Speed** | 1–3 days remittance + cash pickup | Instant assignment; redeem on Eid |
| **Child onboarding** | None | Supervised wallet created on first Eidi |

---

## 11. Economic & Fiscal Analysis

### 11.1 Cost Avoidance Model

| Cost Category | Annual Estimate (PKR) | EDBP Displacement Assumption | Savings (PKR) |
|--------------|----------------------|------------------------------|---------------|
| Banknote printing (Eid share) | 25–40% of PSPC budget | 30% displacement Year 1 | 2.4–4.0B |
| Note replacement (soiled notes) | Correlated with circulation velocity | 10% reduction | 0.8–1.5B |
| ATM loading & logistics | Industry estimates | 15% seasonal reduction | 1.0–2.0B |
| Cash handling (banks) | Branch + CIT costs | 10% seasonal reduction | 0.5–1.0B |
| Informal note premium economy | Unquantified | Significant reduction | Qualitative |
| **Total (Year 1 conservative)** | | | **4.7–8.5B** |
| **Total (mature program)** | | | **7–15B** |

*Methodology note: Author's original estimate of PKR 7–12B printing savings aligns with this model when Eid-related printing share is assumed at 25–40% of total note production costs.*

### 11.2 Temporary Government Financing Benefit

**Purchase-to-redemption float:**

If 20 million citizens purchase an average of PKR 2,000 in EDBs during a 25-day Ramadan window, gross issuance = **PKR 40 billion** held by government until Eid redemption.

| Scenario | Issuance Volume | Avg. Hold Period | Implied Float |
|----------|----------------|------------------|---------------|
| Pilot (5 cities) | PKR 5B | 20 days | PKR 5B |
| Regional (10 provinces) | PKR 25B | 22 days | PKR 25B |
| National | PKR 60B | 25 days | PKR 60B |

At current SBP policy rate, even a zero-coupon instrument provides **fiscal breathing room** equivalent to a short-term T-bill auction — without auction friction.

**Critical safeguard:** Float must be ring-fenced in a **segregated redemption reserve account** at SBP, fully backed 1:1. This is not deficit financing.

### 11.3 Financial Inclusion Economic Returns

Research on financial inclusion consistently links account ownership to:

- Higher formal savings rates
- Improved credit access (especially for women and youth)
- Reduced remittance leakage to informal channels
- Greater tax base documentation

EDBP creates **2 touchpoints per gift** (sender + receiver), doubling onboarding potential vs. a unilateral government campaign.

### 11.4 Fintech & Banking Revenue (Secondary Effects)

| Stakeholder | Revenue / Value Driver |
|------------|----------------------|
| EMIs | Wallet float, transaction fees (interchange), cross-sell to savings/insurance |
| Banks | CASA deposits post-redemption; new account acquisition |
| Government | Reduced printing; documented economy; float |
| Retailers | Higher digital spend post-cash-out via wallets |

---

## 12. Monetary Policy & Inflation Safeguards

### 12.1 The Closed-Loop Principle

EDBP operates as a **closed-loop monetary circuit:**

1. **Purchase:** Digital money leaves citizen wallet → enters government bond registry (SBP/CDNS account)
2. **Gift:** Bond ownership changes; **no new money created**
3. **Redemption:** Government releases **the same funds** to recipient wallet via RAAST

**Net change in M0 (currency in circulation):** Negative or neutral — never positive.

### 12.2 Distinction from Money Printing

SBP defines currency printing drivers as:

- Replacement of soiled notes
- Currency in circulation growth (economic activity)
- **Direct government borrowing from SBP** (monetary financing)

EDBP involves none of these expansionary mechanisms. It is economically equivalent to:

> Citizens temporarily buying a 30-day T-bill and gifting the claim to a relative who redeems it on Eid.

### 12.3 SBP Safeguards (Recommended)

| Safeguard | Implementation |
|-----------|---------------|
| 1:1 reserve backing | Segregated account at SBP matching outstanding EDB face value |
| Issuance cap | National limit per Eid cycle (e.g., PKR 100B) subject to Monetary Policy Committee review |
| No secondary market | Bonds non-tradeable outside gifting to prevent speculation |
| AML/CFT monitoring | Real-time transaction monitoring via existing EMI/bank frameworks |
| Redemption window limit | Prevents indefinite float absorption |

---

## 13. Regulatory & Legal Framework

### 13.1 Proposed Legal Basis

| Instrument | Applicable Law / Rule |
|-----------|----------------------|
| EDB issuance | Public Debt Act, 1944 |
| Digital form | Digital Prize Bonds (Registered) Rules, 2024 (template) |
| New EDB-specific rules | **Eidi Digital Bond Rules, 2026** (proposed SRO) |
| Payment settlement | Payment Systems & Electronic Fund Transfers Act |
| EMI distribution | Electronic Money Institution regulations (SBP) |
| KYC/AML | SBP AML/CFT Regulations; NADRA verification |
| Minor accounts | SBP branchless banking / digital account guidelines |

### 13.2 Regulatory Architecture

```
Finance Division (Policy Owner)
        │
        ├── CDNS (Issuance, Registry, Customer Service)
        │
        ├── SBP (Prudential Oversight, IPS Settlement, EMI/Bank Supervision)
        │
        └── SECP (if structured as marketable security — likely N/A for EDB)
```

### 13.3 EMI & Bank Participation Framework

Participating institutions should sign a **Standard EDBP Participation Agreement** covering:

- API integration specifications
- KYC reliance standards
- Float handling rules
- Customer dispute resolution
- Marketing co-branding guidelines
- Fee schedule (interchange capped by SBP)

---

## 14. Technology & Interoperability

### 14.1 Core Technical Components

| Component | Function | Existing Asset |
|-----------|----------|---------------|
| **EDB Registry** | Mint, transfer, burn bonds | Extend CDNS Digital Prize Bond Gateway |
| **Identity Layer** | CNIC/B-Form verification | NADRA e-KYC APIs |
| **Settlement Layer** | Instant redemption | RAAST Bulk Payments |
| **Distribution APIs** | Bank/EMI integration | Open banking framework (NFIS 2024–28) |
| **Notification Layer** | Eidi gift alerts | SMS, push, WhatsApp (via EMIs) |
| **Analytics Dashboard** | KPI monitoring | SBP payment systems review infrastructure |

### 14.2 API-First Design (For Fintech Partners)

Minimum viable API endpoints:

```
POST /edb/purchase        — Buy bonds from wallet
POST /edb/gift            — Transfer to recipient
POST /edb/redeem          — Cash out via Raast
GET  /edb/balance         — Portfolio view
GET  /edb/history         — Transaction log
POST /edb/save            — Roll to savings (optional)
```

### 14.3 Security Standards

- End-to-end encryption for bond transfer messages
- Multi-factor authentication for redemptions > PKR 5,000
- Guardian co-approval for minor accounts
- Real-time fraud scoring (shared with existing wallet fraud engines)
- Immutable audit trail in CDNS registry

### 14.4 No Blockchain Required (Phase 1)

Unlike Philippines GBonds (DLT registry), Pakistan can launch EDBP on **centralized CDNS registry** integrated with RAAST — faster, cheaper, regulator-native. DLT may be evaluated in Phase 3 if interoperability with regional markets is desired.

---

## 15. Stakeholder Roles & Commercial Model

### 15.1 Stakeholder Matrix

| Stakeholder | Role | Incentive |
|------------|------|-----------|
| **Ministry of Finance** | Policy approval; SRO issuance | Fiscal savings; digitization milestone |
| **SBP** | Oversight; RAAST; prudential supervision | Cashless economy KPI; monetary stability |
| **CDNS** | Issuance, registry, redemption ops | Operational fee; digital savings cross-sell |
| **Commercial Banks** | Distribution; corporate Eidi programs | New accounts; deposit growth |
| **EMIs (JazzCash, Easypaisa)** | Primary retail distribution | MAU growth; transaction revenue |
| **Digital Banks** | Youth/women-focused distribution | Differentiated onboarding |
| **NADRA** | Identity verification | Per-query fee (existing model) |
| **Merchants** | Post-Eid digital spending acceptance | Higher wallet spend |
| **Academia/NGOs** | Impact evaluation; financial literacy | Research funding; publication |
| **Media** | Cultural adoption campaigns | Public service content |

### 15.2 Fee Structure (Recommended — Zero Consumer Cost)

| Party | Fee | Rationale |
|-------|-----|-----------|
| Consumer (sender/receiver) | **PKR 0** | NFIS inclusion mandate; RAAST zero-fee precedent |
| EMI/Bank (interchange) | 0.1–0.25% of face value (from government) | Covers distribution cost |
| CDNS (operations) | 0.05% administration fee | Registry + redemption ops |
| Government (net) | Retains float benefit minus fees | Positive ROI at scale |

---

## 16. Risk Assessment & Mitigation

| # | Risk | Likelihood | Impact | Mitigation |
|---|------|-----------|--------|------------|
| R1 | Low digital adoption (cultural cash preference) | Medium | High | Co-marketing with religious leaders; "Eidi Card" UX; hybrid cash-out at EMI agents |
| R2 | System overload on Eid day | Medium | High | Pre-provisioned RAAST capacity; staggered redemption incentives (early save bonus) |
| R3 | Fraud / social engineering | Medium | Medium | CNIC-linked transfers; redemption limits; guardian controls |
| R4 | Political perception as "eliminating cash Eidi" | Low | High | Clear messaging: tradition preserved, medium modernized |
| R5 | EMI/bank participation imbalance | Medium | Medium | SBP mandate for licensed entities above size threshold |
| R6 | Redemption reserve shortfall | Low | Critical | 1:1 segregated SBP account; daily reconciliation |
| R7 | Regulatory delay | Medium | Medium | Parallel track: amend Digital Prize Bond rules vs. new SRO |
| R8 | Exclusion of unbanked elderly | Medium | Medium | Agent-assisted purchase/redemption; family proxy gifting |
| R9 | Data privacy concerns | Low | Medium | Compliance with Pakistan data protection law; minimal data collection |
| R10 | Scope creep (permanent program drift) | Low | Medium | Sunset clause per Eid cycle; MPC review for renewal |

---

## 17. Implementation Roadmap (18 Months)

### Phase 0 — Policy Design (Months 1–3)

| Task | Owner | Deliverable |
|------|-------|-------------|
| Cabinet / Finance Division approval in principle | MoF | Policy note |
| Draft Eidi Digital Bond Rules, 2026 | MoF + CDNS | SRO draft |
| SBP technical working group | SBP | Terms of reference |
| Stakeholder consultation (banks, EMIs) | SBP | Consultation report |
| Shariah review (if profit variant) | SBP / religious board | Compliance opinion |

### Phase 1 — Build & Integrate (Months 4–8)

| Task | Owner | Deliverable |
|------|-------|-------------|
| Extend CDNS Digital Bond Gateway | CDNS + IT vendor | EDB registry MVP |
| RAAST Bulk Redemption integration | SBP + 1Link | Settlement pipeline |
| EMI API sandbox (JazzCash, Easypaisa) | SBP + EMIs | 2 live integrations |
| KYC/NADRA integration testing | CDNS + NADRA | Verification flow |
| **Diaspora RDA/NRP purchase channel** | SBP + banks | Overseas Eidi purchase API |
| Child wallet framework | SBP + EMIs | Supervised account spec |
| Security audit | Third party | Penetration test report |

### Phase 2 — Pilot (Months 9–12)

| Parameter | Specification |
|-----------|--------------|
| **Geography** | Islamabad, Karachi, Lahore, Peshawar, Quetta |
| **Channels** | JazzCash + 2 banks + 1 RDA bank |
| **Cap** | PKR 5 billion issuance |
| **Target** | 500,000 bonds gifted |
| **Eid** | Eid-ul-Fitr 2027 |
| **Evaluation** | 90-day post-Eid impact report |

### Phase 3 — National Rollout (Months 13–18)

| Task | Detail |
|------|--------|
| All licensed EMIs + top 10 banks + RDA partners | Mandatory participation |
| Diaspora marketing (GCC, UK, US) | Embassy/ community partnerships |
| National marketing campaign | SBP + EMIs + media |
| Both Eids covered | Fitr + Adha |
| Issuance cap raised | PKR 50–100B |
| Optional features launched | Savings mode, donation bonds, family pools |

### Phase 4 — Institutionalize (Month 18+)

- Annual NFIS reporting inclusion
- Academic longitudinal study (3-year child savings outcomes)
- Regional export of model (Afghanistan, Bangladesh, Indonesia Eid markets)

---

## 18. KPIs, Monitoring & Research Agenda

### 18.1 Program KPIs

| KPI | Year 1 Target | Year 3 Target |
|-----|--------------|--------------|
| EDBs issued (volume) | PKR 10B | PKR 75B |
| Unique senders onboarded | 2M | 15M |
| Unique recipients (new accounts) | 3M | 20M |
| % Eidi displaced from cash | 15% | 45% |
| Redemption via digital (no agent cash-out) | 70% | 90% |
| Child wallets opened | 500K | 5M |
| ATM Eid-week withdrawals (vs. baseline) | −10% | −30% |
| Fresh note printing (Eid cycle) | −15% | −35% |
| Customer satisfaction (NPS) | > 50 | > 65 |

### 18.2 Research Questions for Academia

1. Does digital Eidi increase child savings rates vs. cash Eidi?
2. What is the gender differential in sender/receiver adoption?
3. How does Eid deposit volatility at banks change under EDBP?
4. What is the elasticity of cash-Eidi substitution by income decile?
5. Can EDBP serve as a natural experiment for financial literacy outcomes?

*Suggested methodology: Difference-in-differences using pilot cities vs. control cities; partnership with SBP Research Department and LUMS/IBA/State Bank training institutes.*

### 18.3 SBP Reporting Integration

EDBP metrics should be added to the **Quarterly Payment Systems Review** as a supplementary table — giving banking professionals and researchers standardized data series.

---

## 19. Optional Product Extensions

### 19.1 Eidi Savings Mode

- Recipient opts to hold EDB beyond Eid
- Auto-converts to CDNS **Short-Term Savings Certificate** or profit-bearing Islamic instrument
- Teaches compound growth; supports NFIS savings goals
- Shariah-compliant variant essential for national adoption

### 19.2 Donation Bonds

- Sender purchases EDB → transfers to registered charity (Edhi, Shaukat Khanum, etc.)
- Charity redeems at par via RAAST bulk
- Tax receipt auto-generated (if registered with FBR)

### 19.3 Family Group Eidi

- Multiple family members contribute to a pooled EDB
- Recipient receives single "Family Eidi" gift card
- Strengthens digital engagement across generations

### 19.4 Corporate Eidi Program

- Employers distribute EDBs to employees' children
- Bulk issuance API for HR systems
- B2B channel for rapid volume scaling

---

## 20. Policy Recommendations

### For Government (Ministry of Finance)

1. **Approve EDBP in principle** as a flagship NFIS 2024–28 initiative
2. **Issue Eidi Digital Bond Rules, 2026** via SRO under Public Debt Act
3. **Ring-fence redemption reserves** at SBP with 1:1 backing
4. **Mandate CDNS** as operational issuer (leverage existing Digital Prize Bond infrastructure)
5. **Include EDBP savings** in annual budget documentation (printing cost avoidance)

### For State Bank of Pakistan

1. **Charter an EDBP Task Force** (Payments Systems Dept. + Banking Policy + Research)
2. **Integrate redemption** via RAAST Bulk Payments (priority CDNS use case)
3. **Set zero consumer fees** for EDB transactions (consistent with RAAST policy)
4. **Require participation** from systemically important EMIs and banks
5. **Add EDBP metrics** to Quarterly Payment Systems Review
6. **Launch "Digital Eidi" Financial Literacy Week** campaign each Ramadan

### For Banks & Fintechs

1. **API integration** with CDNS EDB Gateway by Q4 2026
2. **UX investment** in culturally resonant Eidi gifting interfaces
3. **Child wallet products** with guardian controls
4. **Agent network training** for assisted onboarding (rural/elderly)
5. **Cross-sell savings products** at redemption moment

### For Researchers & Universities

1. **Apply for SBP Research Department** partnership for pilot evaluation
2. **Publish baseline Eid cash demand study** before pilot launch
3. **Develop financial literacy curriculum modules** around Eidi bonds for schools
4. **Track gender and youth inclusion outcomes** as NFIS contribution evidence

---

## 21. Conclusion

The Eidi Digital Bond Program sits at a rare intersection: **cultural tradition, fiscal discipline, financial inclusion, and existing digital infrastructure** — all aligned in the same direction.

Pakistan has already built the rails (RAAST), the wallets (80M+ accounts), the regulatory framework (Digital Prize Bonds, EMI regulation, NFIS 2024–28), and the policy ambition (75% inclusion, Go Cashless). What has been missing is a **culturally native product** that gives citizens a reason to switch — not because government demands it, but because **giving Eidi digitally is easier, safer, and more meaningful than standing in an ATM line**.

EDBP is that product.

For banking professionals, it represents a scalable, low-risk, high-volume seasonal product with clear interchange economics. For government, it delivers measurable cost savings, documented economic activity, and temporary financing — without inflation. For student researchers, it offers a natural experiment at national scale on financial behavior, gender inclusion, and seasonal liquidity. For families, it preserves Eidi while giving children their first step into the formal economy.

**The infrastructure is built. The culture is ready. The diaspora is connected. The economics are favorable. The time to pilot is now.**

---

## 22. Data Sources & Methodology

This section documents **every category of statistic** used in this paper, how it was obtained, and whether it is **published data** or a **model estimate**.

### 22.1 Data Classification

| Label | Meaning |
|-------|---------|
| **Published** | Sourced from regulator, government, bank, news outlet, or academic paper |
| **Model estimate** | Projection calculated by the authors from published inputs |
| **Program design** | Policy parameter proposed for EDBP — not external data |

### 22.2 Published Statistics — Key Figures & Sources

#### RAAST & Digital Payments

| Stat | Value | Year | Source |
|------|-------|------|--------|
| RAAST transactions (FY25) | 1.27 billion | FY 2024–25 | [INP, 2025](https://www.inp.net.pk/news-detail/inp-wealthpk/raast-handles-pkr-44-trillion-as-pakistans-instant-payment-network-scales-nationwide) |
| RAAST value (FY25) | PKR 29.6 trillion | FY 2024–25 | Same |
| Cumulative RAAST transactions | 1.9 billion | Inception–Jun 2025 | Same |
| Cumulative RAAST value | PKR 44.3 trillion | Inception–Jun 2025 | Same |
| Registered Raast IDs | 45 million | Jun 2025 | Same |
| Q2 FY25 RAAST volume | PKR 6.4 trillion | Q2 FY25 | [Dawn, 2025](https://www.dawn.com/news/1905376) |
| RAAST zero fees / PKR 250K limit | Policy | Current | [Samba Bank RAAST](https://www.samba.com.pk/samba/banking-detail/raast) |
| Mobile banking growth | 62% | Q2 2025 | Dawn, 2025 |

#### Financial Inclusion

| Stat | Value | Year | Source |
|------|-------|------|--------|
| Account ownership | 16% → 64% | 2015 → 2023 | [Business Recorder, Jan 2025](https://www.brecorder.com/news/40342500) |
| Inclusion target | 75% by 2028 | NFIS 2024–28 | Same |
| Gender gap | 34% → 25% target | 2023 baseline | Same |
| Cash preference barrier | Qualitative | NFIS 2024–28 | Same |

#### Eid Economy & Seasonal Cash

| Stat | Value | Year | Source |
|------|-------|------|--------|
| Fresh notes disbursed | PKR 380 billion (peak) | 2017 | [Dawn, 2017](https://www.dawn.com/news/1341892) |
| SBP 8877 SMS notes | ~PKR 30 billion | 2017 | Dawn, 2017 |
| Bank counter + ATM notes | ~PKR 340 billion | 2017 | Dawn, 2017 |
| Pre-Eid withdrawals | ~PKR 250 billion | 2017 est. | Dawn, 2017 |
| Eid remittance inflows | ~$1.8 billion | 2016–17 est. | Dawn, 2017 |
| Deposit volatility (Ramadan/Eid) | Documented | 2002–2010 | [Limodio, UZH](https://www.phd-finance.uzh.ch/dam/jcr:1c25e3b4-75d7-441f-9078-4b71e63e613c/seminar_contract_theory_paper_Limodio.pdf) |
| Pre-Eid withdrawal surge | Qualitative | 2025 | [Dawn, 2025](https://www.dawn.com/news/1916220) |

#### Currency & Printing

| Stat | Value | Year | Source |
|------|-------|------|--------|
| PKR 10 note printing cost | PKR 8–10B/year | ~2025–26 | [Tribune](https://tribune.com.pk/story/2594680/10-rupee-coins-could-save-billions-new-report-recommends) |
| PKR 10 notes share of printing | ~35% | ~2025–26 | Tribune; [Daily Pakistan, Feb 2026](https://en.dailypakistan.com.pk/26-Feb-2026/10-rupee-note-to-be-replaced-with-coin-in-gradual-phase-in-pakistan) |
| Coin transition savings | PKR 40–50B over 10 years | 2026 proj. | Daily Pakistan, Feb 2026 |
| Currency in circulation | ~PKR 11 trillion | 2026 est. | Daily Pakistan, Feb 2026 |

#### Fintech & Wallets

| Stat | Value | Year | Source |
|------|-------|------|--------|
| Total wallet accounts | 80M+ | 2025 | [PaymentBrief](https://paymentbrief.com/markets/pakistan/) |
| JazzCash accounts / MAU | 40M+ / 20.6M | 2025 | [Jazz, Nov 2025](https://jazz.com.pk/media-center/detail/jazz-delivers-strong-2025-growth-as-digital-services-and-network-investments-accelerate-scale) |
| JazzCash GTV | PKR 3.9 trillion | 9M 2025 | Jazz, Nov 2025 |
| Easypaisa users / agents | 35M+ / 170K | 2025 | PaymentBrief; [LIFT](https://itslift.com/insights/jazzcash-vs-easypaisa-payment-integration) |

#### Diaspora & Remittances

| Stat | Value | Year | Source |
|------|-------|------|--------|
| Overseas Pakistanis | ~9–10 million | Est. | [Bureau of Emigration](https://www.beoe.gov.pk); diaspora studies |
| Annual remittances | $30+ billion | FY24–25 | [SBP remittance reports](https://www.sbp.org.pk) |
| Ramadan remittance for Eid | ~60% of inflows | 2016–17 est. | Dawn, 2017 |

#### Global Benchmarks

| Stat | Value | Year | Source |
|------|-------|------|--------|
| Global tokenized bond issuance | $3.7 billion | 2024 | [World Bank](https://blogs.worldbank.org/en/psd/digital-tokenized-bonds--capitalizing-on-future-potential) |
| Philippines GBonds minimum | PHP 500 | 2024–25 | [BusinessWorld, Dec 2024](https://www.bworldonline.com/bloomberg/2024/12/20/642682/philippines-pushes-to-expand-bond-market-with-9-debt-offer/) |
| GCash users | 94 million | 2024 | BusinessWorld, Dec 2024 |

### 22.3 Model Estimates (No Single Official Source)

| Stat | Value | Methodology |
|------|-------|-------------|
| Fresh-note demand displaced | PKR 50–150B/Eid | % of historical fresh-note flows (Dawn 2017) |
| Printing/logistics savings | PKR 7–15B/year | PSPC costs + assumed 25–40% Eid share |
| New account openings (pilot) | 2–5M/Eid | Assumed conversion rate |
| Govt financing float | PKR 30–80B | Purchase-window scenario modelling |
| Diaspora EDB volume | PKR 18–60B | 5–20% adoption × avg bond value |
| Cost avoidance (Year 1) | PKR 4.7–8.5B | Displacement % assumptions (§11.1) |
| KPI targets | Various | Program design parameters |

### 22.4 Primary Official Portals for Updated Data

| Institution | Link |
|-------------|------|
| State Bank of Pakistan | [https://www.sbp.org.pk](https://www.sbp.org.pk) |
| SBP Payment Systems Review | [https://www.sbp.org.pk/psr](https://www.sbp.org.pk/psr) |
| CDNS / National Savings | [https://savings.gov.pk](https://savings.gov.pk) |
| Finance Division (SROs) | [https://www.finance.gov.pk](https://www.finance.gov.pk) |
| SBP RDA (diaspora) | [https://www.sbp.org.pk/rda](https://www.sbp.org.pk/rda) |

### 22.5 Limitations & Caveats

1. **No official Eid withdrawal time series** — SBP does not publish real-time Eid-specific data; historical press estimates (2017) are the best public benchmarks.
2. **Model estimates are illustrative** — all projections require validation through a formal feasibility study and pilot telemetry.
3. **Diaspora figures vary** — overseas Pakistani population estimates range by source; remittance data is official (SBP) but Eid-specific allocation is estimated.
4. **This paper is independent** — it does not represent SBP, MoF, or any commercial institution.

---

## Annexes

### Annex A — Glossary

| Term | Definition |
|------|-----------|
| **EDBP** | Eidi Digital Bond Program |
| **EDB** | Eidi Digital Bond — individual instrument |
| **CDNS** | Central Directorate of National Savings |
| **EMI** | Electronic Money Institution (e.g., JazzCash, Easypaisa) |
| **RAAST** | Pakistan Instant Payment System (SBP-operated) |
| **NFIS** | National Financial Inclusion Strategy |
| **IPS** | Instant Payment System |
| **KYC** | Know Your Customer |
| **P2P** | Person-to-Person (payment) |
| **PSPC** | Pakistan Security Printing Corporation |
| **SRO** | Statutory Regulatory Order |

### Annex B — Denomination Ladder Rationale

| Denomination | Typical Use Case |
|-------------|-----------------|
| PKR 100 | Young children; domestic workers |
| PKR 500 | School-age children; extended family |
| PKR 1,000 | Close relatives; standard adult Eidi |
| PKR 5,000 | Special occasion; urban middle-class gifting |

### Annex C — Pilot City Selection Criteria

1. High mobile wallet penetration
2. RAAST-connected bank branch density
3. Representative urban/rural mix
4. Existing SBP Financial Literacy Week presence
5. Provincial government cooperation for co-marketing

### Annex D — Sample Regulatory Text (Draft Clause)

> *"The Federal Government may issue Eidi Digital Bonds in scripless, registered form for the purpose of facilitating digital transfer of Eidi gifts during Eid-ul-Fitr and Eid-ul-Adha. Such bonds shall be denominated in Pakistani Rupees, shall be fully backed by the Federal Government, and shall be redeemable at par value through the Pakistan Instant Payment System (RAAST) during such periods as may be notified by the Finance Division."*

### Annex E — Implementation Checklist (Quick Reference)

- [ ] Cabinet approval in principle
- [ ] SRO drafted and notified
- [ ] SBP Task Force constituted
- [ ] CDNS registry extended
- [ ] RAAST bulk redemption tested
- [ ] JazzCash + Easypaisa API live
- [ ] NADRA KYC integration verified
- [ ] Child wallet framework approved
- [ ] Redemption reserve account established
- [ ] Security audit completed
- [ ] Pilot marketing campaign ready
- [ ] KPI dashboard operational
- [ ] Academic evaluation partner selected
- [ ] Eid-ul-Fitr 2027 pilot launch

---

## References & Sources

### Pakistan — Diaspora & Remittances

- [SBP — Roshan Digital Account (RDA)](https://www.sbp.org.pk/rda) — Overseas Pakistani account framework
- [Dawn: The expanding Eid economy](https://www.dawn.com/news/1341892) — Eid remittance inflows (~$1.8B, 2016–17 est.)

### Pakistan — Payments & Financial Inclusion

- [SBP National Financial Inclusion Strategy 2024–28](https://www.brecorder.com/news/40342500) — 75% inclusion target; cash culture barrier
- [SBP Quarterly Payment Systems Review Q2 FY25](https://theazb.com/sbp-releases-second-quarterly-payment-systems-review-for-fy-25/) — RAAST 296M txns / PKR 6.4T
- [RAAST handles PKR 44 trillion (INP, 2025)](https://www.inp.net.pk/news-detail/inp-wealthpk/raast-handles-pkr-44-trillion-as-pakistans-instant-payment-network-scales-nationwide) — Cumulative performance data
- [Dawn: Raast quarterly payments surge](https://www.dawn.com/news/1905376) — Go Cashless campaign; 62% mobile banking growth
- [Samba Bank: RAAST overview](https://www.samba.com.pk/samba/banking-detail/raast) — Zero fees; PKR 250K limit
- [CDNS: RAAST integration plans](https://savings.gov.pk/pakistan-instant-payment-system/) — Bulk payments for encashment
- [SBP Digital Bank Regulatory Framework](https://www.sbp.org.pk/dfs/Digital-Bank-Regulatory.html) — DRB licensing
- [Raqami Islamic Digital Bank license (2026)](https://propakistani.pk/2026/05/22/raqami-islamic-digital-bank-limited-granted-commercial-license-by-state-bank-of-pakistan/) — Shariah-compliant digital banking
- [Pakistan Payments Guide (PaymentBrief)](https://paymentbrief.com/markets/pakistan/) — 80M+ wallet accounts

### Pakistan — Currency & Eid Economy

- [Dawn: The expanding Eid economy](https://www.dawn.com/news/1341892) — PKR 380B fresh notes; PKR 250B withdrawals
- [MM News: SBP Eid fresh note guidelines](https://mmnews.tv/sbp-issues-guidelines-for-citizens-to-access-new-currency-notes-ahead-of-eid-ul-fitr/) — 8877 SMS service; ATM loading
- [Tribune: 10-rupee coin transition report](https://tribune.com.pk/story/2594680/10-rupee-coins-could-save-billions-new-report-recommends) — PKR 8–10B annual printing cost
- [Daily Pakistan: Rs10 note replacement](https://en.dailypakistan.com.pk/26-Feb-2026/10-rupee-note-to-be-replaced-with-coin-in-gradual-phase-in-pakistan) — PKR 11T currency in circulation
- [DND: SBP currency printing 2018–2022](https://dnd.com.pk/total-number-of-new-currency-notes-printed-by-sbp-from-2018-2022/276065/) — Printing drivers explained

### Pakistan — Digital Government Savings

- [Digital Prize Bonds Rules 2024 (Finance Division)](https://www.finance.gov.pk/budget/circular_17032025.pdf) — SRO template
- [Business Recorder: Digital prize bonds notified](https://www.brecorder.com/news/40353665) — CDNS mobile app distribution
- [CDNS New Initiatives](https://savings.gov.pk/new-initiatives/) — Scripless certificates; digital prize bonds
- [The News: Govt plans digital prize bonds](https://www.thenews.com.pk/print/1290102-govt-plans-to-introduce-digital-prize-bonds) — Denominations PKR 500–10,000

### Pakistan — Fintech

- [Jazz 2025 Growth Report](https://jazz.com.pk/media-center/detail/jazz-delivers-strong-2025-growth-as-digital-services-and-network-investments-accelerate-scale) — JazzCash 20.6M MAU; PKR 3.9T GTV
- [TechJuice: Mobile wallets momentum](https://www.techjuice.pk/mobile-wallets-gain-momentum-in-push-for-cashless-economy/) — JazzCash 21M MAU; Easypaisa 18M MAU
- [LIFT: JazzCash vs Easypaisa](https://itslift.com/insights/jazzcash-vs-easypaisa-payment-integration) — 70M+ combined accounts

### Global — Tokenized Bonds & Digital Vouchers

- [World Bank: Digital Tokenized Bonds](https://blogs.worldbank.org/en/psd/digital-tokenized-bonds--capitalizing-on-future-potential) — $3.7B global issuance 2024
- [Philippines GBonds via GCash (Ledger Insights)](https://www.ledgerinsights.com/philippines-to-distribute-tokenized-government-bonds-via-gcash-wallet-pdax-crypto-exchange/) — Retail wallet distribution model
- [BusinessWorld: Philippines bond market expansion](https://www.bworldonline.com/bloomberg/2024/12/20/642682/philippines-pushes-to-expand-bond-market-with-9-debt-offer/) — PHP 500 minimum
- [Bank of Korea: Digital voucher pilot](https://koreajoongangdaily.joins.com/news/2024-11-06/business/finance/BOK-to-test-digital-voucher-to-replace-paper-and-plastic-card-vouchers/2172121) — Tokenized deposit vouchers
- [BSP: Digital Christmas cash gifts (Philippines)](https://www.pna.gov.ph/articles/1239715) — Central bank digital gifting advocacy
- [M2P Fintech: India's e-RUPI](https://m2pfintech.com/blog/e-rupi-indias-digital-upgrade-for-the-underbanked/) — Purpose-bound digital voucher model
- [Bangladesh: Prepaid Instrument Guidelines 2024](https://www.vdb-loi.com/bd_publications/regulatory-guidelines-for-prepaid-instruments-in-bangladesh-ensuring-financial-inclusion-and-consumer-protection/) — Gift card regulation

### Academic

- [Limodio: Deposit Volatility & Eid in Pakistan](https://www.phd-finance.uzh.ch/dam/jcr:1c25e3b4-75d7-441f-9078-4b71e63e613c/seminar_contract_theory_paper_Limodio.pdf) — Ramadan/Eid deposit withdrawal patterns

---

**Disclaimer:** This white paper is an independent policy analysis prepared by **Muhammad Ammar Jamshed** in a personal capacity. It does not represent the views of the State Bank of Pakistan, Government of Pakistan, or any commercial institution. The author is not affiliated with any organisation named in this document. All projections are estimates based on publicly available data and should be validated through formal feasibility study before implementation.

---

*© 2026 Muhammad Ammar Jamshed — Eidi Digital Bond Program White Paper v1.1*  
*Author:* [Muhammad Ammar Jamshed on LinkedIn](https://www.linkedin.com/in/goto-resumemuhammad-ammar-jamshed-029280145/)  
*For policy discussion:* independent submission for public and stakeholder review
