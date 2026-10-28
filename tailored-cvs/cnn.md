# DAVID PRADO
Title: Full-Stack Software Developer
Contact: London, ON | +1 (519) 872-5274 | davitprado@outlook.com | linkedin.com/in/davitprado | davitprado.com

## PROFESSIONAL SUMMARY
Full-Stack Software Developer with 6+ years of experience, almost 4 of them on company teams. For the last 2, I’ve worked independently: I talk to the users, make the technical decisions and ship to production myself. I design, implement, test and deploy web applications with modern JavaScript, TypeScript, Node.js, Express, NestJS, React and Next.js, Postgres and Redis, on AWS with Docker, Jenkins and Git. I’ve built mission-critical production systems for essential operations, including technical lead for the order module of a logistics platform processing 5,000+ shipments per day. I bring e-commerce, affiliate program and consumer-facing web experience, and I monitor code health, infrastructure health and application performance with Datadog, Sentry and CloudWatch. I write about AI-assisted development and architecture on LinkedIn a couple of times a month.

## TECHNICAL SKILLS
**Core stack:** JavaScript, TypeScript, Node.js, Express, React, Next.js (SSR/SSG), NestJS, PostgreSQL, Redis
**Cloud & DevOps:** AWS (EC2, S3, Lambda, API Gateway, CloudFront, CloudWatch), AWS SAM (CloudFormation), Serverless, Docker, Jenkins, GitHub Actions, Bitbucket Pipelines, Git, CI/CD, Linux
**Monitoring & code health:** Datadog, Sentry, CloudWatch, Elasticsearch / Kibana (log analysis), SonarQube, test coverage gates, health checks and alerting
**CDN & performance:** CDN and edge caching (CloudFront, Cloudflare), Cache-Control, web performance (Lighthouse), technical SEO
**Backend & data:** REST APIs, GraphQL, PostgreSQL full-text search, Prisma, Drizzle, MongoDB, BullMQ, pg-boss, Socket.IO, Strapi, Row-Level Security
**Frontend:** React Query / TanStack, Vite, PWA, Service Workers, IndexedDB, Tailwind, HTML5, CSS, Sass, Angular (coursework), WCAG
**E-commerce & AI:** Shopify (headless, GraphQL APIs, metaobjects, metafields), affiliate programs, conversion tracking, generative AI (fal.ai, vision models)
**Practices:** Functional-style programming (immutability, pure functions, RxJS, fp-ts), object-oriented JavaScript, Agile (Scrum, Kanban), ADRs, spec-driven development, Jira, Jest, Cypress, integration testing
**AI-assisted development:** Claude Code, Codex, agentic coding workflows

## PROFESSIONAL EXPERIENCE

### Full-Stack Developer (Independent) | Mar 2024 – Present
Self-employed | London, ON · Remote
Custom web systems and AI-powered products for small businesses and my own ventures, mostly replacing paper-based or manual workflows. Spec-driven delivery with AI coding agents (Claude Code, Codex) used daily: architecture decisions recorded as ADRs, specs before code, and integration tests in CI.

#### Claw & Soul · AI Pet Art E-commerce · Technical Co-Founder | Apr 2025 – Present
- Selected for the Fanshawe College Entrepreneurship & Innovation Program. Built end to end a consumer e-commerce site that turns pet photos into AI art and paint-by-numbers kits, with a business partner.
- Designed an asynchronous AI pipeline with BullMQ/Redis: photo analysis with vision models, dynamic prompting, and generation with fal.ai. Implemented swappable art styles using the Strategy pattern.
- Built serverless functions on AWS Lambda and API Gateway, deployed with AWS SAM (CloudFormation), for Shopify webhooks, image processing, fal.ai calls and S3 presigned uploads, served through CloudFront.
- Integrated headless Shopify through its GraphQL APIs, modeling the catalog, art styles and print formats with metaobjects and metafields. Built an affiliate program with referral links and commission tracking, plus conversion tracking.
- Monitored the platform with Sentry, health checks and alerts on the job queues, and added Postgres full-text search.
**Stack:** Next.js · React · TypeScript · NestJS · PostgreSQL · BullMQ/Redis · AWS (Lambda, API Gateway, S3, CloudFront, SAM) · fal.ai · Shopify · GraphQL

#### ClawPuzzle · AI personalization platform for Puzzle Salvaje, Ecuador | Aug 2026 – Oct 2026
- Built the technology for Puzzle Salvaje, a custom puzzle business with **5+ years** of operation and **thousands of units sold** in Ecuador, to launch a new line of AI-personalized wooden puzzles.
- Designed the personalization flow: pet photo upload to S3 with presigned URLs, style selection, and AI-generated artwork ready for production with themed pieces, connected to the Shopify store through its GraphQL API, with affiliate referral links.
**Stack:** Next.js · React · TypeScript · NestJS · PostgreSQL · Prisma · AWS S3 · fal.ai · Shopify · GraphQL

#### Offline Inspection System · Ontario Greenhouses, London, ON | Aug 2026 – Oct 2026
- Gathered requirements with Health & Safety and HR, then designed and built, as the sole developer, an offline-first PWA for health & safety, maintenance, and electrical inspections, piloted with **~30 users**. It organizes work areas, assigns owners, and tracks each finding through to corrective action.
- Solved offline sync with the outbox pattern on IndexedDB and Service Workers. Implemented database-level immutability, per-site Row-Level Security, and hash-chained audit logs for OHSA.
- Documented the architecture in **12 ADRs**, applied spec-driven development (OpenSpec) with integration tests in CI, and added Sentry, health checks and alerts on the sync and job queues, plus Postgres full-text search across findings.
**Stack:** TypeScript · React · Vite · TanStack · NestJS · PostgreSQL · Drizzle · pg-boss · Dexie · Serwist · Sentry · Docker

### Frontend Software Engineer (Contract) | Nov 2024 – Feb 2025
Delphi (via Randstad) | Phoenix, AZ, USA · Remote from London, ON
- Migrated pages and components from WordPress to Next.js with SSR and SSG, as part of a migration that raised Lighthouse Performance from **45 to 90**, along with technical SEO and accessibility improvements.
- Configured CDN caching with Cache-Control headers for pages, images and static assets, and implemented conversion tracking on the consumer-facing parts catalog and store locator.
- Integrated REST APIs with Axios and React Query, optimizing caching and reducing redundant requests.
- Wrote unit tests with Jest and E2E tests with Cypress to ensure migration stability within a distributed Agile/Scrum team.

### Senior Software Developer | Jan 2022 – Aug 2023
Kruger Corp | Quito, Ecuador
- Technical lead for the order tracking module of Urbano, a mission-critical logistics platform processing **5,000+ daily shipments**: the full lifecycle from customer creation to routing, delivery, and payment collection, within a three-developer team.
- Developed order, payment collection, and cash-on-delivery reconciliation services with Node.js, NestJS and PostgreSQL on AWS (EC2, S3), shipped through Jenkins pipelines, plus React and Vite views for customers and internal operations: collections, delivery retries, and per-order success rate.
- Monitored code health, infrastructure health and application performance with Datadog, Sentry, CloudWatch and Kibana (Elasticsearch), with health checks and alerts, and enforced SonarQube and test coverage gates in CI.
- Made architecture decisions and designed the data model for the order and payment flow, working in Scrum and Kanban. Ensured delivery quality through unit testing and production deployment support.

### Software Developer | Jan 2020 – Oct 2021
Idukay | Quito, Ecuador
- Integrated a professional training platform built on MERN (MongoDB, Express, React, Node.js) with the web services of the SRI, Ecuador's tax authority, for electronic invoicing: XML invoice generation, status and error handling, and automatic delivery to users, processing **60–70 invoices per month**.
- Built the reporting module end to end, with backend and React frontend, for **~50 students and 8 courses**: progress, grades and pass rates per course, plus a progress map for students. Tested critical logic with Jest.

## EDUCATION

### Entrepreneurship & Innovation Program and LeapIN Business Accelerator | Apr 2025 – Aug 2025
Fanshawe College | London, ON, Canada

### Diploma, Internet Applications and Web Development | Sep 2023 – Apr 2025
Fanshawe College | London, ON, Canada

### Full Stack Developer with JavaScript · React Front-end Developer | 2019 – 2023
Platzi | Online

## LANGUAGES
**Spanish:** Native · **English:** Professional
