import random
import string
import os
from datetime import datetime

os.system('cls & title "Secure Password Generator | discord.gg/moonlygg"')

def limpiar_consola():
    """Limpia la consola en función del sistema operativo."""
    os.system("cls" if os.name == "nt" else "clear")

def generar_contrasena(longitud=12, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_simbolos=True):
    # Definir los posibles caracteres que se pueden incluir en la contraseña
    caracteres = ''
    
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase  # Letras mayúsculas
    
    if incluir_minusculas:
        caracteres += string.ascii_lowercase  # Letras minúsculas
    
    if incluir_numeros:
        caracteres += string.digits  # Números
    
    if incluir_simbolos:
        caracteres += string.punctuation  # Símbolos
    
    # Comprobar si se definieron caracteres válidos
    if not caracteres:
        return "No se seleccionaron caracteres válidos para la contraseña."
    
    # Generar la contraseña aleatoria
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return contrasena

def guardar_contrasena(contrasena):
    """Guarda la contraseña generada en un archivo de texto dentro de la carpeta 'output'."""
    # Crear la carpeta 'output' si no existe
    if not os.path.exists("output"):
        os.makedirs("output")
    
    # Crear un nombre de archivo único con la fecha y hora
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    nombre_archivo = f"output/contrasenas_generadas {fecha_hora}.txt"
    
    # Guardar la contraseña en el archivo dentro de la carpeta 'output'
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(f"{contrasena}\n")

def interfaz_usuario():
    print("Generador de Contraseñas Seguras\n")
    
    try:
        longitud = int(input("¿Cuántos caracteres tendrá tu contraseña? (Por defecto es 12): ") or 12)
    except ValueError:
        print("Por favor, ingresa un número válido para la longitud.")
        return
    
    # Modificar las preguntas para usar 'si/no'
    incluir_mayusculas = input("¿Incluir mayúsculas? (si/no): ").lower() == 'si'
    incluir_minusculas = input("¿Incluir minúsculas? (si/no): ").lower() == 'si'
    incluir_numeros = input("¿Incluir números? (si/no): ").lower() == 'si'
    incluir_simbolos = input("¿Incluir símbolos? (si/no): ").lower() == 'si'
    
    contrasena = generar_contrasena(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
    print(f"\nTu contraseña generada es: {contrasena}")
    
    # Guardar la contraseña en un archivo
    guardar_contrasena(contrasena)
    
    # Pedir al usuario que presione Enter para regresar al menú principal
    input("\nPresiona Enter para regresar al menú principal...")
    limpiar_consola()  # Limpiar la consola antes de regresar al menú principal

if __name__ == "__main__":
    while True:
        try:
            limpiar_consola()  # Limpiar la consola al inicio del programa
            interfaz_usuario()
        except KeyboardInterrupt:
            print("\n\nPrograma detenido. ¡Adiós!")
            break
