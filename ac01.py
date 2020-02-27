# Atividade Contínua 01
# Aluno 01: Marcos Vinicius 
# Aluno 02: Suelem Suemi 


def adicionar_aluno(alunos, nome, notas):



    for key in alunos:
        if key == nome:
            matriculado = True
            return print(f'O aluno {nome} já está matriculado! {nome}: {alunos[nome]}') 
        else: matriculado = False

    if matriculado == False:
        alunos[nome] = [notas]
        return print(f'O aluno {nome} foi adicionado com sucesso! {alunos}')


def remover_aluno(alunos, nome):
    for key in alunos:
        if key == nome:
            delAluno = key
            alunos.pop(delAluno)
            return print(alunos) 
            
    else:
        print("o aluno não foi encontrado")


def pesquisar_aluno(alunos, nome):
    arr =[]
    for key in alunos:
        if key == nome:
            return print(f'{nome}:{alunos[nome]}')
        else :
            return arr
    
 
def calcular_media(alunos, nome):

    for key in alunos:
        if key == nome:
            media = sum(alunos[nome]) / len(alunos[nome])
            return media
        else:
            return 0


def calcular_media_turma(alunos):
    soma =0
    divisor =0
    for key in alunos:
        num = sum(alunos[key])
        soma += num
        divisor += len(alunos[key])

    return soma/divisor