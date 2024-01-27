def extraction(file_name):
    # Ouvrir le fichier en mode lecture
    with open(file_name, 'r') as fichier:
        # Lire le contenu du fichier
        contenu = fichier.read()

        # Diviser le contenu en mots en utilisant un espace comme séparateur
        mots = contenu.split()

    # Ouvrir le fichier en mode écriture
    with open('text_extract.txt', 'w') as fichier_sortie:
        # Écrire chaque mot sur une ligne distincte
        for mot in mots:
            fichier_sortie.write(mot + '\n')

file_name =input('Entrez le nom du fichier')
extraction(file_name)
