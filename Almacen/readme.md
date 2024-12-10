# Amazon Code Breaker 🏢📦

Amazon tiene que comenzar a repartir paquetes, ¡pero ha olvidado el código secreto de apertura del almacén!  
Tu misión es ayudarles a descifrar el código en 10 intentos o menos.

## Descripción del Problema
- **Código Secreto**:
  - Es una combinación aleatoria de letras y números de longitud 4:
    - **Letras**: A, B, C.
    - **Números**: 1, 2, 3.
  - No se permiten caracteres repetidos.
  - Se genera de forma aleatoria al iniciar el programa.

- **Reglas para el Usuario**:
  - Tienes **10 intentos** para adivinar el código.
  - En cada intento, deberás ingresar un código de **4 caracteres**.
  - El programa te indicará por cada carácter:
    - **Correcto**: El carácter está en la posición correcta.
    - **Presente**: El carácter existe, pero no está en la posición correcta.
    - **Incorrecto**: El carácter no existe en el código secreto.
  - **Control de errores**:
    - Los códigos deben tener exactamente 4 caracteres.
    - Solo se permiten letras de la A a la C y números del 1 al 3.

- **Finalización**:
  - **Victoria**: Si descifras el código antes de 10 intentos.
  - **Derrota**: Si fallas, Amazon no podrá repartir los regalos.


