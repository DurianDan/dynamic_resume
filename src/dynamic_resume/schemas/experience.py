from dynamic_resume.schemas.experience_daterange import ExperienceDateRange
from dynamic_resume.schemas.based_resume_entity import ResumeEntity
from dynamic_resume.schemas.description import WholeDescription, DescriptionLine
from pydantic import HttpUrl



class Experience(ResumeEntity):
    title: DescriptionLine
    associated_url: HttpUrl|None = None
    associated_organization: str
    date_range: ExperienceDateRange|None = None
    description: WholeDescription|None = None
