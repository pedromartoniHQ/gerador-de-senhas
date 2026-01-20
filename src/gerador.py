import random
import string  
#irei importar a biblioteca string para facilitar a geração de caracteres especiais
def gerar_senhas(TAMANHO):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    #ESCOLHERA CARACTERES ALEATORIOS E JUNTAR
    senha = ''.join(random.choice(caracteres) for _ in range(TAMANHO))
    return senha
#---PARTE CENTRAL DO SISTEMA
print("---BEM VINDO AO GERADOR DE SENHAS---")

try:
    qtd = int(input("digite o tamanho da senha que voce deseja:"))
    senha_final = gerar_senhas(qtd)
    print(f"\nsua senha segura é:{senha_final}")
except ValueError:
    # Se o usuário digitar uma letra, o Python cai aqui em vez de dar erro
    print("Erro: digite um número válido!")

  

