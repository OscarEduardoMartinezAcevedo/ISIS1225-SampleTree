"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
from App import model
import datetime
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion del modelo.
    """
    Monika = model.analyzer()
    return Monika


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(analyzer, file):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    file = cf.data_dir + file
    input_file = csv.DictReader(open(file, encoding="utf-8"),
                                delimiter=",")
    for accidente in input_file:
        model.cargaridaccidente(analyzer, accidente)

    return analyzer

# ___________________________________________________
#  Funciones para consultas
def obtener_accidentes_por_fecha(analyzer, criterio):
    A = model.obtener_accidentes_en_una_fecha(analyzer, criterio)
    return A
def estado_y_fecha_con_mas_casos(analyzer, fecha1, fecha2):
    B = model.fecha_con_mas_casos(analyzer, fecha1, fecha2)
    C = model.estado_con_mas_casos(analyzer, fecha1, fecha2)
    A = {"Estado con más accidentes reportados:": C, 
         "Fecha con más casos reportados:": str(B)}
    return A

def numero_de_accidentes_por_hora(analyzer, hora1, hora2):
    A = model.numero_de_casos_por_rango_de_hora(analyzer, hora1, hora2)
    return A

def accidentes_antes_de_una_fecha(analyzer, fecha1, fecha2):
    A = model.total_antes_de_una_fecha(analyzer, fecha2)
    B = model.fecha_con_mas_casos(analyzer, fecha1, fecha2)
    fecha = B.strftime("%Y-%m-%d")
    C = {"Total de accidentes antes de "+ fecha2: A,
         "Fecha con mas accidentes": fecha}
    return C

def accidentes_entre_fechas(analyzer, fecha1, fecha2):
    A = model.total_entre_fechas(analyzer, fecha1, fecha2)
    B = model.severidad_entre_fechas(analyzer, fecha1, fecha2)
    C = {"Total de accidentes entre " + fecha1 + " y "+ fecha2: A,
         "Severidad mas reportada en el rango": B}
    return C
# ___________________________________________________

def prueba(hora1, hora2):
    B = model.prueba(hora1, hora2)
    return(B)