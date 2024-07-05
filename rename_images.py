import os

def rename_files(folder_path):
    # Vérifier si le chemin est un dossier
    if not os.path.isdir(folder_path):
        print("Le chemin spécifié n'est pas un dossier valide.")
        return

    # Liste de toutes les extensions d'images supportées
    image_extensions = ['.jpeg', '.jpg', '.png', '.JPG', '.PNG', '.JPEG']

    # Compteur pour le nommage des fichiers
    counter = 0

    # Parcourir tous les fichiers du dossier
    for filename in os.listdir(folder_path):
        # Vérifier si le fichier est une image
        if any(filename.endswith(ext) for ext in image_extensions):
            # Construire le nouveau nom de fichier
            new_filename = str(counter) + os.path.splitext(filename)[1]

            # Chemin complet du fichier actuel et du nouveau fichier
            current_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)

            # Renommer le fichier
            os.rename(current_file_path, new_file_path)

            # Incrémenter le compteur
            counter += 1

    print(f"Tous les fichiers ont été renommés avec succès.")

if __name__ == "__main__":
    folder_path = input("Veuillez entrer le chemin absolu du dossier : ")
    rename_files(folder_path)

