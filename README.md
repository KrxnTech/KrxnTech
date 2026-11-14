<a id="top"></a>
<div align="center">

<img src="assets/hero.svg" width="100%" alt="Krishna - Software Developer. Backend Developer, MERN Stack, AI Enthusiast">

<a href="#about"><img src="assets/start.svg" height="64" alt="Start"></a>

<br>

<a href="#about"><img src="assets/nav/nav-about.svg" height="36" alt="About"></a>
<a href="#expertise"><img src="assets/nav/nav-expertise.svg" height="36" alt="Expertise"></a>
<a href="#projects"><img src="assets/nav/nav-projects.svg" height="36" alt="Projects"></a>
<a href="#building"><img src="assets/nav/nav-building.svg" height="36" alt="Currently building"></a>
<a href="#toolbox"><img src="assets/nav/nav-toolbox.svg" height="36" alt="Toolbox"></a>
<a href="#journey"><img src="assets/nav/nav-journey.svg" height="36" alt="Journey"></a>
<a href="#contact"><img src="assets/nav/nav-contact.svg" height="36" alt="Contact"></a>

<br><br>

**Backend Developer & Full-Stack Engineer specializing in scalable APIs, databases, and AI-powered systems.**
<br>
Ahmedabad–Gandhinagar, Gujarat, India &nbsp;·&nbsp; B.Tech CSE (Gandhinagar University) &nbsp;·&nbsp; Node.js · Express · Python · MongoDB · AI/VLMs

</div>

<img src="assets/divider.svg" width="100%" alt="">

<!-- ======================= PAGE 02 · ABOUT ======================= -->
<a id="about"></a>
<h2 align="center"><img src="assets/header-about.svg" width="100%" alt="Introduction: About Me"></h2>

<table>
<tr>
<td width="42%" valign="middle" align="center">
<img src="assets/about-photo.svg" width="100%" alt="Krishna Sharma - Profile">
</td>
<td width="58%" valign="middle">

Hi, I'm **Krishna Sharma**, a Software Developer with a backend-focused approach, experienced in building scalable and reliable web applications.

I specialize in designing RESTful APIs, developing robust server-side systems, working with databases (MongoDB, PostgreSQL, SQL), and integrating frontend and backend components to deliver complete, end-to-end applications.

Currently pursuing my **B.Tech in Computer Science and Engineering at Gandhinagar University** (CGPA: **9.65 / 10**), my core engineering focus centers on clean system architecture, secure authentication patterns, microservice data pipelines, and intelligent AI integrations — ranging from local LLM inference via Ollama to high-throughput cloud model orchestration and multimodal vision-language platforms.

> 🎓 **B.Tech CSE @ Gandhinagar University** (CGPA: 9.65 / 10 &nbsp;·&nbsp; 2024 – 2028)  
> 🛠️ **Backend Systems, RESTful APIs, Database Design & AI Orchestration**  
> 📍 **Ahmedabad–Gandhinagar, Gujarat, India** &nbsp;·&nbsp; 🌐 [krxna-tech.vercel.app](https://krxna-tech.vercel.app)

</td>
</tr>
</table>

<img src="assets/divider.svg" width="100%" alt="">

<!-- ======================= PAGE 03 · EXPERTISE ======================= -->
<a id="expertise"></a>
<h2 align="center"><img src="assets/header-expertise.svg" width="100%" alt="Core Expertise"></h2>

- **Backend Architecture & RESTful APIs.** Building scalable, production-ready server-side applications using Node.js, Express.js, and Python (FastAPI / Flask). Implementing secure JWT authentication in HTTP-only cookies, Bcrypt password hashing, structured JSON pipelines, and Role-Based Access Control (RBAC).
- **Full-Stack & Database Engineering.** Developing complete web applications with React, Vite, and Tailwind CSS. Designing relational and NoSQL schemas, indexes, and aggregation pipelines across MongoDB (Mongoose), PostgreSQL, and SQL databases.
- **AI Integration & Model Orchestration.** Architecting practical AI workflows combining local LLM inference (Ollama), cloud model acceleration (Groq API, Llama, Qwen), Vision-Language Models (VLMs), speech transcription (OpenAI Whisper), audio extraction (FFmpeg), and geospatial analysis (Rasterio).

<img src="assets/divider.svg" width="100%" alt="">

<!-- ======================= PAGE 04 · FEATURED PROJECTS ======================= -->
<a id="projects"></a>

<!-- PROJECT 01: SATVISTAAR -->
<h2 align="center"><img src="assets/header-project-1.svg" width="100%" alt="Featured Project 01: SatVistaar"></h2>

<table>
<tr>
<td width="52%" valign="top">

### SatVistaar: Autonomous Vision-Language Platform for Remote-Sensing Intelligence
*Smart India Hackathon (SIH) 2026 Project*

**The problem.** Satellite and Earth-observation data (GeoTIFF, multi-spectral, SAR) is dense and requires specialized GIS software and domain expertise. Analyzing geographic patterns, land-use shifts, and ground features programmatically through natural language has traditionally been inaccessible.

**The solution.** SatVistaar is an agentic geospatial platform that enables natural-language queries directly over satellite imagery using multimodal vision-language reasoning.

**Architecture & Key Capabilities**
- **4 Multimodal Modes:** Visual Question Answering (VQA), pixel-level feature grounding, automated scene description, and bi-temporal change detection across multi-date satellite passes.
- **Provider-Agnostic Model Router:** Engineered a model router with deterministic fallback between cloud Groq VLMs (Qwen/Llama) and a local Ollama VLM instance for latency optimization and offline resilience.
- **Geospatial Microservice:** Python/Flask microservice utilizing Rasterio to ingest GeoTIFF imagery and extract Coordinate Reference System (CRS) data, bounding boxes, and band metadata.
- **Production Security & Test Coverage:** Protected with HTTP-only cookie JWT auth and Bcrypt hashing; backed by a regression test suite achieving 21/21 auth tests and 28/30 pipeline tests passing.

<img src="assets/chips/chip-react.svg" height="28" alt="React">
<img src="assets/chips/chip-node-js.svg" height="28" alt="Node.js">
<img src="assets/chips/chip-express-js.svg" height="28" alt="Express.js">
<img src="assets/chips/chip-python.svg" height="28" alt="Python">
<img src="assets/chips/chip-flask.svg" height="28" alt="Flask">
<img src="assets/chips/chip-groq-vlm.svg" height="28" alt="Groq VLM">
<img src="assets/chips/chip-ollama.svg" height="28" alt="Ollama">
<img src="assets/chips/chip-rasterio.svg" height="28" alt="Rasterio">
<img src="assets/chips/chip-jwt.svg" height="28" alt="JWT">

<br>

**[📁 GitHub Repo](https://github.com/KrxnTech/SatVistaar-SIH)** &nbsp;·&nbsp; **[🌐 Live Demo](https://sat-vistaar.vercel.app)**

</td>
<td width="48%" valign="middle" align="center">
<img src="assets/satvistaar-preview.svg" width="100%" alt="SatVistaar preview in a retro computer window">
</td>
</tr>
</table>

<br>

<!-- PROJECT 02: RESUME BUDDY -->
<h2 align="center"><img src="assets/header-project-2.svg" width="100%" alt="Featured Project 02: Resume Buddy"></h2>

<table>
<tr>
<td width="48%" valign="middle" align="center">
<img src="assets/resume-buddy-preview.svg" width="100%" alt="Resume Buddy preview in a retro computer window">
</td>
<td width="52%" valign="top">

### Resume Buddy: AI Resume & Career Intelligence Platform

**The problem.** Traditional Applicant Tracking Systems (ATS) and job search tools rely on rigid keyword matching, frequently missing qualified candidates and offering no actionable guidance to improve resume impact.

**The solution.** Resume Buddy is an AI career-intelligence platform that parses resume PDFs and evaluates them against target job descriptions using contextual LLM analysis rather than naive keyword matching.

**Architecture & Key Capabilities**
- **Structured Parsing Pipeline:** Uses Multer and `pdf-parse` to convert unstructured PDF resumes into structured JSON schemas for deep inspection.
- **Dual Scoring Engine:** Links parsed data to a dual ATS-compatibility and recruiter-evaluation scoring engine:
  - *ATS Score:* Evaluates machine readability, formatting compliance, and section structure.
  - *Recruiter Score:* Evaluates quantifiable impact, project depth, and role alignment.
- **Skill Gap Analysis:** Pinpoints missing technical proficiencies and domain competencies with targeted recommendations.
- **AI Rewrite Studio:** Section-level resume rewrite engine that helps candidates rewrite bullet points with quantifiable impact and industry-standard phrasing.

<img src="assets/chips/chip-react.svg" height="28" alt="React">
<img src="assets/chips/chip-vite.svg" height="28" alt="Vite">
<img src="assets/chips/chip-node-js.svg" height="28" alt="Node.js">
<img src="assets/chips/chip-express-js.svg" height="28" alt="Express.js">
<img src="assets/chips/chip-mongodb.svg" height="28" alt="MongoDB">
<img src="assets/chips/chip-groq-api.svg" height="28" alt="Groq API">
<img src="assets/chips/chip-multer.svg" height="28" alt="Multer">

<br>

**[📁 GitHub Repo](https://github.com/KrxnTech/Resume-Buddy)** &nbsp;·&nbsp; **[🌐 Live Demo](https://resume-buddy-green.vercel.app)**

</td>
</tr>
</table>

<br>

<!-- PROJECT 03: CONTENTHUB -->
<h2 align="center"><img src="assets/header-project-3.svg" width="100%" alt="Featured Project 03: ContentHub"></h2>

<table>
<tr>
<td width="52%" valign="top">

### ContentHub: AI Video-to-Shorts Platform

**The problem.** Manually extracting engaging moments from 4–5 minute long-form videos, resizing them for vertical formats, and creating subtitles for social media repurposing is tedious and time-consuming.

**The solution.** ContentHub is a microservices platform that automatically ingests long-form videos and converts them into multiple high-engagement short-form vertical clips for social media.

**Architecture & Key Capabilities**
- **Audio Extraction & Timed Transcription:** Python/FastAPI microservice extracts audio tracks via FFmpeg and runs transcription with OpenAI Whisper to generate timestamped text tokens.
- **Engagement Hook Analysis:** Groq-accelerated Llama 3 models analyze transcript pacing and sentiment to detect high-retention moments and highlight clips.
- **Automated Clipping & Metadata:** Programmatically crops and slices vertical clips, generates synchronized subtitles, and auto-generates titles, descriptions, and hashtags.
- **Cloudinary Storage Sync:** Automatically syncs processed video assets and clips to Cloudinary for media management and fast CDN delivery.

<img src="assets/chips/chip-react.svg" height="28" alt="React">
<img src="assets/chips/chip-vite.svg" height="28" alt="Vite">
<img src="assets/chips/chip-node-js.svg" height="28" alt="Node.js">
<img src="assets/chips/chip-express-js.svg" height="28" alt="Express.js">
<img src="assets/chips/chip-mongodb.svg" height="28" alt="MongoDB">
<img src="assets/chips/chip-python.svg" height="28" alt="Python">
<img src="assets/chips/chip-fastapi.svg" height="28" alt="FastAPI">
<img src="assets/chips/chip-whisper.svg" height="28" alt="Whisper">
<img src="assets/chips/chip-groq-api.svg" height="28" alt="Groq API">
<img src="assets/chips/chip-ffmpeg.svg" height="28" alt="FFmpeg">
<img src="assets/chips/chip-cloudinary.svg" height="28" alt="Cloudinary">

<br>

**[📁 GitHub Repo](https://github.com/KrxnTech/ContentHub)**

</td>
<td width="48%" valign="middle" align="center">
<img src="assets/contenthub-preview.svg" width="100%" alt="ContentHub preview in a retro computer window">
</td>
</tr>
</table>

<br>

### 🚀 Additional Projects

| Project | Description | Stack | Links |
|:---|:---|:---|:---:|
| **EduEase** | AI-based educational platform helping teachers streamline lesson planning and content creation using locally-hosted LLM inference and tailored prompt engineering. | React, Vite, Express, Node.js, MongoDB, Ollama API | [📁 GitHub](https://github.com/KrxnTech/EduEase) |
| **Dhoon** | Responsive web music player built with React and Tailwind CSS, focused on smooth audio playback, custom controls, and polished modern UI/UX. | React, Vite, Tailwind CSS, JavaScript | [📁 GitHub](https://github.com/KrxnTech/Dhoooon) &nbsp;·&nbsp; [🌐 Demo](https://dhoooon.vercel.app/) |
| **Production-Backend** | Scalable YouTube-like backend architecture featuring JWT authentication, Role-Based Access Control, MongoDB indexing, and Cloudinary media handling. | Node.js, Express.js, MongoDB, JWT, Cloudinary | [📁 GitHub](https://github.com/KrxnTech/Production-Backend) |

<img src="assets/divider.svg" width="100%" alt="">

<!-- ======================= PAGE 05 · CURRENTLY BUILDING ======================= -->
<a id="building"></a>
<h2 align="center"><img src="assets/header-current.svg" width="100%" alt="Currently Building / Exploring"></h2>

<table>
<tr>
<td width="33%" valign="top" align="center">
<img src="assets/nums/num-01.svg" height="80" alt="01"><br>
<b>SatVistaar SIH 2026</b><br>
Scaling geospatial VLM routing and multi-spectral change detection.
</td>
<td width="33%" valign="top" align="center">
<img src="assets/nums/num-02.svg" height="80" alt="02"><br>
<b>Docker & Microservices</b><br>
Containerizing full-stack microservices for reproducible production builds.
</td>
<td width="33%" valign="top" align="center">
<img src="assets/nums/num-03.svg" height="80" alt="03"><br>
<b>Local LLM / VLM Inference</b><br>
Benchmarking low-latency edge inference with Ollama and vision models.
</td>
</tr>
<tr>
<td width="33%" valign="top" align="center">
<img src="assets/nums/num-04.svg" height="80" alt="04"><br>
<b>Data Structures & Algorithms</b><br>
Practicing advanced problem solving, graph theory, and dynamic programming.
</td>
<td width="33%" valign="top" align="center">
<img src="assets/nums/num-05.svg" height="80" alt="05"><br>
<b>Scalable Distributed Backends</b><br>
Exploring message brokers, caching strategies, and robust API rate limiting.
</td>
<td width="33%"></td>
</tr>
</table>

<img src="assets/divider.svg" width="100%" alt="">

<!-- ======================= PAGE 06 · TECH STACK ======================= -->
<a id="toolbox"></a>
<h2 align="center"><img src="assets/header-tech.svg" width="100%" alt="My Toolbox / Tech Stack"></h2>

<table>
<tr>
<td width="50%" valign="top">
<img src="assets/cats/cat-languages.svg" height="44" alt="Languages"><br>
<img src="assets/chips/chip-javascript.svg" height="28" alt="JavaScript">
<img src="assets/chips/chip-typescript.svg" height="28" alt="TypeScript">
<img src="assets/chips/chip-python.svg" height="28" alt="Python">
<img src="assets/chips/chip-c-c.svg" height="28" alt="C / C++">
<img src="assets/chips/chip-sql.svg" height="28" alt="SQL">
</td>
<td width="50%" valign="top">
<img src="assets/cats/cat-frontend.svg" height="44" alt="Frontend"><br>
<img src="assets/chips/chip-react.svg" height="28" alt="React">
<img src="assets/chips/chip-react-js.svg" height="28" alt="React.js">
<img src="assets/chips/chip-tailwind-css.svg" height="28" alt="Tailwind CSS">
<img src="assets/chips/chip-html.svg" height="28" alt="HTML">
<img src="assets/chips/chip-css.svg" height="28" alt="CSS">
<img src="assets/chips/chip-bootstrap.svg" height="28" alt="Bootstrap">
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="assets/cats/cat-backend.svg" height="44" alt="Backend"><br>
<img src="assets/chips/chip-node-js.svg" height="28" alt="Node.js">
<img src="assets/chips/chip-express-js.svg" height="28" alt="Express.js">
<img src="assets/chips/chip-fastapi.svg" height="28" alt="FastAPI">
<img src="assets/chips/chip-flask.svg" height="28" alt="Flask">
<img src="assets/chips/chip-jwt.svg" height="28" alt="JWT">
<img src="assets/chips/chip-ejs.svg" height="28" alt="EJS">
</td>
<td width="50%" valign="top">
<img src="assets/cats/cat-databases.svg" height="44" alt="Databases"><br>
<img src="assets/chips/chip-mongodb.svg" height="28" alt="MongoDB">
<img src="assets/chips/chip-postgresql.svg" height="28" alt="PostgreSQL">
<img src="assets/chips/chip-sql.svg" height="28" alt="SQL">
<img src="assets/chips/chip-prisma.svg" height="28" alt="Prisma">
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="assets/cats/cat-ai-integrations.svg" height="44" alt="AI / Integrations"><br>
<img src="assets/chips/chip-ollama.svg" height="28" alt="Ollama">
<img src="assets/chips/chip-groq-api.svg" height="28" alt="Groq API">
<img src="assets/chips/chip-groq-vlm.svg" height="28" alt="Groq VLM">
<img src="assets/chips/chip-openai-compatible-apis.svg" height="28" alt="OpenAI-compatible APIs">
<img src="assets/chips/chip-whisper.svg" height="28" alt="Whisper">
<img src="assets/chips/chip-rasterio.svg" height="28" alt="Rasterio">
<img src="assets/chips/chip-ffmpeg.svg" height="28" alt="FFmpeg">
</td>
<td width="50%" valign="top">
<img src="assets/cats/cat-tools.svg" height="44" alt="Tools"><br>
<img src="assets/chips/chip-git.svg" height="28" alt="Git">
<img src="assets/chips/chip-github.svg" height="28" alt="GitHub">
<img src="assets/chips/chip-docker.svg" height="28" alt="Docker">
<img src="assets/chips/chip-postman.svg" height="28" alt="Postman">
<img src="assets/chips/chip-vs-code.svg" height="28" alt="VS Code">
<img src="assets/chips/chip-cloudinary.svg" height="28" alt="Cloudinary">
</td>
</tr>
</table>

<img src="assets/divider.svg" width="100%" alt="">

<!-- ======================= PAGE 07 · GITHUB JOURNEY ======================= -->
<a id="journey"></a>
<h2 align="center"><img src="assets/header-journey.svg" width="100%" alt="My Developer Journey"></h2>

<div align="center">

<img src="assets/window-stats.svg" width="100%" alt="GitHub stats window">

<a href="https://github.com/KrxnTech">
<img height="170" alt="Krishna's GitHub stats" src="https://github-readme-stats.vercel.app/api?username=KrxnTech&show_icons=true&title_color=42305F&text_color=111111&icon_color=C2679A&bg_color=FFF3F5&border_color=42305F&border_radius=0">
<img height="170" alt="Top languages" src="https://github-readme-stats.vercel.app/api/top-langs/?username=KrxnTech&layout=compact&langs_count=6&title_color=42305F&text_color=111111&bg_color=FFF3F5&border_color=42305F&border_radius=0">
</a>

<br>

<img alt="GitHub streak" src="https://streak-stats.demolab.com?user=KrxnTech&background=FFF3F5&border=42305F&ring=C2679A&fire=F06CB5&currStreakLabel=42305F&currStreakNum=111111&sideNums=111111&sideLabels=42305F&dates=42305F&stroke=42305F&border_radius=0">

<br>

<img alt="Contribution graph" width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=KrxnTech&bg_color=FFF3F5&color=42305F&line=F2B8CB&point=42305F&area=true&area_color=F2B8CB&hide_border=true&title_color=42305F">

<br>

<sub>⚡ Activity data updated automatically via GitHub APIs. <a href="https://github.com/KrxnTech">Visit my full GitHub profile</a>.</sub>

</div>

<img src="assets/divider.svg" width="100%" alt="">

<!-- ======================= PAGE 08 · CONTACT ======================= -->
<a id="contact"></a>
<h2 align="center"><img src="assets/header-contact.svg" width="100%" alt="Let's Connect: My Contact"></h2>

<div align="center">
<table>
<tr>
<td><a href="https://github.com/KrxnTech"><img src="assets/contact/btn-github.svg" height="76" alt="GitHub"></a></td>
<td><code>github.com/KrxnTech</code></td>
</tr>
<tr>
<td><a href="https://www.linkedin.com/in/krishna-sharma-10b5ab359/"><img src="assets/contact/btn-linkedin.svg" height="76" alt="LinkedIn"></a></td>
<td><code>linkedin.com/in/krishna-sharma-10b5ab359</code></td>
</tr>
<tr>
<td><a href="mailto:developerkrxna@gmail.com"><img src="assets/contact/btn-email.svg" height="76" alt="Email"></a></td>
<td><code>developerkrxna@gmail.com</code></td>
</tr>
</table>
</div>

<img src="assets/divider.svg" width="100%" alt="">

<!-- ======================= PAGE 09 · THANK YOU ======================= -->
<div align="center">

<img src="assets/thanks.svg" width="100%" alt="Thank you! Let's build something amazing together.">

<a href="#top"><img src="assets/top.svg" height="64" alt="Back to top"></a>

</div>
