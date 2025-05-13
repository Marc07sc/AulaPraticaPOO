from models.aluno import Aluno
from models.curso import Curso

CURSOS = {}
ALUNOS = {}

def cadastrar_aluno(nome, nascimento, nome_curso=None):
    if not nome or not nascimento:
        return "Parâmetros inválidos."

    c = None
    aluno_objeto = Aluno(nome, nascimento)

    if nome_curso:
        c = CURSOS.get(nome_curso)
        c.alunos[aluno_objeto.matricula] = aluno_objeto

   # ALUNOS.append(aluno_objeto.matricula: aluno_objeto)

    ALUNOS[aluno_objeto.matricula] = aluno_objeto

    return {
        "nome_aluno":aluno_objeto.nome,
        "matricula": aluno_objeto.matricula,
        "curso": c.nome or None
    }
def listar_alunos():
    resposta = ""

    if not ALUNOS:
        print("Nenhum aluno cadastrado.")

    for aluno in ALUNOS.values():
        resposta += (f"\nNome: {aluno.nome} \n"
                     f"Matrícula: {aluno.matricula} \n"
                     f"Curso: {aluno.curso.nome or None} \n"
                     f"-------------------------- \n")
    return resposta

def detalhar_aluno(matricula):
    if not matricula:
        return "Parâmetros inválidos."

    aluno = ALUNOS.get(matricula)

    if not aluno:
        return "Este aluno não está cadastrado."

    return (f"Nome: {aluno.nome} \n"
            f"Matrícula: {aluno.matricula} \n"
            f"Data de Nascimento: {aluno.nascimento} \n"
            f"Data de Ingresso: {aluno.ingresso} \n"
            f"Curso: {aluno.curso.nome or "Sem curso no momento"} \n"
            f"Notas: {aluno.notas}")

def deletar_aluno(matricula):
    if not matricula:
        return "Parâmetros inválidos."

    aluno = ALUNOS.get(matricula)

    if not aluno:
        return "Este aluno não está cadastrado."

    if aluno.curso:
        curso = CURSOS.get(aluno.curso.nome)
        curso.alunos.pop(matricula)

    ALUNOS.pop(matricula)

    return "Aluno excluído com sucesso."