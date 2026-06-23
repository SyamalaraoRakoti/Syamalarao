================================================================================
TASK 1: STRATEGIC DIAGNOSIS
Drift Coffee Co. through the Intelligence & Personalisation Lens
================================================================================

STUDENT ID: ........71
SCENARIO CODE: 1 (Drift Coffee Co.)
LENS CODE: 2 (Intelligence & Personalisation)


1. BUSINESS CONTEXT

Drift Coffee Co. operates 28 specialty coffee locations with a loyalty app
counting 45,000 registered users. The business faces a dual crisis: average
monthly customer visits have fallen from 3.2 to 1.8 (a 44% decline), and 70%
of loyalty app members — 31,500 customers — are inactive.

Through the Intelligence and Personalisation lens, the root cause is clear:
Drift Coffee collects data but does not use it to create tailored, relevant
experiences at scale. Every customer receives the same offers, the same menu,
and the same journey regardless of their behaviour, preferences, or lifecycle
stage. The following three challenges are the most critical to address.


2. THREE CRITICAL CHALLENGES


CHALLENGE 1: Dormant Loyalty Data — The Silent 31,500

Why it matters
Drift Coffee's loyalty app holds 45,000 profiles with purchase histories,
location data, and behavioural signals — but 31,500 of these profiles are
inactive. Through the Intelligence lens, this is not a marketing failure; it
is a data activation failure. The business sits on enough behavioural data to
power individual-level re-engagement but runs no personalisation engine to
mine it. Reactivating just 10% of the dormant base (3,150 customers) at the
previous visit rate of 3.2/month would contribute 10,080 incremental visits
per month across the chain. The loyalty programme is currently a cost centre
rather than a growth engine.

Key metrics connected
  - Loyalty app DAU/MAU ratio
  - Time since last visit (in days)
  - Push notification opt-in rate
  - Offer redemption rate
  - App session frequency

Signals for root-cause diagnosis
  - Individual SKU-level purchase histories — to identify favourite products
    for personalised offers
  - Geolocation at visit time — to determine which store each dormant user
    last visited
  - Time-of-day and day-of-week visit patterns — to time re-engagement
    messages for maximum relevance
  - Average spend per historical visit — to calibrate offer value without
    eroding margin
  - Offer redemption history — to distinguish price-sensitive dormant users
    from experience-driven dormant users
  - Last app login date and session duration — to gauge disengagement severity
  - Notification permission status — to select reachable vs. unreachable
    segments


CHALLENGE 2: The Personalisation Gap — Undifferentiated Experience Driving
Churn

Why it matters
Visit frequency has dropped from 3.2 to 1.8 per month. Without intelligence
on why individual customers visit less, Drift Coffee cannot arrest the
decline. The gap signals an undifferentiated experience: every customer sees
the same menu, receives the same generic push notifications, and encounters
the same in-store journey regardless of their preferences, visit patterns, or
lifecycle stage. A student grabbing an espresso at 8am on a weekday and a
freelancer working for three hours ordering multiple oat-milk lattes are
treated identically. If the remaining 13,500 active loyalty members follow
the same trajectory as the 31,500 already dormant, Drift Coffee loses
approximately 18,900 visits per month.

Key metrics connected
  - Average inter-visit interval (trend over time)
  - Cohort retention curves (by join month)
  - Basket size evolution per customer
  - Product affinity clusters
  - Time-of-day attendance patterns by store

Signals for root-cause diagnosis
  - Customer visit cadence — days between consecutive visits, segmented by
    customer archetype
  - Product purchase sequences — does a flat-white buyer ever switch to cold
    brew? Are they stuck in a routine or bored?
  - Customisation patterns — milk alternatives, syrup additions, extra shots,
    signalling sophistication and willingness to pay
  - Store-by-store traffic heatmaps — identifying cannibalisation,
    underserved catchment zones, and location-specific preferences
  - Dwell time — from app check-in to payment, indicating whether customers
    treat Drift as grab-and-go or a third place
  - Seasonal visit patterns — detecting weather-driven or academic-calendar-
    driven churn vs. permanent disengagement
  - Competitive density within 500m of each store — is churn higher where
    three rival cafes opened?


CHALLENGE 3: Blind Onboarding — No AI-Driven First-Visit-to-Loyalty Funnel

Why it matters
Drift Coffee signs up new loyalty app users but has no intelligent mechanism
to convert a first-time visitor into a regular. The first 72 hours after app
registration represent the highest-intent window in the customer lifecycle —
yet the onboarding journey is identical for every user. Through the
Intelligence & Personalisation lens, this is a segmentation and prediction
failure: the business lacks a model that classifies each new sign-up by
likely value, preferred product category, and optimal communication cadence,
and then routes them into a personalised nurture sequence.

If even 20% of the 31,500 dormant users had been properly onboarded from day
one, many might never have gone dormant. The current "leaky bucket" makes
acquisition spend inefficient — new users are added only to drift away within
weeks because there is no intelligent hook.

Key metrics connected
  - First-visit-to-second-visit conversion rate
  - Average days between 1st and 2nd visit
  - 7-day new-user retention
  - 30-day new-user retention
  - Welcome offer redemption rate
  - Profile completion percentage

Signals for root-cause diagnosis
  - Sign-up source — in-store QR code vs. app store search vs. referral link
    (each implies different intent levels)
  - First purchase item and time — a 7am espresso signals a commuter; a 2pm
    pastry signals a different need state entirely
  - Profile completion percentage — users who set preferences and save
    payment are more likely to return
  - Notification permission grant rate — a proxy for willingness to be
    engaged; decline signals low intent
  - Payment method saved — users who add a card have roughly 3x higher
    second-visit probability (industry benchmark)
  - Demographic signals — age bracket and neighbourhood from postcode enable
    hyperlocal offer targeting
  - First-store location — proximity to home vs. workplace drives different
    visit cadences and needs different nurture logic


3. VISUAL: CHALLENGE INTERRELATIONSHIP MATRIX

The three challenges are not independent. Dormant loyalty data (C1) is the
consequence of undifferentiated experience (C2) and failed onboarding (C3).
The personalisation gap (C2) makes onboarding impossible to optimise (C3).
Addressing them requires a sequenced, data-driven approach — fixing
onboarding first, then personalisation, then re-activation.


CAUSAL CHAIN DIAGRAM:

   [C3: Blind        fails to convert     [C2: Personalisation    creates dormant    [C1: Dormant
    Onboarding]  ──────────────────────>   Gap]               ──────────────────>   Loyalty Data]

        |
        └──→ DOWNSTREAM BUSINESS IMPACT:
              - 44% visit-frequency decline
              - 70% loyalty programme inactivity
              - Shrinking active customer base

RELATIONSHIP TABLE:

  C1 is the OUTCOME of C2 — inactive users are created by generic experiences [STRONG]
  C1 contains 31,500 users who passed through C3 and were lost [STRONG]
  C2 cannot re-engage dormant users because it has no active signal [STRONG]
  C2 makes C3 worse — a generic first experience fails to hook new users [MODERATE]
  Fixing C3 prevents future C1 — proactive beats reactive [MODERATE]
  C3 needs C2's personalisation engine to route new users [MODERATE]

The three challenges form a single interconnected problem. You cannot fix C1
(re-activation) without first addressing C2 (personalisation), and you cannot
fix C2 without first fixing C3 (onboarding). Each is a gatekeeper of the next.


4. SEQUENCING AND STRATEGIC IMPLICATION

The Intelligence & Personalisation lens demands a sequenced solution:

    C3 (Onboarding)  →  C2 (Personalisation)  →  C1 (Re-activation)

Fixing onboarding first (C3) stops the leak at the top of the funnel — new
sign-ups become active users rather than adding to the dormant pool.
Personalisation (C2) then keeps them engaged by tailoring every interaction.
Finally, the historical dormant data (C1) is mined using the same
personalisation engine to win back lapsed customers.

Attempting the reverse — re-activating dormant users with generic offers
while onboarding and personalisation remain broken — would win users back
only to lose them again within weeks.

Recommended execution sequence:
  Step 1: C3 — Build intelligent onboarding funnel
  Step 2: C2 — Deploy personalisation engine across all touchpoints
  Step 3: C1 — Mine dormant data and run re-activation campaigns

================================================================================
END OF TASK 1
================================================================================
