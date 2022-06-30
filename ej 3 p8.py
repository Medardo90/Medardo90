#Autor; Patricio Haro
A=int(input("Ingrese A: "))
B=int(input("Ingrese B: "))
C=int(input("Ingrese C: "))
print("\n")
if B < A > C:
    print("Número mayor: ",A)
if A < B > C:
    print("Número mayor: ",B)   
if A < C > B:
    print("Número mayor:",C)
