from proj_alum import alunos, projetos, participantes_projeto

"""Aqui usaremos o Gale-Shapley eu decidi usar como se os alunos fossem os homens que pedem as mãos das mulheres, e elas serem os projetos pq faz mais sentindo na lógica que alunos podem escolher mais de um projeto."""

def asignacao():
    for aluno in alunos:
        print(aluno)
        while aluno not in participantes_projeto.items():
            projeto_quero = alunos[aluno][0]

            if projeto_quero in

asignacao()
