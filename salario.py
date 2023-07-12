salarios=float (input("Informe o seu salario: "))
if salarios < 128000:
    percentagem=0.2
    aumento=salarios*percentagem
    novo_salario=salarios+aumento
elif salarios>=128000 and salarios<=500000:
    percentagem=0.15
    aumento=salarios*percentagem
    novo_salario=salarios+aumento
elif salarios>=500000 and salarios<=1000000:
     percentagem=0.1
     aumento=salarios*percentagem
     novo_salario=salarios+aumento
else:
    percentagem=0.05
    aumento=salarios*percentagem
    novo_salario=salarios+aumento
print("Salario antes do reajuste: ",salarios)
print("Percentagem: ", percentagem)
print("Aumentoa ser aplicado: ",aumento)
print("Novo salario: ", novo_salario)
