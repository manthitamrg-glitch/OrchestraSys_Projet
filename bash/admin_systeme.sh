#!/bin/bash
echo "=== Gestion automatique des etudiants ==="
for etudiant in khadijetou mama ali
do
    echo "Creation du dossier de $etudiant"
    mkdir -p etudiants/$etudiant
    touch etudiants/$etudiant/info.txt
done
chmod 700 etudiants/khadijetou
echo "les dossiers etudiants ont ete crees avec succes."