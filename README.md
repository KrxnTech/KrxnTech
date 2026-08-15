### Hi there! <img src="https://emojis.slackmojis.com/emojis/images/1536351075/4594/blob-wave.gif" width="25"/> 

I’m [**Check Out My Portfolio 🔥 ➦ Backend-Dev KrxnTech**](https://krxna-tech.vercel.app/), a Backend engineer based in India. I like building clean Project keeping things simple.

**These days I’m focused on:**
- React, Express JS, Tailwind, JavaScript, MongoDB
- Working on Backend Development + API's 
- Small, thoughtful projects with polish
 
---

## Professional and Dedicated Working's

### 🎬 ContentHub — AI Video Clipping Platform · Creator & Developer

An automated video processing platform that uses Artificial Intelligence to identify, transcribe, and extract viral short-form clips from full-length videos. By leveraging modern LLMs and Speech-to-Text models, it automates manual video editing to help content creators repurpose media efficiently.

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/51b29e90-3c38-4867-8857-28189f30b287" />  

#### What I've built & shipped:
* 🎙️ **Automated Speech-to-Text Pipeline** — End-to-end audio extraction and transcription using OpenAI Whisper.
* 🧠 **LLM Viral Moment Detection** — AI content analysis powered by Groq (Llama 3) to identify engaging segments.
* ✂️ **Programmatic Video Clipping** — FFmpeg & MoviePy integration for automated frame-accurate video slicing.
* ☁️ **Media Cloud Synchronization** — Scalable storage orchestration with Cloudinary and Node.js.
* ⚡ **Microservices Architecture** — High-performance Python/FastAPI service isolated from standard Web API logic.
* 🛠️ **Environment Engineering** — Custom setup resolving Python 3.13 build conflicts and HTTP client SDK compatibility.

`React.js` · `Vite` · `Tailwind CSS` · `Node.js` · `Express` · `MongoDB` · `FastAPI` · `Python 3.13` · `Whisper AI` · `Groq (Llama 3)` · `FFmpeg` · `Cloudinary`

---

<details>
<summary><b>⚙️ Architecture & Tech Stack Details</b></summary>

<br />

### Tech Stack Breakdown

* **Frontend**: React.js, Vite, Tailwind CSS
* **Backend**: Node.js, Express.js, Mongoose
* **Database**: MongoDB (Local / Atlas)
* **Storage**: Cloudinary (Video & Image Orchestration)
* **AI Service**: Python 3.13, FastAPI, OpenAI Whisper, Groq SDK
* **Media Processing**: FFmpeg, MoviePy

### System Architecture Breakdown

1. **Frontend (React/Vite)**: Responsive interface for video ingestion, library management, and previewing clips.
2. **Backend (Node/Express)**: Core API layer handling authentication, database management (MongoDB), and Cloudinary orchestration.
3. **AI Engine (Python/FastAPI)**: Isolated processing engine handling media extraction, AI transcription, prompt analysis, and rendering.

</details>

<details>
<summary><b>🔄 How a video processing pipeline flows through the system</b></summary>

<br />

```text
[User Upload] ──> (React Frontend) ──> [Cloudinary Storage]
                                              │
                                       (Node Backend)
                                              │
                                    (Python AI Service)
                                              │
               ┌──────────────────────────────┼──────────────────────────────┐
               ▼                              ▼                              ▼
      [Audio Extraction]            [Whisper Transcription]         [Groq Llama 3 Analysis]
        (FFmpeg Engine)                 (Speech-to-Text)              (Viral Cut Detection)
               │                              │                              │
               └──────────────────────────────┼──────────────────────────────┘
                                              │
                                              ▼
                                   [MoviePy Video Slicing]
                                              │
                                              ▼
                                 [Cloudinary Sync & MongoDB]
```

</details>

---

### 😺 Resume Buddy — AI-Powered Career Intelligence Platform · Creator & Developer

An AI-driven SaaS platform that performs contextual resume evaluations against job descriptions, helping candidates understand how their resumes are scored by ATS filters and recruiters before applying. It generates actionable match scores, identifies missing skills, and provides real-time AI rewrites.

<img width="1587" height="716" alt="image" src="https://github.com/user-attachments/assets/b53c4948-2682-4304-9f1a-59aba0fdcd4b" />  

#### What I've built & shipped:

* 📄 **PDF Extraction Pipeline** — Multi-stage document ingestion handling PDF uploads via Multer and text parsing via `pdf-parse`.
* 🤖 **Contextual LLM Analysis** — Custom prompt engineering using Groq (Llama models) to evaluate resumes beyond simple keyword matching.
* 📋 **Structured JSON Contracts** — Strict AI-to-backend schema responses guaranteeing reliable rendering for ATS scores, recruiter verdicts, and section feedback.
* ✍️ **AI Rewrite Studio** — Real-time enhancement studio offering before-and-after comparisons, impact scores, and actionable verb suggestions.
* 📊 **Dual-Lens Recruiter Engine** — Multi-metric scoring system calculating hiring probabilities, ATS compatibility rings, and technical round chances.
* ⚡ **Service-Oriented Architecture** — Clean Express backend API structure with centralized error handling and modular controllers.

`React.js` · `Vite` · `Node.js` · `Express.js` · `Groq API` · `Llama Models` · `Multer` · `pdf-parse` · `Framer Motion`

---

### Tech Stack Breakdown

* **Frontend**: React.js, Vite, JavaScript, React Router, Framer Motion
* **Backend**: Node.js, Express.js, Multer, pdf-parse
* **AI Service**: Groq API, Llama Models (Prompt Engineering & Structured JSON Contracts)
* **Database**: MongoDB *(planned integration)*

### System Architecture Breakdown

1. **Frontend (React/Vite)**: Multi-page SaaS dashboard for PDF ingestion, interactive ATS rings, recruiter metrics, and AI rewrite workflows.
2. **Backend (Express REST API)**: Service-oriented middleware handling file validation, text parsing, error handling, and LLM communication.
3. **AI Core (Groq/Llama)**: Structured processing layer converting candidate data and job descriptions into actionable JSON metrics.

```text
[PDF & Job Description] ──> (React Frontend) ──> [Express REST API]
                                                         │
                                                  (Multer File Upload)
                                                         │
                                                (PDF Text Extractor)
                                                         │
                                               (Groq LLM Engine / Llama)
                                                         │
                                                [Structured JSON Response]
                                                         │
                ┌────────────────────────────────────────┼────────────────────────────────────────┐
                ▼                                        ▼                                        ▼
      [ATS Analysis Engine]                     [Recruiter Dashboard]                    [AI Rewrite Studio]
  (Compatibility Ring & Scores)            (Verdict, Interview & Offer Odds)         (Before/After & Keyword Fixes)
                │                                        │                                        │
                └────────────────────────────────────────┼────────────────────────────────────────┘
                                                         │
                                                         ▼
                                            [Interactive SaaS Dashboard]
```

---

**Some stuff I built:**

* [Dhooon](https://dhoooon-4rme.vercel.app/) - A modern Web Music Application built with React featuring music playback and playlist management
* [Content-Hub](https://github.com/KrxnTech/ContentHub) - An AI-powered web platform that converts long-form videos (4–5 minutes) into multiple engaging short clips automatically
* [Resume-Buddy](https://github.com/KrxnTech/AI-Resume-Portfolio-Analyzer) - AI-powered MERN web application that analyzes resumes against job descriptions, extracts insights, identifies skill gaps, and generates AI-driven improvement suggestions.

---

**Client Works**

* [Pharmaceutical Website - Gulkas Pharma](https://gulkaspharma.vercel.app/) : Client Pharmaceutical Website
* [Easy Label Sticker's Generator - Gulkas Pharma](https://label-qr-generator.vercel.app/) : MERN Based Label Sticker Gen Web Application ( Automation )
* [IRONHAUS GYM](https://ironhaus-gym-xi.vercel.app/) : Live Client Work 

**Tech Stack:**

**Fun Facts:**

* I like tea
* **Hobbies:** Coding, gym & Music

---

* I occasionally go into **coding beast mode** dump a lot of commits then disappear like a mysterious hacker in a movie 😅
