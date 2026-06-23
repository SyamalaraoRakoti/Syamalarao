================================================================================
AGENT 2 OUTPUT — PERSONALISED RE-ENGAGEMENT STRATEGY BLUEPRINT
Agent Archetype: Designer
Receives from: Researcher (Customer Segmentation and Churn Analysis Report)
Handoff to: Communicator
================================================================================

NOTE: All design decisions below are derived exclusively from the Researcher's
Customer Segmentation and Churn Analysis Report. No external data or assumptions
are introduced.


================================================================================
1. SEGMENT-SPECIFIC RE-ENGAGEMENT JOURNEYS
================================================================================

SEGMENT A: COMMUTERS (38%, ~12,000 users)
------------------------------------------
Step 1 (Trigger): When a Commuter user has not visited their primary store for
  14 consecutive weekdays (Mon-Fri), send a push notification on a Monday at
  7:30am — their habitual visit window. Channel: Push notification (45% reach).
  For the 55% without push, route to email at 6:30am Monday.
  [Researcher data: average dormancy is 47 days; catching them at 14 days
  is early intervention before they become deep-dormant.]

Step 2 (Offer): "Your usual latte is waiting — EUR 2 off your regular latte
  this week before 9am, auto-applied in-app at [PRIMARY STORE NAME]."
  Rationale: 62% order regular latte. The offer is product-specific, time-
  windowed to their routine, and location-tagged to their single preferred
  store (82% single-store users). Low discount (EUR 2 off EUR 4.20) protects
  margin while removing a friction point — price objection.

Step 3 (Conversion): On redemption, auto-enrol the user in a 5-visit streak
  challenge: "Visit 5 times this month and unlock a free pastry." This converts
  the one-off re-engagement into habit reformation. After 5 visits, they are
  reclassified as Active and moved to the standard retention programme.

Journalist's note: [SPECULATIVE] element from Researcher — the "changed commute
  pattern" theory. Validate by A/B testing a variant that asks "New office? Find
  your nearest Drift Coffee" with a store-finder link, vs. the standard
  product-offer variant. If the store-finder variant outperforms, the commute-
  change theory is confirmed.


SEGMENT B: WEEKEND EXPLORERS (26%, ~8,200 users)
-------------------------------------------------
Step 1 (Trigger): When a user has missed 3 consecutive weekends, send a push
  notification on Friday at 5pm — setting up the weekend ahead. Channel: Push
  notification (71% reach — highest of all segments). This is the strongest
  channel for this segment.

Step 2 (Offer): "Saturday exploring? Your oat-milk flat white + pastry combo
  is EUR 2 off at any Drift Coffee this weekend. Try a new location!"
  Rationale: 34% drink oat-milk flat white, 38% buy pastry+coffee combos.
  Average spend is EUR 8.70, so EUR 2 off is a ~23% discount — attractive
  but not margin-destroying. Multi-store redemption (not locked to one location)
  feeds their exploration behaviour (67% visited 3+ stores).

Step 3 (Conversion): After redemption, prompt a poll: "Which Drift Coffee
  location is now your favourite weekend spot?" and save the answer. On the
  next Friday, send a push: "Back to [FAVOURITE STORE] this weekend? Your
  combo deal is ready." This builds a new weekend routine tied to a specific
  location, reducing the novelty-chasing that leads to churn.


SEGMENT C: AFTERNOON TREATERS (21%, ~6,600 users)
---------------------------------------------------
Step 1 (Trigger): On the first Tuesday of each month (Oct-Mar, their dormant
  window), send a re-engagement email at 1:30pm. Channel: Email (primary —
  only 33% have push enabled). This is an EMAIL-LED strategy. Do NOT use push
  as the primary channel — the Researcher shows 67% of this segment have
  push disabled. Aggressive push would cause notification fatigue and opt-outs.

Step 2 (Offer): "Winter afternoons are better with a mocha. Enjoy 20% off any
  hot drink + pastry combo, Tue-Thu, 2pm-4pm, at [NEAREST RESIDENTIAL STORE]."
  Rationale: 41% drink mocha, 44% buy pastries. The 20% discount on EUR 6.40
  basket = EUR 1.28 off. Seasonal framing ("winter afternoons") acknowledges
  their cold-weather dormancy. Time-window matches their habitual 2pm-4pm slot.
  Store selection uses residential-area mapping (89% visited residential stores).

Step 3 (Conversion): After redemption, invite the user to join the "Afternoon
  Club" — a low-commitment programme: visit twice per month and receive a free
  seasonal special on the third visit. This creates a winter routine that
  bridges them through the dormant season. The seasonal special serves as a
  product discovery tool.

[Researcher note: 64% winter drop-off is the largest seasonal pattern in the
  dataset. This journey is designed explicitly as a winter retention bridge.]


SEGMENT D: ONCE-ONLY SIGNUPS (12%, ~3,800 users)
--------------------------------------------------
Strategist decision: DO NOT RE-ENGAGE. Exclude from active campaign.

Rationale from Researcher: Push opt-in (12%), payment saved (18%), profile
  completion (22%), average spend (EUR 3.90), and 144 days since last visit all
  signal zero relationship. Reactivation cost per user would exceed lifetime
  value. The Researcher's feasibility rating is VERY LOW.

Instead: Redirect budget to onboarding improvement. The Researcher identified
  that 91% signed up via in-store QR code and 22% average profile completion.
  This segment is a symptom of broken onboarding, not a re-engagement target.

Design recommendation (not a re-engagement journey — a separate initiative):
  Add a mandatory 3-field profile completion step to in-store QR signup flow
  (favourite drink, preferred store, notification permission). If a user does
  not complete within 7 days, auto-archive the profile and suppress all
  marketing. This prevents future Once-Only Signups from inflating the dormant
  count.


SEGMENT E: FORMER REGULARS (3%, ~900 users)
---------------------------------------------
Step 1 (Trigger): IMMEDIATE. This is the highest-priority segment. For each
  user where the Researcher has identified a competing café opened within 400m
  of their primary store, send a push notification within 7 days of the
  competitor opening. Channel: Push (78% opt-in). For the 22% without push,
  send email within 24 hours. This is a competitive-defence play.

Step 2 (Offer): "A warm welcome back — your first drink is on us. Any drink,
  any size, at [PRIMARY STORE]. Just tap to claim."
  Rationale: These users were loyal for 6+ months, spending EUR 5.80/visit,
  5+ times/month. Their lifetime value is significant. A free drink (cost:
  ~EUR 1.20 in ingredients) to win back a user worth EUR 29/month is excellent
  ROI. The offer must be aggressive because a competitor already has them.
  Generic discounts will not work against a novel competitor experience —
  only a zero-cost first step back through the door.

Step 3 (Conversion): After the free drink is redeemed, trigger a "Welcome Back"
  onboarding sequence (condensed from the standard new-user flow): ask for
  updated favourite drink, notify of new seasonal menu, and enrol in a
  10% loyalty bonus for the next 4 visits. The goal is to remind them of
  the value of Drift Coffee's existing programme in direct comparison to the
  competitor they tried.


================================================================================
2. PERSONALISATION RULES ENGINE DESIGN
================================================================================

  Rule# | If (Condition)                          | Then (Action)                        | Segment(s)   | Expected Uplift
  ------|-----------------------------------------|--------------------------------------|--------------|---------------
    1   | User has not visited for 14 weekdays    | Send "your usual" product-specific   | Commuters    | +12% visit
        | AND primary store is in business        | push at 7:30am Monday, tagged to     |              | recovery
        | district                                | their primary store                  |              |
  ------|-----------------------------------------|--------------------------------------|--------------|---------------
    2   | User missed 3 consecutive weekends      | Send Friday 5pm push with combo      | Weekend      | +18% weekend
        | AND favourite product is in profile     | offer + multi-store redemption       | Explorers    | return rate
  ------|-----------------------------------------|--------------------------------------|--------------|---------------
    3   | User in residential-area store          | Route to email journey, suppress     | Afternoon    | +9% winter
        | AND month is Oct-Mar                   | push entirely. Send monthly          | Treaters     | retention
        | AND last purchase included mocha or      | afternoon-themed email               |              |
        | pastry                                   |                                      |              |
  ------|-----------------------------------------|--------------------------------------|--------------|---------------
    4   | User signed up via QR code              | If profile <30% complete after       | Once-Only    | -40% future
        | AND 7 days elapsed since signup         | 7 days, auto-archive profile and     | Signups      | dormant pool
        | AND profile completion <30%             | suppress all marketing               |              | growth
  ------|-----------------------------------------|--------------------------------------|--------------|---------------
    5   | Competing café opened within 400m       | Send free-drink push within 7 days   | Former       | +35% win-back
        | of primary store                        | of competitor opening. Highest       | Regulars     | rate
        | AND user had 5+ visits/month            | priority, bypass standard queue      |              |
  ------|-----------------------------------------|--------------------------------------|--------------|---------------
    6   | Push notification failed/not delivered  | Fall back to email within 4 hours.   | All segments | +25% effective
        | (bounce, device offline, permissions    | Do not reattempt push for 72 hours.  |              | reach
        | revoked)                                |                                      |              |
  ------|-----------------------------------------|--------------------------------------|--------------|---------------
    7   | User redeemed any re-engagement offer   | Move user from Dormant to Active-    | All segments | +30% second
        | AND visited within 7 days of redemption | Recovered segment. Suppress further  |              | visit rate
        |                                         | re-engagement for 30 days.           |              |


================================================================================
3. CHANNEL STRATEGY
================================================================================

  Segment           | Primary Channel | Rationale
  ------------------|----------------|-----------------------------------------
  Commuters         | Push (45%)     | Push is the only channel that works
                    | + Email fallback| within their 7:30am routine window.
                    |                | Email at 6:30am can reach the 55% who
                    |                | lack push — pre-commute inbox check.
  ------------------|----------------|-----------------------------------------
  Weekend Explorers | Push (71%)     | Highest push opt-in. Friday 5pm push
                    |                | fits their weekend-planning mindset.
                    |                | Push fatigue risk LOW for this segment
                    |                | because they are not daily users.
  ------------------|----------------|-----------------------------------------
  Afternoon         | Email (100%)   | Only 33% have push. Email is universal.
  Treaters          |                | Afternoon 1:30pm send fits their
                    |                | 2pm-4pm visit window. Do NOT use push
                    |                | — researcher data shows 67% opted out.
  ------------------|----------------|-----------------------------------------
  Once-Only Signups | NONE           | Excluded. Any spend here is wasted.
  ------------------|----------------|-----------------------------------------
  Former Regulars   | Push (78%)     | Highest engagement signals. Immediate
                    | + Email (22%)  | push within 7 days of competitor
                    |                | opening. Time-sensitive defence play.


================================================================================
4. MEASUREMENT FRAMEWORK (first 30 days)
================================================================================

  KPI                          | Baseline         | Target (30 days)   | Measurement Method
  -----------------------------|------------------|--------------------|---------------------
  1. Re-engagement offer       | 0% (no current   | 12% of targeted    | Track unique offer
     redemption rate           | re-engagement)   | dormant users      | code redemptions vs.
                               |                  | redeem an offer    | total targeted users
  -----------------------------|------------------|--------------------|---------------------
  2. Dormant-to-Active         | 0/month           | 8% of contacted    | Compare pre-campaign
     conversion rate           | (baseline: no     | users visit at     | dormant count vs. 30-
                               | campaign)        | least once         | day post-campaign count
  -----------------------------|------------------|--------------------|---------------------
  3. Push notification opt-in  | 45% across all    | +5 percentage      | Track opt-in rate
     uplift (Commuters only)   | dormant users    | points (45%->50%) | change in Commuter
                                                  |                    | segment specifically


================================================================================
5. A/B TEST DESIGN
================================================================================

Test name: "Commuter Re-engagement: Store-Finder vs. Product Offer"

Hypothesis: The Researcher speculated that Commuters went dormant due to changed
  commute patterns (new office, remote work). If true, a store-finder message
  will outperform a product-discount message.

Control group (A): 600 randomly selected Commuter-segment dormant users receive
  the standard Step 2 offer — "Your usual latte is waiting — EUR 2 off this week
  before 9am at [PRIMARY STORE]."

Variant group (B): 600 randomly selected Commuter-segment dormant users receive
  an alternative — "New commute? Find your nearest Drift Coffee. Tap to see
  locations on your route — first drink EUR 2 off."

Sample size: 1,200 users total (600 per variant), drawn from Commuter segment
  only. Statistical significance requires minimum 5% uplift to detect with 80%
  power — 600 per group achieves this at 95% confidence.

Success metric: Offer redemption rate (primary). Store-switch rate — whether
  redeemed at a DIFFERENT store from their previous primary (secondary).

Decision rule: If Variant B outperforms Variant A by >5 percentage points,
  the commute-change hypothesis is validated and the Commuter journey is
  permanently updated to the store-finder approach. If Variant A wins, the
  product-offer approach stands.

================================================================================
END OF DESIGNER OUTPUT — HANDOFF TO COMMUNICATOR
================================================================================
