import os

def sumar():
    # Valores de ejemplo para la suma
    num1 = 10
    num2 = 5
    resultado = num1 + num2
    
    print("=" * 40)
    print(" EJECUCIÓN DE SCRIPT PYTHON - GITHUB ACTIONS ")
    print("=" * 40)
    print(f"El resultado de sumar {num1} + {num2} es: {resultado}")
    
    # Muestra el mensaje del commit si se está ejecutando desde GitHub Actions
    commit_msg = os.environ.get('COMMIT_MESSAGE')
    if commit_msg:
        print(f"Mensaje del commit actual: {commit_msg}")
    print("=" * 40)

if __name__ == "__main__":
    sumar()