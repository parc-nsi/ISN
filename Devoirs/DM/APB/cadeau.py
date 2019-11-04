def affichage_tri(voeux):
    print('{:<5} {:<40} {:<10} {:<40} {:<20}'.format('Rang', 'Lycée', 'Département', 'Filière', 'Taux'))
    for k in range(len(voeux)):
        v = voeux[k]
        print('{:<5} {:<40} {:<10} {:<40} {:<20}'.format(k + 1, v[2][:40], v[3],v[9][:40],v[32]))
