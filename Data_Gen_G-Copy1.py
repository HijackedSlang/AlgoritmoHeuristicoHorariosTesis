#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Estos tres vectores los declaro para poder usarlos externamente
vector_one = []
vector_two = []
vector_three = []

# Esta es la lista de cuantos cupos tiene cada asignatura, por el momento, todas tienen cupo de 7
replacements = {
    1: 7,
    2: 7,
    3: 7,
    4: 7,
    5: 7,
    6: 7,
    7: 7,
    8: 7,
    9: 7,
    10: 7,
    11: 7,
    12: 7,
    13: 7,
    14: 7,
    15: 7,
    16: 7,
    17: 7,
    18: 7,
    19: 7,
    20: 7,
    21: 7,
    22: 7,
    23: 7,
    24: 7,
    25: 7,
    26: 7,
    27: 7,
    28: 7,
    29: 7,
    30: 7,
    31: 7,
    32: 7,
    33: 7,
    34: 7,
    35: 7,
    36: 7,
    37: 7,
    38: 7,
    39: 7,
    40: 7,
    41: 7,
    42: 7,
    43: 7,
    44: 7,
    45: 7,
    46: 7,
    47: 7,
    48: 7,
    49: 7,
    50: 7,
    51: 7,
    52: 7,
    53: 7,
    54: 7,
    55: 7,
    56: 7,
    57: 7,
    58: 7,
    59: 7,
    60: 7
}

# Crear la lista de números predefinidos, esta lista representa la materia que es y que profesores pueden ofertarla
num_numbers = {
    "1": [1,2,3],
    "2": [9,6,10],
    "3": [11,15,20],
    "4": [24,25,26],
    "5": [28,29,30],
    "6": [31,33,35],
    "7": [36,37,38],
    "8": [39,40,3],
    "9": [4,5,6],
    "10": [7,8,9],
    "11": [10,11,12],
    "12": [13,14,15],
    "13": [16,17,18],
    "14": [19,20,21],
    "15": [22,23,24],
    "16": [25,26,27],
    "17": [28,29,30],
    "18": [31,32,33],
    "19": [34,35,36],
    "20": [37,38,39],
    "21": [40,1,2],
    "22": [3,4,5],
    "23": [6,7,8],
    "24": [9,10,11],
    "25": [12,13,14],
    "26": [15,16,17],
    "27": [18,19,20],
    "28": [21,22,23],
    "29": [24,25,26],
    "30": [27,28,29],
    "31": [30,31,32],
    "32": [33,34,35],
    "33": [36,37,38],
    "34": [39,40,1],
    "35": [2,3,4],
    "36": [5,6,7],
    "37": [8,9,10],
    "38": [11,12,13],
    "39": [14,15,16],
    "40": [17,18,19],
    "41": [20,21,22],
    "42": [23,24,25],
    "43": [26,27,28],
    "44": [29,30,31],
    "45": [32,33,34],
    "46": [35,36,37],
    "47": [38,39,40],
    "48": [1,2,3],
    "49": [4,5,6],
    "50": [7,8,9],
    "51": [10,11,12],
    "52": [13,14,15],
    "53": [16,17,18],
    "54": [19,20,21],
    "55": [22,23,24],
    "56": [25,26,27],
    "57": [28,29,30],
    "58": [31,32,33],
    "59": [34,35,36],
    "60": [37,38,39]
}

# Crear la lista de números predefinidos, esta lista representa la materia que es y que profesores pueden ofertarla
num_numbers = {
    "1": [1,2,3,4],
    "2": [5,6,7,8],
    "3": [9,10,11,12],
    "4": [13,14,15,16],
    
    "8": [17,18,19,20],
    "9": [21,22,23,24],
    "10": [25,26,27,28],
    "11": [29,30,31,32],
    
    "14": [33,34,35,36],
    "15": [37,38,39,40],
    "16": [41,42,1,2],
    "17": [3,4,5,6],
    "18": [7,8,9,10],
    
    "20": [11,12,13,14],
    "21": [15,16,17,18],
    "22": [19,20,21,22],
    "23": [23,24,25,26],
    "24": [27,28,29,30],
    
    "28": [31,32,33,34],
    
    "31": [35,36,37,38],
    "32": [39,40,41,42],
    "33": [1,2,3,4],
    "34": [5,6,7,8],
    "35": [9,10,11,12],
    "36": [13,14,15,16],
    
    "40": [17,18,19,20],
    "41": [21,22,23,24],
    "42": [25,26,27,28],
    "45": [29,30,31,32],
    
    "47": [33,34,35,36],
    "48": [37,38,39,40],
    
    "52": [41,42,1,2],
    "53": [3,4,5,6],
    "54": [7,8,9,10],
    "55": [11,12,13,14],
    
    "57": [15,16,17,18],
    "58": [19,20,21,22],
    "59": [23,24,25,26],
    "60": [27,28,29,30]
}

valid_pairs = {
    1: [1,2,3,4],
    2: [5,6,7,8],
    3: [9,10,11,12],
    4: [13,14,15,16],
    
    8: [17,18,19,20],
    9: [21,22,23,24],
    10: [25,26,27,28],
    11: [29,30,31,32],
    
    14: [33,34,35,36],
    15: [37,38,39,40],
    16: [41,42,1,2],
    17: [3,4,5,6],
    18: [7,8,9,10],
    
    20: [11,12,13,14],
    21: [15,16,17,18],
    22: [19,20,21,22],
    23: [23,24,25,26],
    24: [27,28,29,30],
    
    28: [31,32,33,34],
    
    31: [35,36,37,38],
    32: [39,40,41,42],
    33: [1,2,3,4],
    34: [5,6,7,8],
    35: [9,10,11,12],
    36: [13,14,15,16],
    
    40: [17,18,19,20],
    41: [21,22,23,24],
    42: [25,26,27,28],
    45: [29,30,31,32],
    
    47: [33,34,35,36],
    48: [37,38,39,40],
    
    52: [41,42,1,2],
    53: [3,4,5,6],
    54: [7,8,9,10],
    55: [11,12,13,14],
    
    57: [15,16,17,18],
    58: [19,20,21,22],
    59: [23,24,25,26],
    60: [27,28,29,30]
}

num_numbers = {
    "1": [1, 2, 3, 4, 5, 6, 7],
    "2": [5, 6, 7, 8, 9, 10, 11],
    "3": [9, 10, 11, 12, 13, 14, 15],
    "4": [13, 14, 15, 16, 17, 18, 19],
    "8": [17, 18, 19, 20, 21, 22, 23],
    "9": [21, 22, 23, 24, 25, 26, 27],
    "10": [25, 26, 27, 28, 29, 30, 31],
    "11": [29, 30, 31, 32, 33, 34, 35],
    "14": [33, 34, 35, 36, 37, 38, 39],
    "15": [37, 38, 39, 40, 41, 42, 1],
    "16": [41, 42, 1, 2, 3, 4, 5],
    "17": [3, 4, 5, 6, 7, 8, 9],
    "18": [7, 8, 9, 10, 11, 12, 13],
    "20": [11, 12, 13, 14, 15, 16, 17],
    "21": [15, 16, 17, 18, 19, 20, 21],
    "22": [19, 20, 21, 22, 23, 24, 25],
    "23": [23, 24, 25, 26, 27, 28, 29],
    "24": [27, 28, 29, 30, 31, 32, 33],
    "28": [31, 32, 33, 34, 35, 36, 37],
    "31": [35, 36, 37, 38, 39, 40, 41],
    "32": [39, 40, 41, 42, 1, 2, 3],
    "33": [1, 2, 3, 4, 5, 6, 7],
    "34": [5, 6, 7, 8, 9, 10, 11],
    "35": [9, 10, 11, 12, 13, 14, 15],
    "36": [13, 14, 15, 16, 17, 18, 19],
    "40": [17, 18, 19, 20, 21, 22, 23],
    "41": [21, 22, 23, 24, 25, 26, 27],
    "42": [25, 26, 27, 28, 29, 30, 31],
    "45": [29, 30, 31, 32, 33, 34, 35],
    "47": [33, 34, 35, 36, 37, 38, 39],
    "48": [37, 38, 39, 40, 41, 42, 1],
    "52": [41, 42, 1, 2, 3, 4, 5],
    "53": [3, 4, 5, 6, 7, 8, 9],
    "54": [7, 8, 9, 10, 11, 12, 13],
    "55": [11, 12, 13, 14, 15, 16, 17],
    "57": [15, 16, 17, 18, 19, 20, 21],
    "58": [19, 20, 21, 22, 23, 24, 25],
    "59": [23, 24, 25, 26, 27, 28, 29],
    "60": [27, 28, 29, 30, 31, 32, 33]
}

valid_pairs = {
    1: [1, 2, 3, 4, 5, 6, 7],
    2: [5, 6, 7, 8, 9, 10, 11],
    3: [9, 10, 11, 12, 13, 14, 15],
    4: [13, 14, 15, 16, 17, 18, 19],
    8: [17, 18, 19, 20, 21, 22, 23],
    9: [21, 22, 23, 24, 25, 26, 27],
    10: [25, 26, 27, 28, 29, 30, 31],
    11: [29, 30, 31, 32, 33, 34, 35],
    14: [33, 34, 35, 36, 37, 38, 39],
    15: [37, 38, 39, 40, 41, 42, 1],
    16: [41, 42, 1, 2, 3, 4, 5],
    17: [3, 4, 5, 6, 7, 8, 9],
    18: [7, 8, 9, 10, 11, 12, 13],
    20: [11, 12, 13, 14, 15, 16, 17],
    21: [15, 16, 17, 18, 19, 20, 21],
    22: [19, 20, 21, 22, 23, 24, 25],
    23: [23, 24, 25, 26, 27, 28, 29],
    24: [27, 28, 29, 30, 31, 32, 33],
    28: [31, 32, 33, 34, 35, 36, 37],
    31: [35, 36, 37, 38, 39, 40, 41],
    32: [39, 40, 41, 42, 1, 2, 3],
    33: [1, 2, 3, 4, 5, 6, 7],
    34: [5, 6, 7, 8, 9, 10, 11],
    35: [9, 10, 11, 12, 13, 14, 15],
    36: [13, 14, 15, 16, 17, 18, 19],
    40: [17, 18, 19, 20, 21, 22, 23],
    41: [21, 22, 23, 24, 25, 26, 27],
    42: [25, 26, 27, 28, 29, 30, 31],
    45: [29, 30, 31, 32, 33, 34, 35],
    47: [33, 34, 35, 36, 37, 38, 39],
    48: [37, 38, 39, 40, 41, 42, 1],
    52: [41, 42, 1, 2, 3, 4, 5],
    53: [3, 4, 5, 6, 7, 8, 9],
    54: [7, 8, 9, 10, 11, 12, 13],
    55: [11, 12, 13, 14, 15, 16, 17],
    57: [15, 16, 17, 18, 19, 20, 21],
    58: [19, 20, 21, 22, 23, 24, 25],
    59: [23, 24, 25, 26, 27, 28, 29],
    60: [27, 28, 29, 30, 31, 32, 33]
}


import random

professors = list(range(1, 43)) * 2
random.shuffle(professors)

# Estas son las materias que no están permitidas, las pongo aquí para que se puedan poner restricciones de materias anuales
banned_numbers = [5, 6, 7, 12, 13, 19, 25, 26, 27, 29, 30, 37, 38, 39, 43, 44, 46, 49, 50, 51, 56]


# In[2]:


# Sexto intento

# Por ahora, este es el bueno
# Esta función genera los vectores para la función objetivo.
# Primero genera http://localhost:8888/notebooks/Desktop/tesis/Medianamente%20Estable-Generador%20de%20Vectores-Copy1.ipynb#un vector de tamaño que yo determino y los llena del 0 al 60.
# 0 Significa que no hay materia
# 60 Significa que hay alguna de las 60 materias disponibles

# Después de generar ese vector, clona el vector y lo guarda en un nuevo vector que seleccionará los profesores.
# Este vector representa a los profesores con un número del 1 al 40 (o depende cuantos profesores haya)
# Si aparece u profesor mas de 3 veces, ya no puede volver a aparecer.
# Toma los profesores disponibles de una lista de números posibles.

# Toda la función que genera los vectores, regresa dos vectores que me servirán para optimizar.


import copy
import random
from collections import Counter

banned_numbers = [5, 6, 7, 12, 13, 19, 25, 26, 27, 29, 30, 37, 38, 39, 43, 44, 46, 49, 50, 51, 56]

def remove_zeros(vector):
    output = [n for n in vector if n != 0]
    return output


def generate_vector_one(size, banned_numbers):
    output = []
    max_attempts = 100
    non_zero_count = 0
    count = Counter()

    for _ in range(size):
        attempts = 0
        found = False
        while not found and attempts < max_attempts:
            n = random.randint(0, 60)
            if n not in banned_numbers:
                found = True
            else:
                attempts += 1

        if not found:
            n = 0

        if non_zero_count >= 14 * 200 and n != 0:
            n = 0

        if n == 0 or count[n] < 4:
            output.append(n)
            count[n] += 1
            if n != 0:
                non_zero_count += 1

    output = remove_zeros(output)
    return output



def is_valid_number(num, index, vector_size, count):
    cycles = index // 14
    corrected_index = (index + 1) - 14 * cycles
    if abs(index - corrected_index) >= 3:
        return False
    if num in count and count[num] >= 2:
        return False
    return True

def get_possible_numbers(num, count):
    predefined_numbers = copy.deepcopy(num_numbers)
    if str(num) in predefined_numbers:
        possible_numbers = predefined_numbers[str(num)]
    else:
        possible_numbers = [random.randint(1, 40) for _ in range(3)]
    for n in possible_numbers:
        if n in count and count[n] >= 3:
            possible_numbers.remove(n)
    if not possible_numbers:
        possible_numbers = [0]
    return possible_numbers


def select_number(num, count):
    possible_numbers = get_possible_numbers(num, count)
    if not possible_numbers:
        return 0

    preferred_numbers = [n for n in possible_numbers if count.get(n, 0) < 3]
    if preferred_numbers:
        replacement_num = random.choice(preferred_numbers)
    else:
        replacement_num = random.choice(possible_numbers)

    iterations = 0
    max_iterations = 150000
    while count.get(replacement_num, 0) >= 3:
        replacement_num = random.choice(possible_numbers)
        iterations += 1
        if iterations > max_iterations:
            replacement_num = 0
            break

    count[replacement_num] = count.get(replacement_num, 0) + 1
    return replacement_num

def generate_vector_two(vector_one, valid_pairs, professors):
    vector_two = []
    remaining_professors = list(professors)  # Convertir a lista

    for course in vector_one:
        if course == 0:
            vector_two.append(0)
        else:
            possible_professors = valid_pairs.get(course, [])
            available_professors = [p for p in possible_professors if p in remaining_professors]
            
            if available_professors:
                assigned_professor = random.choice(available_professors)
                vector_two.append(assigned_professor)
                remaining_professors.remove(assigned_professor)
            else:
                vector_two.append(0)

    return vector_two



def check_repeated_numbers(vector_one, vector_two):
    count_one = {}
    for num in vector_one:
        if num in count_one:
            count_one[num] += 1
        else:
            count_one[num] = 1
        if (count_one[num] > 4) and (num != 0):
            return False
    count_two = {}
    for num in vector_two:
        if num in count_two:
            count_two[num] += 1
        else:
            count_two[num] = 1
        if count_two[num] > 3:
            return False
    return True

def check_range(vector_one, vector_two):
    if any(num > 60 for num in vector_one) or any(num > 40 for num in vector_two):
        return False
    return True


def check_size(vector_one, vector_two):
    non_zero_count = vector_two.count(0)
    return len(vector_two) - non_zero_count

def generate_vectors(size, banned_numbers, valid_pairs, professors):
    predefined_numbers = num_numbers
    vector_one = generate_vector_one(size, banned_numbers)
    vector_two = generate_vector_two(vector_one, valid_pairs, professors)
    check_size(vector_one, vector_two)
    
    return vector_one, vector_two


size = 14 * 100

du = 0
vector_one = []
vector_two = []
while du != 84:
    if not vector_one or not vector_two:
        vector_one, vector_two = generate_vectors(size, banned_numbers, valid_pairs, professors)
    du = check_size(vector_one, vector_two)

print(du)


# Inicializar la variable size con un valor de 14
size = 14*10
target_non_zero_count = 80
# Generar los vectores
vector_one, vector_two = generate_vectors(size, banned_numbers, target_non_zero_count)
check_size(vector_one, vector_two)

# In[3]:


pass #print("Vector one:", vector_one)
pass #print("Vector two:", vector_two)


#pass #print_appearances(vector_one, vector_two) #Esta función me dice que numeros aparecen cuantas veces

#Las siguientes funciones me dicen cuantas veces aparecen, pero me lo dice solamente usando números [Vector,Aparicion]
#vector_with_appearances1 = generate_vector_with_appearances(vector_one)
#vector_with_appearances2 = generate_vector_with_appearances(vector_two)

pass #print("")
#pass #print(vector_with_appearances1)
pass #print("") 
#pass #print(vector_with_appearances2) 


# In[4]:


# Después de que el vector haya sido creado, debe ser procesado para ser legible y usable.
# Las siguientes funciones están hechas para hacer parejas de vectores materia, docente
# Después, se agrupan en grupos de 7 para hacer horarios. Si no hay suficientes materias, se rellenan con materias vacías.
# Después, reordenaré las materias para hacer horarios que en la mañana tengan materias de primer bloque
# Y a poder ser, en la tarde del resto.


def compare_vectors(vector_one, vector_two):
    pairs = [[v1, v2] for v1, v2 in zip(vector_one, vector_two) if v1 != 0 and v2 != 0]
    return pairs


# Hago un horario preliminar para que queden en grupos de 14 horas.

from operator import itemgetter

def sort_pairs(pairs):
    # Calculate the number of zeros to add
    num_zeros_to_add = (14 - (len(pairs) % 14)) % 14

    # Extend the pairs list with zeros
    pairs += [[0, 0]] * num_zeros_to_add

    # Divide the pairs into groups of 7
    groups = [pairs[i:i+7] for i in range(0, len(pairs), 7)]

    # Sort the groups by the first element of each pair
    sorted_groups = [sorted(group, key=itemgetter(0)) for group in groups]

    # Pad each group with zeros up to length 7
    sorted_groups = [group + [[0, 0]] * (7 - len(group)) for group in sorted_groups]

    return sorted_groups


old_groups = []


old_groups = []

def find_and_replace(groups):
    replaced_pairs = []
    old_groups = list(groups)

    for group in groups:
        for j, pair in enumerate(group):
            if j > 3 or (j >= 3 and pair[0] > 26):
                replaced_pairs.append(pair)
                group[j] = [0, 0]

    for i, group in enumerate(groups):
        pass  # print(f'Grupo {i+1}: {group}')

    return replaced_pairs, old_groups

def make_groups(replaced_pairs):
    new_groups = []

    while replaced_pairs:
        new_group = [[0, 0]] * 4
        for _ in range(3):
            if replaced_pairs:
                new_group.append(replaced_pairs.pop(0))
            else:
                new_group.append([0, 0])

        new_groups.append(new_group)

    if len(new_groups[-1]) < 7:
        new_groups[-1] += [[0, 0]] * (7 - len(new_groups[-1]))

    return new_groups


# Esta función reordena los grupos para evitar que un profesor se repita en un intervalo mayor a dos horas.


# Imprimir los grupos modificados
#pass #print(reorder_groups(groups))



# In[5]:


# Aquí invoco las funciones anteriores para verificar que todo está en orden

#print("\n Estos son vectores obtenidos al inicio \n")
# Obtener el vector de parejas
pairs = compare_vectors(vector_one, vector_two)

pass #print("\n Estos son los horarios generados con los vectores obtenidos al inicio \n")
# Obtener el vector de grupos de 7 de parejas

groups = sort_pairs(pairs)

pass #print("\n Estos horarios son los de mañana \n")
replaced_pairs, old_groups = find_and_replace(groups)

#pass #print(replaced_pairs)
pass #print("\n Estos horarios son los de tarde \n")
new_groups = make_groups(replaced_pairs)
#pass #print(" ")
#pass #print(f"Vector de parejas filtradas: {filtered_pairs}")

#for i, group in enumerate(modified_groups):
#    pass #print(f"Grupo {i}: {group}")
    
#pass #print(extracted_pairs)

# Todo esto es experimental igual

#pass #print(" ")
#late_groups = make_groups(special_numbers)
#pass #print(modified_groups)
#pass #print(" ")
#pass #print(late_groups)


# In[6]:


# Voy a usar todo este espacio para hacer algoritmos que reordenen los horarios para tener viabilidad
# Primero voy a analizar los vectores para retirar todos los que violen las reglas 
# (aparecer a más de dos vectores de distancia de su primera aparición en cualquier grupo)
# Más tarde haré un bubble sort que me ayude a reordenarlos hasta que tengan sentido
# Si al final no consigo que todos tengan sentido, los ordenaré en cualquier lugar que tenga sentido con la regla
# Ese será el vector que meta al algoritmo genético para tener la mayor cantidad de horarios posibles.

vec1=[]
vec2=[]

def analizar_vectores(vec1, vec2):
    malas_parejas = []
    primeras_apariciones = {}
    
    for vec in [vec1, vec2]:
        for i, grupo in enumerate(vec):
            for j, pareja in enumerate(grupo):
                if pareja[1] not in primeras_apariciones:
                    primeras_apariciones[pareja[1]] = (j, i, vec.index(grupo) + 1)
                elif abs(primeras_apariciones[pareja[1]][0] - j) > 2:
                    malas_parejas.append(pareja)
                    grupo[j] = [0, 0]
    
    for i, grupo in enumerate(vec1):
        pass  # print(f"V1_G{i}: {grupo}")

    for i, grupo in enumerate(vec2):
        pass  # print(f"V2_G{i}: {grupo}")
    
    return vec1, vec2, malas_parejas

vec1, vec2, malas_parejas = analizar_vectores(old_groups, new_groups)


# Voy a escribir una función que rellene los horarios para tener viabilidad


# In[7]:


def remove_zero_pairs(vector):
    vector = [[pair for pair in group if pair != [0, 0]] for group in vector]
    vector = [group for group in vector if group]
    pass  # print(f'El nuevo tamaño del vector es {len(vector)}')
    pass  # print(f'El vector modificado es {vector}')
    return vector

malas_parejas = remove_zero_pairs(malas_parejas)

def count_non_zero_pairs_nested(vector):
    non_zero_pairs = sum(1 for group in vector for pair in group if pair != [0, 0])
    non_zero = [pair for group in vector for pair in group if pair != [0, 0]]
    return non_zero_pairs, non_zero

# Lo que estoy haciendo aquí es conocer cuantas parejas sí pasaron el filtro


# In[8]:


# Necesito un algoritmo que tome las parejas violadoras y las meta en los espacios aleatoriamente.
# Necesito otra función que revise si aun hay parejas que violan esa regla y remueva las que lo hagan.
# Se me ocurre que puedo generar diversos arreglos de las parejas aleatoriamente y eventualmente alguno será suficientemente útil

pass #print(vec2)


# In[9]:


# Este algoritmo actualmente funciona suficientemente bien. Actualmente, las parejas no causan conflicto, pero no sé que tanto pueda escalarse.

def acomodar_malas_parejas(vec1, vec2, malas_parejas):
    # Diccionario para almacenar las primeras apariciones de cada número
    primeras_apariciones = {}
    # Recorrer ambos vectores para obtener las primeras apariciones de cada numero
    for i, grupo in enumerate(vec1):
        for j, pareja in enumerate(grupo):
            if pareja[1] not in primeras_apariciones:
                primeras_apariciones[pareja[1]] = (j, i, 1)
    for i, grupo in enumerate(vec2):
        for j, pareja in enumerate(grupo):
            if pareja[1] not in primeras_apariciones:
                primeras_apariciones[pareja[1]] = (j, i, 2)
    # Ordenar las parejas violadoras
    malas_parejas.sort()
    # Lista para almacenar las parejas que no se pudieron acomodar
    parejas_no_acomodadas = []
    # iterar sobre las parejas violadoras
    for pareja in malas_parejas:
        # flag para indicar si la pareja fue acomodada
        acomodada = False
        # buscar parejas [0,0] para reemplazar
        for i, grupo in enumerate(vec1):
            for j, p in enumerate(grupo):
                if p == [0,0]:
                    # verificar si la pareja cumple con la regla
                    if (abs(primeras_apariciones[pareja[1]][0] - j) <= 2 or (abs(primeras_apariciones[pareja[1]][0] - j) == 0)):
                        vec1[i][j] = pareja
                        primeras_apariciones[pareja[1]] = (j, i, 1)
                        acomodada = True
                        break
            if acomodada:
                break
        if not acomodada:
            for i, grupo in enumerate(vec2):
                for j, p in enumerate(grupo):
                    if p == [0,0]:
                        # verificar si la pareja cumple con la regla
                        if (abs(primeras_apariciones[pareja[1]][0] - j) <= 2  or (abs(primeras_apariciones[pareja[1]][0] - j) == 0)):
                            vec2[i][j] = pareja
                            
                            primeras_apariciones[pareja[1]] = (j, i, 2)
                            acomodada = True
                            break
                if acomodada:
                    break
        if not acomodada:
            parejas_no_acomodadas.append(pareja)
    
    # Imprimir los vectores modificados
    pass #print("Vector 1:")
    for i, grupo in enumerate(vec1):
        pass #print(f"V1_G{i}: {grupo}")
    pass #print("Vector 2:")
    for i, grupo in enumerate(vec2):
        pass #print(f"V2_G{i}: {grupo}")
    # Regresar los vectores modificados y las parejas violadoras
    return vec1, vec2, malas_parejas


vec1, vec2, malas_parejas = acomodar_malas_parejas(vec1, vec2, malas_parejas)
#pass #print(malas_parejas)

def count_non_zero_pairs_nested(vector):
    non_zero_pairs = sum(1 for group in vector for pair in group if pair != [0, 0])
    non_zero = [pair for group in vector for pair in group if pair != [0, 0]]
    # pass #print(f'El vector no nulo es: {non_zero}')
    return non_zero_pairs, non_zero



pass #print(f"El número total de parejas no nulas, no violadoras es : {count_non_zero_pairs_nested(vec1)+count_non_zero_pairs_nested(vec2)}")


# In[10]:


# Ya sólo faltaría dividir los horarios de nuevo en mañana o tarde.
# La función sería meramente estética, así que por ahora no la escribiré, pero si la escribo, aquí la pondré


# In[11]:


# Voy a dar preprocesamiento para que haya más vectores que permitan intercambiar paridad, estos vectores serán grupos nulos
def agregar_grupos_nulos(vector, n):
    vector.extend([[[0, 0]] * 7 for _ in range(n)])
    return vector

vec1 = agregar_grupos_nulos(vec1, 2)
vec2 = agregar_grupos_nulos(vec2, 2)


# In[12]:


vec1, vec2


# In[ ]:





# In[13]:


# Voy a hacer el esqueleto del algoritmo genético.

# Primero declararé las restricciones


import random

def intercambiar_grupos(vector):
    primer_aparicion = {}
    
    for _ in range(100):
        for j in range(len(vector)):
            for k in range(len(vector[j])):
                if vector[j][k][1] != 0:
                    if vector[j][k][1] not in primer_aparicion:
                        primer_aparicion[vector[j][k][1]] = j
                    else:
                        diferencia = abs(primer_aparicion[vector[j][k][1]] - j)
                        if diferencia == 0 and j % 2 == primer_aparicion[vector[j][k][1]] % 2:
                            if j % 2 == 0:
                                grupo_random = random.choice([i for i in range(len(vector)) if i % 2 != 0])
                            else:
                                grupo_random = random.choice([i for i in range(len(vector)) if i % 2 == 0])
                            vector[j], vector[grupo_random] = vector[grupo_random], vector[j]
                            primer_aparicion = {}
                            break
    return vector

primer_aparicion = {}




def cumple_restricciones_apariciones(vector):
    primer_aparicion = {}
    for grupo in vector:
        for j, pareja in enumerate(grupo):
            if pareja[1] != 0:
                if pareja[1] not in primer_aparicion:
                    primer_aparicion[pareja[1]] = j
                else:
                    diferencia = abs(primer_aparicion.get(pareja[1], 0) - j)
                    if diferencia > 2:
                        # pass #print("La restriccion de diferencia entre apariciones se viola con la pareja: {}".format(pareja))
                        return False
    return True



def cumple_restriccion_paridad(vector):
    primer_aparicion = {}
    violaciones_paridad = []
    for i, grupo in enumerate(vector):
        for j, pareja in enumerate(grupo):
            if pareja[1] != 0:
                if pareja[1] not in primer_aparicion:
                    primer_aparicion[pareja[1]] = i
                else:
                    diferencia = abs(primer_aparicion[pareja[1]] - i)
                    if diferencia == 0 and i % 2 != primer_aparicion[pareja[1]] % 2:
                        violaciones_paridad.append([i, j, pareja])
    if violaciones_paridad:
        # pass #print("Las restriccion de paridad se viola con las parejas: {}".format(violaciones_paridad))
        return False
    else:
        return True
    
def cumple_restricciones_repeticiones(vector):
    apariciones_y = {}
    for grupo in vector:
        for pareja in grupo:
            if pareja[1] != 0:
                apariciones_y[pareja[1]] = apariciones_y.get(pareja[1], 0) + 1
                if apariciones_y[pareja[1]] > 3:
                    return False
    return True

def cumple_restricciones_indices(vector):
    apariciones_indice = {}
    for grupo in vector:
        for j, pareja in enumerate(grupo):
            if pareja[1] != 0:
                apariciones_indice[j] = apariciones_indice.get(j, 0) + 1
                if apariciones_indice[j] > 18:
                    return False
    return True




def cumplen_restricciones(vector_total):
    restricciones_violadas = []
    if not cumple_restricciones_apariciones(vector_total):
        restricciones_violadas.append("La restriccion de apariciones no se cumple")
    if not cumple_restricciones_repeticiones(vector_total):
        restricciones_violadas.append("La restriccion de repeticiones no se cumple")
    if not cumple_restricciones_indices(vector_total):
        restricciones_violadas.append("La restriccion de indices no se cumple")
    return len(restricciones_violadas) == 0, restricciones_violadas



# In[ ]:





# In[14]:


# Aqui hay un check para que se sepa si pasa la restricción o no, pero este check devuelve un vector que servirá para la función que arregla el fallo
vector_total = vec1 + vec2

def check_parity(vector):
    wrong_pairs = []
    unique_wrong_pairs = []
    unique_wrong_index = []
    first_appearance = {}

    for i, group in enumerate(vector):
        for j, pair in enumerate(group):
            if pair[1] != 0:
                if pair[1] not in first_appearance:
                    first_appearance[pair[1]] = (i, j)
                else:
                    if (i % 2) == (first_appearance[pair[1]][0] % 2) and abs(j - first_appearance[pair[1]][1]) == 0:
                        if pair not in unique_wrong_pairs:
                            unique_wrong_pairs.append(pair)
                            unique_wrong_index.append(j)
                        wrong_pairs.append(pair)

    return unique_wrong_pairs, unique_wrong_index


def check_parity_v3(vector):
    parejas_malas = []
    first_appearance = {}

    for i, group in enumerate(vector):
        for j, pair in enumerate(group):
            if pair[1] != 0:
                if pair[1] not in first_appearance:
                    first_appearance[pair[1]] = (i, j)
                else:
                    if (i % 2) == (first_appearance[pair[1]][0] % 2) and abs(j - first_appearance[pair[1]][1]) == 0:
                        parejas_malas.append([i, j, pair[1]])

    return parejas_malas


parejas_malas = check_parity_v3(vector_total)


# Esta parte utiliza un algoritmo rotativo para arreglar los fallos de paridad
import heapq
from collections import defaultdict
import sys

def correct_parity_violations(vector, parejas_fallidas):
    runs = 0
    max_runs = 1000

    # Initialize null groups set
    null_groups = set(i for i, group in enumerate(vector) if all(pair == [0, 0] for pair in group))

    while parejas_fallidas and runs < max_runs:
        runs += 1

        best_improvement = -sys.maxsize
        best_violation = -1
        best_null_group = -1

        for violation in parejas_fallidas:
            for null_group in null_groups:
                # Temporarily swap the violation and null group
                vector[violation[0]], vector[null_group] = vector[null_group], vector[violation[0]]
                new_parejas_fallidas = check_parity_v3(vector)
                improvement = len(parejas_fallidas) - len(new_parejas_fallidas)

                # Undo the temporary swap
                vector[violation[0]], vector[null_group] = vector[null_group], vector[violation[0]]

                # Update the best improvement found so far
                if improvement > best_improvement:
                    best_improvement, best_violation, best_null_group = improvement, violation[0], null_group

        # Swap the violation with the null group that resulted in the best improvement
        if best_violation != -1 and best_null_group != -1:
            vector[best_violation], vector[best_null_group] = vector[best_null_group], vector[best_violation]
            parejas_fallidas = check_parity_v3(vector)

            # Update null groups if necessary
            if best_violation in null_groups and not all(pair == [0, 0] for pair in vector[best_violation]):
                null_groups.remove(best_violation)
            if all(pair == [0, 0] for pair in vector[best_null_group]):
                null_groups.add(best_null_group)

    if not parejas_fallidas:
        pass #print("Fallos de paridad corregidos.")
    else:
        pass #print("Fallos aún presentes, no se han podido corregir")

    return vector






vector_total = correct_parity_violations(vector_total, parejas_malas)


# In[ ]:





# In[15]:


vector_total


# In[16]:


# Aqui hay un check para que se sepa si pasa la restricción o no

check_parity(vector_total)


# In[17]:


babb, _ = cumplen_restricciones(vector_total)
pass #print(babb)


# In[18]:


# Estoy declarando un checker general

def check_restrictions_and_parity(vector_total):
    cumplen, restricciones = cumplen_restricciones(vector_total)
    if cumplen and not restricciones:
        unique_wrong_pairs, unique_wrong_index = check_parity(vector_total)
        if not unique_wrong_pairs and not unique_wrong_index:
            return True
    return False


check_restrictions_and_parity(vector_total)


# In[19]:


import concurrent.futures

def analizar_vectores(vec1, vec2):
    malas_parejas = []
    primeras_apariciones = {}
    valid_positions = {}

    def is_valid_position(primeras_apariciones, pareja, j):
        if pareja[1] not in primeras_apariciones:
            return True
        return abs(primeras_apariciones[pareja[1]][0] - j) <= 2

    def process_group(i, group, primeras_apariciones, valid_positions, malas_parejas, vec_id):
        for j, pareja in enumerate(group):
            if is_valid_position(primeras_apariciones, pareja, j):
                valid_positions.setdefault(pareja[1], []).append((j, i, vec_id))
                primeras_apariciones[pareja[1]] = (j, i, vec_id)
            else:
                malas_parejas.append(pareja)
                group[j] = [0, 0]
        return group

    for i, group in enumerate(vec1):
        vec1[i] = process_group(i, group, primeras_apariciones, valid_positions, malas_parejas, 1)

    for i, group in enumerate(vec2):
        vec2[i] = process_group(i, group, primeras_apariciones, valid_positions, malas_parejas, 2)

    # Regresar los vectores modificados y las parejas violadoras
    return vec1, vec2, malas_parejas

vec1, vec2, malas_parejas = analizar_vectores(old_groups, new_groups)


# In[20]:


import concurrent.futures

def acomodar_malas_parejas(vec1, vec2, malas_parejas):
    primeras_apariciones = {}
    for i, grupo in enumerate(vec1):
        for j, pareja in enumerate(grupo):
            if pareja[1] not in primeras_apariciones:
                primeras_apariciones[pareja[1]] = (j, i, 1)
    for i, grupo in enumerate(vec2):
        for j, pareja in enumerate(grupo):
            if pareja[1] not in primeras_apariciones:
                primeras_apariciones[pareja[1]] = (j, i, 2)

    parejas_no_acomodadas = []

    empty_positions1 = {i: set(j for j, pareja in enumerate(grupo) if pareja == [0, 0]) for i, grupo in enumerate(vec1)}
    empty_positions2 = {i: set(j for j, pareja in enumerate(grupo) if pareja == [0, 0]) for i, grupo in enumerate(vec2)}

    vector_total = vec1 + vec2

    def try_match(pareja):
        try:
            vec_id = primeras_apariciones[pareja[1]][2]
            empty_positions = empty_positions1 if vec_id == 1 else empty_positions2
            i = pareja[0] // 7
            j = empty_positions[i][pareja[0] % 7]
            vec_to_use = [vec1, vec2][vec_id]
            vec_to_use[i][j] = pareja
            prev_aparicion = primeras_apariciones.get(pareja[1])
            primeras_apariciones[pareja[1]] = (j, i, vec_id)
            success = check_restrictions_and_parity(vector_total)
            if success:
                empty_positions[i].remove(j)
            else:
                vec_to_use[i][j] = [0, 0]
                if prev_aparicion:
                    primeras_apariciones[pareja[1]] = prev_aparicion
                else:
                    del primeras_apariciones[pareja[1]]
            return success
        except Exception as e:
            return False

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(try_match, malas_parejas))

    parejas_no_acomodadas = [pareja for pareja, result in zip(malas_parejas, results) if not result]

    return vec1, vec2, parejas_no_acomodadas


# In[21]:


# Estos tres vectores los declaro para poder usarlos externamente
vector_one = []
vector_two = []
vector_three = []

# Esta es la lista de cuantos cupos tiene cada asignatura, por el momento, todas tienen cupo de 7
replacements = {
    1: 7,
    2: 7,
    3: 7,
    4: 7,
    5: 7,
    6: 7,
    7: 7,
    8: 7,
    9: 7,
    10: 7,
    11: 7,
    12: 7,
    13: 7,
    14: 7,
    15: 7,
    16: 7,
    17: 7,
    18: 7,
    19: 7,
    20: 7,
    21: 7,
    22: 7,
    23: 7,
    24: 7,
    25: 7,
    26: 7,
    27: 7,
    28: 7,
    29: 7,
    30: 7,
    31: 7,
    32: 7,
    33: 7,
    34: 7,
    35: 7,
    36: 7,
    37: 7,
    38: 7,
    39: 7,
    40: 7,
    41: 7,
    42: 7,
    43: 7,
    44: 7,
    45: 7,
    46: 7,
    47: 7,
    48: 7,
    49: 7,
    50: 7,
    51: 7,
    52: 7,
    53: 7,
    54: 7,
    55: 7,
    56: 7,
    57: 7,
    58: 7,
    59: 7,
    60: 7
}

# Crear la lista de números predefinidos, esta lista representa la materia que es y que profesores pueden ofertarla
num_numbers = {
    "1": [1,2,3],
    "2": [9,6,10],
    "3": [11,15,20],
    "4": [24,25,26],
    "5": [28,29,30],
    "6": [31,33,35],
    "7": [36,37,38],
    "8": [39,40,3],
    "9": [4,5,6],
    "10": [7,8,9],
    "11": [10,11,12],
    "12": [13,14,15],
    "13": [16,17,18],
    "14": [19,20,21],
    "15": [22,23,24],
    "16": [25,26,27],
    "17": [28,29,30],
    "18": [31,32,33],
    "19": [34,35,36],
    "20": [37,38,39],
    "21": [40,1,2],
    "22": [3,4,5],
    "23": [6,7,8],
    "24": [9,10,11],
    "25": [12,13,14],
    "26": [15,16,17],
    "27": [18,19,20],
    "28": [21,22,23],
    "29": [24,25,26],
    "30": [27,28,29],
    "31": [30,31,32],
    "32": [33,34,35],
    "33": [36,37,38],
    "34": [39,40,1],
    "35": [2,3,4],
    "36": [5,6,7],
    "37": [8,9,10],
    "38": [11,12,13],
    "39": [14,15,16],
    "40": [17,18,19],
    "41": [20,21,22],
    "42": [23,24,25],
    "43": [26,27,28],
    "44": [29,30,31],
    "45": [32,33,34],
    "46": [35,36,37],
    "47": [38,39,40],
    "48": [1,2,3],
    "49": [4,5,6],
    "50": [7,8,9],
    "51": [10,11,12],
    "52": [13,14,15],
    "53": [16,17,18],
    "54": [19,20,21],
    "55": [22,23,24],
    "56": [25,26,27],
    "57": [28,29,30],
    "58": [31,32,33],
    "59": [34,35,36],
    "60": [37,38,39]
}

# Crear la lista de números predefinidos, esta lista representa la materia que es y que profesores pueden ofertarla
num_numbers = {
    "1": [1,2,3,4],
    "2": [5,6,7,8],
    "3": [9,10,11,12],
    "4": [13,14,15,16],
    
    "8": [17,18,19,20],
    "9": [21,22,23,24],
    "10": [25,26,27,28],
    "11": [29,30,31,32],
    
    "14": [33,34,35,36],
    "15": [37,38,39,40],
    "16": [41,42,1,2],
    "17": [3,4,5,6],
    "18": [7,8,9,10],
    
    "20": [11,12,13,14],
    "21": [15,16,17,18],
    "22": [19,20,21,22],
    "23": [23,24,25,26],
    "24": [27,28,29,30],
    
    "28": [31,32,33,34],
    
    "31": [35,36,37,38],
    "32": [39,40,41,42],
    "33": [1,2,3,4],
    "34": [5,6,7,8],
    "35": [9,10,11,12],
    "36": [13,14,15,16],
    
    "40": [17,18,19,20],
    "41": [21,22,23,24],
    "42": [25,26,27,28],
    "45": [29,30,31,32],
    
    "47": [33,34,35,36],
    "48": [37,38,39,40],
    
    "52": [41,42,1,2],
    "53": [3,4,5,6],
    "54": [7,8,9,10],
    "55": [11,12,13,14],
    
    "57": [15,16,17,18],
    "58": [19,20,21,22],
    "59": [23,24,25,26],
    "60": [27,28,29,30]
}

valid_pairs = {
    1: [1,2,3,4],
    2: [5,6,7,8],
    3: [9,10,11,12],
    4: [13,14,15,16],
    
    8: [17,18,19,20],
    9: [21,22,23,24],
    10: [25,26,27,28],
    11: [29,30,31,32],
    
    14: [33,34,35,36],
    15: [37,38,39,40],
    16: [41,42,1,2],
    17: [3,4,5,6],
    18: [7,8,9,10],
    
    20: [11,12,13,14],
    21: [15,16,17,18],
    22: [19,20,21,22],
    23: [23,24,25,26],
    24: [27,28,29,30],
    
    28: [31,32,33,34],
    
    31: [35,36,37,38],
    32: [39,40,41,42],
    33: [1,2,3,4],
    34: [5,6,7,8],
    35: [9,10,11,12],
    36: [13,14,15,16],
    
    40: [17,18,19,20],
    41: [21,22,23,24],
    42: [25,26,27,28],
    45: [29,30,31,32],
    
    47: [33,34,35,36],
    48: [37,38,39,40],
    
    52: [41,42,1,2],
    53: [3,4,5,6],
    54: [7,8,9,10],
    55: [11,12,13,14],
    
    57: [15,16,17,18],
    58: [19,20,21,22],
    59: [23,24,25,26],
    60: [27,28,29,30]
}

num_numbers = {
    "1": [1, 2, 3, 4, 5, 6, 7],
    "2": [5, 6, 7, 8, 9, 10, 11],
    "3": [9, 10, 11, 12, 13, 14, 15],
    "4": [13, 14, 15, 16, 17, 18, 19],
    "8": [17, 18, 19, 20, 21, 22, 23],
    "9": [21, 22, 23, 24, 25, 26, 27],
    "10": [25, 26, 27, 28, 29, 30, 31],
    "11": [29, 30, 31, 32, 33, 34, 35],
    "14": [33, 34, 35, 36, 37, 38, 39],
    "15": [37, 38, 39, 40, 41, 42, 1],
    "16": [41, 42, 1, 2, 3, 4, 5],
    "17": [3, 4, 5, 6, 7, 8, 9],
    "18": [7, 8, 9, 10, 11, 12, 13],
    "20": [11, 12, 13, 14, 15, 16, 17],
    "21": [15, 16, 17, 18, 19, 20, 21],
    "22": [19, 20, 21, 22, 23, 24, 25],
    "23": [23, 24, 25, 26, 27, 28, 29],
    "24": [27, 28, 29, 30, 31, 32, 33],
    "28": [31, 32, 33, 34, 35, 36, 37],
    "31": [35, 36, 37, 38, 39, 40, 41],
    "32": [39, 40, 41, 42, 1, 2, 3],
    "33": [1, 2, 3, 4, 5, 6, 7],
    "34": [5, 6, 7, 8, 9, 10, 11],
    "35": [9, 10, 11, 12, 13, 14, 15],
    "36": [13, 14, 15, 16, 17, 18, 19],
    "40": [17, 18, 19, 20, 21, 22, 23],
    "41": [21, 22, 23, 24, 25, 26, 27],
    "42": [25, 26, 27, 28, 29, 30, 31],
    "45": [29, 30, 31, 32, 33, 34, 35],
    "47": [33, 34, 35, 36, 37, 38, 39],
    "48": [37, 38, 39, 40, 41, 42, 1],
    "52": [41, 42, 1, 2, 3, 4, 5],
    "53": [3, 4, 5, 6, 7, 8, 9],
    "54": [7, 8, 9, 10, 11, 12, 13],
    "55": [11, 12, 13, 14, 15, 16, 17],
    "57": [15, 16, 17, 18, 19, 20, 21],
    "58": [19, 20, 21, 22, 23, 24, 25],
    "59": [23, 24, 25, 26, 27, 28, 29],
    "60": [27, 28, 29, 30, 31, 32, 33]
}

valid_pairs = {
    1: [1, 2, 3, 4, 5, 6, 7],
    2: [5, 6, 7, 8, 9, 10, 11],
    3: [9, 10, 11, 12, 13, 14, 15],
    4: [13, 14, 15, 16, 17, 18, 19],
    8: [17, 18, 19, 20, 21, 22, 23],
    9: [21, 22, 23, 24, 25, 26, 27],
    10: [25, 26, 27, 28, 29, 30, 31],
    11: [29, 30, 31, 32, 33, 34, 35],
    14: [33, 34, 35, 36, 37, 38, 39],
    15: [37, 38, 39, 40, 41, 42, 1],
    16: [41, 42, 1, 2, 3, 4, 5],
    17: [3, 4, 5, 6, 7, 8, 9],
    18: [7, 8, 9, 10, 11, 12, 13],
    20: [11, 12, 13, 14, 15, 16, 17],
    21: [15, 16, 17, 18, 19, 20, 21],
    22: [19, 20, 21, 22, 23, 24, 25],
    23: [23, 24, 25, 26, 27, 28, 29],
    24: [27, 28, 29, 30, 31, 32, 33],
    28: [31, 32, 33, 34, 35, 36, 37],
    31: [35, 36, 37, 38, 39, 40, 41],
    32: [39, 40, 41, 42, 1, 2, 3],
    33: [1, 2, 3, 4, 5, 6, 7],
    34: [5, 6, 7, 8, 9, 10, 11],
    35: [9, 10, 11, 12, 13, 14, 15],
    36: [13, 14, 15, 16, 17, 18, 19],
    40: [17, 18, 19, 20, 21, 22, 23],
    41: [21, 22, 23, 24, 25, 26, 27],
    42: [25, 26, 27, 28, 29, 30, 31],
    45: [29, 30, 31, 32, 33, 34, 35],
    47: [33, 34, 35, 36, 37, 38, 39],
    48: [37, 38, 39, 40, 41, 42, 1],
    52: [41, 42, 1, 2, 3, 4, 5],
    53: [3, 4, 5, 6, 7, 8, 9],
    54: [7, 8, 9, 10, 11, 12, 13],
    55: [11, 12, 13, 14, 15, 16, 17],
    57: [15, 16, 17, 18, 19, 20, 21],
    58: [19, 20, 21, 22, 23, 24, 25],
    59: [23, 24, 25, 26, 27, 28, 29],
    60: [27, 28, 29, 30, 31, 32, 33]
}


professors = list(range(1, 43)) * 2
random.shuffle(professors)

# Estas son las materias que no están permitidas, las pongo aquí para que se puedan poner restricciones de materias anuales
banned_numbers = [5, 6, 7, 12, 13, 19, 25, 26, 27, 29, 30, 37, 38, 39, 43, 44, 46, 49, 50, 51, 56]


# In[22]:


#predefined_numbers = num_numbers


# In[23]:


import time

def generate_full_vec():
    eff = 0

    while True:
        vector_one, vector_two = None, None
        while vector_one is None and vector_two is None:
            vector_one, vector_two = generate_vectors(14*50, banned_numbers, valid_pairs, professors)
            if check_size(vector_one, vector_two) != 84:
                vector_one, vector_two = None, None

        pairs = compare_vectors(vector_one, vector_two)
        groups = sort_pairs(pairs)
        replaced_pairs, old_groups = find_and_replace(groups)
        new_groups = make_groups(replaced_pairs)

        vec1, vec2, malas_parejas = analizar_vectores(old_groups, new_groups)
        vec1, vec2, malas_parejas = acomodar_malas_parejas(vec1, vec2, malas_parejas)

        vec1 = agregar_grupos_nulos(vec1, 2)
        vec2 = agregar_grupos_nulos(vec2, 2)

        vector_total = vec1 + vec2

        parejas_malas = check_parity_v3(vector_total)
        vector_total = correct_parity_violations(vector_total, parejas_malas)

        if check_restrictions_and_parity(vector_total):
            return vector_total, eff
        else:
            eff += 1


def generate_population(population_size):
    population = []
    total_eff = 0
    start_time = time.time()

    while len(population) < population_size:
        individual, eff = generate_full_vec()
        population.append(individual)
        total_eff += eff

        bob_time = time.time()
        elapsed_time = bob_time - start_time
        #print(f'Generated individual {len(population)}. Time elapsed: {elapsed_time} seconds.')

    elapsed_time = time.time() - start_time

    print(f"--- {elapsed_time} seconds ---")
    print(f"Average time per individual: {elapsed_time / len(population)} seconds")
    print(f"Average efficiency: {(len(population) / (len(population) + total_eff)) * 100} percent")

    return population

population = generate_population(200)


# In[26]:


# Assuming array is a list of individuals
all_true = True
for individual in population:
    result = check_restrictions_and_parity(individual)
    if not result:
        all_true = False
if all_true:
    print("All individuals passed the restrictions and parity check!")


# In[ ]:


import pickle

# Salvarlo en un pickle
with open("databasic.pickle", "wb") as file:
    pickle.dump(population, file)

