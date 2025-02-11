# -*- coding: utf-8 -*-
"""Correlación

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Jrs17ntVnliE2qh0XN94vb7bjzFxHQ1r
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, mean, corr

spark = SparkSession.builder.appName("estadistica").getOrCreate()
spark

#Utilizaremos la correlación para poder saber que estudiantes tienen mejores notas con respecto a los cursos
#En este caso manejamos una variable Cursos que tendrá 1.Matematica y 2. Lenguaje
#Una vez encontrada la correlación veremos que tan altas o bajas son las notas de los estudiantes de acuerdo al curso
data = [("Elvis",12),("Juan",18),
        ("Ronaldo",20),("Pablo",18),
         ("Alexis",14),("Cris",20),
          ("Ana",13),("Carlos",15),
           ("Fabian",15),("Carla",14),
            ("Fabiola",12),("Adriana",16),
             ("Fatima",20)]
columns = ["Nombre", "Nota"]
variable = spark.createDataFrame(data,columns)

data_var =[(12,1),(18,2),(20,1),(18,2),(14,1),(20,2),(13,1),(15,2),(15,1),(14,2),(12,1),(16,2),(20,1)]
columns_var = ["var1", "var2"]
variable_corr = spark.createDataFrame(data_var, columns_var)

correlacion = variable_corr.select(corr(col("var1"),col("var2")).alias("correlacion")).collect()[0]["correlacion"]

print("La correlacion es: ", correlacion)