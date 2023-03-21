x = int(input("Qual a largura da placa?\nR: "))
y = int(input("Qual o comprimento da laca?\nR: "))
m = int(input("Qual a quantidade de pedidos?\nR: "))
for linhas in range(0, m):
    xi = int(input("Qual a largura do pedal?\nR: "))
    yi = int(input("Qual o comprimento do pedal?\nR: "))
    cabe = 1
    if (xi > x and xi > y):
        cabe = 2
    if (yi > y and yi > x):
        cabe = 2
    if cabe == 1:
        print("Esse pedal cabe na placa")
    else:
        print("Esse pedal não cabe na placa")