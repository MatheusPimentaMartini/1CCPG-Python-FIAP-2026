temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]
nun_sala = 1
qtd_max = 0
sala_max = 0
for sala in temperaturas:
    print()
    print("SALA",nun_sala )
    
    
    print(sum(sala)/len(temperaturas))
    qtd = 0
    for temp in sala:
        if temp >= 33:
            qtd += 1
    print(qtd)
    print()

    if qtd > qtd_max:
        qtd_max = qtd
        sala_max = nun_sala
    nun_sala += 1
print(f"Sala com maior risco: {sala_max}")
 

print()
