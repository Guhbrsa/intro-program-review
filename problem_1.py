def main(Cargo, salario):
  if (Cargo == "Junior") or (Cargo == "junior"):
    print("Seu cargo é de Junior")
    return print(f"O seu novo Salaio sera: R${salario *(1.15):.2f}")
  elif (Cargo == "Pleno") or (Cargo == "pleno"):
    print("Seu cargo é de Pleno")
    return print(f"O seu novo Salaio sera: R${salario *(1.26):.2f}")
  elif (Cargo == "Senior") or (Cargo == "senior"):
    print("Seu cargo é de Senior")
    return print(f"O seu novo Salaio sera: R${salario *(1.34):.2f}")
  else:
    print("-1")

main (input("Digite o seu cargo(Junior,Pleno ou Senior): "), float(input("Digite o valor do seu salario: ")))

#Outra maneira

# def main(Cargo, salario):
#   if (Cargo == "Junior") or (Cargo == "junior"):
#     aumento = salario * 1.15
#     print(f"Seu cargo é de Junior")
#     return aumento
#   elif (Cargo == "Pleno") or (Cargo == "pleno"):
#     aumento = salario * 1.26
#     print(f"Seu cargo é de Pleno")
#     return aumento
#   elif (Cargo == "Senior") or (Cargo == "senior"):
#     aumento = salario * 1.34
#     print(f"Seu cargo é de Senior")
#     return aumento
#   else:
#     print("-1")

# main (input("Digite o seu cargo(Junior,Pleno ou Senior): "), float(input("Digite o valor do seu salario: ")))