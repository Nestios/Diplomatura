import random
minusCase="abcdefghijklmnopqrstuvwxyz"
mayusCase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numCase="0123456789"
simCase="@#$%&/\?¿"
uso=minusCase+mayusCase+numCase+simCase
cantPass=int(input("Cuantas Vamos a Crear? : "))
largo=int(input("Que tan larga? : "))
print("Vamos a Generar ",cantPass," Con un largo de ",largo,"carateres.")
conf=input("Estas Seguro? (Y/N).")
if conf=="Y"or conf=="y" :
    for i in range(cantPass):
        pass_final="".join(random.sample(uso,largo))
        print("\nContraseña ",i+1," ha sido Creada:\n\n\t===> ",pass_final)
