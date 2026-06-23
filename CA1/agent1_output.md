================================================================================
AGENT 1 OUTPUT — CUSTOMER SEGMENTATION AND CHURN ANALYSIS REPORT
Agent Archetype: Researcher
Handoff to: Designer
================================================================================

================================================================================
1. BEHAVIOURAL SEGMENTS (5 segments among 31,500 dormant users)
================================================================================

SEGMENT A: COMMUTERS (38%, ~12,000 users)
------------------------------------------
Defining traits:
  - Visit Mon-Fri, 6:30am-8:30am. Never weekends.
  - Average 4.1 visits/month before dormancy (highest frequency of all segments).
  - Top products: Regular latte (62%), Americano (23%), Espresso (15%).
  - Average spend: EUR 4.20/visit (lowest spend, high volume).
  - 82% visited only ONE store — same location every time.
  - 45% have push notifications enabled.
  - 61% have payment method saved.
  - Average 47 days since last visit.

Most likely reason for dormancy:
  Commuters are routine-driven. The most likely cause is a change in commute
  pattern — moved jobs, changed office location, or switched to remote/hybrid
  work — meaning their habitual store is no longer on their route. The data
  supports this: 82% use a single store, and their drop-off has no seasonal
  pattern, suggesting a permanent behaviour shift.

Early-warning signal before dormancy:
  A drop from 4+ visits/month to 2 or fewer visits in a single month, combined
  with zero weekend visits, predicts dormancy within 45 days with ~78% accuracy
  [SPECULATIVE — based on pattern logic, not regression model].

Revenue opportunity (10% reactivation):
  1,200 users × 4.1 visits/month × EUR 4.20 = EUR 20,664/month.

Reactivation feasibility: MEDIUM
  Payment method saved (61%) is good. Push notifications (45%) is moderate.


SEGMENT B: WEEKEND EXPLORERS (26%, ~8,200 users)
--------------------------------------------------
Defining traits:
  - Visit Sat-Sun, 10am-2pm. Never weekdays.
  - Average 2.1 visits/month before dormancy.
  - Top products: Oat-milk flat white (34%), Cold brew (28%), Pastry+coffee
    combo (38%).
  - Average spend: EUR 8.70/visit (highest spend of all segments).
  - 67% visited 3+ different stores — they explore locations.
  - 71% have push notifications enabled (highest of all segments).
  - Only 38% have payment method saved.
  - Average 68 days since last visit.
  - 58% signed up via weekend in-store QR code promotions.

Most likely reason for dormancy:
  Weekend Explorers treat Drift Coffee as a leisure activity, not a necessity.
  They are easily distracted by competing weekend experiences — brunch spots,
  farmers markets, new café openings. Their multi-store exploration pattern
  suggests they value novelty. Without new seasonal products or weekend events,
  they lose interest. The 68-day dormancy is longer than Commuters, suggesting
  gradual drift rather than sudden stop.

Early-warning signal before dormancy:
  A decline from visiting 2+ different stores to visiting only 1, or a shift from
  weekend to no visits for 3 consecutive weekends, predicts dormancy [SPECULATIVE].

Revenue opportunity (10% reactivation):
  820 users × 2.1 visits/month × EUR 8.70 = EUR 14,981/month.

Reactivation feasibility: HIGH
  Push notifications (71%) is excellent. Payment method saved (38%) is low.


SEGMENT C: AFTERNOON TREATERS (21%, ~6,600 users)
---------------------------------------------------
Defining traits:
  - Visit Tue-Thu, 2pm-4pm. Afternoon-only pattern.
  - Average 2.8 visits/month before dormancy.
  - Top products: Mocha (41%), Pastries (44%), Seasonal specials (15%).
  - Average spend: EUR 6.40/visit.
  - 89% visited only stores near residential areas (not business districts).
  - Only 33% have push notifications enabled (lowest of all segments).
  - 52% have payment method saved.
  - Average 92 days since last visit (longest dormancy of recurring segments).
  - 64% stopped visiting in winter months (Nov-Feb).

Most likely reason for dormancy:
  Strongly seasonal. 64% winter drop-off suggests weather-driven behaviour —
  these users prefer walking to a nearby café in pleasant weather and stay
  home in cold/dark months. The afternoon-only pattern suggests they are
  likely remote workers, stay-at-home parents, or students with flexible
  afternoons.

Early-warning signal before dormancy:
  A visit in October followed by no visits in November is the strongest single
  seasonal predictor. Adding: no response to autumn seasonal specials [SPECULATIVE].

Revenue opportunity (10% reactivation):
  660 users × 2.8 visits/month × EUR 6.40 = EUR 11,827/month.

Reactivation feasibility: LOW
  Push notifications (33%) is very low. Payment method saved (52%) is moderate.
  Re-engagement must rely on email primarily.


SEGMENT D: ONCE-ONLY SIGNUPS (12%, ~3,800 users)
--------------------------------------------------
Defining traits:
  - Visited exactly ONCE, then never returned.
  - First visit evenly distributed across all dayparts — no pattern.
  - Top products: any single item. No repeatable pattern detectable.
  - Average spend: EUR 3.90 (lowest spend — one item, no upsell).
  - 91% signed up via in-store QR code (at point of sale).
  - Only 12% have push notifications enabled.
  - Only 18% have payment method saved.
  - Profile completion: 22% on average.
  - Average 144 days since last visit (longest dormancy).

Most likely reason for dormancy:
  These users were never "customers" in a loyalty sense — they signed up at
  the till for a one-time discount or because the barista prompted them. They
  had no intent to become regulars. The low profile completion (22%) and low
  payment method save rate (18%) signal zero commitment. They are essentially
  "accidental signups" with no relationship to the brand.

Early-warning signal before dormancy:
  Profile completion under 30% + no payment method saved within 7 days of signup
  predicts permanent dormancy with near-certainty. This segment can be identified
  immediately — within the first week.

Revenue opportunity (10% reactivation):
  380 users × 1.0 visits × EUR 3.90 = EUR 1,482/month (negligible).

Reactivation feasibility: VERY LOW
  Push (12%) and payment saved (18%) are both critically low. Not worth direct
  re-engagement investment. Better to exclude from reactivation campaigns.


SEGMENT E: FORMER REGULARS (3%, ~900 users)
---------------------------------------------
Defining traits:
  - Previously 5+ visits/month sustained for >6 months, then dropped to zero
    abruptly.
  - All dayparts, all stores — diverse, loyal behaviour.
  - Top products: varied, diverse basket (no single preference).
  - Average spend: EUR 5.80/visit.
  - 78% have push notifications enabled.
  - 85% have payment method saved (highest of all segments).
  - Average 31 days since last visit (most recently dormant).
  - 71% went dormant within 2 weeks of a competing specialty coffee shop
    opening within 400m.

Most likely reason for dormancy:
  Competitive defection. The data is unambiguous: 71% correlate with a new
  competitor opening nearby. These were the most loyal, highest-value customers
  who were poached by a rival. Their abrupt stop (not gradual decline) confirms
  an external trigger, not dissatisfaction with Drift Coffee.

Early-warning signal before dormancy:
  A new specialty coffee shop opening within 400m of a user's primary store,
  combined with that user having 5+ visits/month, predicts defection within
  30 days with high confidence. This is a GEO-COMPETITIVE trigger.

Revenue opportunity (10% reactivation):
  90 users × 5.0 visits/month × EUR 5.80 = EUR 2,610/month.

Reactivation feasibility: HIGH
  Push (78%) and payment saved (85%) are both excellent. These users KNOW the
  brand and had a strong relationship. They are the easiest to win back if the
  right offer is made.


================================================================================
2. CHURN PREDICTOR MATRIX (top 5 signals ranked strongest to weakest)
================================================================================

Rank  Signal                                      Correlation Strength  Notes
----  ------                                      --------------------  -----
  1   Profile completion <30% + no payment         Very Strong           Predicts Once-Only
      method saved within 7 days of signup                               Signups with near-
                                                                         certainty

  2   Competing café opening within 400m of         Strong                Predicts Former
      primary store + user with 5+ visits/month                          Regular defection
                                                                         in 71% of cases

  3   Monthly visit count drops by >50%            Strong                Applies across
      compared to 3-month trailing average                               Commuters and
                                                                         Afternoon Treaters

  4   No weekend visit for 3+ consecutive           Moderate              Specific to Weekend
      weekends + previously consistent weekend                            Explorers
      pattern

  5   No visit in November after visiting in        Moderate              Specific to Afternoon
      October + user in residential-area store                            Treaters (seasonal)

[NOTE: All correlation strengths are derived from the synthetic data patterns
provided. A real production model would require logistic regression or random
forest analysis on the full 45,000-user dataset to produce precise coefficient
values — the above rankings represent directional pattern strength, not
statistical coefficients.]


================================================================================
3. STORE-LEVEL VARIANCE ANALYSIS
================================================================================

Churn is NOT uniform across stores. Significant geographic concentration exists:

  BUSINESS DISTRICT STORES (8 locations):
  - 72% Commuter profiles
  - 4% MoM churn rate increase — steepest and most consistent decline
  - Root cause: remote/hybrid work trends reducing commuter footfall
  - These stores are overexposed to a single segment (Commuters)

  MIXED RESIDENTIAL/COMMERCIAL STORES (12 locations):
  - Balanced segment mix (Weekend Explorers + Afternoon Treaters + Commuters)
  - 2% MoM churn rate increase — moderate
  - More resilient due to segment diversity

  UNIVERSITY CAMPUS STORES (5 locations):
  - High turnover but high new signup volume
  - Strong seasonal pattern: dead in summer (Jun-Aug), peak in term time
  - Net churn offset by new student signups each semester

  SUBURBAN RETAIL PARK STORES (3 locations):
  - 78% of local loyalty users inactive — highest dormant rate
  - Correlate with low footfall outside lunch hours (12pm-1:30pm)
  - These stores have almost no morning or evening trade
  - Likely candidate for operational review beyond loyalty intervention

Key insight: Suburban stores need a fundamentally different strategy — the
location may itself be the problem, not the loyalty programme. Business
district stores need Commuter-specific retention tactics. University stores
should align campaigns with the academic calendar.


================================================================================
4. REACTIVATION FEASIBILITY SUMMARY
================================================================================

  Segment           % of Dormant  Push Opt-in  Payment Saved  Feasibility
  -------           ------------  -----------  -------------  -----------
  Commuters          38%          45%          61%            MEDIUM
  Weekend Explorers  26%          71%          38%            HIGH
  Afternoon Treaters 21%          33%          52%            LOW
  Once-Only Signups  12%          12%          18%            VERY LOW
  Former Regulars     3%          78%          85%            HIGH

Recommendation: Prioritise Weekend Explorers and Former Regulars for immediate
reactivation (highest feasibility). Commuters require channel work (push opt-in
campaign). Afternoon Treaters need email-led seasonal strategy. Once-Only
Signups should be excluded from re-engagement — acquisition cost is better
spent on fresh signups.

================================================================================
END OF RESEARCHER OUTPUT — HANDOFF TO DESIGNER
================================================================================
