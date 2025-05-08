#

print("pizzaria dos guri - seja bem vindo")
print("_____CARDÁPIO - PREÇOS_____")
print(" ")
print("*****PIZZAS - SABORES*****")
print("CALABREZA,FRANGO,CATUPIRY")
print("*******PIZZAS - TAMANHOS*****")
print(" PIZZA PEQUENA: R$ 12.90 ")
print(" PIZZA MÉDIA: R$ 16.90 ")
print(" PIZZA GRANDE: R$ 19.90 ")
print("*****REFRIGERANTES*****")
print(" COCA-COLA R$ 5.50 ")
print(" GUARANÁ R$ 7.50 ")
print(" FANTA R$ 3.00 ")
print("__________________")
print(" ")
print("FAÇA O SEU PEDIDO PARA PIZZA:")
print("1 - CALABREZA")
print("2 - FRANGO")
print("3 - CATUPIRY")
print("__________________")

pedidopizza = int(input())
print("DIGITE O TAMANHO DA PIZZA:")
print("P - PEQUENA")
print("M - MÉDIA")
print("G - GRANDE")
print("________________")

tampizza = input().upper()

print("FAÇA O SEU PEDIDO PARA REFRIGERANTE:")
print("1 - COCA-COLA")
print("2 - GUARANÁ")
print("3 - FANTA")
print("_________________")

pedidorefri = int(input())

if(pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 1):
    precopagar = 12.90 + 5.50
    pedidos = "CALABREZA - P - COCA-COLA"

elif(pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 1):
    precopagar = 16.90 + 5.50
    pedidos = "FRANGO - M - COCA-COLA"

elif(pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 19.90 + 5.50
    pedidos = "CALABREZA - G - COCA-COLA"

elif(pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 2):
    precopagar = 12.90 + 7.50
    pedidos = "CALABREZA - P - GUARANÁ"

elif(pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 3):
    precopagar = 12.90 + 3.00
    pedidos = "CALABREZA - P - FANTA"

elif(pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 1):
    precopagar = 12.90 + 5.50
    pedidos = "FRANGO - P - COCA-COLA"

elif(pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 1):
    precopagar = 12.90 + 5.50
    pedidos = "CATUPIRY - P - COCA-COLA" 

elif(pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 1):
    precopagar = 16.90 + 5.50
    pedidos = "CATUPIRY - M - COCA-COLA"    

elif(pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 19.90 + 5.50
    pedidos = "CALABREZA - G - COCA-COLA" 

elif(pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 1):
    precopagar = 16.90 + 5.50
    pedidos = "FRANGO - M - COCA-COLA"  

elif(pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 16.90 + 5.50
    pedidos = "FRANGO - G - COCA-COLA"

elif(pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 2):
    precopagar = 16.90 + 7.50
    pedidos = "FRANGO - P - GUARANÁ"

elif(pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 3):
    precopagar = 12.90 + 3.00
    pedidos = "FRANGO - P - FANTA"

elif(pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 1):
    precopagar = 12.90 + 5.50
    pedidos = "CATUPIRY - P - COCA-COLA"

elif(pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 2):
    precopagar = 12.90 + 7.50
    pedidos = "CATUPIRY - P - GUARANÁ"

elif(pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 3):
    precopagar = 12.90 + 3.00
    pedidos = "CALABREZA - P - FANTA"   

elif(pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 3):
    precopagar = 19.90 + 3.00
    pedidos = "CATUPIRY - M - FANTA"

elif(pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 3):
    precopagar = 19.90 + 3.00
    pedidos = "CATUPIRY - G - FANTA"
else:
    precopagar = 0.0
    pedidos = "PEDIDO NÃO ENCONTRADO"

print ("_________________")
print (f"O TOTAL A PAGAR É R$ {precopagar:.2f}")
print ("_________________")
print (f"OS PEDIDOS FORAM {pedidos}")
print ("_________________")
print ("BOM APETITE E SEJA BEM VINDO GURI")