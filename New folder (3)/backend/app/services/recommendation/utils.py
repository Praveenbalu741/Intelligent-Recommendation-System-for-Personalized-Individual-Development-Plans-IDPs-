import logging
from typing import List

logger = logging.getLogger(__name__)

def generate_sbert_embeddings(text_list: List[str]) -> List[List[float]]:
    """
    Mock utility to generate SBERT embeddings for skills and courses.
    In a real implementation, this would use sentence-transformers/all-MiniLM-L6-v2.
    """
    logger.info(f"Generating embeddings for {len(text_list)} items.")
    # Return dummy embeddings (384 dimensions is standard for all-MiniLM-L6-v2)
    return [[0.1] * 384 for _ in text_list]

def query_pinecone_similar_skills(skill_embedding: List[float], top_k: int = 5) -> List[dict]:
    """
    Mock utility to query Pinecone for similar skills or pre-requisites.
    This vector search allows for semantic matching rather than exact string matching.
    """
    logger.info("Querying Pinecone vector database for similar skills.")
    # Dummy related skills for demonstration
    return [
        {"id": "skill_1", "name": "Python", "score": 0.95},
        {"id": "skill_2", "name": "FastAPI", "score": 0.88},
        {"id": "skill_3", "name": "Machine Learning", "score": 0.82}
    ]

def call_gemini_llm(prompt: str) -> str:
    """
    Mock utility to call the Gemini API via LangChain to generate personalized mentorship advice.
    This provides the LLM natural language component of the IDP.
    """
    logger.info("Calling Gemini API for natural language insight.")
    return "To achieve your goal, focus consistently on your core skills. Given your recent performance dip, I recommend starting with foundational videos to strengthen your understanding before moving to advanced architecture."
