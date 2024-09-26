peso = float(input("\nDigite seu peso: "))
altura = float(input("\nDigite sua altura: "))

imc = peso / (altura ** 2)
if imc < 18.5:
        print(f"\nSeu IMC é {imc: .2f}. Você está abaixo do peso")
elif 18.5 <= imc < 24.9:
        print(f"\nSeu IMC é {imc: .2f}. Você está no peso ideal")
elif 25 <= imc < 29.9:
        print(f"\nSeu IMC é {imc: .2f}. Você está com sobrepeso")
else:
        print(f"\nSeu IMC é {imc: .2f}. Você está com obesidade")

#print (imc)