from fastapi import APIRouter
from typing import Annotated
from fastapi import Depends
from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()],) -> STaskId:
    task_id = await TaskRepository.add_one_task(task)
    return {"staus_code": 200, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:    
    tasks = await TaskRepository.find_all()
    return {"status_code": 200, "tasks": tasks}