#!/usr/bin/env bash
#Petit script pour démarrer les conversions .mbox en .txt et .json facilement
#zf250306, zf250306.1417

# source: 


echo -e "
Démarrage de la conversion...
"

# Extraire le chemin et le nom du fichier sans l'extension
zfilepath="$1"
zdirname=$(dirname "$zfilepath")
zbasename=$(basename "$zfilepath" .mbox)

# converti le fichier .mbox et .txt
echo -e "Conversion en txt..."
./conv_mbox_to_txt.py "$1" "$zdirname/$zbasename.txt"

# converti le fichier .mbox et .json
echo -e "Conversion en json..."
./conv_mbox_to_json.py "$1" "$zdirname/$zbasename.json"


echo -e "
Conversion terminée

"
