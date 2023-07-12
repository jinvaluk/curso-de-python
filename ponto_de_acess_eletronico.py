identidade=input("qual é o numero do seu bilhete?")
resultado=identidade.strip()
print(resultado)
base_de_dados={
    "004965392LA041":
               {
                   "nome":"Liria Tomas",
                   "cursos":["Python","Desenvolvimento Web"],
                  "computador": "Mediateca"
               }
}                    


aluna=base_de_dados.get(resultado)

if aluna:
    print ("Aluna foi encontrada com sucesso")
else:
    print ("O BI não corresponde a nenhuma aluna") 
