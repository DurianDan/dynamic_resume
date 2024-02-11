from pydantic import BaseModel
from typing import Iterable, List
from enum import Flag


class EntityUsage(Flag):
    on = True
    off = False


class ResumeEntity(BaseModel):
    tags: List[str] = []
    visibility: EntityUsage = EntityUsage.on

    def find_tag(self, tag: str) -> int:
        return self.tags.index(tag)
    
    def add_tags(
        self,
        tags: Iterable[str],
        inplace: bool = False
    ) -> None|'ResumeEntity':
        if inplace:
            self.tags.extend(tags)
        else:
            return self.partial_copy(tags)
    
    def partial_copy(
        self,
        tags: Iterable[str]|None=None,
        visibility: EntityUsage|None=None
    ) -> 'ResumeEntity':
        return ResumeEntity(
            tags=tags if tags else self.tags,
            visibility=visibility if visibility else self.visibility
        )