###  https://www.w3schools.com/python/python_user_input.asp
entree = input("Insérer un texte : ")
nombre_caracteres = len(entree)
nombre_mots = len(entree.split())
print("Le texte a :\n {} caractères \n {} mots"\
                .format(nombre_caracteres,nombre_mots))