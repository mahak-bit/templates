# -*- coding: utf-8 -*-
"""Front matter, the brief, the worked example, the checklist and back matter.

Light markup supported by the builders: **bold** and *italic*.
"""

TITLE = "The AI Website Copy Kit"
SUBTITLE = "50 Ready-to-Use AI Prompts for Better Website Content"
YEAR = "2026"
VERSION = "Edition 1.0"
PUBLISHER = "Mahak's Studio"

AUDIENCE_LINE = "For freelance web designers, developers, small agencies and small-business owners"

INTRO = {
    "heading": "Introduction",
    "lead": "Website copy is where most small projects stall. The design is ready, the code works, and the "
            "page still says “Lorem ipsum” because nobody has the words.",
    "paras": [
        "This kit gives you fifty prompts that fix that. Each one is written to be pasted into an AI chat "
        "assistant, filled in with your own details, and used to produce a draft you can edit, check and "
        "publish with confidence.",
        "The prompts are built around one idea: **AI writes better when you give it real facts, and "
        "worse when you let it improvise.** Every prompt asks for the information it needs, tells the AI to "
        "use only what you provide, and asks it to flag anything missing instead of inventing it. That "
        "gives you drafts that are easier to check and edit.",
    ],
    "for_heading": "Who it is for",
    "for_items": [
        ("Freelance designers and developers", "who need real copy before a layout can be approved."),
        ("Small agencies", "that want a consistent, repeatable way to brief and edit copy across clients."),
        ("Small-business owners", "who write their own site and want a structure to follow."),
    ],
    "inside_heading": "What is inside",
    "inside_items": [
        "**50 prompts** in 10 categories, from the hero headline to the client revision policy",
        "**A reusable client and business brief** that feeds every prompt",
        "**A quick-start guide** and a “which prompt do I need?” finder",
        "**A complete worked example** for a fictional neighbourhood bakery",
        "**A website-copy quality checklist** to review any draft before it goes live",
    ],
    "honest_heading": "What it is not",
    "honest": "These prompts do not replace your judgement, your client’s approval or professional advice. "
              "AI tools can make mistakes, so every draft needs a human read and a fact check. "
              "No result is promised: the quality of the output depends on the facts you supply, the tool you "
              "use and the editing you do.",
}

LICENCE = {
    "heading": "Licence & Notes",
    "items": [
        ("What you may do", "Use the prompts and templates in this kit to create copy for your own business "
                            "and for your clients’ websites, as often as you like."),
        ("What you may not do", "Resell, share, post online or redistribute this kit or its prompts, in whole or in part, "
                                "or include them in another product, course or template pack."),
        ("Tools and trademarks", "The prompts are written to work with any modern AI chat assistant. Product and company names "
                                 "mentioned belong to their owners. This kit is independent and is not affiliated with or endorsed by any AI provider."),
        ("Your data", "Do not paste confidential or personal client information into any AI tool unless you have "
                      "permission and have checked that tool’s data and privacy settings."),
        ("No professional advice", "The kit contains writing aids. It does not provide legal, medical, financial or "
                                   "advertising-compliance advice. Check regulated claims with a qualified professional."),
        ("Copying from the PDF", "Text copied from a PDF can carry extra line breaks. If your pasted prompt looks broken, "
                                 "use the plain-text Prompt Library file that comes with this kit."),
    ],
}

QUICKSTART = {
    "heading": "Quick-Start Guide",
    "lead": "Here is the shortest route to a first draft. The times are rough estimates and will vary with your project.",
    "steps": [
        ("Fill in the brief", "About 20 minutes",
         "Complete at least the **Core Six** on the brief (business name, description, audience, key facts, "
         "tone and main goal). Leave unknowns blank rather than guessing. Blanks are useful: they show you "
         "what to ask the client."),
        ("Choose your prompt", "1 minute",
         "Use the finder on the next page or the contents list. Pick the one prompt that matches the page "
         "or task in front of you. Do not paste several at once."),
        ("Copy, then replace every [PLACEHOLDER]", "5 minutes",
         "Paste the prompt into a text editor first. Replace every square-bracket placeholder with your own "
         "details. Search for “[” to catch leftovers. Longer facts work best as short bullet points."),
        ("Run it and read the flags", "5 minutes",
         "Paste the finished prompt into your AI chat. Look for any [NEEDS INFO: …] or [CHECK: …] markers. "
         "Those are gaps the AI could not fill honestly. Answer them and ask for a revised version."),
        ("Edit like a human, then run the checklist", "10 minutes",
         "Read the draft aloud, cut anything that is not true or not useful, and run the quality checklist at "
         "the back of this kit before anything is published."),
    ],
    "followups_heading": "Follow-up requests that work",
    "followups": [
        "“Make that 20% shorter without losing any facts.”",
        "“Give me three alternatives for the second sentence only.”",
        "“Rewrite it for someone who has never heard of us.”",
        "“Which statement here is least supported by my key facts?”",
        "“List every claim in this draft that I need to verify.”",
    ],
    "habits_heading": "Good habits",
    "habits": [
        "One task per message. Long, mixed requests give muddy drafts.",
        "Keep one chat per project so the AI remembers earlier decisions, then paste approved copy back in as reference.",
        "Never publish unreviewed AI text. Check every number, name, date, price and promise.",
        "Keep a file of your verified facts. It is the best asset in the whole process.",
    ],
}

FINDER = {
    "heading": "Which Prompt Do I Need?",
    "rows": [
        ("The homepage does not say clearly what we do", "1, 2, 5"),
        ("I need a complete homepage draft", "3, 4"),
        ("The About page is weak or missing", "6, 7, 8, 9, 10"),
        ("Service or product pages need writing", "11, 12, 13, 14, 15"),
        ("Visitors read but do not enquire or buy", "16, 17, 18, 19, 20"),
        ("The site has little proof or trust", "21, 22, 23, 24, 25"),
        ("We need to be found in search or locally", "26, 27, 28, 29, 30"),
        ("We need blog or social content", "31, 32, 33, 34, 35"),
        ("The copy is inconsistent or off-brand", "36, 37, 38, 39, 40"),
        ("I am handing copy to a designer or developer", "41, 42, 43, 44, 45"),
        ("The client is slow, vague or expanding the scope", "46, 47, 48, 49, 50"),
    ],
    "order_heading": "A sensible order for a five-page small-business site",
    "order": [
        ("Brief", "Fill it first."),
        ("2, then 1", "Positioning, then the hero."),
        ("3", "Draft the homepage."),
        ("9, then 6", "Credentials, then the About page."),
        ("11, per service", "One page for each main service."),
        ("14 and 24", "Pricing and FAQ, if relevant."),
        ("18", "Contact page and form."),
        ("27", "Titles and descriptions."),
        ("40", "Consistency audit, then the checklist."),
    ],
}

ANATOMY = {
    "heading": "How Every Prompt Works",
    "lead": "All fifty prompts follow the same pattern, so once you have used one you can use them all.",
    "parts": [
        ("Use it when", "A one-line situation, so you can tell quickly whether the prompt fits."),
        ("Fill in", "The placeholders specific to that prompt, with a hint for each. The Core Six are explained on the brief."),
        ("The prompt", "Copy everything inside the box. Square-bracket placeholders are shown in blue."),
        ("Tip", "A single practical idea for getting more from that prompt."),
    ],
    "fg_heading": "The Fact Guard",
    "fg_lead": "Every prompt ends with the same four sentences. This is a safeguard that helps keep drafts honest. It reduces, but does "
               "not eliminate, invented details, so you still need to check. If you adapt a prompt, keep it.",
    "markers_heading": "Markers you will see in the AI's reply",
    "markers": [
        ("[NEEDS INFO: …]", "The AI needs a fact you did not supply. Provide it or remove the line."),
        ("[CHECK: …]", "A statement depends on an outside fact or source. Verify it or cut it."),
    ],
    "placeholder_note": "A placeholder in capital letters inside square brackets, like [BUSINESS NAME], is for you to replace. "
                        "Text inside brackets that contains a colon, like [NEEDS INFO: price], is a marker the AI writes back to you.",
}

# ------------------------------------------------------------------ THE BRIEF
BRIEF = {
    "heading": "The Client & Business Brief",
    "lead": "Complete this once per project. It is the source for every placeholder in the kit. "
            "You can fill it yourself or send it to a client. A Word version is included for typing into.",
    "core_note": "The Core Six are the answers that appear in almost every prompt. Fill these first.",
    "sections": [
        ("A", "The business", [
            "Business name (exactly as it should appear)",
            "Website address, if one exists",
            "In one sentence: what you do, for whom, and where",
            "Location and areas you serve",
            "How long you have been operating",
            "Who approves the final copy?",
        ]),
        ("B", "Your customers", [
            "Who is your ideal customer? Describe one real example",
            "What is happening in their life or work when they look for you?",
            "What are their three biggest problems or wishes?",
            "What worries or doubts stop them from buying?",
            "Where do they usually find you? (search, referral, social, walk-in)",
        ]),
        ("C", "Your offer", [
            "Main service or product, in plain words",
            "Other services or products",
            "Prices or price ranges you are happy to publish",
            "How a customer buys or books, step by step",
            "What is included, and what is not",
        ]),
        ("D", "Proof & facts you can verify", [
            "Qualifications, licences, memberships (with evidence)",
            "Real numbers: years, customers served, projects completed",
            "Real testimonials you have permission to publish",
            "Policies: refunds, revisions, cancellations, warranties",
            "Awards or press, only if you can link to the source",
        ]),
        ("E", "What makes you different", [
            "Three things you do that competitors do not, each with evidence",
            "What do customers do instead of hiring you?",
            "What would you honestly say you are not the best choice for?",
        ]),
        ("F", "Voice", [
            "Three to five words that describe how you sound",
            "Words you love, words you never use",
            "Do you write as “we”, “I” or in the third person?",
            "Two websites whose writing you like, and why",
        ]),
        ("G", "Website goals", [
            "The single most important action a visitor should take",
            "Secondary actions",
            "Pages needed (list them)",
            "Contact details exactly as they should appear",
        ]),
        ("H", "Search & local", [
            "Phrases customers use to find you (from enquiries, not guesses)",
            "Towns or areas you want to be found in",
            "Do you have a Google Business Profile?",
        ]),
        ("I", "Limits & logistics", [
            "Anything you cannot say (regulated claims, legal limits, contracts)",
            "Content you already have: photos, brochures, reviews",
            "Deadline and launch date",
            "Words or topics to avoid",
        ]),
    ],
    "core_six": "The Core Six",
    "context_heading": "Your Context Block",
    "context_lead": "When a prompt does not fit your situation exactly, paste this block at the top of your chat first, then ask your own question.",
    "context_template": """About my business: [BUSINESS NAME] – [BUSINESS DESCRIPTION]
My audience: [TARGET AUDIENCE]
Facts you may use (nothing else): [KEY FACTS]
Tone of voice: [TONE OF VOICE]
The main goal of my website: [MAIN GOAL]

Use only the facts above. If you need a detail that is missing, write [NEEDS INFO: what is missing] instead of guessing. Do not invent statistics, awards, testimonials, prices, guarantees or client names.""",
}

# -------------------------------------------------------------- WORKED EXAMPLE
EX = {
    "business": "Saltgrain Bakehouse",
    "town": "Eastbrook",
}

EX_FACTS = [
    "Neighbourhood bakery on Mill Lane, Eastbrook, opened in 2019 by Meera and Daniel Rao.",
    "Sourdough breads, pastries and custom celebration cakes (birthdays, anniversaries, family occasions), all baked in-house daily.",
    "Sourdough is made with stoneground flour from a regional mill. The starter has been kept since 2019.",
    "Open Tuesday to Sunday, 7:30 am to 2:00 pm. Closed Mondays.",
    "Bread pre-orders: order by 6 pm the day before and collect in the shop.",
    "Custom cakes: order at least 5 days ahead; from ₹1,400 for a 1 kg cake; 50% deposit confirms the order, balance on collection; collection from the shop only.",
    "Core cake flavours: vanilla bean, dark chocolate, lemon and poppy seed. Piped message and fresh fruit or flower topping included. No sculpted or fondant-figure cakes.",
    "The kitchen handles wheat, milk, eggs, nuts and sesame, so no item can be guaranteed free of them.",
]

EX_CORE = [
    ("[BUSINESS NAME]", "Saltgrain Bakehouse"),
    ("[BUSINESS DESCRIPTION]", "A neighbourhood bakery in Eastbrook making sourdough bread, pastries and custom celebration cakes."),
    ("[TARGET AUDIENCE]", "Local households who want better everyday bread, and people in Eastbrook planning a birthday, anniversary or family celebration."),
    ("[KEY FACTS]", "(the eight facts listed above)"),
    ("[TONE OF VOICE]", "Warm, plain-spoken and a little proud of the craft; never salesy or flowery."),
    ("[MAIN GOAL]", "Get people to pre-order bread for collection, or send a custom-cake enquiry."),
]

EX_HERO_FILLED = """Act as a conversion-focused website copywriter. Write hero-section copy for the homepage of Saltgrain Bakehouse.

About the business: A neighbourhood bakery in Eastbrook making sourdough bread, pastries and custom celebration cakes.
Who it is for: Local households who want better everyday bread, and people in Eastbrook planning a birthday, anniversary or family celebration.
Main offer: Sourdough loaves to pre-order and collect, plus custom celebration cakes
The visitor's biggest problem: Wanting good bread and a reliable cake without a long wait or guesswork
Facts you may use: [the eight facts above]
Tone: Warm, plain-spoken and a little proud of the craft; never salesy or flowery.
The page should lead visitors to: Pre-order bread for collection, or send a custom-cake enquiry.

… (the rest of Prompt 1 follows, unchanged) …"""

EX_HERO_OUT = [
    ("Outcome-led", "Fresh sourdough, ready when you are",
     "Pre-order by 6 pm and collect freshly baked loaves from our Mill Lane bakery, Tuesday to Sunday.",
     "Pre-order bread", "Order by 6 pm the day before."),
    ("Problem-led", "Planning a celebration? Let us bake the cake.",
     "Custom cakes made to order from ₹1,400, with at least five days’ notice.",
     "Plan your cake", "Collection from our Mill Lane shop."),
    ("Specific-detail-led", "Sourdough from a starter we have kept since 2019",
     "Baked in-house with stoneground flour from a regional mill, Tuesday to Sunday.",
     "See our breads", "Open 7:30 am to 2 pm, Tuesday to Sunday."),
]
EX_HERO_REC = ("Angle 3 is the most distinctive: only this bakery can say it, and every word comes from the facts. "
               "Swap its button to “Pre-order bread” so it matches the main goal.")

EX_SERVICE = {
    "prompt_no": 11,
    "h1": "Custom celebration cakes in Eastbrook",
    "intro": "A celebration cake should suit the occasion and the people eating it. We bake custom cakes to order "
             "in our Mill Lane kitchen for birthdays, anniversaries and family occasions.",
    "for": "Anyone in Eastbrook planning a family celebration who can order at least five days ahead. "
           "Not for: sculpted or fondant-figure cakes, which we do not make.",
    "included": [
        "Cakes from 1 kg, from ₹1,400",
        "Choice of vanilla bean, dark chocolate, or lemon and poppy seed",
        "A piped message and a fresh fruit or flower topping",
    ],
    "steps": ["Send us the date, size and flavour you would like.",
              "Pay the 50% deposit to confirm your order.",
              "Collect your cake from the shop and pay the balance."],
    "cost": "From ₹1,400 for a 1 kg cake. [NEEDS INFO: price list for larger sizes]",
    "cta": "Send a cake enquiry",
}

EX_FAQ = [
    ("How far ahead should I order a custom cake?",
     "Please order at least five days ahead. [NEEDS INFO: can short-notice cake orders be accepted?]"),
    ("Can I pre-order bread?",
     "Yes. Order by 6 pm the day before and collect it in the shop. We are open Tuesday to Sunday, 7:30 am to 2:00 pm."),
    ("Do you deliver?",
     "Not at the moment. Cakes and bread pre-orders are for collection from our Mill Lane shop."),
    ("Do you make eggless or allergen-free cakes?",
     "Our kitchen handles wheat, milk, eggs, nuts and sesame, so we cannot guarantee that any item is free of them. "
     "[NEEDS INFO: is an eggless cake available?]"),
]

EX_META = [
    ("Homepage",
     "Sourdough Bakery in Eastbrook | Saltgrain Bakehouse",
     "Sourdough, pastries and custom cakes baked daily on Mill Lane, Eastbrook. Pre-order bread by 6 pm the day before. Open Tuesday to Sunday, 7:30 am to 2 pm."),
    ("Custom cakes page",
     "Custom Celebration Cakes in Eastbrook | Saltgrain Bakehouse",
     "Custom celebration cakes from ₹1,400 for 1 kg, baked to order in Eastbrook. Please order at least five days ahead. Collection from our Mill Lane shop."),
]

EX_REVIEW = [
    ("pass", "Hours match everywhere", "Tuesday to Sunday, 7:30 am to 2:00 pm appears the same in the hero, FAQ and meta text."),
    ("pass", "Price matches the facts", "“From ₹1,400” is identical on the cake page, the hero and the meta description."),
    ("pass", "No invented proof", "No testimonial, award or review was added; the proof slot is left open."),
    ("flag", "Eggless cake", "The AI left a marker instead of guessing. The owner must answer before any “eggless” claim is published."),
    ("flag", "“Regional mill”", "True to the facts, but the owner may prefer to name the mill. This is a human decision."),
    ("flag", "Short-notice orders", "A marker remains in the FAQ. Settle the policy, then update the FAQ and the cake page together."),
]

EX_TAKEAWAYS = [
    "The brief did the heavy lifting. The prompt needed nothing the brief did not already contain.",
    "The Fact Guard worked as designed: gaps became visible markers, not confident guesses.",
    "A human decision (which angle, which button) is still needed. The AI offers options; you choose.",
    "The review step found three real questions for the owner before a single word went live.",
]

# ------------------------------------------------------------------ CHECKLIST
CHECKLIST = {
    "heading": "Website-Copy Quality Checklist",
    "lead": "Run every page through this list before it goes to the client or goes live. "
            "Tick each item only when you have actually checked it.",
    "groups": [
        ("1  Facts & accuracy", [
            "Every number, name, date, price and address matches a source document.",
            "All [NEEDS INFO] and [CHECK] markers are resolved or removed.",
            "No invented testimonials, awards, statistics or client names.",
            "Contact details and opening hours are identical on every page.",
            "Claims in regulated areas have been checked by someone qualified.",
        ]),
        ("2  Clarity", [
            "A stranger can tell what the business does, and for whom, within five seconds.",
            "The headline says something specific, not “Welcome”.",
            "Sentences are short; most paragraphs are three lines or fewer.",
            "Jargon is removed or explained the first time it appears.",
            "Every section answers a question the visitor really has.",
        ]),
        ("3  Audience & voice", [
            "The copy speaks to one reader, using “you” more than “we”.",
            "The tone matches the agreed voice on every page.",
            "Spelling, terms and punctuation follow one style (UK or US, “clients” or “customers”).",
            "Phrases that could be on any competitor’s site are replaced with specifics.",
        ]),
        ("4  Conversion", [
            "Each page has one clear primary action.",
            "Button labels say what happens next, not “Submit”.",
            "Likely doubts (price, trust, time, effort) are answered before the call to action.",
            "Urgency or scarcity appears only where it is real.",
            "Contact is easy to find, and the form asks only for what is needed.",
        ]),
        ("5  Proof & trust", [
            "Proof is real, attributable and approved by the person quoted.",
            "Policies (refunds, revisions, cancellations) are stated plainly and match the contract.",
            "Credentials are worded exactly as the issuing body words them.",
        ]),
        ("6  Search & structure", [
            "One H1 per page, and headings read as an outline of the page.",
            "Title tag and meta description are unique, accurate and the right length.",
            "The main phrase appears naturally, not repeated for its own sake.",
            "Internal links use descriptive anchor text.",
            "Local pages contain genuinely local information, not swapped town names.",
        ]),
        ("7  Accessibility & readability", [
            "Images have useful alt text; decorative images have empty alt text.",
            "Link text makes sense on its own (no “click here”).",
            "Text can be read comfortably on a phone.",
            "Heading levels follow a logical order.",
        ]),
        ("8  Final sign-off", [
            "Copy has been read aloud once, start to finish.",
            "All links and forms have been tested.",
            "The client has approved the final text in writing.",
            "Sources for factual claims are saved in the project folder.",
        ]),
    ],
    "redflags_heading": "Red-flag phrases to search for",
    "redflags": [
        "welcome to", "world-class", "best in class", "cutting-edge", "one-stop shop", "solutions",
        "seamless", "unique", "passionate", "tailored", "leading provider", "guaranteed", "No. 1",
    ],
    "redflags_note": "Each of these is fine if you can back it up and say it concretely. If you cannot, change it.",
}

CLOSING = {
    "heading": "Thank You",
    "lead": "You now have a repeatable way to turn real facts into useful website copy.",
    "next_heading": "Your next three steps",
    "next": [
        ("Fill in the brief", "for your next project, or for your own business."),
        ("Run Prompt 1 or Prompt 11", "on a page you already have, and compare the draft with what is live."),
        ("Save your best versions", "as your own template library. The more verified facts you store, the faster every future project gets."),
    ],
    "closing_line": "Write from facts. Edit like a human. Check before you publish.",
}
