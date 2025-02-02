meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "DAMN": "Asombroso",
            "POV": "Punto de vista raro"
            }

pregunta = input("Ingrese la palabra que quiera conocer: ")

for palabra in meme_dict.keys():
    if pregunta == palabra:
        print(f"El significado de la palabra {pregunta} es {meme_dict[palabra]}")
