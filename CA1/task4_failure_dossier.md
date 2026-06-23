================================================================================
TASK 4: FAILURE DOSSIER
Drift Coffee Co. | Intelligence & Personalisation Lens | Student ID ...71
================================================================================

Three distinct failures the pipeline produced, identified and corrected.


================================================================================
FAILURE 1: Fabricated Uplift Percentages in the Rules Engine
================================================================================

Agent that produced it: Designer (Agent 2)

Exact offending output:
  From the "Personalisation Rules Engine Design" table, Expected Uplift column:

  Rule 1: "+12% visit recovery"
  Rule 2: "+18% weekend return rate"
  Rule 3: "+9% winter retention"
  Rule 4: "-40% future dormant pool growth"
  Rule 5: "+35% win-back rate"
  Rule 6: "+25% effective reach"
  Rule 7: "+30% second visit rate"

How I detected it:
  The Researcher's output — the only input the Designer was allowed to use —
  contains no historical campaign data, no A/B test results, no baseline
  conversion rates, and no statistical models. The Researcher produced a
  descriptive segmentation report, not a predictive model. There is no data
  anywhere in the pipeline that could support a claim like "+18% weekend
  return rate." The Designer invented these numbers. This is a clear
  hallucination: the Designer was asked to produce a rules engine, and it
  filled the "Expected Uplift" column with specific-sounding but entirely
  unsupported percentages to make the table look complete.

Why this failure matters:
  A business that acts on these uplift numbers would set targets, allocate
  budgets, and make staffing decisions based on fabricated projections. If
  the actual uplift for Commuter re-engagement is 3% rather than the claimed
  12%, the business might declare the campaign a failure and abandon it
  prematurely — or worse, continue investing in a campaign that is actually
  performing reasonably well but falling short of an impossible target.

Fix applied:
  Removed the Expected Uplift column from the rules engine entirely. In its
  place, added a column marked [BASELINE REQUIRED] with the instruction:
  "Run each rule against a 5% holdout sample for 14 days before setting
  targets. Only rules with statistically significant uplift (p<0.05) graduate
  to full deployment."

Corrected output (replacement table):

  Rule# | If (Condition)                    | Then (Action)              | Segment  | Uplift
  ------|-----------------------------------|----------------------------|----------|----------
    1   | 14 weekdays no visit + business   | Monday 7:30am product-     | Commuters| [BASELINE
        | district store                    | specific push              |          | REQUIRED]
  ------|-----------------------------------|----------------------------|----------|----------
    2   | 3 missed weekends + favourite     | Friday 5pm combo offer     | Weekend  | [BASELINE
        | product in profile                | push, multi-store          | Explorers| REQUIRED]
  ------|-----------------------------------|----------------------------|----------|----------
    3   | Residential store + Oct-Mar +     | Monthly afternoon email.   | Afternoon| [BASELINE
        | last purchase mocha/pastry        | Suppress push.             | Treaters | REQUIRED]
  ------|-----------------------------------|----------------------------|----------|----------
    4   | QR sign-up + 7 days + profile     | Auto-archive profile.      | Once-Only| [BASELINE
        | <30% complete                    | Suppress marketing.        | Signups  | REQUIRED]
  ------|-----------------------------------|----------------------------|----------|----------
    5   | Competitor within 400m + 5+       | Free-drink push within     | Former   | [BASELINE
        | visits/month                      | 7 days, highest priority   | Regulars | REQUIRED]
  ------|-----------------------------------|----------------------------|----------|----------
    6   | Push bounce / permissions revoked | Fallback to email within   | All      | [BASELINE
        |                                   | 4 hours                    |          | REQUIRED]
  ------|-----------------------------------|----------------------------|----------|----------
    7   | Offer redeemed + visit within     | Move to Active-Recovered.  | All      | [BASELINE
        | 7 days                            | 30-day cooldown.           |          | REQUIRED]

  [BASELINE REQUIRED] = Deploy each rule to a 5% holdout group for 14 days.
  Measure actual uplift against a matched control. Only deploy rules with
  statistically significant positive uplift (p<0.05) to the full audience.


================================================================================
FAILURE 2: Hardcoded Product Names Instead of Personalisation Variables
================================================================================

Agent that produced it: Communicator (Agent 3)

Exact offending output:
  From the Weekend Explorers segment messaging:

  PUSH (72 chars):
  "Saturday exploring? Oat-milk flat white + pastry, EUR 2 off. Any location."

  EMAIL BODY:
  "Hi [FIRST NAME], it's been a few weekends since we saw you. Your favourite
  oat-milk flat white and pastry combo is EUR 2 off this Saturday or Sunday
  at any Drift Coffee — try a location you've not visited yet."

How I detected it:
  The Communicator's own output includes a "Personalisation Variable Map" that
  lists [FAVOURITE PRODUCT] as a variable field with example value "oat-milk
  flat white." This means the Communicator understood, in principle, that
  product names should be personalisation variables — yet the actual push
  notification and email body hardcode "oat-milk flat white" as static text.
  The Researcher's data shows that only 34% of Weekend Explorers prefer
  oat-milk flat white. The remaining 66% prefer cold brew (28%) or
  pastry+coffee combos (38%). For two-thirds of this segment, the
  Communicator is promoting a product they may not even like.

  This is a handoff failure: the Communicator received the Designer's
  instruction that offers should use "the product they prefer," but failed to
  implement that instruction as a dynamic variable in the actual copy. Instead,
  it defaulted to the most common product in the segment and treated it as
  universal.

Why this failure matters:
  A push notification offering "oat-milk flat white" to a customer whose
  purchase history shows exclusively cold brew communicates the opposite of
  personalisation — it tells the customer "we don't actually know you." This
  damages the very trust the Intelligence & Personalisation lens is meant to
  build. In a production deployment, this bug would affect approximately 5,400
  Weekend Explorers (66% of 8,200) who would receive an irrelevant product
  offer.

Fix applied:
  Replaced all hardcoded product names with the [FAVOURITE PRODUCT] variable
  placeholder in 3 out of 5 segments where product specificity was used
  (Commuters, Weekend Explorers, Afternoon Treaters). Former Regulars and
  Once-Only Signups were unaffected — Former Regulars receive a free "any
  drink" offer, and Once-Only Signups are excluded.

Corrected output:

  Commuters — PUSH (variable-length):
  "Your usual [FAVOURITE PRODUCT] is waiting. EUR 2 off this week before 9am."

  Commuters — EMAIL BODY first sentence:
  "Hi [FIRST NAME], we noticed it's been a little while since your last visit
  to [PRIMARY STORE NAME]. Your regular [FAVOURITE PRODUCT] is waiting — and
  this week, it's EUR 2 off when you stop by before 9am."

  Weekend Explorers — PUSH (variable-length):
  "Saturday exploring? [FAVOURITE PRODUCT] + pastry, EUR 2 off. Any location."

  Weekend Explorers — EMAIL BODY first sentence:
  "Hi [FIRST NAME], it's been a few weekends since we saw you. Your favourite
  [FAVOURITE PRODUCT] and pastry combo is EUR 2 off this Saturday or Sunday
  at any Drift Coffee."

  Afternoon Treaters — EMAIL BODY (already correct — used variable):
  "Your favourite mocha is waiting." — BUT corrected to "Your favourite
  [FAVOURITE PRODUCT] is waiting."

  Note: For segments where the Designer specified a combo offer (Weekend
  Explorers: drink + pastry), the pastry part remains static. The variable
  applies only to the drink component. This is acceptable because the
  Researcher's data shows 38% of Weekend Explorers already buy pastry combos
  — it is a segment-wide behaviour, not an individual preference that needs
  personalisation.


================================================================================
FAILURE 3: Unsupported A/B Test Sample Size Claim
================================================================================

Agent that produced it: Designer (Agent 2)

Exact offending output:
  "Sample size: 1,200 users total (600 per variant), drawn from Commuter
  segment only. Statistical significance requires minimum 5% uplift to detect
  with 80% power — 600 per group achieves this at 95% confidence."

How I detected it:
  A power calculation requires knowing the expected baseline conversion rate.
  The formula is:

    n = (Z_alpha/2 + Z_beta)^2 x (p1(1-p1) + p2(1-p2)) / (p2 - p1)^2

  Where p1 = baseline rate, p2 = expected variant rate. Without p1, the
  calculation is mathematically impossible.

  If the baseline redemption rate is 2% (a realistic cold-email/push rate for
  dormant users), detecting a 5 percentage point uplift (to 7%) with 80% power
  at 95% confidence requires approximately 1,100 per group — nearly double the
  stated 600. If the baseline is 0.5% (more realistic for 47-day-dormant
  users), the required sample size exceeds 5,000 per group.

  The Designer stated a sample size with apparent statistical precision but
  omitted the single most important input — the baseline rate — making the
  claim unfalsifiable and the sample size unsupportable. This is a dressed-up
  guess presented as a calculation.

Why this failure matters:
  An underpowered A/B test produces false negatives. If the store-finder
  variant genuinely outperforms the product-offer variant by 5 percentage
  points but the test is underpowered, the result will not reach statistical
  significance and the Designer will incorrectly conclude "no difference" —
  missing the single most strategically important insight in the entire
  pipeline (whether Commuters churned due to changed commute patterns).

Fix applied:
  Replaced the unsupported power calculation with an honest statement of what
  is unknown and a two-phase testing recommendation.

Corrected output:

  Sample size: 1,200 users (600 per variant), drawn from the Commuter segment.

  IMPORTANT CAVEAT: The minimum required sample size depends on the baseline
  redemption rate, which is currently unknown because Drift Coffee has never
  run a re-engagement campaign. If the baseline redemption rate is:
    - 10%: 600 per group is sufficient to detect a 5pp uplift (80% power, 95% confidence)
    - 5%:  600 per group is sufficient to detect a 5pp uplift
    - 2%:  ~1,100 per group required
    - 1%:  ~2,400 per group required
    - 0.5%: >5,000 per group required

  RECOMMENDATION: Run a 7-day pilot on 200 users per variant first. Use the
  observed redemption rate from the pilot as the baseline for a proper power
  calculation before scaling to the full 1,200-user test. If the pilot shows
  a baseline rate below 2%, increase the sample size or extend the test
  duration before declaring a result.

  Success metric: Offer redemption rate (primary). Store-switch rate (secondary).

  Decision rule: If Variant B outperforms Variant A by a statistically
  significant margin (p<0.05), the commute-change hypothesis is supported
  and the Commuter journey is updated. If no significant difference is found,
  the product-offer approach stands as the default.


================================================================================
LESSON CARRIED FORWARD
================================================================================

The Designer produced the two most dangerous failures in this pipeline:
fabricated numbers (Failure 1) and false statistical precision (Failure 3).
Both share a common root cause: when an agent is asked to produce a
"complete" output — a table with all columns filled, a test with all
parameters stated — it will invent data to fill gaps rather than leave a cell
empty or admit what it does not know.

The honest, specific lesson I will carry forward is: prompt every agent in a
multi-agent pipeline with an explicit "do not guess" instruction that names
the specific data types the agent is likely to invent. For a Designer agent,
that instruction must include: "If a number cannot be derived from the
Researcher's data, do not invent it. Write [UNKNOWN] and state what data
you would need." The pipeline's vulnerability is not that agents produce bad
answers — it is that they produce plausible-looking answers with no
evidentiary basis, and those answers look identical to real ones in a
formatted table. A downstream agent or a human reviewer cannot distinguish a
calculated number from an invented one unless the inventing agent is forced to
label its own uncertainty. This must be a design constraint on the system
prompt, not a trust-based expectation of agent behaviour.

================================================================================
END OF FAILURE DOSSIER
================================================================================
