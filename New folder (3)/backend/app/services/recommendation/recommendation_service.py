from typing import List
from .models import UserProfile, IndividualDevelopmentPlan, IDPMilestone, CourseResource
from .utils import generate_sbert_embeddings, query_pinecone_similar_skills, call_gemini_llm

class AIRecommendationEngine:
    """
    Core engine handling Content-Based Filtering, Collaborative Filtering, 
    and LLM integration for generating a personalized IDP.
    """
    
    def __init__(self):
        # We would initialize SBERT model, Pinecone client, and LangChain LLM here
        self.role_requirements_db = {
            "Data Scientist": ["Python", "Machine Learning", "SQL", "Deep Learning", "Statistics"],
            "Backend Engineer": ["Python", "FastAPI", "SQL", "System Design", "Docker"]
        }
        
        self.course_catalog = [
            CourseResource(id="c1", title="FastAPI Fundamentals", provider="Coursera", url="http://coursera.org/fastapi", difficulty="Beginner", tags=["FastAPI", "Python"]),
            CourseResource(id="c2", title="Advanced ML", provider="YouTube", url="http://youtube.com/ml", difficulty="Advanced", tags=["Machine Learning", "Deep Learning"]),
            CourseResource(id="c3", title="System Design Interview", provider="ByteByteGo", url="http://bytebytego.com", difficulty="Advanced", tags=["System Design", "Architecture"]),
            CourseResource(id="c4", title="Docker for Beginners", provider="YouTube", url="http://youtube.com/docker", difficulty="Beginner", tags=["Docker", "DevOps"])
        ]

    def _perform_skill_gap_analysis(self, current_skills: List[str], target_role: str) -> List[str]:
        """Identifies missing skills based on the target 'Dream Job'."""
        required_skills = self.role_requirements_db.get(target_role, [])
        # Content-based approach: SBERT embeddings would be used here to match semantic similarity 
        # instead of exact string matching. For simplicity, we use exact matching in this stub.
        missing_skills = [skill for skill in required_skills if skill not in current_skills]
        return missing_skills

    def _collaborative_filtering_course_mapping(self, missing_skills: List[str]) -> List[CourseResource]:
        """
        Suggests courses based on what similar users found helpful (Collaborative Filtering).
        In this implementation, we map missing skills to our catalog.
        """
        recommended = []
        for course in self.course_catalog:
            if any(skill in course.tags for skill in missing_skills):
                recommended.append(course)
        return recommended

    def _generate_adaptive_milestones(self, missing_skills: List[str], performance_score: float) -> List[IDPMilestone]:
        """
        Creates time-bound milestones. If the user failed a previous assessment (low performance),
        we inject foundational/remedial steps automatically.
        """
        milestones = []
        courses = self._collaborative_filtering_course_mapping(missing_skills)
        
        # Adaptive Roadmap Logic: Automatically add foundational steps if performance is low
        if performance_score < 60.0:
            foundational_course = CourseResource(
                id="c0", title="Foundations of Computer Science", provider="YouTube", 
                url="http://youtube.com/basics", difficulty="Beginner", tags=["Basics", "Fundamentals"]
            )
            milestones.append(IDPMilestone(
                milestone_id="m0", title="Remedial Foundations", 
                description="Strengthen your basics based on recent assessment results.",
                target_date="Week 1-2", recommended_courses=[foundational_course]
            ))
            
        milestones.append(IDPMilestone(
            milestone_id="m1", title="Core Skill Acquisition", 
            description=f"Learn missing skills: {', '.join(missing_skills)}",
            target_date="Week 3-6", recommended_courses=courses
        ))
        
        return milestones

    def _generate_mentorship_advice(self, user: UserProfile, gaps: List[str]) -> str:
        """Uses Gemini LLM to generate natural language mentorship advice."""
        prompt = (f"Act as a professional career mentor. The user wants to be a {user.target_role}. "
                  f"They currently know {user.current_skills}. They are missing {gaps}. "
                  f"Their recent performance score is {user.performance_score}/100. "
                  "Provide a short, encouraging 2-sentence mentorship advice for their IDP.")
        return call_gemini_llm(prompt)

    def generate_idp(self, user: UserProfile) -> IndividualDevelopmentPlan:
        """Main orchestration method to generate the complete Individual Development Plan."""
        
        # 1. Skill Gap Analysis
        missing_skills = self._perform_skill_gap_analysis(user.current_skills, user.target_role)
        
        # 2. Adaptive Roadmaps & Course Mapping
        milestones = self._generate_adaptive_milestones(missing_skills, user.performance_score)
        
        # 3. LLM Mentorship Advice
        advice = self._generate_mentorship_advice(user, missing_skills)
        
        # 4. Assemble the Plan
        plan = IndividualDevelopmentPlan(
            user_id=user.user_id,
            target_role=user.target_role,
            skill_gap_analysis=missing_skills,
            mentorship_advice=advice,
            milestones=milestones
        )
        return plan

# Example usage/tester block
if __name__ == "__main__":
    import json
    engine = AIRecommendationEngine()
    test_user = UserProfile(
        user_id="emp_001", 
        target_role="Backend Engineer", 
        current_skills=["Python", "SQL"], 
        # Score < 60 triggers Adaptive Roadmap foundational course
        performance_score=55.0  
    )
    idp = engine.generate_idp(test_user)
    print("Generated Personalized IDP payload:\n")
    print(idp.model_dump_json(indent=2))
