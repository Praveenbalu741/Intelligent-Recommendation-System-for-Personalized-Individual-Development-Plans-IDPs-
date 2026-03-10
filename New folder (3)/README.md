# Intelligent Recommendation System for Personalized IDPs (SIH25194)

## Overview
This repository contains the architecture and core implementation of an enterprise-grade Intelligent Recommendation System designed to dynamically generate Personalized Individual Development Plans (IDPs). By analyzing skill gaps, career goals, and performance data, the system produces actionable, time-bound learning roadmaps.

## Key Features
- **Skill Gap Analysis**: Users input current skills and target roles; the AI highlights missing competencies.
- **Automated Course Mapping**: Recommends specific learning resources (courses, videos) using content-based and collaborative filtering.
- **Adaptive Roadmaps**: Dynamically adjusts milestones based on user progress and assessments.
- **Natural Language Mentorship**: Integrates Gemini API to provide personalized, human-like mentorship advice.
- **Goal Tracker & Skill Heatmap**: High-performance dashboard elements for tracking IDP compliance.

## System Architecture (Microservices-Lite)

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Frontend** | Next.js 14, Tailwind CSS | Fast, SEO-friendly, "Glassmorphic" UI for the IDP dashboard. |
| **Backend** | FastAPI | High-concurrency async modular API, perfect for AI orchestration. |
| **AI Engine** | SBERT + Gemini | SBERT for semantic skill matching; Gemini for plan personalization. |
| **Database** | PostgreSQL | Relational data storage (user profiles, catalogs, progress). |
| **Vector DB** | Pinecone | Storing and retrieving skill-based embeddings for fast semantic search. |
| **Caching** | Redis | Speeds up recommendation results for frequent queries. |

## Clean Architecture Folder Structure
Run the provided `scripts/setup_structure.ps1` script to generate the complete backend (FastAPI) and frontend (Next.js) directory structures exactly like top-tier SIH winners.

## Getting Started

### Prerequisites
- Python 3.10+
- Node.js 18+
- PostgreSQL
- Redis
- Pinecone API Key
- Gemini API Key

### Installation

1. Clone the repository and run the setup script:
   ```powershell
   .\scripts\setup_structure.ps1
   ```
2. Navigate to the backend directory and install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
3. Set up environment variables locally in a `.env` file for Postgres, Redis, Pinecone, and Gemini.
4. Run the FastAPI development server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Included Core Logic
This repository includes the core intelligence in `backend/app/services/recommendation/`:
- `models.py`: Data schemas for requests and IDP generation.
- `utils.py`: Stubbed integrations for SBERT and Gemini.
- `recommendation_service.py`: The AI engine orchestrating Collaborative/Content-Based Filtering and Adaptive Roadmaps.
