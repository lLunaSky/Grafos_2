from proj_alum import alunos, projetos, participantes_projeto

"""Aqui usaremos o Gale-Shapley eu decidi usar como se os alunos fossem os homens que pedem as mãos das mulheres, e elas serem os projetos pq faz mais sentindo na lógica que alunos podem escolher mais de um projeto. Esse algoritmo é uma base, eh preciso que sejam selecionados o sprojeto e ver se a nota dos alunos é sulficiente e se ha vagas. Mas esse algoritmo faz uma seleção. Poemos construir o resto a partir dele."""

def asignacao(alunos, projetos, participantes_projeto):
    #Estado atual
    alunos_livres = list(alunos.keys())
    #chamamos participantes_projeto
    propostas = {al: [] for al in alunos}

    while alunos_livres:
        aluno = alunos_livres[0]
        
        for projeto in alunos[aluno]:
            if projeto not in propostas[aluno]:
                propostas[aluno].append(projeto)
                #Se o projeto esta livre ent da match

                if projeto not in participantes_projeto.values():
                    participantes_projeto[aluno] = projeto
                    alunos_livres.pop(0)
                    break

                else:
                    outro_aluno = [al for al, proj in participantes_projeto.items() if proj == projeto][0]
                    if projetos[projeto].index(aluno) < projetos[projeto].index(outro_aluno):
                        # Projeto prefere outro aluno
                        participantes_projeto[aluno] = projeto
                        alunos_livres.pop(0)
                        alunos_livres.append(outro_aluno)
                        del participantes_projeto[outro_aluno]
                        break
                    else:
                        # Projeto prefere o atual
         
                        continue
    return participantes_projeto


resultado = asignacao(alunos, projetos, participantes_projeto)
print("Pares estáveis:")
for aluno, projeto in resultado.items():
    print(f"{aluno} - {projeto}")