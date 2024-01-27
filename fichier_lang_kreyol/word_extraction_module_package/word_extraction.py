import os

from fichier_lang_kreyol.word_sorting_module_package.word_sorting import sorting_word


def extraction(file_name):
    try:

        with open(file_name, 'r') as fichier:
            # Lire le contenu du fichier
            contenu = fichier.read()

            # Diviser le contenu en mots en utilisant un espace comme séparateur
            mots = contenu.split()

        # Obtenir le chemin complet du fichier de sortie
        chemin_sortie = os.path.abspath('text_extract.txt')

        # Ouvrir le fichier en mode écriture
        with open(chemin_sortie, 'w') as fichier_sortie:
            # Écrire chaque mot sur une ligne distincte
            for mot in mots:
                lower_words = mot.lower()
                fichier_sortie.write(lower_words + '\n')

        # Afficher un message de confirmation
        print(f'Fichier sauvegardé dans : {chemin_sortie}')
        print('Maintenant procédons au tri ')

        # Retourner le chemin complet du fichier créé
        return chemin_sortie

    except FileNotFoundError:
        print('Le fichier n\'existe pas')




file_name = input('Entrez le nom du fichier (chemin complet du fichier) : ')

sorting_word(extraction(file_name))

# extraction(file_name)
# sorting_word()