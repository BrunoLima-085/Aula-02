num = float(input("\nDigite um número qualquer: "))

if num % 2 == 0:
    print(f"\nO número {num} é par")
else:
    print(f"\nO número {num} é ímpar") 

if num > 0:
    print(f"\nO número {num} é positivo")
elif num < 0:
    print(f"\nO número {num} é negativo")
else:
    print(f"\nO número é zero, não sendo positivo ou negativo")