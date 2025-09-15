students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}


student_name = input("Entrez le nom de l'étudiant : ")
print(f"Etudiant: {student_name}: ")

if student_name in students:
    print(f"Notes de {student_name}: ")
    for note, valeur in students[student_name].items():
        print(f" {note} : {valeur}")
else:
    print(f"L'étudiant {student_name} n'existe pas dans la liste.")