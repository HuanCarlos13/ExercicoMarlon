# #questão 1
metro = float(input(f"Digite o metro: "))
Converter = (metro)/100
print(f"O valor convertido é:{Converter}")

# #questão 2
sexo = input(f"Digite seu sexo (F) para feminino ou (M) Para masculino:").upper()
print(type(sexo))
if sexo == "M":
        print("Seu sexo é masculino")
elif sexo == "F":
        print("Seu sexo é Feminino")
else:
        print("Sexo invalido")


#Questão 3
print("fazer Cadastro")
usuario= input(f"Nome do Usuario:")
senha= input(f"Sua Senha:")

while usuario == senha :
    print(f"Usuario e senha não pode ser iguais, tente novamente")
    usuario = input("Nome do usuario:")
    senha = input("Sua Senha:")
    

else:
    print("Usuario cadastrado com sucesso")





