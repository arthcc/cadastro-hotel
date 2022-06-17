from ast import For
from datetime import datetime
from distutils.log import error
from errno import errorcode
import re

formatar_data = None
global check_in
global chech_out
global numero_de_criancas

lista_clientes = []
lista_funcionarios = []
tipo_quarto = []

#Listas com as Variáveis de Cliente, Quartos e Funcionários

class Endereco():
    def __init__(self, cidade, bairro, rua, numero, complemento, cep):
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.cep = cep


class Cliente():
    def __init__(self, nome, cpf, email, celular, endereco, quantidade_de_pessoas, tem_criancas, numero_de_criancas,
               check_in, check_out, quantidade_de_quartos, quarto):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.celular = celular
        self.Endereco = endereco
        self.quantidade_de_pessoas = quantidade_de_pessoas
        self.tem_criancas = tem_criancas
        self.numero_de_criancas = numero_de_criancas
        self.check_in = check_in
        self.check_out = check_out
        self.quantidade_de_quartos = quantidade_de_quartos
        self.quarto = quarto

endereco1 = Endereco("País das maravilhas", "Docelândia", "Rua do gnomos", 3, "Pertinho da maiceira de algodão doce", 123456789)        
cliente1 = Cliente("Alice", 14017674780, "alice@gmail.com", 21972303355, endereco1, 3, False, 0, "2022-01-21 12:00:00", "2022-02-21 12:00:00", 1, "solteiro")
        
lista_clientes.append(cliente1)

def cadastrar_endereco():
    cidade=str(input("Digite sua Cidade: "))
        
    bairro=str(input("Digite seu Bairro: "))
    rua=str(input("Digite sua Rua: "))
   
    numero = None
    while numero == None:
        try:
            numero = float (input("Numero: "))
        except ValueError:
            print("Digite um valor númerico! ")    
    complemento=str(input("Digite seu complemento: "))
    cep = input("Cep: ")
    while len(cep) < 8 or len(cep) > 8:
        print("O CEP precisa ter 8 dígitos!")
        cep = input("Digite Novamente: ")
    else:
        print("CEP Válido!")
        
    return Endereco(cidade, bairro, rua, numero, complemento, cep)

def cadastrar_novo_cliente(lista_clientes, Cliente):
    global numero_de_criancas
    print("Vamos começar o Processo de Cadastro!")
    nome_novo_cliente = input("\nNome: ")
    
    cpf_novo_cliente = cadastrar_cpf()   
     
    email_novo_cliente = input("\nEmail: ")
    celular_novo_cliente = cadastrar_celular()
    
    print("\nAgora vamos gravar o seu endereço!")
    endereco = cadastrar_endereco()
    
    quantidade_de_pessoas = input ("\nQuantos adultos? Informe aqui: ")
    print ("Quarto para crianças?")
    tem_criancas = (input(" 1- Sim \n 2- Não \nDigite sua opção: ")) 
    if tem_criancas == "1":
        numero_de_criancas = input("Quantas crianças? Informe aqui: ")
    else:
        print("Nenhuma criança informada!")
        numero_de_criancas = 0
    #Validação do Check In
    check_in, check_out = cadastrar_datas()
                
    quantidade_de_quartos = int(input("\nDigite o número de quartos: "))
    while (quantidade_de_quartos > 0):
        tipo_quarto.append (input("\nVocê deseja quarto de 1 - Solteiro, 2 - casal ou 3- Premium?\nDigite ao lado sua opção: "))
        
        quantidade_de_quartos = quantidade_de_quartos - 1

    novo_cliente = Cliente(nome_novo_cliente,
                           cpf_novo_cliente,
                           email_novo_cliente,
                           celular_novo_cliente,
                           endereco,
                           quantidade_de_pessoas,
                           tem_criancas,
                           numero_de_criancas,
                           check_in,
                           check_out,
                           quantidade_de_quartos,
                           tipo_quarto
                           )

    lista_clientes.append(novo_cliente)
    return print(f"Cadastro feito com sucesso {novo_cliente.nome}!" )

def cadastrar_datas():
    print("Qual a data do Check In?")
    formatar_data = "%d/%m/%Y"
    check_in = None
    while check_in == None:
        try:
            check_in = datetime.strptime(input("Digite a data em [dd/mm/aaaa]: "),formatar_data)
        except ValueError:
            print("A Data precisa estar escrita em Dia (1 a 31), Mês (1 a 12) e Ano!")    
    
    #Validação do Check Out 
    print("Qual a data de Check Out?")
    formatar_data = "%d/%m/%Y"
    check_out = None
    while check_out == None:
        try:
            check_out = datetime.strptime(input("Digite a data em [dd/mm/aaaa]: "),formatar_data)
            
            if check_in > check_out:
                raise NameError()
            
            
        except ValueError:
            print("A Data precisa estar escrita em Dia (1 a 31), Mês (1 a 12) e Ano")
        except NameError:
            print("A data de de Check In deve ser menor que de Check Out")    
            check_out = None
            
    return check_in,check_out

def cadastrar_celular():
    celular_novo_cliente = input('Digite o número do Telefone Celular [DDD] (9)(XXXX-XXXX): ' )
    try:
        while len(celular_novo_cliente) >= 0 and len(celular_novo_cliente) < 11:
            raise ValueError
        else:
            celular_novo_cliente = int(celular_novo_cliente)
            celular_novo_cliente = str(celular_novo_cliente)
            celular = celular_novo_cliente
            telFormatado = '({}) {}-{}-{}'.format(celular[0:2],
                            celular[2] ,celular[3:7], celular[7:])
            print(f"O número de telefone salvo foi: {telFormatado}")

    except ValueError:
        while len(celular_novo_cliente) != 11:            
            print('Número inválido, o número precisa ter 11 números inteiros')
            celular_novo_cliente = input("Digite Novamente: ")
            celular= celular_novo_cliente
            celular = celular_novo_cliente
            telFormatado = '({}) {}-{}-{}'.format(celular[0:2],
                            celular[2] ,celular[3:7], celular[7:])
        else:
            print(f'O número {telFormatado} é válido!')
    return celular_novo_cliente

def cadastrar_cpf():
    cpf_novo_cliente = None
    while cpf_novo_cliente == None:
        try:
            cpf_novo_cliente=float(input("Digite seu CPF: "))
        except ValueError:
            print("O CPF precisa ser digitado em números! Por favor tente novamente!")
    return cpf_novo_cliente

while True:
    print("---------------------HOTEL DOS CRIA---------------------")
    print("\n Deseja fazer o check-in?")
    
    cliente_ou_funcionario = input (" 1- Cadastrar Check-in\n 2- Mostrar clientes\n Digite sua opção: ")
    print("\n")
    
    if cliente_ou_funcionario == "1" or cliente_ou_funcionario.lower() == "mostrar clientes":
          cadastrar_novo_cliente(lista_clientes, Cliente)     
    else:
        for cli in lista_clientes:
            print(f"Nome: {cli.nome}  | Check-in: {cli.check_in}  | Check-out: {cli.check_out}\n")