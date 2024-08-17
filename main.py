numero = int(input("digiite um numero de 1 a 10: ") )
if 1 <= numero <= 10:
  for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")
  else:
    print("numero invaido. digite um numero de 1 a 10")