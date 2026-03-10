from typing import List, Optional
from pydantic import BaseModel

class UserProfile(BaseModel):
    user_id: str
    target_role: str
    current_skills: List[str]
    performance_score: float
    learning_style: Optional[str] = "visual"

class CourseResource(BaseModel):
    id: str
    title: str
    provider: str
    url: str
    difficulty: str
    tags: List[str]

class IDPMilestone(BaseModel):
    milestone_id: str
    title: str
    description: str
    target_date: str
    recommended_courses: List[CourseResource]
    status: str = "pending"

class IndividualDevelopmentPlan(BaseModel):
    user_id: str
    target_role: str
    skill_gap_analysis: List[str]
    mentorship_advice: str
    milestones: List[IDPMilestone]
    is_adaptive: bool = True
