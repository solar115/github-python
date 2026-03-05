import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

senha = int(input("qual vai ser o tamanaho da senha?"))
senhas = ""


for i in range(senha):
    randomsenha = random.choice(caracteres)
    senhas += randomsenha

print(senhas)
