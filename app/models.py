from sqlalchemy import Enum, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import enum

from database import Base


class Results(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    address = Column(String(300),  unique=False, nullable=True)
    words_count = Column(Integer(), unique=False, nullable=True)
    http_status_code = Column(Integer)

    def __str__(self):
        return f'id: {self.id} | matches: {self.words_count} | code {self.http_status_code}'


class TaskStatus (enum.Enum):
    NOT_STARTED = 1
    PENDING = 2
    FINISHED = 3


class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    address = Column(String(300), unique=False, nullable=True)
    timestamp = Column(DateTime())
    task_status = Column(Enum(TaskStatus))
    http_status_code = Column(Integer, nullable=True)

    def __str__(self):
        return f'id: {self.id} | status: {self.task_status} | code {self.http_status_code}'
