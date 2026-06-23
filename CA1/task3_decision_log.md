================================================================================
TASK 3: DECISION LOG
Drift Coffee Co. | Intelligence & Personalisation Lens | Student ID ...71
================================================================================

Every consequential decision made in designing and orchestrating the three-agent
pipeline. Each entry states the choice made, the credible alternative rejected,
and the specific reason for the choice.


================================================================================
DECISION 1: Archetype Selection — Researcher, Designer, Communicator
================================================================================

Choice made:
  Selected Researcher, Designer, and Communicator from the five available
  archetypes (Researcher, Designer, Maker, Communicator, Manager).

Alternative rejected:
  A Maker-Communicator-Manager pipeline, where the Maker would build a working
  dashboard or prototype, the Communicator would present it, and the Manager
  would orchestrate and quality-check.

Reason:
  The brief asked for something "the business could act on" — a strategy,
  campaign, or operational plan. Drift Coffee Co. does not need a software
  prototype; it needs to understand WHO its dormant customers are (Researcher),
  WHAT to do about them (Designer), and HOW to say it to them (Communicator).
  A Maker would have produced a dashboard or app feature, which sounds
  impressive but is not what a 28-location coffee chain needs to deploy
  immediately. The Researcher-Designer-Communicator chain produces a complete
  marketing-operations handoff: data → strategy → execution-ready copy. This is
  directly deployable by a marketing team without engineering dependency.

Trade-off created:
  By excluding Maker, we produced no interactive prototype or dashboard that
  could demonstrate the personalisation rules in real-time. The pipeline's
  output must be manually implemented by a marketing team rather than automated
  through a system. This is acceptable for a strategy-phase engagement but
  would need a Maker step before production deployment.


================================================================================
DECISION 2: Pipeline Sequence — Researcher First
================================================================================

Choice made:
  Researcher → Designer → Communicator. The Researcher produces a segmentation
  report first, which the Designer then uses to build journeys, which the
  Communicator then translates into copy.

Alternative rejected:
  Designer → Researcher → Communicator — starting with a strategy, then
  validating it against data, then writing copy. Or Communicator-first — writing
  copy first and then checking if the data supports it.

Reason:
  Through the Intelligence & Personalisation lens, data must precede strategy.
  If the Designer creates journeys before seeing the Researcher's segmentation,
  those journeys would be built on assumptions rather than evidence. The
  Researcher identified, for example, that Afternoon Treaters had only 33% push
  notification opt-in — a fact that fundamentally changed the Designer's
  channel strategy to email-only. That decision could not have been made without
  the Researcher's data. Sequencing data before design ensures every downstream
  choice is evidence-grounded, which is the core demand of the Intelligence lens.

Trade-off created:
  Data-first means the Researcher needs rich input to produce useful output.
  If the Researcher's segmentation were weak or generic, the entire pipeline
  would fail at the first step. A Designer-first approach would have been more
  resilient to poor data — but also more likely to produce data-ungrounded
  recommendations, which contradicts the lens.


================================================================================
DECISION 3: Five Segments, Not Three or Seven
================================================================================

Choice made:
  The Researcher produced exactly five customer segments: Commuters, Weekend
  Explorers, Afternoon Treaters, Once-Only Signups, and Former Regulars.

Alternative rejected:
  Three broader segments (High-value, Mid-value, Low-value dormant) — simpler
  but less actionable — or seven narrower segments that split Commuters into
  bus commuters, train commuters, and car commuters.

Reason:
  Five segments is the minimum number that captures meaningfully different
  re-engagement strategies. Three segments would have collapsed Commuters and
  Former Regulars into "high-value," losing the critical distinction that
  Former Regulars defected due to local competition while Commuters drifted due
  to routine change — two problems requiring two completely different offers.
  Seven segments would have added granularity without adding strategic value:
  the difference between a bus commuter and a train commuter does not change
  the re-engagement message. Five is the point where each segment demands a
  different journey without creating segments too small to target profitably.

Trade-off created:
  Five segments means the Communicator had to write for five audiences, which
  is more work than three. But it also means the output is genuinely
  personalised rather than generically segmented, which is the entire point
  of the Intelligence & Personalisation lens.


================================================================================
DECISION 4: Excluding Once-Only Signups from Re-engagement
================================================================================

Choice made:
  The Designer explicitly excluded the Once-Only Signups segment (12% of
  dormant users) from all re-engagement activity, redirecting budget to
  onboarding improvement instead.

Alternative rejected:
  Including Once-Only Signups in a "light-touch" re-engagement campaign — a
  single generic push notification or email offering a small discount.

Reason:
  The Researcher's data showed 12% push opt-in, 18% payment method saved, 22%
  profile completion, and average spend of EUR 3.90 on a single visit 144 days
  ago. These users were never real customers — they signed up at the till for
  a one-time discount and had no brand relationship. Sending even one push
  notification to 3,800 people who mostly have push disabled (88%) would reach
  only ~456 users. At an industry-average re-engagement conversion rate of 2-3%,
  that is roughly 10-14 redemptions at EUR 3.90 — approximately EUR 40-55 in
  recovered revenue. The operational cost of creating, testing, and sending
  the campaign exceeds that return. More importantly, sending unwanted
  notifications to 3,800 near-strangers risks app deletions and spam complaints
  that would reduce deliverability for all other segments.

Trade-off created:
  The business permanently writes off 12% of its dormant base. If Drift Coffee
  later developed a very low-cost reactivation channel (e.g., a passive in-app
  offer that requires no push or email), this segment could be reconsidered.
  For now, the resources are better spent on the 88% of dormant users who have
  demonstrated genuine prior engagement.


================================================================================
DECISION 5: Email-Only Route for Afternoon Treaters
================================================================================

Choice made:
  The Designer routed all Afternoon Treater communications through email only,
  with an explicit instruction that no push notifications should be sent.

Alternative rejected:
  A mixed-channel approach — push notification first, email as fallback — which
  is the same strategy used for Commuters and Weekend Explorers.

Reason:
  Only 33% of Afternoon Treaters had push notifications enabled — the lowest
  of all recurring segments. Sending push to a segment with 67% opt-out would
  mean two-thirds of messages bounce or are silently blocked, creating
  unreliable delivery metrics. Worse, if the system sends repeated push
  attempts to users who have explicitly disabled push, it risks violating
  platform policies (both iOS and Android penalise apps that send notifications
  to users who opted out). Email is universal — it reaches 100% of the
  segment's registered addresses. While email open rates are lower (~20%
  vs. push's ~40%), the effective reach (100% × 20% = 20%) is still higher
  than push (33% × 40% = 13.2%) for this segment.

Trade-off created:
  Email is slower than push. A push notification can drive a visit within
  minutes; an email might sit unread for hours. For the Afternoon Treaters'
  2pm-4pm visit window, the email must be sent at 1:30pm to allow discovery
  time. If it arrives at 3pm, the window is mostly gone. This timing
  sensitivity is a real risk that push would have mitigated — but the opt-in
  numbers make email the only responsible choice.


================================================================================
DECISION 6: Free Drink for Former Regulars (Not a Discount)
================================================================================

Choice made:
  The Designer offered Former Regulars a completely free drink — "any drink,
  any size" — as the re-engagement incentive. This is the most aggressive
  offer in the entire campaign.

Alternative rejected:
  A 50% discount or a "buy one get one free" offer — still aggressive but
  requiring the customer to spend money on the first visit back.

Reason:
  Former Regulars were the highest-value segment: EUR 5.80/visit, 5+ visits
  per month, sustained for over 6 months — a customer worth approximately EUR
  29/month in revenue. They did not drift away gradually; 71% defected to a
  specific competitor that opened within 400 metres. A discount says "we are
  cheaper than the new place." A free drink says "we value your relationship
  enough to make the first step back completely frictionless." The psychology
  is different: the competitor is novel and exciting; a discount framed as
  "cheaper" might actually reinforce the perception that Drift Coffee is the
  budget option. A free welcome-back drink framed as "we missed you" positions
  Drift Coffee as the brand that cares, while the competitor is the brand that
  is simply new. The cost of one free drink (approximately EUR 1.20 in
  ingredients) against a EUR 29/month revenue opportunity is a 24x ROI at
  breakeven.

Trade-off created:
  A free offer can attract deal-seekers who redeem and leave again. The
  Designer mitigated this by making the free drink a Step 2 offer followed by
  a Step 3 loyalty bonus for 4 subsequent visits — the free drink is the hook,
  not the entire value proposition. The risk remains that some users will
  redeem the free drink and defect again, but the data (85% payment method
  saved, 78% push enabled, long prior relationship) suggests these users are
  not serial deal-seekers. They are former loyal customers who need one reason
  to come back.


================================================================================
DECISION 7: Synthetic Data Embedded in the Researcher Prompt
================================================================================

Choice made:
  The Researcher's system prompt included a complete synthetic dataset
  describing five segments with visit patterns, product preferences, spend
  data, opt-in rates, and store-level statistics. The Researcher analysed this
  data rather than generating or retrieving external data.

Alternative rejected:
  Prompting the Researcher with "generate realistic synthetic data for a
  28-location coffee chain and then analyse it." This would have the
  Researcher creating its own evidence base and then drawing conclusions from
  evidence it invented.

Reason:
  This is a critical methodological choice. If the Researcher generates its
  own data and then analyses it, there is a circular validation problem: the
  agent could produce data that perfectly supports whatever conclusions it
  wants to draw. In a real production system, the Researcher would query a
  live database. For this build session, the closest approximation is
  providing a fixed dataset that the Researcher cannot modify, ensuring
  analytical integrity. The dataset was designed to contain realistic tensions
  (e.g., Weekend Explorers have high push opt-in but low payment save rate —
  a real-world contradiction that forces genuine analytical reasoning rather
  than pattern-matching). This decision is central to the Intelligence lens:
  the data must constrain the strategy, not the other way around.

Trade-off created:
  The Researcher cannot challenge the data. If the synthetic data contained an
  error or unrealistic pattern, the Researcher would analyse it as truth and
  the entire pipeline would produce a flawed output. In a production system,
  a data validation step would precede analysis. For this build, the single
  source of data was a deliberate constraint to simulate a fixed database
  environment.


================================================================================
DECISION 8: 100-Character Push Notification Limit
================================================================================

Choice made:
  The Communicator was constrained to produce push notifications between 40
  and 100 characters, and the actual outputs were 53, 72, and 73 characters.

Alternative rejected:
  No character limit — allowing push notifications of any length, which many
  push platforms technically support (iOS allows ~178 characters on the lock
  screen, Android allows more).

Reason:
  While platforms allow longer push notifications, truncation behaviour varies
  by device, OS version, and font size settings. A push notification that reads
  perfectly on one phone may cut off mid-sentence on another. The 100-character
  cap is a safe harbour: it ensures the message renders in full on virtually
  every device. It also enforces copy discipline — the Communicator must
  deliver a complete message (offer + call-to-action) in roughly the length of
  a single sentence. This constraint was lifted from real-world push
  notification best practices at companies like Duolingo and Headspace, which
  routinely keep notifications under 80 characters to maximise tap-through
  rates. The Designer did not specify this constraint; it was an architectural
  decision at the Communicator level to prevent the most common push
  notification failure mode: truncation.

Trade-off created:
  Conciseness comes at the cost of warmth. A longer notification could include
  a pleasantry, a personal detail, or a stronger emotional appeal. The
  Communicator compensated by moving warmth into the email body, where
  character limits do not apply, and keeping push notifications as efficient
  triggers designed to drive the user to the app where richer content awaits.


================================================================================
DECISION 9: No In-App Messages Across Any Segment
================================================================================

Choice made:
  The Communicator produced zero in-app messages. Every segment was served by
  push notification and email. In-app was marked "N/A" for all five segments.

Alternative rejected:
  A three-channel approach — push + email + in-app — or at minimum in-app
  messages for the highest-engagement segments (Weekend Explorers, Former
  Regulars).

Reason:
  In-app messages only reach users who open the app. The target audience is
  dormant users — by definition, they are not opening the app. Sending an
  in-app message to a dormant user is like leaving a note inside a house
  whose owner has moved out. In-app messaging is a retention tool for active
  users, not a re-activation tool for dormant ones. The Designer correctly
  identified this in the channel strategy and did not specify in-app for any
  segment, and the Communicator respected that constraint. Including in-app
  messages "for completeness" would have been dishonest about their likely
  effectiveness and would have inflated the channel count without adding real
  reach.

Trade-off created:
  If a dormant user spontaneously returns to the app (e.g., to check store
  locations or reload their payment card), there is no in-app welcome-back
  message waiting. This is a minor missed opportunity, but the likelihood of
  a truly dormant user opening the app without being prompted by a push or
  email is negligible enough that it does not justify the design and
  engineering effort of an in-app re-engagement module.


================================================================================
DECISION 10: A/B Test on Commuter Store-Finder vs. Product Offer
================================================================================

Choice made:
  The Designer designed one A/B test — testing whether Commuters respond
  better to a product-offer message ("Your usual latte, EUR 2 off") or a
  store-finder message ("New commute? Find your nearest Drift Coffee"). Sample
  size 1,200 (600 per variant), success metric = redemption rate.

Alternative rejected:
  A/B testing the offer amount instead (EUR 1 vs. EUR 2 vs. EUR 3 discount) or
  testing across all five segments simultaneously.

Reason:
  The Researcher speculated — marked [SPECULATIVE] — that Commuters went
  dormant because of changed commute patterns, not dissatisfaction. This is a
  testable hypothesis with a single A/B test. If the store-finder variant wins,
  the entire Commuter journey strategy changes from "discount their usual
  product" to "help them find their new nearest store" — a fundamentally
  different approach. If the product-offer variant wins, the commute-change
  hypothesis is disproven and the standard discount approach stands. Testing
  offer amounts would have been optimisation, not hypothesis validation. The
  brief demands that the pipeline catch and correct its own assumptions — this
  A/B test is the mechanism for doing exactly that with the Researcher's
  [SPECULATIVE] claim about commute pattern change.

Trade-off created:
  Only one A/B test was designed when there are multiple testable hypotheses
  in the pipeline (e.g., is the free drink for Former Regulars too generous?
  Does email timing matter for Afternoon Treaters?). The Designer prioritised
  the test that would produce the most strategically consequential insight —
  the one that could fundamentally reshape a segment's entire journey. The
  other testable hypotheses remain untested and would need follow-up
  experimentation cycles.


================================================================================
DECISION 11: Measurement Framework — 3 KPIs, Not a Dashboard
================================================================================

Choice made:
  The Designer specified exactly three KPIs for the first 30 days: re-engagement
  offer redemption rate (target 12%), dormant-to-active conversion rate (target
  8%), and push notification opt-in uplift for Commuters (target +5pp).

Alternative rejected:
  A full dashboard of 10-15 metrics covering every segment, every channel
  (open rates, click rates, conversion rates, revenue per segment, cost per
  reactivation, etc.), and weekly reporting.

Reason:
  The brief asked for something "the business could act on" — not "the business
  could drown in." A 28-location coffee chain does not have a data science team
  to monitor a 15-metric dashboard. Three KPIs chosen for the first 30 days
  provide a clear success/failure signal:
    1. Did anyone redeem the offers? (Redemption rate — direct action)
    2. Did redemptions convert into visits? (Dormant-to-active — behaviour
       change)
    3. Did we improve our ability to reach customers? (Push opt-in — channel
       health)
  These three KPIs together answer the question "did the campaign work?" A
  15-metric dashboard would generate 15 answers, some of which would
  contradict each other, requiring analyst interpretation that the business
  does not have. The constraint was driven by the real organisational context
  of the assigned business, not by what would look impressive in a submission.

Trade-off created:
  If the campaign fails on redemption rate but succeeds on push opt-in uplift,
  the three-KPI framework cannot tell us why — it can only tell us that the
  result is mixed. A richer measurement framework would enable failure
  diagnosis. However, the pipeline's output includes a recommendation to run
  the A/B test on Commuters specifically, which provides a built-in diagnostic
  for at least one segment's performance.


================================================================================
DECISION 12: Fallback Generic Variant for Incomplete Data
================================================================================

Choice made:
  The Communicator produced a generic push notification and email as a
  fallback for users whose data is incomplete — no favourite product, no
  primary store, no segment assignment. However, the Designer noted that this
  fallback should have zero recipients in practice if the Researcher's
  segmentation covers all users.

Alternative rejected:
  No fallback at all — if a user cannot be segmented, they receive nothing.
  Or alternatively, forcing every user into a segment even with incomplete
  data.

Reason:
  Production systems encounter edge cases: corrupted profiles, partially
  migrated data, users who signed up but made zero purchases and have no
  behavioural history. A pipeline without a fallback would throw an error or,
  worse, send a message with blank personalisation fields ("Hi [FIRST NAME],
  your favourite [PRODUCT] is waiting at [STORE]"). The fallback exists as a
  graceful degradation mechanism — a generic but functional message that
  maintains brand presence without exposing technical failures to the
  customer. This is a defensive design decision borrowed from production
  engineering practice: "fail gracefully, not silently."

Trade-off created:
  A generic message barely qualifies as "personalisation." For any user who
  receives it, the pipeline has failed to deliver its core value proposition.
  The fallback is an admission that the pipeline is not perfect — but it is
  better than sending a broken message or sending nothing at all, both of
  which would actively harm customer trust.


================================================================================
DECISION 13: HTML Pipeline Output for GitHub Pages
================================================================================

Choice made:
  The final pipeline output was formatted as a single styled HTML page hosted
  on GitHub Pages, with all three agents' outputs displayed sequentially with
  visible handoff markers between them.

Alternative rejected:
  A multi-file format — three separate documents linked together — or a plain
  text concatenation of the three outputs.

Reason:
  A single HTML page satisfies three requirements simultaneously: (1) it
  serves as the live GitHub Pages deployment the brief requests, (2) it
  provides the visible-handoff evidence the rubric demands (handoff bars
  between each agent), and (3) it is accessible from any browser without
  requiring the marker to download or install anything. The handoff markers are
  visually distinct (dashed red bars with arrow symbols), making the pipeline
  flow immediately scannable. A multi-file approach would require the marker to
  cross-reference between documents to verify handoffs, adding friction to
  assessment. The HTML format also allows tables, colour-coding, and
  responsive layout that plain text cannot provide.

Trade-off created:
  HTML is harder to print or annotate than a PDF or Word document. If the
  marker prefers to print submissions for grading, the HTML page may not print
  as cleanly as a document format. This was accepted because the brief
  explicitly asks for a "screen-recording link" or "live deployment" — the
  HTML page serves that purpose directly.


================================================================================
END OF DECISION LOG
================================================================================
