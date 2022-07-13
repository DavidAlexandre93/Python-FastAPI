from datetime import datetime
from typing import Dict, Generator
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session  # type: ignore

from app.service.crud import (
    create_student,
    remove_student,
    retrieve_all_students,
    retrieve_student,
    update_student,
)
from app.database.database import Base, SessionLocal, engine
from app.database.datatypes import StudentType
from app.model.schemas import CreateStudentSchema, UpdateStudentSchema

# instancia o FastAPI
app = FastAPI()

Base.metadata.create_all(bind=engine)

"""
Retorna a sessão de conexão do banco de dados.
"""


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""
Retorna a data e hora atuais do servidor (use para verificar se o serviço
está no ar; consulte regularmente e terá ideia de quando ele deixou de
funcionar).
"""


@app.get("/health/")
async def alive() -> Dict[str, datetime]:
    return {"timestamp": datetime.now()}


"""
Retorna todos os estudantes armazenados.
"""


@app.get("/students/", status_code=status.HTTP_200_OK)
async def get_all_students(db: Session = Depends(get_db)) -> Generator:
    if result := retrieve_all_students(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Não existem estudantes cadastrados.",
    )  # pragma: nocover


"""
Retorna os dados do estudante, recebe o _id_ do estudante em `student_id`
e retorna as informações armazenadas ou gera uma exceção caso não seja
encontrado.
"""


@app.get(
    "/students/{student_id}/", status_code=status.HTTP_200_OK,
)
async def get_student(student_id: int, db: Session = Depends(get_db)) -> StudentType:
    if result := retrieve_student(db, student_id):
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Estudante de 'id={student_id}' não encontrado.",
    )


"""
Remove um estudante do banco de dados, recebe o _id_ do estudante em
`student_id` e retorna uma mensagem de sucesso, caso contrário gera uma
exceção de não encontrado.
"""


@app.delete("/students/{student_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(student_id: int, db: Session = Depends(get_db)) -> None:
    if not remove_student(db, student_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Estudante de 'id={student_id}' não encontrado.",
        )


"""
Insere um novo estudante no banco de dados, recebe todos os campos
necessários, valida e insere no banco de dados. Retorna o registro
inserido acrescido do seu `id`.
"""


@app.post(
    "/students/", status_code=status.HTTP_201_CREATED,
)
async def post_student(
    student: CreateStudentSchema, db: Session = Depends(get_db),
) -> StudentType:
    if result := create_student(db, student):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )  # pragma: nocover


"""
Atualiza os dados de um estudante, recebe o _id_  em `student_id` e a
lista de campos a modificar dentro do JSON (campos com valor `None`
serão ignorados).
"""


@app.put(
    "/students/{student_id}/", status_code=status.HTTP_201_CREATED,
)
async def put_student(
    student_id: int,
    student: UpdateStudentSchema,
    db: Session = Depends(get_db),
) -> StudentType:
    if result := update_student(
        db, student_id, {key: value for key, value in student if value}
    ):
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Estudante de 'id={student_id}' não encontrado.",
    )
