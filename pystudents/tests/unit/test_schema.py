"""
Testes unitários do _schema_ de dados da API.
"""
from app.model.schemas import CreateStudentSchema, UpdateStudentSchema

from tests.datatypes import StudentType
from tests.fixtures import student  # noqa: F401


class TestStudentchema:
    """
    Como a validação dos estudantes está por conta do `pydantic` é bom
    acrescentar testes para verificar se está tudo certo por lá (caso
    contrário os testes que passaram para a API não valerão de muita
    coisa).
    """

    invalid_state = "Guanabara"
    valid_postal = ["99999-999"]
    invalid_postal = ["99999", "999-999", ""]

    async def test_success_student_validation(self, student: StudentType) -> None:
        """
        Verifica a validação de dados para um novo estudante.
        """
        try:
            __ = CreateStudentSchema(**student)

        except ValueError:
            assert False

        else:
            assert True

    async def test_fail_student_validation(self, student: StudentType) -> None:
        """
        Verifica a validação de dados para um novo estudante.
        """
        try:
            student["postal_code"] = self.invalid_postal[0]
            student["state"] = self.invalid_state
            __ = CreateStudentSchema(**student)

        except ValueError:
            assert True

        else:
            assert False

    async def test_postal_code_validation(self, student: StudentType) -> None:
        """
        Valida que o CEP está sempre dentro do padrão de "99999-999".
        """
        try:
            for postal_code in self.valid_postal + self.invalid_postal:
                student["postal_code"] = postal_code
                __ = CreateStudentSchema(**student)

        except ValueError:
            assert True

        else:
            assert False

    async def test_state_validation(self, student: StudentType) -> None:
        """
        Faz a validação do nome do estado, a tentativa de usar um nome
        de estado que não existe deve retornar a exceção `ValueError`.

        Grátis uma pequena aula de história... :grinning:
        """
        new_student = CreateStudentSchema(**student)

        try:

            new_student_dict = new_student.dict()
            new_student_dict["state"] = self.invalid_state

            __ = UpdateStudentSchema(**new_student_dict)

        except ValueError:
            assert True

        else:
            assert False
