# DAVID PRADO
Title: Senior Software Engineer
Contact: London, ON | +1 (519) 872-5274 | davitprado@outlook.com | linkedin.com/in/davitprado | davitprado.com

## PROFESSIONAL SUMMARY
Senior Software Engineer with 6+ years building and supporting production web applications. I’ve worked on the systems behind orders and payments: as technical lead for the order module of a logistics platform processing 5,000+ shipments per day, I designed the data model and built order, payment collection and cash-on-delivery reconciliation services with NestJS and PostgreSQL. I work across the stack with Node.js, TypeScript, React and Next.js, and I own the technical decisions: I document why each solution is chosen, define specs before writing code, and test with Jest, Cypress and integration tests in CI. I use Claude Code and Codex daily, with specs and tests keeping the output reviewable. Recent work includes headless Shopify e-commerce with asynchronous AI pipelines and offline-first apps that replaced paper workflows.

## TECHNICAL SKILLS
**Core stack:** Node.js, NestJS, TypeScript, JavaScript, React, Next.js (SSR/SSG), PostgreSQL
**Backend & data:** REST APIs, GraphQL, Express, Prisma, Drizzle, Redis, BullMQ, pg-boss, Socket.IO, MongoDB, Strapi, Row-Level Security
**Frontend:** React Query / TanStack, Vite, Tailwind, PWA, Service Workers (Serwist), IndexedDB (Dexie), HTML5, CSS, Sass, Axios, webpack
**Testing:** Jest, Cypress, integration testing
**E-commerce & AI:** Shopify (GraphQL APIs, headless, metaobjects and metafields), generative AI integration, fal.ai, vision models, dynamic prompting
**AI-assisted development:** Claude Code, Codex, agentic coding workflows, spec-driven development
**Architecture:** Modular monolith, monorepos (pnpm), offline-first (outbox), immutable audit trails, Strategy pattern
**DevOps & cloud:** Docker, Kubernetes, CI/CD, Git, GitHub, Bitbucket, Vercel, Railway, Render, Linux VPS
**Quality & practices:** Agile/Scrum, ADRs, web performance (Lighthouse), technical SEO, WCAG, Jira

## PROFESSIONAL EXPERIENCE

### Full-Stack Developer (Independent) | Mar 2024 – Present
Self-employed | London, ON · Remote
Custom web systems and AI-powered products for small businesses and my own ventures, mostly replacing paper-based or manual workflows. Spec-driven delivery with AI coding agents (Claude Code, Codex) used daily: architecture decisions recorded as ADRs, specs before code, and integration tests in CI.

#### Claw & Soul · AI Pet Art E-commerce, Technical Co-Founder | Apr 2025 – Present
- Selected for the Fanshawe College Entrepreneurship & Innovation Program. Built end to end an e-commerce platform that turns pet photos into AI art and paint-by-numbers kits, and shaped technical and product decisions with a business partner.
- Integrated headless Shopify through its GraphQL APIs, modeling the product catalog, art styles and print formats with metaobjects and metafields.
- Designed an asynchronous AI pipeline with BullMQ/Redis: photo analysis with vision models, dynamic prompting, and generation with fal.ai. Implemented swappable art styles using the Strategy pattern.
- Created an in-browser paint-by-numbers generator: color reduction, segmentation, and SVG/PDF export, with a free preview at zero server cost.
**Stack:** Next.js · React · TypeScript · NestJS · PostgreSQL · BullMQ/Redis · fal.ai · Shopify · GraphQL

#### ClawPuzzle · AI personalization platform for Puzzle Salvaje, Ecuador | Aug 2026 – Oct 2026
- Built the technology for Puzzle Salvaje, a custom puzzle business with **5+ years** of operation and **thousands of units sold** in Ecuador, to launch a new line of AI-personalized wooden puzzles.
- Designed the personalization flow: pet photo upload, style selection, and AI-generated artwork ready for production with themed pieces, connected to the Shopify store through its GraphQL API.
- Adapted an in-house generation engine: redesigned the data model, removed **90+ obsolete files**, and merged two repositories into a monorepo while preserving Git history.
**Stack:** Next.js · React · TypeScript · NestJS · PostgreSQL · Prisma · fal.ai · Shopify · GraphQL

#### Offline Inspection System · Ontario Greenhouses, London, ON | Aug 2026 – Oct 2026
- Gathered requirements with Health & Safety and Human Resources to digitize inspections across two sites. Identified the lack of connectivity in the greenhouse as the reason the previous tool was abandoned.
- Designed and built, as the sole developer, an offline-first PWA for health & safety, maintenance, and electrical inspections, piloted with **~30 users**. It organizes work areas, assigns owners, and tracks each finding through to corrective action.
- Solved offline sync with an outbox on IndexedDB and Service Workers. Added database-level immutability, per-site Row-Level Security, and hash-chained audit logs aligned with OHSA requirements.
- Documented the architecture in **12 ADRs** and applied spec-driven development (OpenSpec) with integration tests in CI.
**Stack:** TypeScript · React · TanStack · NestJS · PostgreSQL · Drizzle · pg-boss · Dexie · Docker

#### Meal Ordering System · Horizon Place care residence, London, ON | Mar 2024 – Aug 2024
- Identified the need to digitize paper meal orders while working in the residence's dietary department, then designed and built a full-stack web application to replace them.
- Piloted the app with **60+ residents**, **14 tables**, and **two shifts**. Eliminated errors by displaying allergies, diets, and preferences in real time, saving **10–20 minutes per service**.
- Generated per-shift consumption logs and presented the solution to leadership, earning approval from the manager and the regional coordinator.
**Stack:** Next.js · React · Strapi · Socket.IO

### Frontend Software Engineer (Contract) | Nov 2024 – Feb 2025
Delphi (via Randstad) | Phoenix, AZ, USA · Remote from London, ON
- Migrated pages and components from WordPress to Next.js with SSR and SSG, as part of a migration that raised Lighthouse Performance from **45 to 90**, along with technical SEO and accessibility improvements.
- Integrated REST APIs with Axios and React Query for the vehicle parts catalog and store locator, managing client-side server state and caching to cut redundant requests.
- Wrote unit tests with Jest and E2E tests with Cypress to keep the migration stable within a distributed Agile/Scrum team.

### Senior Software Developer | Jan 2022 – Aug 2023
Kruger Corp | Quito, Ecuador
- Technical lead for the order tracking module of Urbano, a logistics platform processing **5,000+ daily shipments**: the full order lifecycle from customer creation to routing, delivery, and payment collection, within a three-developer team.
- Developed order, payment collection, and cash-on-delivery reconciliation services with NestJS and PostgreSQL, plus React and Vite views for customers and internal operations: collections, delivery retries, and per-order success rate.
- Made architecture decisions and designed the data model for the order and payment flow. Ensured delivery quality through unit testing and supported production deployments.

### Software Developer | Jan 2020 – Oct 2021
Idukay | Quito, Ecuador
- Integrated a professional training platform (MERN) with the web services of the SRI, Ecuador's tax authority, for electronic invoicing: XML invoice generation, status and error handling, and automatic delivery to users, processing **60–70 invoices per month**.
- Built the reporting module end to end, with backend and React frontend, for **~50 students and 8 courses**: progress, grades, and pass rates per course for instructors and administrators, plus a progress map for students. Tested critical logic with Jest.

## EDUCATION

### Entrepreneurship & Innovation Program and LeapIN Business Accelerator | Apr 2025 – Aug 2025
Fanshawe College | London, ON, Canada
- Developed a startup project from concept to prototype with mentorship from industry experts.

### Diploma, Internet Applications and Web Development | Sep 2023 – Apr 2025
Fanshawe College | London, ON, Canada

### Full Stack Developer with JavaScript · React Front-end Developer | 2019 – 2023
Platzi | Online

## LANGUAGES
**Spanish:** Native · **English:** Professional
