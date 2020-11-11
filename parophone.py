import csv
f = open("assets/distance_sons.csv")
distance_sons = f.readlines()


def similarite_son(a,b):
    if a == "Â":
        a = '@'
    if b == "Â":
        b = '@'   
    'renvoie un score de similarité entre 2 sons'
    index_a = distance_sons[0].strip().split(';').index(a)
    index_b = distance_sons[0].strip().split(';').index(b)

    if index_a < index_b:
        index_a,index_b = index_b, index_a

    return(float(distance_sons[index_a].split(';')[index_b])/10)

def similarite_syllabe(a,b):
    'renvoie un score de similarité entre 2 syllabes'
    score = 0
    longeur_min = min(len(a),len(b))
    longeur_max = max(len(a),len(b))
    for i in range(longeur_min):
        score += similarite_son(a[i],b[i])
    return (score/longeur_max)

def similarite_mot(a,b):
    'renvoie un score de similarité entre 2 mots décomposés en syllabes'        
    les_syllabes_a = a.split('-')
    les_syllabes_b = b.split('-')
    longeur_min = min(len(les_syllabes_a),len(les_syllabes_b))
    longeur_max = max(len(les_syllabes_a),len(les_syllabes_b))
    score = 0
    for syllabe in range(longeur_min):
        if (syllabe == 0 or syllabe == (longeur_min-1)):
            score += similarite_syllabe(les_syllabes_a[syllabe],les_syllabes_b[syllabe])
        else:
            score += 0.6*similarite_syllabe(les_syllabes_a[syllabe],les_syllabes_b[syllabe])
    return (score/longeur_max)

def parophone(mot,nb_mots):
    'Renvoie *nb_mots* de parophones de *mot*. *mot* doit être ecrit en fo-ne-tik'
    parophones_trouves = []
    tsv_file = open("assets/Lexique383.tsv")
    dictionnaire = csv.reader(tsv_file, delimiter="\t")
    
    for row in dictionnaire:
        score = similarite_mot(mot,str(row[22]))
        if score > 0.5:
            parophones_trouves.append([score,(str(row[0]))])    
    tsv_file.close()
    parophones_trouves.sort(reverse=True)
    belle_liste = parophones_trouves[0:nb_mots]

    for mot in belle_liste:

        special_char = [['Ã»','ê'],['Ã§','ç'],['Ã®','î'],['Ã©','é'],['Ã¨','è'],['Ã¯','ï'],['Ã ','à'],['Ã¢','â'],['Ãª','ê'],['Ã´','ô']]

        for c in special_char:
            if c[0] in mot[1]:
                mot[1] = mot[1].replace(c[0], c[1])
        
        print (mot[1] + (30 - len(mot[1]))*' ' + 'score :  ' + str(round(mot[0],2)))


