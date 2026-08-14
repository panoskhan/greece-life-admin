# Greece Life Admin — Next-generation feature plan

This document defines the product direction for a genuinely useful, free, Greece-wide civic companion.

## 1. One search box for real-life problems

Users should be able to type normal language such as:

- «Θέλω να αλλάξω διεύθυνση»
- «Πού βρίσκω ΚΕΠ;»
- «Χρειάζομαι νοσοκομείο»
- «Είμαι αλλοδαπός και θέλω άδεια διαμονής»
- «Πώς βρίσκω δωρεάν νομική βοήθεια;»

The app should map the request to a category and then to an official source.

## 2. Life-event templates

Prebuilt journeys should turn a complex situation into a checklist:

- Μετακόμιση στην Ελλάδα
- Νέα εργασία
- Έναρξη επιχείρησης
- Γέννηση παιδιού
- Αλλαγή κατοικίας
- Αγορά/μεταβίβαση οχήματος
- Συνταξιοδότηση
- Σπουδές
- Αλλοδαπός που εγκαθίσταται στην Ελλάδα
- Απώλεια εγγράφων
- Ανάγκη κοινωνικής υποστήριξης

## 3. Location-aware directory

Support all 13 regions, municipalities, KEPs, hospitals, health facilities, police, courts, tax/insurance offices and other public bodies. Each record should have a source URL and a review date.

## 4. Trusted help hub

Separate information-only pathways for:

- δωρεάν νομική βοήθεια
- υγεία και πρόσβαση σε υπηρεσίες υγείας
- φάρμακα and official medicine safety information
- mental-health support
- disability services
- social support
- consumer rights
- employment support
- services for foreigners

The app must never present itself as a doctor, pharmacist or lawyer and must not diagnose, prescribe, or give personalised legal advice.

## 5. Emergency mode

A prominent emergency mode should provide verified official emergency information, including 112, without cluttering ordinary navigation.

## 6. Accessibility mode

Build to WCAG 2.1 AA principles: keyboard navigation, visible focus, semantic headings, readable contrast, reduced motion, large text, screen-reader labels and an easy-to-find accessibility statement.

## 7. Personal checklist

Allow users to create and complete a local-only checklist. No account should be required for the basic feature. Data should remain in the browser unless a future opt-in sync feature is explicitly introduced.

## 8. Saved places and services

Users can save frequently used services locally: a hospital, KEP, municipality, tax service, insurance office, or other official destination.

## 9. Source confidence and freshness

Every important entry should show:

- Official source
- Last reviewed date
- Service owner, where known
- Region/scope
- Whether the link is a direct service or an official directory

Do not publish a specific phone number, address, deadline, eligibility rule or requirement without verifying it from an authoritative source.

## 10. Offline-first shell

The core app shell, navigation and saved checklist should remain usable when connectivity is poor. Live official links obviously require a connection.

## 11. PWA / installable app

The project should become an installable Progressive Web App. The app should remain free and not require an app-store account for the web version.

## 12. Change alerts without surveillance

A future source-monitoring system can detect when a tracked official URL changes. Users should be able to opt into update notifications without sending their personal checklist to a server.

## 13. “Explain this” layer

For difficult administrative language, provide plain-language explanations that link back to the official source. Explanations must be clearly labelled as summaries, not official wording.

## 14. Accessibility and language helpers

Greek should be complete, with English as the first additional language. Later languages can be added based on genuine need. Avoid machine-translated legal or medical instructions unless clearly labelled and reviewed.

## 15. Community correction system

A user should be able to report:

- broken link
- outdated information
- wrong category
- accessibility problem
- missing service

Reports should create review work, not automatically change official information.

## 16. Open data and transparency

Where lawful and technically appropriate, use public/open government datasets and APIs. Always preserve attribution and source provenance. Never scrape private or access-controlled systems.

## 17. “What changed?”

A small changelog can show newly verified services, removed links and recently reviewed categories. This creates trust and gives maintainers a clear update workflow.

## 18. No fake government identity

The app must always state that it is an independent open-source project. Official government logos, seals or branding should not be used in a way that implies government ownership or endorsement.
