import streamlit as st
import pandas as pd
import csv




# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")

st.subheader("Actividad #1. Crea DataFrames desde diferentes fuentes")
st.subheader("Objetivo de la actividad ")
st.markdown("Familiarizarse con la creación de DataFrames en Pandas y mostrarlos usando Streamlit.")
# ejercicio 1#
st.header("Crea DataFrames desde Diccionario")
st.write("DataFrame de Libros")

code = '''
datos = {"Titulo": ["Cien años de soledad", "El Alquimista", "El principito","Algebra"],
         "Autor": ["Gabriel García Márquez", "Paulo Coelho", "Antoine de Saint-Exupéry","Aurelio Baldor"],
         "Año de publicacion": ["1967 ","1988","1943","1941"],
         "Genero": ["Ficcion", "Drama", "Fabula", "Ciencia"]}
df = pd.DataFrame(datos)
st.dataframe(df)
    '''
st.code(code, language="python")
st.write("Resultado del codigo")

datos = {"Titulo": ["Cien años de soledad", "El Alquimista", "El principito","Algebra"],
         "Autor": ["Gabriel García Márquez", "Paulo Coelho", "Antoine de Saint-Exupéry","Aurelio Baldor"],
         "Año de publicacion": ["1967 ","1988","1943","1941"],
         "Genero": ["Ficcion", "Drama", "Fabula", "Ciencia"]}
df = pd.DataFrame(datos)
st.dataframe(df)

# ejercicio 2 #
st.header("Crea DataFrames desde Lista de diccionarios")
st.write("DataFrame de Información de Ciudades")

code ='''
paises = [{"Nombre": "Medellin", "Poblacion": "2.533.424", "Pais": "Colombia"},
          {"Nombre": "Paris", "Poblacion": "2 087 577", "Pais": "Francia"},
          {"Nombre": "Caracas", "Poblacion": "7 826 165 ", "Pais": "Venezuela"}]
df = pd.DataFrame(paises)
st.dataframe(df)
'''
st.code(code, language="python")
st.write("Resultado del codigo")

paises = [{"Nombre": "Medellin", "Poblacion": "2.533.424", "Pais": "Colombia"},
          {"Nombre": "Paris", "Poblacion": "2 087 577", "Pais": "Francia"},
          {"Nombre": "Caracas", "Poblacion": "7 826 165 ", "Pais": "Venezuela"}]
df = pd.DataFrame(paises)
st.dataframe(df)

# ejercicio 3 #

st.header("Crea DataFrames desde Listas de Listas")
st.write("DataFrame de Productos en Inventario")
code ='''
productos = [["Rubor", "25.000","3"],
             ["Pestañina", "10.000","5"],
             ["Labial", "8.000", "4"]]
df = pd.DataFrame(productos, columns=["Nombre", "Pecio", "stock "])
st.dataframe(df)
'''
st.code(code, language="python")
st.write("Resultado del codigo")

productos = [["Rubor", "25.000","3"],
             ["Pestañina", "10.000","5"],
             ["Labial", "8.000", "4"]]
df = pd.DataFrame(productos, columns=["Nombre", "Pecio", "stock "])
st.dataframe(df)

# ejercicio 4 #

st.header("Crea DataFrames desde Series")
st.write("DataFrame de Datos de Personas")
code ='''
nombres = pd.Series(['Daniela', 'Maria', 'Andres'])
edades = pd.Series([27, 30, 40])
ciudades = pd.Series(['Cucuta', 'Roma', 'Bogota'])

personas = pd.DataFrame({'Nombre': nombres, 'Edad': edades, 'Ciudad': ciudades})
st.dataframe(personas)
'''
st.code(code, language="python")
st.write("Resultado del codigo")


nombres = pd.Series(['Daniela', 'Maria', 'Andres'])
edades = pd.Series([27, 30, 40])
ciudades = pd.Series(['Cucuta', 'Roma', 'Bogota'])

personas = pd.DataFrame({'Nombre': nombres, 'Edad': edades, 'Ciudad': ciudades})
st.dataframe(personas)

# ejercicio 5 #

st.header("Crea DataFrames desde Archivo CSV (local):")
st.write("DataFrame de Datos desde CSV")
code ='''
column_names = ["Id", "Nombre", "Valor"]

data = [
    ["111", "Mango","2.000"],
    ["222", "Pera", "1.000"],
    ["333", "Fresa", "5.000"]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(column_names)

    for row in data:
        writer.writerow(row)

df = pd.read_csv("data.csv")

st.dataframe(df)

'''
st.code(code, language="python")
st.write("Resultado del codigo")

column_names = ["Id", "Nombre", "Valor"]

data = [
    ["111", "Mango","2.000"],
    ["222", "Pera", "1.000"],
    ["333", "Fresa", "5.000"]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(column_names)

    for row in data:
        writer.writerow(row)

df = pd.read_csv("data.csv")

st.dataframe(df)

# ejercicio 6 #
