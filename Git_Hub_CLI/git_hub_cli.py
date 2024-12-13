import os
import subprocess
import sys

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.stderr.decode('utf-8')

def is_git_repository():
    try:
        subprocess.run("git status", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def is_valid_git_branch(branch_name):
    # Validación básica para nombres de ramas
    return branch_name and not any(c in branch_name for c in [' ', '/', '\\', ':', '*', '?', '"', '<', '>', '|'])

def paginated_output(output, lines_per_page=10):
    lines = output.splitlines()
    for i in range(0, len(lines), lines_per_page):
        print("\n".join(lines[i:i + lines_per_page]))
        if i + lines_per_page < len(lines):
            input("Presiona Enter para continuar...")

def set_working_directory():
    path = input("Introduce el directorio de trabajo: ")
    try:
        os.chdir(path)
        print(f"Directorio de trabajo cambiado a {path}")
    except FileNotFoundError:
        print("Directorio no encontrado")

def create_repository():
    print(run_command("git init"))

def check_remote_repository():
    if not is_git_repository():
        print("No estás en un repositorio de Git. Por favor, inicializa uno primero.")
        return

    output = run_command("git remote -v")
    if output.strip():
        print("Repositorios remotos configurados:")
        print(output)
    else:
        print("No hay repositorios remotos configurados.")

def create_branch():
    if not is_git_repository():
        print("No estás en un repositorio de Git. Por favor, inicializa uno primero.")
        return

    branch_name = input("Introduce el nombre de la nueva rama: ")
    if not is_valid_git_branch(branch_name):
        print("Nombre de rama no válido. Intenta de nuevo.")
        return

    print(run_command(f"git branch {branch_name}"))

def switch_branch():
    if not is_git_repository():
        print("No estás en un repositorio de Git. Por favor, inicializa uno primero.")
        return

    branch_name = input("Introduce el nombre de la rama a la que quieres cambiar: ")
    if not is_valid_git_branch(branch_name):
        print("Nombre de rama no válido. Intenta de nuevo.")
        return

    print(run_command(f"git checkout {branch_name}"))

def show_pending_files():
    if not is_git_repository():
        print("No estás en un repositorio de Git. Por favor, inicializa uno primero.")
        return

    print(run_command("git status"))

def make_commit():
    if not is_git_repository():
        print("No estás en un repositorio de Git. Por favor, inicializa uno primero.")
        return

    message = input("Introduce el mensaje del commit: ")
    print(run_command("git add ."))
    print(run_command(f"git commit -m \"{message}\""))

def show_commit_history():
    if not is_git_repository():
        print("No estás en un repositorio de Git. Por favor, inicializa uno primero.")
        return

    paginated_output(run_command("git log"))

def delete_branch():
    if not is_git_repository():
        print("No estás en un repositorio de Git. Por favor, inicializa uno primero.")
        return

    branch_name = input("Introduce el nombre de la rama a eliminar: ")
    if not is_valid_git_branch(branch_name):
        print("Nombre de rama no válido. Intenta de nuevo.")
        return

    print(run_command(f"git branch -d {branch_name}"))

def set_remote_repository():
    if not is_git_repository():
        print("No estás en un repositorio de Git. Por favor, inicializa uno primero.")
        return

    remote_url = input("Introduce la URL del repositorio remoto: ")
    print(run_command(f"git remote add origin {remote_url}"))

def pull_changes():
    if not is_git_repository():
        print("No estás en un repositorio de Git. Por favor, inicializa uno primero.")
        return

    print(run_command("git pull"))

def push_changes():
    if not is_git_repository():
        print("No estás en un repositorio de Git. Por favor, inicializa uno primero.")
        return

    print(run_command("git push"))

def configure_user():
    name = input("Introduce tu nombre de usuario: ")
    email = input("Introduce tu correo electrónico: ")
    print(run_command(f"git config --global user.name \"{name}\""))
    print(run_command(f"git config --global user.email \"{email}\""))

def main():
    while True:
        print("\nOpciones:")
        print("1. Establecer el directorio de trabajo")
        print("2. Crear un nuevo repositorio")
        print("3. Crear una nueva rama")
        print("4. Cambiar de rama")
        print("5. Mostrar ficheros pendientes de hacer commit")
        print("6. Hacer commit (junto con un add de todos los ficheros)")
        print("7. Mostrar el historial de commits")
        print("8. Eliminar rama")
        print("9. Establecer repositorio remoto")
        print("10. Ver repositorios remotos configurados")
        print("11. Hacer pull")
        print("12. Hacer push")
        print("13. Configurar nombre de usuario y correo electrónico")
        print("14. Salir")

        choice = input("Selecciona una opción: ")

        if choice == '1':
            set_working_directory()
        elif choice == '2':
            create_repository()
        elif choice == '3':
            create_branch()
        elif choice == '4':
            switch_branch()
        elif choice == '5':
            show_pending_files()
        elif choice == '6':
            make_commit()
        elif choice == '7':
            show_commit_history()
        elif choice == '8':
            delete_branch()
        elif choice == '9':
            set_remote_repository()
        elif choice == '10':
            check_remote_repository()
        elif choice == '11':
            pull_changes()
        elif choice == '12':
            push_changes()
        elif choice == '13':
            configure_user()
        elif choice == '14':
            sys.exit()
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()