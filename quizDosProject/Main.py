nombre = input("Ingrese el nombre del empleado")
dias = int(input("Ingrese numero dias laborados"))
salario = int(input("Ingrese su salario"))

#calcular la prima
prima = (salario * dias) / 360
#calcular cesantias
cesantias = (salario * dias) / 360
#calcular intereses cesantias
intereses_cesantias = (cesantias * 0.12)/ dias
#calcular vacaciones
vacaciones = (salario * dias) / 720
liquidacion = prima + cesantias + intereses_cesantias + vacaciones

print(f"Señor@ {nombre} para los {dias} dias laborados y {salario}, su liquidacion se compone asi: ")
print (f"Prima: ${prima}")
print (f"cesantias: ${cesantias}")
print(f"intereses cesantias: ${intereses_cesantias}")
print(f"vacaciones: ${vacaciones}")
print(f"total liquidacion: ${liquidacion}")