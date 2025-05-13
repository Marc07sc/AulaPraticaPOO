from models.Aluno import Aluno

CURSOS = {}
ALUNOS = []

def cadastrar_aluno(nome, nascimento, curso):
    if not nome or not nascimento:
        return "Parâmetros inválidos."

    c = {}
    aluno_objeto = Aluno(nome, nascimento)

    if curso:
        c = CURSOS.get("curso")
        c["alunos"].append(aluno_objeto)

    ALUNOS.append(aluno_objeto)

    return {
        "nome_aluno":aluno_objeto.nome,
        "matricula": aluno_objeto.matricula,
        "curso": c.get("nome_curso")
    }
def listar_alunos():
    resposta = ""
    for aluno in ALUNOS:
        resposta += (f"\nNome: {aluno.nome} \n"
                     f"Matrícula: {aluno.matricula} \n"
                     f"Curso: {aluno.curso} \n"
                     f"-------------------------- \n")
    return resposta
