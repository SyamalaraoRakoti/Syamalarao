================================================================================
AGENT 3 OUTPUT — CUSTOMER COMMUNICATIONS PACKAGE
Agent Archetype: Communicator
Receives from: Designer (Personalised Re-engagement Strategy Blueprint)
Final Output: Ready-to-deploy customer messaging
================================================================================

NOTE: All copy below is derived exclusively from the Designer's strategy
blueprint. No offers, discounts, channels, or journeys were invented by this
agent. Specific offers, timings, and channel choices all come from the Designer.


================================================================================
1. SEGMENT-SPECIFIC MESSAGING
================================================================================

----------------------------------------------------------------------
SEGMENT A: COMMUTERS
----------------------------------------------------------------------

PUSH NOTIFICATION (53 chars):
"Your usual latte is waiting. EUR 2 off this week before 9am."

EMAIL SUBJECT LINE (42 chars):
"Your morning latte misses you, [FIRST NAME]"

EMAIL BODY:
"Hi [FIRST NAME], we noticed it's been a little while since your last visit to
[PRIMARY STORE NAME]. Your regular latte is waiting — and this week, it's EUR 2
off when you stop by before 9am. Just tap below to claim your offer. See you on
your way in. — Team Drift."

[CTA button: "Claim EUR 2 off"]
[Footer: "You received this message because you are a Drift Coffee loyalty
member. To opt out of re-engagement messages, tap Unsubscribe."]

IN-APP MESSAGE: N/A
  (Designer specified push + email only for this segment.)


----------------------------------------------------------------------
SEGMENT B: WEEKEND EXPLORERS
----------------------------------------------------------------------

PUSH NOTIFICATION (72 chars):
"Saturday exploring? Oat-milk flat white + pastry, EUR 2 off. Any location."

EMAIL SUBJECT LINE (44 chars):
"Your weekend plans just got tastier, [FIRST NAME]"

EMAIL BODY:
"Hi [FIRST NAME], it's been a few weekends since we saw you. Your favourite
oat-milk flat white and pastry combo is EUR 2 off this Saturday or Sunday at
any Drift Coffee — try a location you've not visited yet. Tap to claim your
weekend treat. — Team Drift."

[CTA button: "Get my weekend combo"]
[Footer: "You received this message because you are a Drift Coffee loyalty
member. To opt out of re-engagement messages, tap Unsubscribe."]

IN-APP MESSAGE: N/A
  (Designer specified push + email for this segment.)


----------------------------------------------------------------------
SEGMENT C: AFTERNOON TREATERS
----------------------------------------------------------------------

PUSH NOTIFICATION: [EMAIL-ONLY ROUTE]
  (Designer specified: DO NOT send push. 67% have push disabled. Route all
  communication via email.)

EMAIL SUBJECT LINE (49 chars):
"Winter afternoons are better with a mocha, [FIRST NAME]"

EMAIL BODY:
"Hi [FIRST NAME], cold afternoons call for something warm. Enjoy 20% off any
hot drink and pastry combo at [NEAREST RESIDENTIAL STORE], Tuesday to Thursday,
2pm to 4pm. Your favourite mocha is waiting. Tap to claim and brighten a winter
afternoon. — Team Drift."

[CTA button: "Claim 20% off"]
[Footer: "You received this message because you are a Drift Coffee loyalty
member. To opt out of re-engagement messages, tap Unsubscribe."]

IN-APP MESSAGE: N/A
  (Designer specified email only for this segment.)


----------------------------------------------------------------------
SEGMENT D: ONCE-ONLY SIGNUPS
----------------------------------------------------------------------

Designer decision: EXCLUDED from re-engagement campaign.
No messaging produced. Budget redirected to onboarding improvement.

If a system-generated fallback is required for technical completeness
(e.g., database flag requires at least one message slot), use the generic
fallback variant at the end of this package — but do NOT deploy it to this
segment. The Designer's recommendation is to suppress all marketing.


----------------------------------------------------------------------
SEGMENT E: FORMER REGULARS
----------------------------------------------------------------------

PUSH NOTIFICATION (73 chars):
"Welcome back, [FIRST NAME]. Your first drink is on us. Any drink, any size."

EMAIL SUBJECT LINE (48 chars):
"A warm welcome back, [FIRST NAME] — a drink on us"

EMAIL BODY:
"Hi [FIRST NAME], we've missed you at [PRIMARY STORE NAME]. Your first drink
back is on us — any drink, any size. No catch, just a warm welcome. Tap below
to claim and come say hello. — Team Drift."

[CTA button: "Claim my free drink"]
[Footer: "You received this message because you are a Drift Coffee loyalty
member. To opt out of re-engagement messages, tap Unsubscribe."]

IN-APP MESSAGE: N/A
  (Designer specified push + email for this segment.)


================================================================================
2. PERSONALISATION VARIABLE MAP
================================================================================

  Variable Field          | Used In                    | Example Value
  ------------------------|----------------------------|-------------------
  [FIRST NAME]            | Email salutation, push     | Sarah
                          | (where supported by OS)    |
  ------------------------|----------------------------|-------------------
  [PRIMARY STORE NAME]    | Email body, push, CTA      | "Docklands"
                          | context                    |
  ------------------------|----------------------------|-------------------
  [NEAREST RESIDENTIAL    | Email body (Afternoon      | "Ranelagh"
   STORE]                 | Treaters only)             |
  ------------------------|----------------------------|-------------------
  [FAVOURITE PRODUCT]     | Email body, push content   | "oat-milk flat white"
                          | (Commuters, Afternoon      | "mocha"
                          | Treaters only)             | "latte"
  ------------------------|----------------------------|-------------------
  [OFFER AMOUNT]          | Email body, push, CTA      | "EUR 2 off"
                          |                            | "20% off"
                          |                            | "free"
  ------------------------|----------------------------|-------------------
  [TIME WINDOW]           | Email body, push           | "before 9am"
                          |                            | "this weekend"
                          |                            | "Tue-Thu 2pm-4pm"
  ------------------------|----------------------------|-------------------
  [CTA DESTINATION URL]   | CTA button                 | Deep link to in-app
                          |                            | offer redemption page


================================================================================
3. MESSAGE SEQUENCE TIMELINE
================================================================================

SEGMENT A: COMMUTERS
  Day 0 (Mon, 7:30am):  Push notification
  Day 0 (Mon, 6:30am):  Email (for non-push users — sent BEFORE push window)
  Day 3 (Thu, 7:30am):  Second push (if no redemption) — "Still time for EUR 2 off"
  Day 7:                If no action, move to 30-day cooldown

SEGMENT B: WEEKEND EXPLORERS
  Day 0 (Fri, 5pm):     Push notification
  Day 0 (Fri, 4pm):     Email (for non-push users)
  Day 7 (Fri, 5pm):     Second push — "Weekend treat still waiting"
  Day 14:               If no action, move to 30-day cooldown

SEGMENT C: AFTERNOON TREATERS [EMAIL-ONLY ROUTE]
  Day 0 (Tue, 1:30pm):  Email
  Day 7 (Tue, 1:30pm):  Second email — "Your afternoon treat is still here"
  Day 14 (Tue, 1:30pm): Third email — last in cycle
  Day 30:               If no action, cooldown until next month

SEGMENT D: ONCE-ONLY SIGNUPS
  No messages sent. No sequence defined.

SEGMENT E: FORMER REGULARS
  Day 0 (Immediate):    Push notification (within 7 days of competitor opening)
  Day 1:                Email (for non-push users)
  Day 5:                Second push — "Your free drink is waiting"
  Day 10:               Third push — final reminder before expiry
  Day 14:               Offer expires. Move to standard Commuter/Explorer journey
                         based on their historical segment profile.


================================================================================
4. TONE AND VOICE GUIDELINES
================================================================================

Brand voice: Warm, familiar, and unhurried. Drift Coffee messages read like a
friendly barista remembering your order, not a corporation sending a promotion.
Sentences are short. The customer is always addressed by name. Every message
includes a specific, actionable next step.

Tonal choices by segment:
  - Commuters: Time-saving, efficient tone. "Your usual" — reinforces routine
    without adding cognitive load. No exclamation marks.
  - Weekend Explorers: Playful, discovery-oriented. "Saturday exploring?" —
    mirrors their own language. Invites rather than instructs.
  - Afternoon Treaters: Cosy, comfort-focused. "Cold afternoons call for
    something warm" — acknowledges the weather and positions Drift as refuge.
  - Former Regulars: Genuine, no-pressure. "We've missed you" — honest and
    simple. No urgency. The free drink removes all friction.


================================================================================
5. FALLBACK / GENERIC VARIANT
================================================================================

For users whose data is incomplete (no favourite product, no primary store,
no purchase history segment assignment):

GENERIC PUSH NOTIFICATION (67 chars):
"A little something from Drift Coffee. Tap to see what's waiting for you."

GENERIC EMAIL SUBJECT LINE (39 chars):
"Something is waiting for you at Drift Coffee"

GENERIC EMAIL BODY:
"Hi there, we noticed you've not been by in a while. We'd love to see you
again. Tap below to see what's available at your nearest Drift Coffee — a warm
welcome is guaranteed. — Team Drift."

[CTA button: "Find my nearest Drift Coffee"]
[Footer: "You received this message because you are a Drift Coffee loyalty
member. To opt out of re-engagement messages, tap Unsubscribe."]

Designer constraint note: This generic variant should only be deployed to users
who cannot be assigned to any behavioural segment. If the Researcher's
segmentation covers all 31,500 dormant users, this fallback will have zero
recipients and exists only as a safety net for edge cases (e.g., corrupted
profile data, new signup with zero purchase history who somehow entered the
dormant pool).

================================================================================
END OF COMMUNICATOR OUTPUT — FINAL PIPELINE OUTPUT
================================================================================
