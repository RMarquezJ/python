import random


def generarLista(num):
    lista = []
    for i in range(num):
        lista.append(random.randint(0, 1000))
    return lista

lista1 = generarLista(100)
lista2 = generarLista(100)

def burbuja(lista):
    largo = len(lista)
    for techo in range(largo - 1, 1, -1):
        for i in range(techo):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    
    return lista

personajes = [
    {
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "19BBY",
        "gender": "male",
        "homeworld": "https://swapi.dev/api/planets/1/"
    },
    {
        "name": "Leia Organa",
        "height": "150",
        "mass": "49",
        "hair_color": "brown",
        "skin_color": "light",
        "eye_color": "brown",
        "birth_year": "19BBY",
        "gender": "female",
        "homeworld": "http://swapi.dev/api/planets/2/"
    },
    {
        "name": "Darth Vader",
        "height": "202",
        "mass": "136",
        "hair_color": "none",
        "skin_color": "white",
        "eye_color": "yellow",
        "birth_year": "41.9BBY",
        "gender": "male",
        "homeworld": "http://swapi.dev/api/planets/1/"
    },
    {
        "name": "Obi-Wan Kenobi",
        "height": "182",
        "mass": "77",
        "hair_color": "auburn, white",
        "skin_color": "fair",
        "eye_color": "blue-gray",
        "birth_year": "57BBY",
        "gender": "male",
        "homeworld": "http://swapi.dev/api/planets/20/"
    },
    {
        "name": "Jabba Desilijic Tiure",
        "height": "175",
        "mass": "1,358",
        "hair_color": "n/a",
        "skin_color": "green-tan, brown",
        "eye_color": "orange",
        "birth_year": "600BBY",
        "gender": "hermaphrodite",
        "homeworld": "http://swapi.dev/api/planets/24/"
    },
    {
        "name": "Han Solo",
        "height": "180",
        "mass": "80",
        "hair_color": "brown",
        "skin_color": "fair",
        "eye_color": "brown",
        "birth_year": "29BBY",
        "gender": "male",
        "homeworld": "http://swapi.dev/api/planets/22/",
        "films": [
            "http://swapi.dev/api/films/1/",
            "http://swapi.dev/api/films/2/",
            "http://swapi.dev/api/films/3/"
        ],
        "species": [],
        "vehicles": []  
    }
]
# acá vamos a resolver los 3 desafíos

list(map(lambda personaje: print(personaje["name"] + ' has ' + personaje["eye_color"] + ' eyes.'), personajes))

print(list(filter(lambda personaje: int(personaje["height"])>=180, personajes)))

print(list(map(lambda x:{'name': x["name"], 'height': x["height"]}, sorted(personajes,key=lambda personaje: personaje["birth_year"], reverse=True))))