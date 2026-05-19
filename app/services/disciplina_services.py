from sqlalchemy.orm import Session
from app.models.disciplina import Disciplina
from app.schemas.disciplina import DisciplinaCreate

def crear_disciplina(db: Session, data: DisciplinaCreate):
    nueva = Disciplina(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def obtener_disciplinas(db: Session):
    return db.query(Disciplina).all()