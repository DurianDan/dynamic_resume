from dynamic_resume.schemas.based_resume_entity import ResumeEntity
from typing import List, Annotated
import os

def check_line_length(line: str)-> str:
    words_limit = os.getenv(
        "EXPERIENCE_DESCRIPTION_LINE_WORDS_LIMIT"
    )
    words_count = len(line.strip().split(" "))
    assert words_count < words_limit, f"Each line of the description must be less than {words_limit}"
    return line


class DescriptionLine(ResumeEntity):
    line: Annotated[str, check_line_length]


class WholeDescription(ResumeEntity):
    description: List[DescriptionLine]

    def add(
        self, lines: List[DescriptionLine], inplace: bool = False
    ) -> None | "WholeDescription":
        """Add lines to description.
        If `inplace` is `False` output another updated `WholeDescription`,
        if `False`, return None and modify this description object"""
        if inplace:
            self.description.append(lines)
        else:
            return WholeDescription(description=self.description + lines)
