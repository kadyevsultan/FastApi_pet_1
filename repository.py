from sqlalchemy import select
from database import new_session, TaskModel
from schemas import STask, STaskAdd


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TaskModel(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id
    
    @classmethod
    async def get_all(cls) -> list[STask]:
        """
        Retrieve all tasks from the repository.
        """
        async with new_session() as session:
            query = select(TaskModel)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return task_schemas