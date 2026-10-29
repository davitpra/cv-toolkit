# DAVID PRADO
Title: Senior Full Stack Engineer
Contact: London, ON | +1 (519) 872-5274 | davitprado@outlook.com | linkedin.com/in/davitprado | davitprado.com

## PROFESSIONAL SUMMARY
Senior Full Stack Engineer with 6+ years of experience, almost 4 of them on company teams. For the last 2, I’ve worked independently: I talk to the users, make the technical decisions and ship to production myself. I build with React, Node.js, Express, NestJS and TypeScript on top of PostgreSQL and REST APIs, and I own the road to production: Docker, Kubernetes on Microsoft Azure (AKS), CI/CD with GitHub Actions, Nginx on Linux servers, and monitoring with Datadog and Sentry. I document why each solution is chosen, define specs before writing code, and ensure quality with automated tests. Technical lead for the order module of a logistics platform processing 5,000+ shipments per day.

## TECHNICAL SKILLS
**Core stack:** TypeScript, JavaScript, React, Node.js, Express, NestJS, PostgreSQL, REST APIs, Next.js
**Cloud & DevOps:** Microsoft Azure, AKS, Docker, Kubernetes, CI/CD, GitHub Actions, Git, GitHub, Nginx, Linux VPS, Vercel
**Monitoring & production:** Datadog, Sentry, production deployment support
**Backend & data:** Row-Level Security, GraphQL, Prisma, Drizzle, MongoDB, Redis, BullMQ, pg-boss, Socket.IO
**Frontend:** Vite, React Query / TanStack, PWA, Service Workers, IndexedDB, Tailwind, Axios
**Architecture:** Strategy pattern, offline-first (outbox pattern), modular monolith, monorepos, immutable audit trails
**AI-assisted development:** Claude Code, Codex, agentic coding workflows, spec-driven development
**Testing & practices:** Jest, Cypress, integration testing, Agile/Scrum, ADRs, Jira

## PROFESSIONAL EXPERIENCE

### Full-Stack Developer (Independent) | Mar 2024 – Present
Self-employed | London, ON · Remote
Custom web systems and AI-powered products for small businesses and my own ventures, mostly replacing paper-based or manual workflows, self-hosted on Linux VPS with Docker and Nginx. Spec-driven delivery with AI coding agents (Claude Code, Codex) used daily: architecture decisions recorded as ADRs, specs before code, and integration tests in CI.

#### Offline Inspection System · Ontario Greenhouses, London, ON | Aug 2026 – Oct 2026
- Gathered requirements with Health & Safety and Human Resources to digitize inspections across two sites. Identified the lack of connectivity in the greenhouse as the reason the previous tool was abandoned.
- Designed and built, as the sole developer, an offline-first PWA with a NestJS and PostgreSQL backend for health & safety, maintenance, and electrical inspections, piloted with **~30 users**. It organizes work areas, assigns owners, and tracks each finding through to corrective action.
- Solved offline sync with the outbox pattern on IndexedDB and Service Workers. Secured data with database-level immutability, per-site Row-Level Security, and hash-chained audit logs for OHSA.
- Documented the architecture in **12 ADRs**, applied spec-driven development (OpenSpec) and ran integration tests in CI; the system runs in Docker containers.
**Stack:** TypeScript · React · Vite · NestJS · PostgreSQL · Drizzle · pg-boss · Dexie · Serwist · Docker

#### Claw & Soul · AI Pet Art E-commerce, Technical Co-Founder | Apr 2025 – Present
- Selected for the Fanshawe College Entrepreneurship & Innovation Program. Built end to end an e-commerce platform that turns pet photos into AI art and paint-by-numbers kits, and shaped technical and product decisions with a business partner.
- Designed an asynchronous AI pipeline on Node.js with BullMQ/Redis: photo analysis with vision models, dynamic prompting, and generation with fal.ai. Swappable art styles use the Strategy pattern.
- Integrated headless Shopify through its GraphQL APIs, modeling the product catalog, art styles and print formats with metaobjects and metafields.
**Stack:** Next.js · React · TypeScript · NestJS · PostgreSQL · BullMQ/Redis · fal.ai · Shopify · GraphQL

#### ClawPuzzle · AI personalization platform for Puzzle Salvaje, Ecuador | Aug 2026 – Oct 2026
- Built the technology for Puzzle Salvaje, a custom puzzle business with **5+ years** of operation and **thousands of units sold** in Ecuador, to launch a new line of AI-personalized wooden puzzles.
- Designed the personalization flow: pet photo upload, style selection, and AI-generated artwork ready for production with themed pieces, connected to the Shopify store through its GraphQL API.**Stack:** Next.js · React · TypeScript · NestJS · PostgreSQL · Prisma · fal.ai · Shopify · GraphQL

### Frontend Software Engineer (Contract) | Nov 2024 – Feb 2025
Delphi (via Randstad) | Phoenix, AZ, USA · Remote from London, ON
- Migrated pages and components from WordPress to Next.js with SSR and SSG, as part of a migration that raised Lighthouse Performance from **45 to 90**, along with technical SEO and accessibility improvements.
- Integrated REST APIs with Axios and React Query for the vehicle parts catalog and store locator, optimizing caching and reducing redundant requests.
- Wrote unit tests with Jest and E2E tests with Cypress to ensure migration stability within a distributed Agile/Scrum team.

### Senior Software Developer | Jan 2022 – Aug 2023
Kruger Corp | Quito, Ecuador
- Technical lead for the order tracking module of Urbano, a logistics platform processing **5,000+ daily shipments**: the full lifecycle from customer creation to routing, delivery, and payment collection, within a three-developer team.
- Developed order, payment collection, and cash-on-delivery reconciliation services with Node.js, NestJS and PostgreSQL behind REST APIs, plus React and Vite views for customers and internal operations: collections, delivery retries, and per-order success rate.
- Deployed the services on Microsoft Azure with Docker and Kubernetes (AKS), and monitored them in production with Datadog and Sentry.
- Made architecture decisions and designed the data model for the order and payment flow. Ensured delivery quality through unit testing and production deployment support.

### Software Developer | Jan 2020 – Oct 2021
Idukay | Quito, Ecuador
- Integrated a professional training platform (MERN: MongoDB, Express, React, Node.js) with the web services of the SRI, Ecuador's tax authority, for electronic invoicing: XML invoice generation, status and error handling, and automatic delivery to users, processing **60–70 invoices per month**.
- Built the reporting module end to end, with an Express backend and React frontend, for **~50 students and 8 courses**: progress, grades, and pass rates per course for instructors and administrators, plus a progress map for students. Tested critical logic with Jest.

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
