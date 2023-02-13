
def average_of_subject(subject):

    print(f"Ingrese las notas de {subject}:")
    tcp1 = float(input("Primer TCP: "))
    tcp2 = float(input("Segundo TCP: " ))
    tcp3 = float(input("Prueba Final: " ))

    return round((tcp1 + tcp2 + tcp3) / 3, 2)



math_average = average_of_subject("Matemáticas")
spanish_average = average_of_subject("Español")
physics_average = average_of_subject("Física")
biology_average = average_of_subject("Biología")
hostory_average = average_of_subject("Historia de Cuba")


total_average = round((math_average + spanish_average + physics_average + 
biology_average + hostory_average) / 5, 2)


print(f"\n Tu promedio en Matemáticas es: {math_average}")
print(f"\n Tu promedio en Español es: {spanish_average}")
print(f"\n Tu promedio en Física es: {physics_average}")
print(f"\n Tu promedio en Bilogía es: {biology_average}")
print(f"\n Tu promedio en Historia es: {hostory_average}")

print(f"\n xc  {total_average}")
