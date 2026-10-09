# -*- coding: utf-8 -*-
"""The 50 prompts. Single source of truth for the PDF, DOCX, TXT and Canva plan.

Conventions
-----------
* [ALL CAPS IN SQUARE BRACKETS] = a placeholder the buyer replaces.
* Bracketed text containing a colon, e.g. [NEEDS INFO: ...], is a marker the AI
  should output; it is NOT a placeholder.
* {FG} is expanded to the Fact Guard sentence below.
* "fill" lists only prompt-specific placeholders. The six "Core Six" placeholders
  (see CORE_SIX) are explained once in the brief and are not repeated.
"""

FACT_GUARD = (
    "Use only the facts I have given you. If you need a detail that is missing, "
    "write [NEEDS INFO: what is missing] instead of guessing. Do not invent "
    "statistics, awards, testimonials, prices, guarantees or client names."
)

CORE_SIX = [
    ("[BUSINESS NAME]", "The trading name exactly as it should appear on the site."),
    ("[BUSINESS DESCRIPTION]", "One plain sentence: what it sells or does, for whom, and where. "
     "Example: “A family-run physiotherapy clinic for office workers in Eastbrook.”"),
    ("[TARGET AUDIENCE]", "Who the page is for, their situation, and what they want. "
     "Be specific: “First-time home buyers comparing three local solicitors” beats “everyone”."),
    ("[KEY FACTS]", "Verified facts the AI may use: services, prices, opening hours, years in business, "
     "credentials, policies, real numbers. This is the only source of truth, so keep it accurate."),
    ("[TONE OF VOICE]", "Three to five adjectives plus one “not”. Example: “Warm, plain-spoken, practical; "
     "never salesy or jokey.”"),
    ("[MAIN GOAL]", "The one action the page should prompt. Example: “Book a free 15-minute call.”"),
]

CATEGORIES = [
    dict(
        n=1, title="Homepage & Hero Messaging",
        blurb="Your homepage has about five seconds to answer three questions: what is this, is it for me, "
              "and what do I do next. These prompts get you from a vague first screen to a clear one, then "
              "build the rest of the page underneath it.",
        order="Start with Prompt 2 to fix the positioning, then 1 for the hero, then 3 to draft the full page.",
        prompts=[
            dict(
                n=1, title="Hero Headline & Subheadline Lab",
                use="The homepage opens with something vague (“Welcome to our website”) or a client needs options to choose from.",
                fill=[("[PRIMARY OFFER]", "The main thing a visitor can buy or book, in plain words."),
                      ("[CUSTOMER'S BIGGEST PROBLEM]", "The frustration that sends people to you, in their words if you have them.")],
                prompt="""Act as a conversion-focused website copywriter. Write hero-section copy for the homepage of [BUSINESS NAME].

About the business: [BUSINESS DESCRIPTION]
Who it is for: [TARGET AUDIENCE]
Main offer: [PRIMARY OFFER]
The visitor's biggest problem: [CUSTOMER'S BIGGEST PROBLEM]
Facts you may use: [KEY FACTS]
Tone: [TONE OF VOICE]
The page should lead visitors to: [MAIN GOAL]

Give me three distinct angles:
1. Outcome-led (what life looks like afterwards)
2. Problem-led (the frustration they want gone)
3. Specific-detail-led (a concrete fact from my key facts)

For each angle write: a headline (max 10 words), a subheadline (max 25 words), a button label (max 4 words), and one line of reassurance under the button (max 12 words).

Then recommend one angle and explain why in two sentences.

Rules: say what the business does in plain words. Avoid “welcome to”, “one-stop shop”, “best in class”, “solutions” and “passionate”. {FG}""",
                tip="Paste your favourite headline back and ask for five variations that keep the meaning but change the first word."),
            dict(
                n=2, title="Value Proposition Builder",
                use="Before writing any page, when you cannot yet say in one sentence what the business does, for whom, and why it is a good choice.",
                fill=[("[WHAT CUSTOMERS DO INSTEAD]", "The alternatives: other providers, doing it themselves, or doing nothing."),
                      ("[PROVABLE DIFFERENCES]", "What genuinely sets the business apart, each with the evidence behind it.")],
                prompt="""Help me define the value proposition for [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
What customers do instead: [WHAT CUSTOMERS DO INSTEAD]
Provable differences: [PROVABLE DIFFERENCES]
Other facts: [KEY FACTS]

Produce:
1. One value-proposition sentence in this pattern: “We help ___ to ___ by ___, so that ___.”
2. Three supporting proof points. Under each, quote the exact fact from my notes that supports it.
3. A “what we are not” line that sets honest expectations (for example, not the cheapest, not the fastest).
4. A short positioning paragraph (60 words max) that contrasts us with the alternatives without naming or criticising competitors.
5. A list of claims people in this industry often make that I could not prove from the facts above, so I can avoid them.

Tone: [TONE OF VOICE]. {FG}""",
                tip="Ask a follow-up: “Now shorten the sentence to 15 words without losing the audience or the result.”"),
            dict(
                n=3, title="Full Homepage Draft, Section by Section",
                use="You have the positioning and facts and need a complete first draft of the homepage for a designer or CMS.",
                fill=[("[SECTIONS TO INCLUDE]", "For example: hero, problem, services, how it works, proof, FAQ, final call to action."),
                      ("[TARGET WORD COUNT]", "Total length, for example 450–600 words.")],
                prompt="""Write a complete homepage draft for [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Facts to use: [KEY FACTS]
Tone: [TONE OF VOICE]
Goal of the page: [MAIN GOAL]
Sections to include, in this order: [SECTIONS TO INCLUDE]
Total length: about [TARGET WORD COUNT] words.

For every section give me:
- Purpose: one line on what this section must achieve for the visitor
- Heading
- Body copy
- Button text, if the section needs one
- Designer note: a one-line suggestion for the image or layout

Where a section needs proof such as a testimonial, case study or number that is not in my facts, leave a clearly marked gap: [NEEDS INFO: what is needed]. Keep paragraphs to three lines or fewer and use the visitor's language, not industry jargon. {FG}""",
                tip="Run the sections you like through Prompt 37 later to line the voice up across the whole page."),
            dict(
                n=4, title="Benefits Section That Avoids Clichés",
                use="A “Why choose us” section lists features (“10 years’ experience”) but never says what that means for the customer.",
                fill=[("[FEATURES TO TURN INTO BENEFITS]", "A list of real features, policies or facts, one per line."),
                      ("[NUMBER OF BENEFITS]", "How many blocks the design has, usually 3, 4 or 6.")],
                prompt="""Turn these features into customer benefits for the website of [BUSINESS NAME].

Audience: [TARGET AUDIENCE]
Features and facts: [FEATURES TO TURN INTO BENEFITS]
Other context: [KEY FACTS]
Tone: [TONE OF VOICE]

Create [NUMBER OF BENEFITS] benefit blocks. Each block has:
- A heading of six words or fewer that states the benefit, not the feature
- One or two sentences explaining what changes for the customer
- A “proof line” naming the exact fact the benefit rests on

If a feature does not support a clear benefit, or a benefit cannot be backed by my facts, do not force it. List it separately under “Needs a better story” and say what information would help.

Avoid vague words such as quality, excellence, seamless, tailored and bespoke unless you immediately make them concrete. {FG}""",
                tip="Read each heading aloud and ask “so what?”. If the answer is not in the sentence below it, rewrite."),
            dict(
                n=5, title="Five-Second Clarity Rewrite",
                use="An existing homepage feels muddled and you want an outsider's reading before you rewrite anything.",
                fill=[("[CURRENT HOMEPAGE TEXT]", "Paste the first screen of text, or the whole page. Keep the original order.")],
                prompt="""Act as a first-time visitor who matches this profile: [TARGET AUDIENCE]. You have never heard of [BUSINESS NAME] and you will give this page five seconds.

Here is the current homepage text:
[CURRENT HOMEPAGE TEXT]

Step 1 – Report honestly:
- What do you think the business does?
- Who do you think it is for?
- What do you think you are supposed to do next?
- Which phrases are vague, repetitive or jargon-heavy? Quote them.

Step 2 – Compare your answers with the truth: [BUSINESS DESCRIPTION]. Where do they differ?

Step 3 – Rewrite only the first screen: a headline, a subheadline and a button label. Keep what already works. After each change, explain it in one line.

Tone: [TONE OF VOICE]. The page should lead to: [MAIN GOAL]. {FG}""",
                tip="Test the same text on a real person who has never seen the business. The AI is a helpful stand-in, not a replacement."),
        ]),
    dict(
        n=2, title="About, Story & Credibility",
        blurb="People read the About page to decide whether to trust you. These prompts turn rough notes about the "
              "business and the people behind it into pages that are specific, human and honest, without inventing "
              "a single detail.",
        order="Gather your real notes first. Then use Prompt 6 for the page and 7 for each person.",
        prompts=[
            dict(
                n=6, title="Story-Led About Page",
                use="The About page is a list of dates and adjectives, or it does not exist yet.",
                fill=[("[ORIGIN STORY NOTES]", "Rough bullet points on why and how the business started, in your own words."),
                      ("[POINT OF VIEW]", "“we”, “I” or third person.")],
                prompt="""Write an About page for [BUSINESS NAME] from the raw notes below.

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Origin and story notes: [ORIGIN STORY NOTES]
Other facts: [KEY FACTS]
Point of view: [POINT OF VIEW]
Tone: [TONE OF VOICE]
The page should lead to: [MAIN GOAL]

Structure (350–450 words):
1. An opening line that connects to what the visitor needs, not “Founded in…”
2. The story: why this business exists, told only from my notes
3. How we work and what we believe, shown as behaviour rather than slogans
4. Who we serve
5. A short proof paragraph using only my facts
6. A closing invitation to take the next step

Do not add dramatic details, dates, quotes or feelings that are not in my notes. If the story has a gap, ask me up to three questions at the end. {FG}""",
                tip="Voice-record yourself telling the story and paste the transcript as the notes. It captures phrasing you would never type."),
            dict(
                n=7, title="Founder & Team Bio Set",
                use="You need bios of different lengths for the About page, team cards, proposals and directory listings.",
                fill=[("[PERSON NAME & ROLE]", "For example: Asha Menon, lead designer."),
                      ("[BIO NOTES]", "Background, experience, qualifications and one or two personal details you are happy to publish.")],
                prompt="""Write three versions of a professional bio for [PERSON NAME & ROLE] at [BUSINESS NAME].

Source notes: [BIO NOTES]
Audience reading it: [TARGET AUDIENCE]
Tone: [TONE OF VOICE]

Versions, all in the third person:
1. 40 words, for team cards
2. 100 words, for the About page
3. 200 words, for proposals and press

Each bio should lead with what this person does for clients, then support it with experience, then end with one human detail. Include a personal detail only if it appears in my notes. Do not exaggerate seniority or credentials, and do not use “passionate”, “guru”, “ninja” or “expert” unless I have supplied a qualification that justifies it. {FG}""",
                tip="Have each person read their own bio and strike anything that does not sound like them."),
            dict(
                n=8, title="Values & Mission, Minus the Clichés",
                use="The site says “integrity, passion, excellence” like every other site and you want values that customers can actually feel.",
                fill=[("[HOW YOU ACTUALLY WORK]", "Real habits: how fast you reply, how you quote, what you refuse to do.")],
                prompt="""Write a short mission statement and a values section for [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
How we actually work (real behaviours): [HOW YOU ACTUALLY WORK]
Other facts: [KEY FACTS]
Tone: [TONE OF VOICE]

Deliver:
1. A one-sentence mission that names who we serve and what we do for them.
2. Three or four values. For each: a short name, one sentence on what we do because of it, and one sentence on what the customer can expect.

Every value must be traceable to a behaviour in my notes. Do not use the words integrity, passion, excellence, innovation or customer-centric unless you immediately back them with a specific action. If my notes do not support a fourth value, stop at three. {FG}""",
                tip="Test each value: could a competitor claim the same sentence? If yes, make it more specific."),
            dict(
                n=9, title="Credentials & Trust-Signal Block",
                use="Qualifications, memberships and experience are buried or missing and visitors cannot tell why to trust you.",
                fill=[("[CREDENTIALS & EXPERIENCE]", "Qualifications, licences, memberships, years in business, notable work, each with the evidence you hold.")],
                prompt="""Create a “Why you can trust us” section for the website of [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Audience and their worries: [TARGET AUDIENCE]
Credentials and evidence: [CREDENTIALS & EXPERIENCE]
Tone: [TONE OF VOICE]

Deliver:
1. A section heading and a one-sentence intro
2. Three to five trust items, each with a short heading and one plain-language line on why it matters to the visitor
3. A one-line “trust strip” for the footer or header (for example: licence · membership · years in business)
4. A checklist titled “Verify before publishing” listing every licence number, date, name or membership I should confirm
5. A list titled “Do not claim” with trust claims that I have not given evidence for

Present credentials exactly as written in my notes; do not upgrade wording such as “trained in” to “certified in”. {FG}""",
                tip="Link each credential to its issuing body's public page where one exists. It lets visitors verify what you say."),
            dict(
                n=10, title="“How We Work” Process Section",
                use="Clients are nervous about what happens after they say yes and the site does not explain it.",
                fill=[("[STEPS IN YOUR PROCESS]", "The real sequence, even if rough: what happens first, next, last."),
                      ("[TYPICAL TIMELINE]", "How long each step or the whole process usually takes, only if you know.")],
                prompt="""Write a “How it works” section for [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Our real process: [STEPS IN YOUR PROCESS]
Typical timeline: [TYPICAL TIMELINE]
Other facts: [KEY FACTS]
Tone: [TONE OF VOICE]

Deliver:
1. A heading and a one-sentence intro that lowers the visitor's anxiety
2. Three to five steps. For each: a verb-led step name, what happens, what the customer needs to do, and how long it takes if my notes say
3. A closing line that leads to: [MAIN GOAL]

Do not add steps I did not describe, and do not promise timings I did not give. If a step is unclear, list your questions at the end. {FG}""",
                tip="Ask for a mobile-friendly version: step names only, one line each."),
        ]),
    dict(
        n=3, title="Services & Product Pages",
        blurb="Service and product pages are where decisions are made. These prompts give each offer a page that says "
              "what is included, who it suits, how it works and what it costs, so the visitor does not have to ask.",
        order="Use Prompt 11 for each main service, 12 for the overview cards, and 14 where you publish prices.",
        prompts=[
            dict(
                n=11, title="Service Page Draft",
                use="You need a full page for one service, covering what it is, who it suits and how to start.",
                fill=[("[SERVICE NAME]", "The service exactly as customers would search for or call it."),
                      ("[SERVICE DETAILS]", "What is included, how it works, limits, price or price ranges, timelines."),
                      ("[IDEAL CLIENT FOR THIS SERVICE]", "Who benefits most, and who does not.")],
                prompt="""Write a service page for “[SERVICE NAME]” at [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Ideal client: [IDEAL CLIENT FOR THIS SERVICE]
Service details: [SERVICE DETAILS]
Other facts: [KEY FACTS]
Tone: [TONE OF VOICE]
The page should lead to: [MAIN GOAL]

Use this structure:
1. H1 that includes the service name in natural language
2. Intro of two or three sentences: the problem, then what we do about it
3. “Who this is for” (and one line on who it is not for)
4. “What is included” as a bullet list
5. “How it works” in three or four steps
6. “What it costs”: use only the pricing information I gave you, or write [NEEDS INFO: pricing]
7. Three FAQs a hesitant customer would ask
8. A closing call to action

Keep sentences short and specific. {FG}""",
                tip="Use the same structure for every service page so visitors learn where to look."),
            dict(
                n=12, title="Service Cards: Short Descriptions",
                use="The homepage or services overview needs consistent, scannable summaries of every service.",
                fill=[("[LIST OF SERVICES WITH ONE-LINE NOTES]", "One service per line, with a note on what it is and who wants it."),
                      ("[CHARACTER LIMIT]", "The limit each card can hold, for example 120.")],
                prompt="""Write short service-card descriptions for the website of [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Services and notes:
[LIST OF SERVICES WITH ONE-LINE NOTES]
Other facts: [KEY FACTS]
Tone: [TONE OF VOICE]

For each service give me:
- A card title (max 4 words)
- A description of no more than [CHARACTER LIMIT] characters, including spaces, that starts with the customer's need or result
- A link label (max 3 words) that is more specific than “Learn more”

Keep the cards parallel: same length, same grammar pattern, same level of detail. Do not repeat the same opening word across cards. Finish with a table showing each description's character count so I can check it. {FG}""",
                tip="AI counts characters unreliably. Paste the final text into a character counter before it goes into the design."),
            dict(
                n=13, title="Product Description: Benefit, Feature, Spec",
                use="A product page lists specifications but does not help anyone decide.",
                fill=[("[PRODUCT NAME]", "The product's name and any model or variant."),
                      ("[PRODUCT DETAILS]", "Materials, sizes, ingredients or specs, care, delivery, returns: everything you know to be true.")],
                prompt="""Write product-page copy for [PRODUCT NAME], sold by [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Buyer: [TARGET AUDIENCE]
Product details: [PRODUCT DETAILS]
Other facts: [KEY FACTS]
Tone: [TONE OF VOICE]

Deliver:
1. A product title that includes the key attribute shoppers look for
2. A one-line hook (max 15 words)
3. A description of 40–60 words that starts with what the product does for the buyer
4. Four to six bullets, each pairing a feature with its benefit (“Feature → what it means for you”)
5. A specifications list, formatted exactly from my details
6. “Best for” and “May not suit” lines that set honest expectations
7. Delivery and returns text, only if I supplied the terms

Do not invent materials, sizes, certifications, origin claims or reviews. {FG}""",
                tip="The “May not suit” line reduces returns and builds trust. Keep it even if a client resists."),
            dict(
                n=14, title="Packages & Pricing Page Copy",
                use="You publish packages or prices and need copy that makes the differences obvious without hiding the cost.",
                fill=[("[PACKAGES]", "Each package: name, price, what it includes, what it does not."),
                      ("[PRICING NOTES]", "Taxes, payment terms, deposits, contract length, anything that affects the final cost.")],
                prompt="""Write the copy for the pricing page of [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Packages (exact names, prices and inclusions): [PACKAGES]
Pricing notes: [PRICING NOTES]
Other facts: [KEY FACTS]
Tone: [TONE OF VOICE]
The page should lead to: [MAIN GOAL]

Deliver:
1. Page heading and a two-sentence intro that explains how pricing works
2. For each package: its name, a one-line “best for”, the inclusions as a bullet list, the price exactly as given, and a button label
3. A comparison table of packages, rows for features and columns for packages
4. A short “Not sure which to choose?” paragraph that leads to: [MAIN GOAL]
5. Four pricing FAQs (payment, changes, what is not included, how to start)

Use my prices and terms exactly. Do not invent discounts, “most popular” labels, urgency or limited-time offers. {FG}""",
                tip="Only mark a package “Most popular” if your sales records support it."),
            dict(
                n=15, title="“Which Option Is Right for Me?” Guide",
                use="Visitors hesitate between two or more options and leave without choosing.",
                fill=[("[OPTIONS TO COMPARE]", "The options, with the real differences between them."),
                      ("[DECISION FACTORS]", "What usually decides it: budget, timing, size, experience, goals.")],
                prompt="""Write a short decision guide titled “Which option is right for you?” for [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Options: [OPTIONS TO COMPARE]
Decision factors: [DECISION FACTORS]
Other facts: [KEY FACTS]
Tone: [TONE OF VOICE]

Deliver:
1. A two-sentence intro that makes choosing feel easy
2. A set of “Choose A if… / Choose B if…” statements, one pair per decision factor
3. A three-question quick quiz with a recommended option for each combination of answers
4. A final paragraph offering a no-pressure way to get help: [MAIN GOAL]

Be fair to every option, including the cheaper or smaller one. If two options overlap too much for a fair comparison, tell me so at the end. {FG}""",
                tip="The quiz can be built as a simple form or a set of buttons; you do not need software for it."),
        ]),
    dict(
        n=4, title="Calls to Action & Conversion",
        blurb="A page that informs but never asks leaves visitors stranded. These prompts write the asks: buttons, "
              "offers, forms and the answers to the doubts that stop people from clicking.",
        order="Write the button copy (16) after the page is drafted, and handle objections (20) before the final call to action.",
        prompts=[
            dict(
                n=16, title="Button & Microcopy Variants",
                use="The buttons say “Submit” or “Learn more”, or you want options to test.",
                fill=[("[ACTION]", "What happens when someone clicks: book, request a quote, download, buy."),
                      ("[BUTTON LOCATION]", "Header, hero, pricing table, footer, or form."),
                      ("[WHAT HAPPENS NEXT]", "The very next step after the click, in one sentence.")],
                prompt="""Write call-to-action button copy for [BUSINESS NAME].

Audience: [TARGET AUDIENCE]
Action the button triggers: [ACTION]
Button location: [BUTTON LOCATION]
What happens next: [WHAT HAPPENS NEXT]
Facts: [KEY FACTS]
Tone: [TONE OF VOICE]

Give me 12 button labels (max 4 words each) in four styles, three per style:
- Direct (names the action)
- Benefit-led (names the result)
- Low-commitment (lowers the perceived risk)
- Specific (mentions the time, the format or the item)

Under each label add reassurance microcopy of 12 words or fewer, but only reassurance that is true according to my facts (for example, no card needed, only if the facts say so).

Finish by recommending the two labels I should test first and why. Avoid “Submit”, “Click here” and “Learn more”. {FG}""",
                tip="Match the button to the page: a pricing-page button can be more committal than a homepage one."),
            dict(
                n=17, title="Single-Offer Landing Page",
                use="You are promoting one offer (a consultation, a workshop, a seasonal service) and need a focused page.",
                fill=[("[OFFER]", "The single offer, named plainly."),
                      ("[OFFER DETAILS]", "What the customer gets, price, format, dates, conditions."),
                      ("[DEADLINE OR LIMIT]", "A real deadline or capacity limit. Write “none” if there isn't one.")],
                prompt="""Write a landing page for one offer from [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Offer: [OFFER]
Offer details: [OFFER DETAILS]
Real deadline or limit: [DEADLINE OR LIMIT]
Other facts: [KEY FACTS]
Tone: [TONE OF VOICE]
Single goal: [MAIN GOAL]

Structure:
1. Hero: headline, subheadline, button
2. The problem in the visitor's words
3. The offer and exactly what they get
4. Who it is for and who it is not for
5. Proof: use real facts, or leave [NEEDS INFO: testimonial or result]
6. Four FAQs
7. A final call to action that repeats the offer

Remove navigation distractions: there should be one action only. If the deadline says “none”, do not create urgency of any kind. {FG}""",
                tip="Landing pages work best when the headline echoes the advert or link that brought people there."),
            dict(
                n=18, title="Contact Page & Form Copy",
                use="The contact page is only a form and a phone number, and enquiries come in vague or incomplete.",
                fill=[("[CONTACT DETAILS]", "Phone, email, address, hours, map link: exactly as they should appear."),
                      ("[WHAT YOU NEED TO KNOW FROM ENQUIRER]", "The details that let you reply usefully the first time."),
                      ("[RESPONSE TIME]", "How quickly you really reply.")],
                prompt="""Write the contact page and form copy for [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Contact details: [CONTACT DETAILS]
Information I need from enquirers: [WHAT YOU NEED TO KNOW FROM ENQUIRER]
Real response time: [RESPONSE TIME]
Tone: [TONE OF VOICE]

Deliver:
1. Page heading and a short intro that tells people what to expect
2. Form fields: a label, helper text and required/optional status for each
3. Button label
4. The confirmation message shown after sending, including what happens next and when
5. A line for people who prefer to phone or message instead
6. A one-sentence note on how their details will be used. Keep it generic and flag it for review by whoever handles my privacy policy; do not make legal claims.

Keep the form as short as possible and justify any field that is not essential. {FG}""",
                tip="Every extra field lowers the number of enquiries. Keep only the ones you use in the first reply."),
            dict(
                n=19, title="Lead Magnet & Newsletter Signup",
                use="You want email addresses and need a sign-up box, thank-you page and first email that deliver on the promise.",
                fill=[("[LEAD MAGNET OR NEWSLETTER]", "What people get: a checklist, a guide, a monthly update."),
                      ("[WHAT SUBSCRIBERS RECEIVE & HOW OFTEN]", "The real content and frequency.")],
                prompt="""Write signup copy for [BUSINESS NAME].

Audience: [TARGET AUDIENCE]
What we are offering: [LEAD MAGNET OR NEWSLETTER]
What subscribers receive and how often: [WHAT SUBSCRIBERS RECEIVE & HOW OFTEN]
Tone: [TONE OF VOICE]
Facts: [KEY FACTS]

Deliver:
1. The signup box: headline (max 8 words), one supporting line, button label, and consent microcopy
2. The thank-you page: confirm the action, say what happens next, and give one useful link
3. The first welcome email: subject line options (three), then body text of about 120 words that delivers the promised item or sets expectations

Promise only what the offer actually delivers. Do not use “exclusive”, “secret” or “ultimate”. Mark anything you need from me as [NEEDS INFO: what is needed]. {FG}""",
                tip="Ask permission-based, honest questions in the welcome email. Reply rates tell you what your audience cares about."),
            dict(
                n=20, title="Objection Handler Section",
                use="Visitors almost buy, but price, trust, timing or switching effort holds them back.",
                fill=[("[TOP OBJECTIONS]", "The real doubts you hear in calls, emails and reviews, one per line.")],
                prompt="""Write an objection-handling section for the website of [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Top objections: [TOP OBJECTIONS]
Facts that help answer them: [KEY FACTS]
Tone: [TONE OF VOICE]
After the section, the visitor should: [MAIN GOAL]

For each objection write a block with:
- A heading phrased the way a worried visitor would say it (for example, “What if it costs more than I expected?”)
- A two- or three-sentence answer that first acknowledges the concern, then gives evidence from my facts, then explains how we reduce the risk

Then add a short closing paragraph and a button. If an objection cannot be answered honestly with my facts, list it under “Open question” with the information I would need, rather than writing a reassuring but unsupported answer. {FG}""",
                tip="Place this section just above the final call to action, where doubts are loudest."),
        ]),
    dict(
        n=5, title="Social Proof & Trust",
        blurb="Real proof does more than any adjective. These prompts help you ask for testimonials, tidy them "
              "honestly, turn projects into case studies, answer common questions and state policies clearly. "
              "Every prompt is built to keep the proof genuine.",
        order="Collect proof first (21), tidy it (22), then build the case study (23) and FAQ (24).",
        prompts=[
            dict(
                n=21, title="Testimonial Request Message",
                use="Happy clients exist, but nobody has asked them for a few words.",
                fill=[("[CLIENT FIRST NAME]", "How you address them."),
                      ("[PROJECT OR PURCHASE]", "What you did for them or what they bought."),
                      ("[YOUR NAME]", "Who the message is from.")],
                prompt="""Write two short messages asking a happy client for a testimonial for [BUSINESS NAME].

Client: [CLIENT FIRST NAME]
What we did for them: [PROJECT OR PURCHASE]
From: [YOUR NAME]
Tone: [TONE OF VOICE]

Versions:
1. An email (max 120 words) with a subject line
2. A WhatsApp or SMS message (max 50 words)

Each message must:
- Thank them for something specific from the project
- Make it easy by asking three short questions (for example: what was the situation before, what was it like working with us, what has changed since)
- Say they can answer in a few lines or by voice note
- Ask clearly whether we may publish their first name, business name or photo, and explain that we will send them the final wording to approve

Never suggest what they should say, offer payment for a review, or draft the testimonial for them. {FG}""",
                tip="Send within a week of delivery, while the result is fresh."),
            dict(
                n=22, title="Testimonial Tidy-Up (Real Reviews Only)",
                use="You have a real testimonial full of typos or run-on sentences and want it publishable without changing what the client meant.",
                fill=[("[RAW TESTIMONIAL TEXT]", "The client's own words, pasted exactly."),
                      ("[CLIENT NAME & DETAILS AS APPROVED]", "Name, role or business, location, only as the client agreed.")],
                prompt="""I have a genuine testimonial from a client of [BUSINESS NAME]. Help me prepare it for the website without changing its meaning.

Client's words, pasted exactly:
[RAW TESTIMONIAL TEXT]

Attribution approved by the client: [CLIENT NAME & DETAILS AS APPROVED]

Deliver:
1. A lightly edited version: fix spelling and punctuation, trim repetition, keep the client's voice and every claim exactly as stated
2. A pull-quote of 20 words or fewer taken word for word from the text
3. A suggested heading drawn from the client's own words
4. A change log showing what you altered
5. A list of any claims in the testimonial I should verify before publishing (numbers, results, superlatives)

Never add words that strengthen or change the claim, never combine different testimonials, and never create a testimonial where none was given. The client must approve the final wording. {FG}""",
                tip="Send the edited version back to the client for a quick yes. Keep their reply on file."),
            dict(
                n=23, title="Case Study From Project Notes",
                use="You completed good work but have only notes, emails and a few numbers.",
                fill=[("[PROJECT NOTES]", "Situation, what you did, what happened, in rough form."),
                      ("[RESULTS YOU CAN VERIFY]", "Real numbers or outcomes, each with the source or date. Write “none yet” if there are none."),
                      ("[CASE STUDY LENGTH]", "For example 300 or 500 words.")],
                prompt="""Write a case study for [BUSINESS NAME] from the notes below.

Business: [BUSINESS DESCRIPTION]
Reader: [TARGET AUDIENCE]
Project notes: [PROJECT NOTES]
Results I can verify: [RESULTS YOU CAN VERIFY]
Tone: [TONE OF VOICE]
Length: about [CASE STUDY LENGTH] words
Goal: [MAIN GOAL]

Structure:
1. Title that names the client type and the outcome (only if the outcome is verified)
2. Snapshot box: client type, service, timeframe, what changed
3. The challenge
4. What we did, in plain steps
5. The result, using only the verified results above
6. A quote slot: [NEEDS INFO: client quote with permission]
7. A closing line that leads to the next step

Do not invent client names, figures, timelines or quotes. If the results are weak or missing, say so and suggest what I could measure next time. {FG}""",
                tip="Get written permission before naming a client or publishing their numbers."),
            dict(
                n=24, title="FAQ Builder",
                use="The same questions arrive by email and phone, and the site does not answer them.",
                fill=[("[PAGE OR TOPIC]", "Where the FAQ will sit, for example the pricing page."),
                      ("[QUESTIONS CUSTOMERS ASK]", "Real questions from enquiries, in the customers' words."),
                      ("[ANSWER FACTS]", "The correct answers or the policy details behind them.")],
                prompt="""Write an FAQ section for [PAGE OR TOPIC] on the website of [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Real customer questions: [QUESTIONS CUSTOMERS ASK]
Facts for the answers: [ANSWER FACTS]
Other facts: [KEY FACTS]
Tone: [TONE OF VOICE]

Deliver:
1. Eight to ten questions grouped under two or three headings
2. Answers of 30–70 words each. The first sentence must answer the question directly; the rest adds the detail that matters
3. A mark next to the three questions that should sit closest to the call to action
4. A list of any questions I supplied that my facts cannot answer yet, with what information would settle them

Rewrite questions into the way a visitor would phrase them, not the way a business would. {FG}""",
                tip="Review the FAQ every quarter and add the questions you answered by email since."),
            dict(
                n=25, title="Guarantee, Policy & Risk-Reversal Wording",
                use="Refund, revision, cancellation or warranty terms exist but are hidden in small print.",
                fill=[("[REAL POLICY TERMS]", "The actual terms, copied from your contract or policy, including conditions and exceptions.")],
                prompt="""Turn the policy below into clear, customer-friendly wording for the website of [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Actual policy terms: [REAL POLICY TERMS]
Tone: [TONE OF VOICE]

Deliver:
1. A plain-language summary of 60 words or fewer for the pricing or product page
2. A longer version with conditions and exceptions stated clearly, in short paragraphs or bullets
3. Three heading options for the section
4. A “Words to avoid” list: any promise word (such as “guaranteed”, “no risk” or “full refund”) that my terms do not fully support

Do not soften, extend or add conditions. If the terms are ambiguous or incomplete, list the questions I need to settle first. This is a copy draft, not legal advice; the final wording should be reviewed by a qualified professional. {FG}""",
                tip="Clear, honest terms build more trust than a bigger promise you cannot always keep."),
        ]),
    dict(
        n=6, title="SEO & Local Visibility",
        blurb="Search copy works when it matches what people actually type and reads naturally. These prompts "
              "help you plan pages, write titles and descriptions, create genuinely local pages and shape headings. "
              "AI cannot see search volumes, so the prompts ask you to bring the data.",
        order="Plan pages with 26, outline each with 30, then write titles and descriptions with 27.",
        prompts=[
            dict(
                n=26, title="Keyword-to-Page Plan",
                use="You have a list of search phrases and need to decide which page should target which.",
                fill=[("[SEARCH PHRASES]", "Phrases from your keyword tool, Search Console, customer emails or client input, one per line."),
                      ("[EXISTING PAGES]", "The pages and URLs that exist now."),
                      ("[SERVICE AREA]", "Towns or regions you serve, or “online”.")],
                prompt="""Create a keyword-to-page plan for [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Service area: [SERVICE AREA]
Search phrases I have collected: [SEARCH PHRASES]
Existing pages: [EXISTING PAGES]
Other facts: [KEY FACTS]

Deliver a table with these columns: page (existing or proposed), primary phrase, two or three related phrases, search intent (learn, compare or buy), recommended page type, and action (keep, improve or create).

Rules:
- One primary phrase per page; do not assign the same primary phrase to two pages
- Group phrases with the same intent on one page
- Flag any phrases that suggest a blog post rather than a service page
- You cannot know search volume, competition or rankings. Do not state or estimate any. Add a note telling me to check the plan in a keyword tool before building

Finish with a prioritised list of the first five pages to write. {FG}""",
                tip="If you have no keyword tool, Google's autocomplete and “People also ask” are a free place to start."),
            dict(
                n=27, title="Title Tags & Meta Descriptions",
                use="Pages share the same title, or search results show cut-off, unhelpful snippets.",
                fill=[("[PAGES AND PRIMARY PHRASES]", "Each page's name or URL with its main search phrase, one per line.")],
                prompt="""Write title tags and meta descriptions for the pages of [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Pages and primary phrases: [PAGES AND PRIMARY PHRASES]
Facts: [KEY FACTS]
Tone: [TONE OF VOICE]

For each page provide:
- Two title-tag options of about 50–60 characters, with the primary phrase near the front and the business name at the end where it fits
- One meta description of about 140–155 characters that reads like a short promise to a human, includes a reason to click, and ends with a light call to action

Rules: every title and description must be unique across the site; do not stuff keywords; do not promise anything the page does not deliver. Show a character count beside each line, and add a note that counts are approximate so I should verify them in a counter before publishing. {FG}""",
                tip="Search engines sometimes rewrite snippets. Good descriptions still improve the odds that yours is used."),
            dict(
                n=28, title="Local Service-Area Landing Page",
                use="You serve more than one town or neighbourhood and want pages that are useful, not copies with the town name swapped.",
                fill=[("[SERVICE]", "The service the page is about."),
                      ("[TOWN OR AREA]", "The place the page targets."),
                      ("[LOCAL FACTS]", "Real local detail: neighbourhoods served, local customers, travel times, local regulations, landmarks. Only what you can verify.")],
                prompt="""Write a local landing page for [BUSINESS NAME] about [SERVICE] in [TOWN OR AREA].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Genuine local facts: [LOCAL FACTS]
Other facts: [KEY FACTS]
Tone: [TONE OF VOICE]
Goal: [MAIN GOAL]

Structure:
1. H1 including the service and the place, written naturally
2. An intro that shows we understand local needs, using only the local facts I gave
3. How the service works for customers in this area, including coverage and any travel or timing details I supplied
4. Local proof: work or customers in the area, only if provided; otherwise [NEEDS INFO: local proof]
5. Three FAQs specific to this area
6. A call to action with a name, address and phone block for me to complete

The page must be genuinely different from pages for other towns. If my local facts are too thin to make that true, tell me, and suggest what I should gather instead of padding. {FG}""",
                tip="If you cannot say anything real about an area, a single service-area page listing all towns is better than many thin ones."),
            dict(
                n=29, title="Google Business Profile Text",
                use="The profile description is empty, repeated from the site, or stuffed with keywords.",
                fill=[("[CATEGORIES & SERVICES]", "The profile category and the services you list there."),
                      ("[OPENING HOURS & AREA]", "Hours and the area you serve.")],
                prompt="""Write text for the Google Business Profile of [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Categories and services: [CATEGORIES & SERVICES]
Opening hours and area: [OPENING HOURS & AREA]
Facts: [KEY FACTS]
Tone: [TONE OF VOICE]

Deliver:
1. A business description of 750 characters or fewer that states what we do, for whom, where, and what makes us worth contacting. No keyword stuffing, no all-caps, no promotional offers, and no links or phone numbers in the description (I will check Google's current guidelines before publishing)
2. A short description for each service, max 300 characters each
3. Four ideas for posts, each with a one-line draft and a suggested photo
4. Three reply templates for reviews: positive, mixed and negative. Each must be polite, specific and free of defensiveness or personal data

Use only my facts. {FG}""",
                tip="Guidelines and limits change. Check Google's current profile rules before pasting."),
            dict(
                n=30, title="Heading Outline & Internal Links",
                use="A page is a wall of text, or headings are chosen for the design rather than the reader.",
                fill=[("[PAGE TOPIC]", "What the page is about and the main search phrase."),
                      ("[OTHER PAGES ON THE SITE]", "Titles and URLs of related pages, for link suggestions.")],
                prompt="""Create a heading outline and internal-linking plan for a page on the website of [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Page topic: [PAGE TOPIC]
Other pages on the site: [OTHER PAGES ON THE SITE]
Facts: [KEY FACTS]
Goal: [MAIN GOAL]

Deliver:
1. One H1, followed by H2 and H3 headings in a logical hierarchy. Headings should work as an outline on their own: someone skimming only the headings should understand the page
2. A one-line note under each H2 on what the section must cover
3. A table of internal links: section, page to link to, suggested natural anchor text (not “click here”)
4. Where the call to action belongs

Use one H1 only, and keep keyword use natural. {FG}""",
                tip="Read only the headings aloud. If the story still makes sense, the structure is working."),
        ]),
    dict(
        n=7, title="Blog & Content Marketing",
        blurb="A blog earns its place when it answers real questions better than anyone else nearby. These prompts "
              "find the questions, shape the posts, draft them safely, refresh the old ones and stretch each post "
              "further, while keeping your own expertise at the centre.",
        order="Mine topics with 31, outline with 32, draft with 33, then repurpose with 35.",
        prompts=[
            dict(
                n=31, title="Blog Topics From Customer Questions",
                use="You need a content plan grounded in what real customers ask, not generic lists.",
                fill=[("[CUSTOMER QUESTIONS & ENQUIRIES]", "Real questions from emails, calls, messages and reviews, pasted raw."),
                      ("[SERVICES TO SUPPORT]", "The services or products the blog should lead towards.")],
                prompt="""Generate blog topics for [BUSINESS NAME] from real customer questions.

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Real questions and enquiries: [CUSTOMER QUESTIONS & ENQUIRIES]
Services the blog should support: [SERVICES TO SUPPORT]

Deliver 15 topics grouped by the reader's stage: learning, comparing, and ready to act. For each topic give:
- A working title
- The reader's question in their words
- Why it matters to the business
- The page it should link to
- Best format (how-to, checklist, comparison, story)

Mark the three topics with the strongest link to a service, and say why. Do not make claims about search demand or traffic. Prefer topics where a local, experienced business can add something that general websites cannot. {FG}""",
                tip="Keep a running document of customer questions. It becomes a topic bank that never runs dry."),
            dict(
                n=32, title="Blog Post Outline",
                use="You have a topic and want a structure that answers the reader's question before you write.",
                fill=[("[POST TOPIC]", "The subject of the post."),
                      ("[READER'S QUESTION]", "The question this post answers."),
                      ("[SEARCH PHRASE]", "The main phrase, if you have one."),
                      ("[WORD COUNT]", "Target length, for example 800.")],
                prompt="""Create an outline for a blog post on the website of [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Reader: [TARGET AUDIENCE]
Topic: [POST TOPIC]
The reader's question: [READER'S QUESTION]
Main search phrase: [SEARCH PHRASE]
Target length: [WORD COUNT] words
Facts and experience I can add: [KEY FACTS]
Goal: [MAIN GOAL]

Deliver:
1. Three title options (max 65 characters)
2. An outline with H2 and H3 headings; under each, the points it must cover
3. Marked slots, titled “EXPERIENCE NEEDED”, where only the business can add an example, photo, number or story, with a prompt for what to supply
4. Where the call to action belongs and what it says

The post should answer the question in the first 100 words, then give the detail. {FG}""",
                tip="The “EXPERIENCE NEEDED” slots are what make a post better than a generic one. Do not skip them."),
            dict(
                n=33, title="Blog Draft From Outline and Facts",
                use="The outline is approved and you want a first draft that does not invent facts.",
                fill=[("[APPROVED OUTLINE]", "The outline from Prompt 32, after your edits."),
                      ("[FACTS & EXAMPLES]", "Your real examples, numbers, quotes, and the sources for any outside facts.")],
                prompt="""Write a blog post draft for [BUSINESS NAME] from the approved outline below.

Reader: [TARGET AUDIENCE]
Tone: [TONE OF VOICE]
Approved outline:
[APPROVED OUTLINE]
Facts, examples and sources I can vouch for:
[FACTS & EXAMPLES]
Closing call to action: [MAIN GOAL]

Write in short paragraphs (max four lines), with plain words and active verbs. Open with the answer, not with background.

Mark any statement that depends on an outside fact, statistic, law or date that is not in my materials as [CHECK: claim needs a source]. After the draft, list those claims in a table titled “Verify before publishing”. Do not add quotes, studies, or named sources that I did not supply. {FG}""",
                tip="Add your own example in each major section. Readers and search engines both prefer first-hand detail."),
            dict(
                n=34, title="Refresh an Old Post",
                use="An old post still gets visits but is outdated, thin or off-brand.",
                fill=[("[OLD POST TEXT]", "The full text of the existing post."),
                      ("[WHAT HAS CHANGED]", "New prices, services, rules, dates or examples since it was written.")],
                prompt="""Refresh an old blog post for [BUSINESS NAME].

Reader: [TARGET AUDIENCE]
Tone: [TONE OF VOICE]
Old post:
[OLD POST TEXT]
What has changed since it was written: [WHAT HAS CHANGED]
Current facts: [KEY FACTS]

Step 1 – Audit: list what is outdated, unclear, repetitive or missing, quoting the text. Flag anything that may now be factually wrong.
Step 2 – Rewrite: keep the original topic and the parts that still work, update what has changed, and tighten the writing. Keep or improve the headings and do not change the topic of the page.
Step 3 – Summarise the changes in a short list I can use for an “Updated on” note.

Do not add facts, statistics or sources I have not supplied. Mark uncertain statements as [CHECK: claim needs a source]. {FG}""",
                tip="Keep the URL. Change the content and the published/updated date, not the address."),
            dict(
                n=35, title="Repurpose a Page Into Email & Social",
                use="You published something good and want to share it without writing from scratch.",
                fill=[("[SOURCE PAGE TEXT]", "The page or post you want to repurpose."),
                      ("[PLATFORMS]", "Where you post: LinkedIn, Instagram, Facebook, a newsletter.")],
                prompt="""Repurpose the content below for [BUSINESS NAME].

Audience: [TARGET AUDIENCE]
Tone: [TONE OF VOICE]
Platforms: [PLATFORMS]
Source content:
[SOURCE PAGE TEXT]

Deliver:
1. A newsletter section of about 120 words with a subject line and link text
2. Three social posts, each taking a different angle (a surprising fact from the source, a mistake to avoid, a practical tip), each with a hook line, body and call to action
3. Three Instagram or carousel caption ideas, each with a slide-by-slide outline of five slides

Adapt style to each platform, but every fact must come from the source. Do not add hashtags beyond three per post, statistics or claims not in the source. {FG}""",
                tip="Schedule posts across two weeks so one page keeps working long after it is published."),
        ]),
    dict(
        n=8, title="Editing, Tone & Brand Voice",
        blurb="Good copy sounds like one person wrote it, even when five people did. These prompts define a voice from "
              "real samples, apply it, simplify jargon, trim length and catch inconsistencies across pages.",
        order="Define the voice once (36), then reuse its “voice paragraph” in every other prompt as [TONE OF VOICE].",
        prompts=[
            dict(
                n=36, title="Brand Voice Profile From Real Samples",
                use="The client says “friendly but professional” and every draft sounds different.",
                fill=[("[WRITING SAMPLES]", "Three to five real pieces (emails, existing site copy, social posts) of 100–300 words each, by the people whose voice you want to capture.")],
                prompt="""Analyse the writing samples below and build a brand voice profile for [BUSINESS NAME].

Audience: [TARGET AUDIENCE]
Samples:
[WRITING SAMPLES]

Deliver:
1. Five voice traits. For each: a one-line description, a short example phrase taken from the samples, and a “never sounds like” contrast
2. Habits: typical sentence length, use of questions, contractions, humour, and how formal the greetings and sign-offs are
3. Vocabulary: ten words and phrases to use, ten to avoid
4. A ten-line style guide with spelling and punctuation conventions I can hand to other writers
5. A single “voice paragraph” (maximum 80 words) that I can paste into any future prompt in place of the tone-of-voice line

Base everything on the samples. If the samples contradict each other, tell me where. {FG}""",
                tip="Use samples from the people customers actually talk to, not from a brand guideline that nobody follows."),
            dict(
                n=37, title="Rewrite in Brand Voice",
                use="Copy is accurate but flat, or written by several people with different styles.",
                fill=[("[VOICE PARAGRAPH]", "The voice paragraph from Prompt 36, or your tone-of-voice note."),
                      ("[TEXT TO REWRITE]", "The copy to change.")],
                prompt="""Rewrite the text below in the voice of [BUSINESS NAME].

Voice: [VOICE PARAGRAPH]
Audience: [TARGET AUDIENCE]
Text to rewrite:
[TEXT TO REWRITE]

Keep every fact, number, name, date and price exactly as in the original. Change only wording, rhythm and structure. Keep the length within 10% of the original unless I say otherwise.

After the rewrite, list the three biggest changes you made and one place where the original meaning was unclear, so I can confirm it. If you had to choose between sounding on-brand and being accurate, choose accurate. {FG}""",
                tip="Compare the two versions side by side. If a fact moved, the rewrite went too far."),
            dict(
                n=38, title="Plain-Language Pass (Remove Jargon)",
                use="The text is technically correct but your readers have to decode it.",
                fill=[("[TEXT TO SIMPLIFY]", "The copy to clarify."),
                      ("[READER'S KNOWLEDGE LEVEL]", "What they already know, for example “no technical background”.")],
                prompt="""Make the text below clearer for people with this level of knowledge: [READER'S KNOWLEDGE LEVEL].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Tone: [TONE OF VOICE]
Text:
[TEXT TO SIMPLIFY]

Rewrite it using short sentences, common words and the active voice. Keep necessary technical terms but explain each in a few words the first time it appears.

Then provide:
1. A list of the jargon, passive phrases and long sentences you replaced, with the replacements
2. A warning on any place where simplifying might change the meaning (technical, legal, medical or financial content), so a specialist can check it

Do not remove facts or conditions to make the text shorter. {FG}""",
                tip="Replace what you can, but never at the cost of accuracy. In regulated topics, a specialist should have the last word."),
            dict(
                n=39, title="Tighten to a Word Count",
                use="The copy overflows its space or readers are skimming past it.",
                fill=[("[TEXT]", "The copy to shorten."),
                      ("[TARGET WORD COUNT]", "The length it needs to reach.")],
                prompt="""Shorten the text below for the website of [BUSINESS NAME].

Audience: [TARGET AUDIENCE]
Tone: [TONE OF VOICE]
Text:
[TEXT]

Give me three versions:
1. Light trim: remove repetition and filler, about 10% shorter
2. Target: exactly [TARGET WORD COUNT] words, or as close as possible
3. One-sentence summary

Keep every fact, number, name and call to action. Then list what you cut from version 2 and why, so I can restore anything that matters. Report the word count of each version, and tell me that your counts may be slightly off so I should verify them. {FG}""",
                tip="Cut the first paragraph first. It is often warm-up that the reader does not need."),
            dict(
                n=40, title="Consistency & Terminology Audit",
                use="You have drafted a whole site and need to catch contradictions before launch.",
                fill=[("[PAGES TO CHECK]", "Paste several pages, each labelled with its name."),
                      ("[PREFERRED TERMS]", "Your decisions: spelling (UK or US), “clients” vs “customers”, date style, capitalisation.")],
                prompt="""Audit the pages below for consistency. They belong to the website of [BUSINESS NAME].

Preferred terms and style decisions: [PREFERRED TERMS]
Verified facts to check against: [KEY FACTS]
Intended tone: [TONE OF VOICE]
Pages:
[PAGES TO CHECK]

Report in a table: issue, page and quote, suggested fix. Cover:
- Contradicting facts (prices, hours, phone numbers, names, services)
- Mixed terms for the same thing
- Spelling and punctuation variants
- Heading capitalisation and date, number and currency formats
- Pages where the tone drifts

End with a short style-decisions list I can adopt as the project's style guide. Do not rewrite the pages; only report. {FG}""",
                tip="Run this just before client sign-off, then again after the last round of changes."),
        ]),
    dict(
        n=9, title="Web Design Handoff & UX Copy",
        blurb="Designers need real words, not lorem ipsum, and users need interface text that helps. These prompts "
              "produce navigation, form and error copy, a ready-to-paste copy deck, a content-first outline, and "
              "alt text and accessibility checks.",
        order="Outline content first (44), build the copy deck (43), then the microcopy (41, 42), then accessibility (45).",
        prompts=[
            dict(
                n=41, title="Navigation, Button & Interface Microcopy",
                use="Menus, buttons and form labels were named by whoever built the template.",
                fill=[("[SITE PAGES]", "The page list or sitemap."),
                      ("[KEY ACTIONS]", "The actions users take: enquire, book, buy, download, log in.")],
                prompt="""Write the interface copy for the website of [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Pages: [SITE PAGES]
Key actions: [KEY ACTIONS]
Tone: [TONE OF VOICE]

Deliver as a table (element, location, text, notes):
- Main navigation labels (max 2 words each, in the order users need them)
- Footer link groups and labels
- Button labels for each key action
- Form field labels, placeholders and helper text
- Tooltips or short explanations for anything that needs one

Use the same verb for the same action everywhere. Choose plain words visitors use, not internal terms. Mark where a label is a deliberate choice between options and give both with a recommendation. {FG}""",
                tip="Name menu items for what visitors want to find, not for how the company is organised."),
            dict(
                n=42, title="Error, Empty-State & Confirmation Messages",
                use="Users see “Error 404”, “Invalid input” or nothing at all after submitting a form.",
                fill=[("[FORMS & FEATURES ON THE SITE]", "Every form, search box, cart or login that can fail or return nothing."),
                      ("[CONTACT FALLBACK]", "How a stuck visitor can reach a human, exactly as written.")],
                prompt="""Write system-message copy for the website of [BUSINESS NAME].

Audience: [TARGET AUDIENCE]
Forms and features: [FORMS & FEATURES ON THE SITE]
Contact fallback: [CONTACT FALLBACK]
Tone: [TONE OF VOICE]

Deliver as a table (situation, message, where it appears):
1. A 404 page with a heading, a helpful line and two useful links
2. Validation messages for name, email, phone, required fields and file upload
3. Form success and form failure messages
4. An empty search-results message
5. Any other message the listed features need

Each message must say what happened, what to do next, and never blame the user. Keep messages under 25 words except the 404 page. Use my contact fallback exactly as written. {FG}""",
                tip="Developers often skip these. Handing them over finished saves a round of questions."),
            dict(
                n=43, title="Copy Deck for a Wireframe or Design",
                use="A wireframe is approved and each block needs real copy that fits.",
                fill=[("[WIREFRAME BLOCKS]", "Each block with its type and any character limit, for example: Hero headline (60), Hero subhead (120), Card title ×3 (30)."),
                      ("[PAGE NAME]", "The page being designed.")],
                prompt="""Create a copy deck for the “[PAGE NAME]” page of [BUSINESS NAME].

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Facts: [KEY FACTS]
Tone: [TONE OF VOICE]
Goal: [MAIN GOAL]
Wireframe blocks and limits:
[WIREFRAME BLOCKS]

Deliver a table with these columns: block ID, element type, copy, character count, notes. Make sure the copy fits every limit. Include a shorter mobile variant for any block longer than 80 characters.

Where the wireframe needs content that my facts do not provide, write [NEEDS INFO: what is needed] in the copy column instead of filler text. Do not use lorem ipsum. {FG}""",
                tip="Paste the table into your design tool and keep the block IDs in layer names to track changes."),
            dict(
                n=44, title="Content-First Page Outline",
                use="You want to define the content hierarchy before any design starts.",
                fill=[("[PAGE GOAL]", "The one thing this page must achieve."),
                      ("[VISITOR QUESTIONS IN ORDER]", "What a visitor wants to know, in the order they ask it."),
                      ("[AVAILABLE ASSETS]", "Photos, logos, testimonials, data, documents you already have.")],
                prompt="""Create a content-first outline for a page on the website of [BUSINESS NAME] before any design is made.

Business: [BUSINESS DESCRIPTION]
Audience: [TARGET AUDIENCE]
Page goal: [PAGE GOAL]
Visitor questions, in order: [VISITOR QUESTIONS IN ORDER]
Assets we have: [AVAILABLE ASSETS]
Facts: [KEY FACTS]

Deliver a table with columns: order, content block, question it answers, content needed (text, image, proof, data), status (have it or need it), priority (must, should, could), and suggested word count.

Then list the missing content I must request from the client, written as clear requests. Order blocks by what the visitor needs, not by what the business wants to say first. {FG}""",
                tip="Share this with the client before design starts. It exposes missing content while there is still time."),
            dict(
                n=45, title="Alt Text & Accessibility Copy Check",
                use="Images have no alt text, links say “click here”, or you want a quick accessibility pass on the words.",
                fill=[("[IMAGE DESCRIPTIONS]", "For each image: what it shows, why it is on the page, and where it appears."),
                      ("[PAGE TEXT]", "The page copy including link text and button labels.")],
                prompt="""Review the copy of a page on the website of [BUSINESS NAME] for accessibility.

Audience: [TARGET AUDIENCE]
Images, as I describe them: [IMAGE DESCRIPTIONS]
Page text:
[PAGE TEXT]

Deliver:
1. Alt text for each image, 125 characters or fewer, describing what matters in context. Mark purely decorative images as alt=\"\"
2. A list of vague link texts (“click here”, “read more”) with clear replacements
3. Button labels that are unclear out of context, with fixes
4. Heading-order problems
5. Sentences or words that are hard to read, with simpler versions

You cannot see the images, so base alt text only on my descriptions and tell me if any description is too thin. This is a quick copy check, not a full audit; a person should test the page with an accessibility tool and a screen reader. {FG}""",
                tip="Good alt text answers: what would a person using a screen reader miss if this image were gone?"),
        ]),
    dict(
        n=10, title="Client Workflow & Agency Ops",
        blurb="Content delay and vague feedback sink more projects than bad design. These prompts handle the "
              "human side: discovery, getting content from clients, presenting copy, decoding feedback and "
              "defining scope in plain language.",
        order="Use 46 at kick-off, 47 when content is late, 48 at delivery, 49 during revisions, 50 while quoting.",
        prompts=[
            dict(
                n=46, title="Tailored Discovery Questionnaire",
                use="Generic onboarding forms bring generic answers and you want questions fitted to this client.",
                fill=[("[CLIENT INDUSTRY]", "The client's field."),
                      ("[PROJECT TYPE]", "New site, redesign, landing page, copy refresh."),
                      ("[WHAT YOU ALREADY KNOW]", "Everything already learned, so the AI does not ask it again.")],
                prompt="""Create a discovery questionnaire for a website copy project.

Client industry: [CLIENT INDUSTRY]
Project type: [PROJECT TYPE]
What we already know: [WHAT YOU ALREADY KNOW]
The audience for the questionnaire: a small-business owner with no marketing background

Deliver 15 questions grouped under: the business, the customers, the offer, proof, competitors, voice, goals, and logistics. For each question give a one-line reason for asking (written for the client) and a short example answer.

Skip anything I have already told you. Make questions concrete and answerable in a sentence or two. End with a short “please send us” list of documents and assets (for example brochures, price lists, photos, existing reviews). {FG}""",
                tip="Send it as a shared document so clients can answer in short sessions instead of one sitting."),
            dict(
                n=47, title="Content Request & Chaser Emails",
                use="The project is stuck waiting for text, photos or approvals.",
                fill=[("[CLIENT NAME]", "Who you are writing to."),
                      ("[YOUR NAME]", "Who the emails are from."),
                      ("[CONTENT NEEDED & DEADLINE]", "Exactly what is missing and by when."),
                      ("[LAUNCH DATE AT RISK]", "The date that moves if the content is late.")],
                prompt="""Write a sequence of four emails to a client who owes content for their website project.

Client: [CLIENT NAME]
From: [YOUR NAME] at [BUSINESS NAME]
What we need, and by when: [CONTENT NEEDED & DEADLINE]
What it affects: [LAUNCH DATE AT RISK]
Tone: [TONE OF VOICE]

Emails:
1. The initial request, with a clear checklist
2. A friendly reminder after the deadline passes
3. A firmer, still kind follow-up that explains how the delay affects the schedule
4. A final note that offers two options: send what they have, or agree a new date

Each email is 120 words or less, has a subject line, makes the next step easy and never threatens. Do not mention fees, penalties or terms that I have not given you. {FG}""",
                tip="Offer to take dictated answers by phone. Many clients cannot write but can talk."),
            dict(
                n=48, title="Explain the Copy to the Client",
                use="You are about to deliver a draft and want the client to judge it against their goals, not their taste.",
                fill=[("[COPY BEING PRESENTED]", "The draft or its key sections."),
                      ("[CLIENT BRIEF GOALS]", "The goals and priorities the client gave you.")],
                prompt="""Prepare a short rationale to accompany copy I am delivering to a client of [BUSINESS NAME].

Client goals from the brief: [CLIENT BRIEF GOALS]
Audience: [TARGET AUDIENCE]
Tone chosen: [TONE OF VOICE]
Copy being presented:
[COPY BEING PRESENTED]

Deliver:
1. A cover email of about 120 words
2. A one-page rationale: for each section, what it does, why I wrote it that way, and which goal from the brief it serves
3. “Decisions we need from you”: a short list of questions
4. “Facts to confirm”: every number, name and claim the client must verify
5. Three plain instructions on how to give useful feedback (for example, “Say what feels wrong and why, not just the new wording”)

Stay honest about trade-offs and do not oversell the draft. {FG}""",
                tip="Frame feedback around the brief's goals. It shifts the conversation from preference to purpose."),
            dict(
                n=49, title="Client Feedback Translator",
                use="Feedback like “make it pop” or “it doesn't feel us” needs turning into specific changes.",
                fill=[("[CLIENT FEEDBACK]", "Paste the comments word for word."),
                      ("[CURRENT COPY]", "The text the feedback refers to.")],
                prompt="""Translate client feedback into an actionable revision list for [BUSINESS NAME].

Audience: [TARGET AUDIENCE]
Goal of the page: [MAIN GOAL]
Tone: [TONE OF VOICE]
Current copy:
[CURRENT COPY]
Client feedback, verbatim:
[CLIENT FEEDBACK]

Deliver a table with columns: feedback quote, two possible meanings, the question I should ask to find out which, the proposed change, and the risk of making it.

Then:
1. Highlight any comments that conflict with each other or with the original brief
2. Provide a prioritised list of changes I can make now, without more information
3. Draft a short reply to the client that confirms what I will change, lists the questions, and flags any conflicts politely

Do not rewrite the copy yet. {FG}""",
                tip="Ask clients to point to the line that bothers them. Specific location beats general mood."),
            dict(
                n=50, title="Copy Scope & Revision Wording",
                use="You want to state in plain language what a copy project includes and where extra work begins.",
                fill=[("[DELIVERABLES]", "Pages or items included."),
                      ("[REVISION ROUNDS]", "How many rounds are included."),
                      ("[FEEDBACK WINDOW]", "How long the client has to respond."),
                      ("[WHAT COSTS EXTRA]", "Work that falls outside the scope.")],
                prompt="""Write plain-language scope wording for a website copy project at [BUSINESS NAME].

Deliverables: [DELIVERABLES]
Revision rounds included: [REVISION ROUNDS]
Feedback window: [FEEDBACK WINDOW]
Work that costs extra: [WHAT COSTS EXTRA]
Client responsibilities and other facts: [KEY FACTS]
Tone: [TONE OF VOICE]

Deliver:
1. A scope paragraph for a proposal (about 120 words) stating what is included, delivery format and client responsibilities
2. A revision policy that defines the difference between a revision and new work, with two examples of each
3. A one-line version for quotes and invoices
4. A list of questions I have not answered that could cause disputes later

Use only the numbers and terms I supplied. This is a plain-language draft, not legal advice. Have your contract reviewed by a qualified professional before relying on it. {FG}""",
                tip="Share the scope in writing before the work starts. It protects both sides."),
        ]),
]


def expanded(p):
    return p["prompt"].replace("{FG}", FACT_GUARD)


def all_prompts():
    out = []
    for c in CATEGORIES:
        for p in c["prompts"]:
            out.append((c, p))
    return out
