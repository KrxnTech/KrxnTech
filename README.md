<a id="top"></a>
<div align="center">

<img src="assets/hero.svg" width="100%" alt="Krishna - Software Developer. Backend Developer, MERN Stack, AI Enthusiast">

<a href="#about"><img src="assets/start.svg" height="64" alt="Start"></a>

<br>

<a href="#about"><img src="assets/nav/nav-about.svg" height="36" alt="About"></a>
<a href="#expertise"><img src="assets/nav/nav-expertise.svg" height="36" alt="Expertise"></a>
<a href="#projects"><img src="assets/nav/nav-projects.svg" height="36" alt="Projects"></a>
<a href="#toolbox"><img src="assets/nav/nav-toolbox.svg" height="36" alt="Toolbox"></a>
<a href="#journey"><img src="assets/nav/nav-journey.svg" height="36" alt="Journey"></a>
<a href="#contact"><img src="assets/nav/nav-contact.svg" height="36" alt="Contact"></a>

<br><br>

**Backend Developer & Full-Stack Engineer specializing in scalable APIs, databases, and AI systems.**
<br>
Ahmedabad–Gandhinagar, Gujarat, India &nbsp;·&nbsp; B.Tech CSE (Gandhinagar University) &nbsp;·&nbsp; Node.js · Express · Python · MongoDB · AI/VLMs

</div>

<img src="assets/divider.svg" width="100%" alt="">

<!-- ======================= PAGE 02 · ABOUT ======================= -->
<a id="about"></a>
<h2 align="center"><img src="assets/header-about.svg" width="100%" alt="Introduction: About Me"></h2>

<table>
<tr>
<td width="36%" valign="middle" align="center">
<img src="assets/about-photo.png" width="100%" alt="Krishna Sharma - Profile">
</td>
<td width="64%" valign="middle">

Hi, I'm **Krishna Sharma** — a Software Developer with a backend-focused approach, experienced in building scalable and reliable web applications.

I design RESTful APIs, develop robust server-side systems, model databases (MongoDB, PostgreSQL, SQL), and integrate full-stack components into complete end-to-end applications.

- 🎓 **Education:** B.Tech CSE @ Gandhinagar University (CGPA: 9.65 / 10 · 2024–2028)
- 🛠️ **Core Focus:** Scalable REST APIs, Microservices & Database Architecture
- 🤖 **AI Engineering:** Local LLM Inference (Ollama) & Cloud Model Orchestration
- 📍 **Location:** Ahmedabad–Gandhinagar, Gujarat, India &nbsp;·&nbsp; [krxna-tech.vercel.app](https://krxna-tech.vercel.app)

</td>
</tr>
</table>

<img src="assets/divider.svg" width="100%" alt="">

<!-- ======================= PAGE 03 · EXPERTISE ======================= -->
<a id="expertise"></a>
<h2 align="center"><img src="assets/header-expertise.svg" width="100%" alt="Core Expertise"></h2>

- **Backend Architecture & RESTful APIs.** Building scalable, production-ready server applications with Node.js, Express.js, and Python (FastAPI / Flask). Implementing secure JWT authentication, Bcrypt hashing, structured JSON pipelines, and Role-Based Access Control (RBAC).
- **Full-Stack & Database Engineering.** Developing complete web applications with React, Vite, and Tailwind CSS. Designing relational and NoSQL schemas, indexes, and queries across MongoDB (Mongoose), PostgreSQL, and SQL databases.
- **AI Integration & Model Orchestration.** Architecting practical AI workflows combining local LLM inference (Ollama), cloud model acceleration (Groq API, Llama, Qwen), speech transcription (OpenAI Whisper), and audio extraction (FFmpeg).

<img src="assets/divider.svg" width="100%" alt="">

<!-- ======================= PAGE 04 · FEATURED PROJECTS ======================= -->
<a id="projects"></a>

<!-- PROJECT 01: RESUME BUDDY -->
<h2 align="center"><img src="assets/header-project-1.svg" width="100%" alt="Featured Project 01: Resume Buddy"></h2>

<table>
<tr>
<td width="52%" valign="top">

### Resume Buddy: AI Resume & Career Intelligence Platform

**The problem.** Traditional Applicant Tracking Systems (ATS) rely on naive keyword matching, discarding qualified candidates without providing actionable feedback to improve resume impact.

**The solution.** An AI career-intelligence platform that parses resume PDFs and evaluates them against target job descriptions using contextual LLM analysis rather than keyword counting.

**Architecture & Key Capabilities**
- **Structured Parsing Pipeline:** Uses Multer and `pdf-parse` to convert unstructured PDF resumes into validated JSON schemas for deep inspection.
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
<td width="48%" valign="middle" align="center">
<img src="assets/resume-buddy-preview.svg" width="100%" alt="Resume Buddy preview in a retro computer window">
</td>
</tr>
</table>

<br>

<!-- PROJECT 02: CONTENTHUB -->
<h2 align="center"><img src="assets/header-project-2.svg" width="100%" alt="Featured Project 02: ContentHub"></h2>

<table>
<tr>
<td width="48%" valign="middle" align="center">
<img src="assets/contenthub-preview.svg" width="100%" alt="ContentHub preview in a retro computer window">
</td>
<td width="52%" valign="top">

### ContentHub: AI Video-to-Shorts Platform

**The problem.** Manually scrubbing 4–5 minute videos to find engaging moments, resizing them for vertical formats, and generating synced subtitles is slow and repetitive.

**The solution.** A microservices platform that automatically ingests long-form videos and converts them into multiple high-engagement vertical short clips for social media repurposing.

**Architecture & Key Capabilities**
- **Audio Extraction & Timed Transcription:** Python/FastAPI microservice extracts audio tracks via FFmpeg and runs transcription with OpenAI Whisper to generate timestamped text tokens.
- **Engagement Hook Analysis:** Groq-accelerated Llama 3 models analyze transcript pacing and sentiment to detect high-retention moments and highlight clips.
- **Automated Clipping & Captions:** Programmatically crops 9:16 vertical clips, generates synchronized subtitles, and creates SEO-optimized descriptions and hashtags.
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
</tr>
</table>

<br>

<!-- PROJECT 03: DHOON -->
<h2 align="center"><img src="assets/header-project-3.svg" width="100%" alt="Featured Project 03: Dhoon"></h2>

<table>
<tr>
<td width="52%" valign="top">

### Dhoon: Modern React Music Streaming Web Application

**The problem.** Many web music players suffer from sluggish playback state transitions, clunky playlist management, and inconsistent audio controls across devices.

**The solution.** A responsive, modern music player web app built with React and Tailwind CSS, focused on seamless audio playback interactions, instant feedback, and a polished modern UI/UX.

**Architecture & Key Capabilities**
- **Seamless Playback Engine:** Custom audio controller with persistent playback state, smooth progress scrubbing, volume regulation, and track skipping.
- **Dynamic Playlist Management:** Interactive track queue with real-time search, album art presentation, and active song highlighting.
- **Modern Responsive Design:** Crafted with Tailwind CSS featuring fluid animations, responsive layouts for desktop and mobile, and fast client-side rendering.

<img src="assets/chips/chip-react.svg" height="28" alt="React">
<img src="assets/chips/chip-vite.svg" height="28" alt="Vite">
<img src="assets/chips/chip-tailwind-css.svg" height="28" alt="Tailwind CSS">
<img src="assets/chips/chip-javascript.svg" height="28" alt="JavaScript">

<br>

**[📁 GitHub Repo](https://github.com/KrxnTech/Dhoooon)** &nbsp;·&nbsp; **[🌐 Live Demo](https://dhoooon.vercel.app/)**

</td>
<td width="48%" valign="middle" align="center">
<img src="assets/dhoon-preview.svg" width="100%" alt="Dhoon preview in a retro computer window">
</td>
</tr>
</table>

<img src="assets/divider.svg" width="100%" alt="">

<!-- ======================= PAGE 05 · TECH STACK ======================= -->
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

<!-- ======================= PAGE 06 · GITHUB JOURNEY ======================= -->
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

<!-- ======================= PAGE 07 · CONTACT ======================= -->
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

<!-- ======================= PAGE 08 · THANK YOU ======================= -->
<div align="center">

<img src="assets/thanks.svg" width="100%" alt="Thank you! Let's build something amazing together.">

<a href="#top"><img src="assets/top.svg" height="64" alt="Back to top"></a>

</div>
