import os

# from fichier_lang_kreyol.word_extraction_module_package.word_extraction import file_name

word_category = ['non', 'pwonon', 'veb', 'adjektif', 'adveb', 'pwepozisyon', 'konjonksyon', 'detèminan',
                 'entèjeksyon', 'karakte_spesyal']
repertoire = 'all_word_cat'


def sorting_word(text_file, category=word_category, rep=repertoire):
    if not os.path.exists(rep):

        try:
            os.mkdir(rep)
            print(f'Création du répertoire {rep}')
        except FileExistsError:
            pass

    for word in category:
        with open(os.path.join(rep, f'{word}.txt'), 'w') as f:
            f.write(word)


    # Boucle à travers les catégories de mots
    with open(text_file, 'r') as fichier_sortie:
        mots = fichier_sortie.read().split()

        for mot in mots:
            try:
                print(word_category)
                fichier_destination = input(f'Dans quel fichier voulez-vous enregistrer le mot "{mot}" ? ')

                with open(os.path.join(rep, f'{fichier_destination}.txt'), 'a') as f:
                    f.writelines(mot + '\n')

            except FileExistsError:
                pass

