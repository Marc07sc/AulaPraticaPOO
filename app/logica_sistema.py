from models.Aluno import Aluno

CURSOS = {}

def cadastrar_aluno(nome, nascimento, curso):
    if not nome or not nascimento:
        return "Parâmetros inválidos."

    c = {}
    aluno_objeto = Aluno(nome, nascimento)

    if curso:
        c = CURSOS.get("curso")
        c["alunos"].append(aluno_objeto)

    return {
        "nome_aluno":aluno_objeto.nome,
        "matricula": aluno_objeto.matricula,
        "curso": c.get("nome_curso")
    }