import os

def is_image_file(filename):
    # Vérifie si le fichier est une image en se basant sur son extension
    image_extensions = ['.jpeg', '.jpg', '.png', '.JPG', '.PNG', '.JPEG']
    return any(filename.endswith(ext) for ext in image_extensions)

def rename_file(current_file_path, new_file_path, counter):
    # Renomme un fichier en utilisant le compteur pour générer un nouveau nom unique
    os.rename(current_file_path, new_file_path)
    return counter + 1

def rename_files_in_folder(folder_path, counter):
    # Renomme tous les fichiers du dossier spécifié et retourne le nouveau compteur
    i = 0
    for filename in os.listdir(folder_path):
        if is_image_file(filename):
            new_filename = str(i) + os.path.splitext(filename)[1]
            current_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            i = rename_file(current_file_path, new_file_path, i)
    return i

def rename_files_recursive(folder_path, counter):
    # Renomme récursivement les fichiers de tous les sous-dossiers
    for root, dirs, files in os.walk(folder_path):
        for directory in dirs:
            subdir_path = os.path.join(root, directory)
            counter += rename_files_in_folder(subdir_path, counter)
    return counter

def rename_files(folder_path, option):
    # Vérifie si le chemin est un dossier
    if not os.path.isdir(folder_path):
        print("Le chemin spécifié n'est pas un dossier valide.")
        return

    # Initialise le compteur
    counter = 0

    # Renomme les fichiers en fonction de l'option choisie
    if option == 1:
        counter = rename_files_in_folder(folder_path, counter)
    elif option == 2:
        counter = rename_files_recursive(folder_path, counter)
    else:
        print("Option invalide. Veuillez choisir 1 ou 2.")

    print(f"Tous les fichiers ont été renommés avec succès. ({counter} fichiers renommés)")

if __name__ == "__main__":
    folder_path = input("Veuillez entrer le chemin absolu du dossier : ")
    option = int(input("Choisissez l'option (1 pour un seul dossier, 2 pour tous les dossiers récursivement) : "))
    rename_files(folder_path, option)

