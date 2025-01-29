# [PY-A11] Você foi contratado para desenvolver o software de controle de um elevador inteligente. 
# A classe Elevador foi criada para modelar esse sistema e possui os seguintes atributos:
# totalCapacidade, atualCapacidade, totalAndar e atualAndar, que representam, respectivamente,
# a capacidade máxima do elevador, a capacidade atual, o total de andares do prédio e o andar atual do elevador.
# A classe Elevador também possui os seguintes métodos:
# Subir(): caso o elevador não esteja no andar mais alto, o método incrementa o número do andar atual e exibe "Subindo".
# Caso contrário, exibe "VOCÊ ESTÁ NO ANDAR MAIS ALTO!".
# Descer(): caso o elevador não esteja no térreo, o método decrementa o número do andar atual e exibe "Descendo".
# Caso contrário, exibe "VOCÊ JÁ ESTÁ NO TÉRREO!".
# Entrar(): caso a capacidade atual do elevador não tenha sido atingida,
# o método incrementa o número de pessoas presentes no elevador e exibe "Entrando uma pessoa". 
# Caso contrário, exibe "O ELEVADOR ESTÁ CHEIO!".
# Sair(): caso haja pelo menos uma pessoa no elevador,
# o método decrementa o número de pessoas presentes e exibe "Saindo uma pessoa". Caso contrário, exibe "NÃO TEM NINGUÉM".
import time

class Elevador:
    def __init__(self):
        self.total_capacidade = 6
        self.atual_capacidade = 0
        self.total_andar = 10
        self.atual_andar = 0

    def subir(self, destino ):
        if self.atual_andar < self.total_andar:
            self.atual_andar += destino
            print('Subido')
        elif self.atual_andar == self.total_andar:
            print('Não é possivel subir, estamos no último andar.')
        elif self.atual_andar < destino:
            print('Aperte o botão descer.')
        elif self.atual_andar == destino:
            print(f'Você chegou no andar desejado.')
        else:
            print('Andar indisponivel!.')
        time.sleep(1)

    def descer(self, destino):
        if self.atual_andar > 0:
            self.atual_andar -= destino
            print('Descendo.')
        elif self.atual_andar == 0:
            print('Você  está no Terreo.')
        else:
            print('Andar Indisponivel')
        time.sleep(1)

    def entrar(self):
        if self.atual_capacidade < self.total_capacidade:
            self.atual_capacidade += 1
            print('Entrando uma pessoa.')
        elif self.atual_capacidade == self.total_capacidade:
            print('O Elevador está cheio!')
        time.sleep(1)    
            
    def sair(self):
        if self.atual_capacidade > 0:
            self.atual_capacidade -= 1
            print('Saindo uma pessoa.')
        elif self.atual_capacidade == 0:
            print('O elevador está vazio!')
        time.sleep(1)    

    def mostrar_andar_atual(self):
        print(f'Você está no {self.atual_andar} andar.')
        time.sleep(1)

elevador = Elevador()

while True:

    print('Menu Elevador:')
    print('1 -- Entrar')
    print('2 -- Subir')
    print('3 -- Descer')
    print('4 -- Sair')
    print('5 -- Visualizar Andar')
    opcao = input('Informe a opção desejada (1 ao 5): ')

    match opcao:
        case '1':
            elevador.entrar()

        case '2':
            andar_subir = int(input('Informe o andar (1 ao 10): '))
            elevador.subir(andar_subir)

        case '3':
            andar_descer = int(input('Informe o andar (1 ao 9): '))
            elevador.descer(andar_descer)

        case '4':
            elevador.sair()  

        case '5':
            elevador.mostrar_andar_atual() 