#listas
funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sofia', 'Bruno', 'Melissa']
turno_diurno = ['Ana', 'Marcos', 'Alice','Melissa']
turno_noturno = ['Pedro', 'Sofia', 'Bruno']
funcionarios_com_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

print(f"Funcionários no turno diurno que possuem carro: {set(turno_diurno).intersection(funcionarios_com_carro)}")
print(f"Funcionários no turno noturno que possuem carro: {set(turno_noturno).intersection(funcionarios_com_carro)}")
print(f"Funcionários que não possuem carro: {set(funcionarios).difference(funcionarios_com_carro)}")