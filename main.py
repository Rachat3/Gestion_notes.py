#Gestion Des Notes D'un Groupe
#Les Entrees
#Ce que l'utilisateur doit siasir( Le nombre d'etudiants et leurs notes).
nb_etudiants=int(input("Entrees le nombre d'etudiants dans le groupe"))
#Les traitements
#Boucle pour additionner les notes et compter les echecs(<60)
sommes_notes= 0
nb_echecs =0
#Boucle pour demander chaque note automatiquement
for i in range(nb_etudiants):
    note = float (input(f"Entrez la note de l'etudiant {i+1}"))
    sommes_notes += note

    # compter un echec si la note est inferieure a 60
    if note <60:
        nb_echecs = nb_echecs + 1
# Calcule de la moyenne finale du groupe
moyenne=sommes_notes/nb_etudiants
#Les Sorties
# Afficher la moyenne du groupe et le nombre total d'echecs
print("\n---STATISTIQUE DU GROUPE")
print(f"Nombre du groupe : {moyenne:.1f}%")
print(f"Nombre totale d'echecs: {nb_echecs:.1f}%")