# DAVID PRADO
Title: Senior Full Stack Engineer
Contact: Canada | +1 (519) 872-5274 | davitprado@outlook.com | linkedin.com/in/davitprado | davitprado.com

## PROFESSIONAL SUMMARY
Senior Full Stack Engineer with 6+ years shipping products from idea to production with TypeScript, React and Node.js. I own delivery end to end, from refining requirements with users to architecture, data model, APIs, real-time services, frontend experiences and deployment pipelines, and I own the technical decisions: I document why each solution is chosen, define specs before writing code, and ensure quality with automated tests in CI. I use Claude Code and Codex daily, with specs and tests keeping the output reviewable. Security is part of the design: Row-Level Security, database-level immutability and hash-chained audit logs. Technical lead for the order module of a logistics platform processing 5,000+ shipments per day, where I made the architecture and data model decisions within a three-developer team.

## TECHNICAL SKILLS
**Core stack:** TypeScript, JavaScript, React, Node.js, NestJS, Next.js (SSR/SSG), PostgreSQL
**DevOps & cloud:** Docker, Kubernetes, CI/CD, Git, GitHub, Bitbucket, Vercel, Railway, Render, Linux VPS
**Architecture:** Modular monolith, offline-first (outbox pattern), monorepos (pnpm), immutable audit trails, Strategy pattern, ADRs
**Backend & data:** REST APIs, GraphQL, Express, Redis, BullMQ, pg-boss, Socket.IO, Prisma, Drizzle, Row-Level Security, MongoDB, Strapi
**Testing:** Jest, Cypress, integration testing
**AI-assisted development:** Claude Code, Codex, agentic coding workflows, spec-driven development
**Frontend:** Vite, React Query / TanStack, PWA, Service Workers (Serwist), IndexedDB (Dexie), Tailwind, HTML5, CSS, Sass, Axios, webpack
**AI & e-commerce:** Generative AI integration, fal.ai, vision models, dynamic prompting, Shopify (GraphQL APIs, headless, metaobjects and metafields)
**Quality & practices:** web performance (Lighthouse), WCAG, technical SEO, Agile/Scrum, Jira

## PROFESSIONAL EXPERIENCE

### Full-Stack Developer (Independent) | Mar 2024 – Present
Self-employed | Canada · Remote
Custom web systems and AI-powered products for small businesses and my own ventures, mostly replacing paper-based or manual workflows. Spec-driven delivery with AI coding agents (Claude Code, Codex) used daily: architecture decisions recorded as ADRs, specs before code, and integration tests in CI.

#### Offline Inspection System · Ontario Greenhouses, London, ON | Aug 2026 – Oct 2026
- Gathered requirements with Health & Safety and Human Resources to digitize inspections across two sites, and identified the lack of connectivity in the greenhouse as the reason the previous tool was abandoned.
- Defined the architecture and built, as the sole developer, an offline-first PWA for health & safety, maintenance, and electrical inspections, piloted with **~30 users**. It organizes work areas, assigns owners, and tracks each finding through to corrective action.
- Solved offline sync with the outbox pattern on IndexedDB and Service Workers. Built security into the data layer: database-level immutability, per-site Row-Level Security and hash-chained audit logs aligned with OHSA requirements.
- Documented the architecture in **12 ADRs** and applied spec-driven development (OpenSpec) with integration tests in CI and Docker-based deployment.
**Stack:** TypeScript · React · Vite · TanStack · NestJS · PostgreSQL · Drizzle · Dexie · Serwist · Docker

#### Claw & Soul · AI Pet Art E-commerce · Technical Co-Founder | Apr 2025 – Present
- Selected for the Fanshawe College Entrepreneurship & Innovation Program. Built end to end an e-commerce platform that turns pet photos into AI art and paint-by-numbers kits, shaping technical and product decisions with a business partner.
- Designed an asynchronous AI pipeline with BullMQ/Redis: photo analysis with vision models, dynamic prompting, and generation with fal.ai, with swappable art styles through the Strategy pattern.
- Integrated headless Shopify through its GraphQL APIs, modeling the product catalog, art styles and print formats with metaobjects and metafields.
**Stack:** Next.js · React · TypeScript · NestJS · PostgreSQL · BullMQ/Redis · fal.ai · Shopify · GraphQL

#### ClawPuzzle · AI personalization platform for Puzzle Salvaje, Ecuador | Aug 2026 – Oct 2026
- Built the technology for Puzzle Salvaje, a custom puzzle business with **5+ years** of operation and **thousands of units sold** in Ecuador, to launch a new line of AI-personalized wooden puzzles.
- Designed the personalization flow end to end: pet photo upload, style selection, and AI-generated artwork ready for production with themed pieces, connected to the Shopify store through its GraphQL API.
- Took ownership of an in-house generation engine and refactored it: redesigned the data model, removed **90+ obsolete files**, and merged two repositories into a monorepo while preserving Git history.
**Stack:** Next.js · React · TypeScript · NestJS · PostgreSQL · Prisma · fal.ai · Shopify · GraphQL

#### Meal Ordering System · Horizon Place care residence, London, ON | Mar 2024 – Aug 2024
- Identified the need to digitize paper meal orders while working in the residence's dietary department, then designed and built a full-stack web application with real-time updates over Socket.IO to replace them.
- Piloted the app with **60+ residents**, **14 tables**, and **two shifts**. Eliminated errors by displaying allergies, diets, and preferences in real time, saving **10–20 minutes per service**.
- Generated per-shift consumption logs and presented the solution to leadership, earning approval from the manager and the regional coordinator.
**Stack:** Next.js · React · Strapi · Socket.IO

### Frontend Software Engineer (Contract) | Nov 2024 – Feb 2025
Delphi (via Randstad) | Phoenix, AZ, USA · Remote from Canada
- Migrated pages and components from WordPress to Next.js with SSR and SSG, as part of a migration that raised Lighthouse Performance from **45 to 90**, along with technical SEO and accessibility improvements.
- Integrated REST APIs with Axios and React Query for the vehicle parts catalog and store locator, optimizing caching and reducing redundant requests.
- Wrote unit tests with Jest and E2E tests with Cypress to keep the migration stable within a distributed Agile/Scrum team.

### Senior Software Developer | Jan 2022 – Aug 2023
Kruger Corp | Quito, Ecuador
- Technical lead for the order tracking module of Urbano, a logistics platform processing **5,000+ daily shipments**: the full lifecycle from customer creation to routing, delivery, and payment collection, within a three-developer team.
- Made the architecture decisions and designed the data model for the order and payment flow, translating operations requirements into order, payment collection and cash-on-delivery reconciliation services with NestJS and PostgreSQL.
- Built React and Vite views for customers and internal operations (collections, delivery retries, per-order success rate), and ensured delivery quality through unit testing and production deployment support.

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
