from dataclasses import dataclass
from typing import List, Any

from taiga_client.models.base import Base
from taiga_client.models.fields import Field
from taiga_client.models.project_item import ProjectItem


@dataclass
class Attribute(Base):
    description: str = Field()
    extra: Any = Field()
    name: str = Field()
    order: int = Field()
    project_id: int = Field()
    type: str = Field()


@dataclass
class Status(Base):
    color: str = Field()
    is_closed: bool = Field()
    name: str = Field()
    order: int = Field()
    project_id: int = Field()
    slug: str = Field()


@dataclass
class User(Base):
    color: str = Field()
    full_name: str = Field()
    full_name_display: str = Field()
    gravatar_id: str = Field()
    is_active: bool = Field()
    photo: Any = Field()
    role: int = Field()
    role_name: str = Field()
    username: str = Field()


@dataclass
class DueDate(Base):
    by_default: bool = Field()
    color: str = Field()
    days_to_due: Any = Field()
    name: str = Field()
    order: int = Field()
    project_id: int = Field()


@dataclass
class IssueType(Base):
    color: str = Field()
    name: str = Field()
    order: int = Field()
    project_id: int = Field()


@dataclass
class Priority(Base):
    color: str = Field()
    name: str = Field()
    order: int = Field()
    project_id: int = Field()


@dataclass
class Severity(Base):
    color: str = Field()
    name: str = Field()
    order: int = Field()
    project_id: int = Field()


class Milestone(Base):
    close: bool = Field()
    name: str = Field()
    slug: str = Field()


@dataclass
class Point(Base):
    name: str = Field()
    order: str = Field()
    project_id: int = Field()
    value: int = Field()


@dataclass
class Role(Base):
    computable: bool = Field()
    name: str = Field()
    order: str = Field()
    permissions: List[str] = Field()
    project_id: int = Field()
    slug: str = Field()


@dataclass
class Project(ProjectItem):
    epic_custom_attributes: List[Attribute] = Field()
    epic_statuses: List[Status] = Field()
    epics_csv_uuid: Any = Field()
    is_out_of_owner_limits: bool = Field()
    is_private_extra_info: Any = Field()
    issue_custom_attributes: List[Attribute] = Field()
    issue_duedates: List[DueDate] = Field()
    issue_statuses: List[Status] = Field()
    issue_types: List[IssueType] = Field()
    issues_csv_uuid: Any = Field()
    max_memberships: Any = Field()
    members: List[User] = Field()
    milestones: List[Milestone] = Field()
    owner: User = Field()
    points: List[Point] = Field()
    priorities: List[Priority] = Field()
    roles: List[Role] = Field()
    severities: List[Severity] = Field()
    task_custom_attributes: List[Attribute] = Field()
    task_duedates: List[DueDate] = Field()
    task_statuses: List[Status] = Field()
    tasks_csv_uuid: Any = Field()
    total_memberships: int = Field()
    transfer_token: str = Field()
    us_duedates: List[DueDate] = Field()
    us_statuses: List[Status] = Field()
    userstories_csv_uuid: Any = Field()
    userstory_custom_attributes: List[Attribute] = Field()
