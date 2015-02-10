from datetime import datetime
from sqlalchemy import Column ,Integer,String, TEXT, Boolean, DateTime

from database import db

class Skill(db.base):
    """Model to store skills information.

    properties:
        __tablename__: Name of the table
        skill_id: Primary key, stores ID of skill.
        skill_name: Name of the skill.
        skill_description: Description of the skill.
        is_deleted: Boolean to check if the skill is active or not
        created_by: SSO of the racker creating the skill
        created_date: Skill created date
        modified_by: SSO of the racker who modifies the skill
        modified_date: Skill modified date
    """
    __tablename__ = 'skills'
    skill_id = Column(Integer, primary_key=True, autoincrement=True)
    skill_name =Column(String(200),nullable=False)
    skill_description=Column(TEXT, nullable=False)
    is_deleted = Column(Boolean, nullable=False, default=False)
    created_by = Column(String(200), nullable=False)
    created_date = Column(DateTime(timezone=False),default=datetime.utcnow,nullable=False)
    modified_by = Column(String(200))
    modified_date = Column(DateTime(timezone=False),default=datetime.utcnow)
