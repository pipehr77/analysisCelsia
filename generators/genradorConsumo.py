import random
def generarDatos():
    datos = []
    for i in range(5000):
        dato={}
        id=random.randint(1,10000)
        referencia=random.choice(["ACH01","ACH02","ACH03"])
        marca=random.choice(["SONY","SAMSUNG","KALLEY"])
        capacidad=random.randint(100,2000)
        ciudad=random.choice(["Bogota", "Cali", "Bucaramanga", "Titiribi", "Saragoza"])
        responsable=random.choice(["Benavides","Sacarias","Armando","Romulo", "Ortencio"])

        dato=[id,referencia,marca,capacidad,ciudad,responsable]
        datos.append(dato)
    return datos
print(generarDatos())