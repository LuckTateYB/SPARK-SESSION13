# -*- coding: utf-8 -*-
"""Media

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mMWm1S0zPW4hjLMo9bNBuQd2_McxEAl6
"""

#Vamos a utilizar un excel donde tendremos dos columnas. Almno y Nota.
#Implementaremos PySpark para analizar la media en la lista de estudiantes
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, mean, corr

spark = SparkSession.builder.appName("estadistica").getOrCreate()
spark

#Cargaremos los datos de los estudiantes, nombres y notas y luego podremos analizar el promedio del salón
#Una vez encontrado el promedio de la clase, veremos si es necesaria una clase de reforzamiento.
#Tambien podemos hacer una comparación con otras clases y ver el rendimiento de ellas
data = [("Elvis",12),("Juan",18),
        ("Ronaldo",20),("Pablo",18),
         ("Alexis",14),("Cris",20),
          ("Ana",13),("Carlos",15),
           ("Fabian",15),("Carla",14),
            ("Fabiola",12),("Adriana",16),
             ("Fatima",20)]
columns = ["Nombre", "Nota"]
variable = spark.createDataFrame(data,columns)

variable.select(mean(col("Nota")).alias("Media")).show()