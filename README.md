# Prueba_Equilibrha
Dado un fichero Excel o CSV (tú eliges cual usar).
Hacer un programa que lea el fichero de datos de empleados y se cargue de forma correcta en un modelo en memoria.
Una vez cargado en memoria indicar por consola:
1. Indicar cuantos hombre y mujeres hay del total de empleado.
2. Indica la suma el salario bruto anual de los empleados de la empresa 1 (Equilibra IT) y el centro de trabajo CT2 (Alovera)
3. Imprime un listado de empleados (id empleado, nombre, apellidos, salario y empresa) de los empleados que cobren más de 28000 euros y que pertenezcan a la empresa 2 (Equilibra RRHH)

## User laucnch

1. Create a virtual environment

    ```Shell
    # Windows
    python -m venv env

    # Mac / Linux
    python3 -m venv env
    ```

2. Activate the virtual environment

    ```Shell
    # Windows
    env\Scripts\activate

    # Mac / Linux
    source ./env/bin/activate
    ```

3. Install dependencies

    ```Shell
    pip install -r requirements.txt
    ```

8. With the virtual environment active, launch the lector_csv.py
