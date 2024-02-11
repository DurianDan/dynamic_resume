from pydantic import BaseModel
from datetime import date


class ExperienceDateRange(BaseModel):
    start_at: date
    end_at: date
