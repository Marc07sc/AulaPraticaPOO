class Curso:

# ATRIBUTOS

    def __init__(self, nome, duracao, professor, materias):
        self.nome = nome
        self.alunos = {}
        self.duracao = duracao
        self.professor = professor
        self.materias = materias
        self.aulas = []

# COMPORTAMENTOS

    def contabilizar_presenca(self):
        pass

    def listar_alunos_aprovados(self):
        pass