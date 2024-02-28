from Archive import Archive
from Entry import Entry

folder = input("Escriba la carpeta donde se encuentran los archivos: ")
route = input("Escriba la ruta de la carpeta donde se encuentran los archivos: ")
select_word = input("Escriba la palabra que desea buscar: ")

e = Entry(folder, route, select_word)

if not Archive.verify_exist_route(e.route):
    print("La ruta no existe")
else:
    if len(Archive.count_files_text(e.route)) == 0:
        print("No hay archivos de texto en la ruta")
    else:
        j = 0
        for routes in Archive.count_files_text(e.route):
            i = 0
            for word in Archive.get_words_file(routes):
                if Archive.delete_score(word).lower() == select_word.lower():
                    i += 1
                    j += 1
            print(f"La palabra {select_word} se encontró {i} veces en el archivo {routes}")
        print(f"La palabra {select_word} se encontró {j} veces en total")
