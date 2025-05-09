from sqlalchemy.orm import Session
import models, schemas

TASK_NOT_FOUND = "Task not found"

def get_tasks(db: Session):
    return db.query(models.Task).all()

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(title=task.title)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise Exception(TASK_NOT_FOUND)
    db.delete(task)
    db.commit()
