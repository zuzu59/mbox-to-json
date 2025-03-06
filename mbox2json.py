#!/usr/bin/env python3

import mailbox
import json
from email import policy
from email.parser import BytesParser

def mbox_to_json(mbox_path, json_path):
    # Ouvrir le fichier mbox
    mbox = mailbox.mbox(mbox_path)

    # Liste pour stocker les emails en format JSON
    emails_json = []

    # Parcourir chaque message dans le fichier mbox
    for message in mbox:
        # Analyser le message avec la politique par défaut
        msg = BytesParser(policy=policy.default).parsebytes(message.as_bytes())

        # Extraire les informations souhaitées
        email_data = {
            'subject': msg['subject'],
            'from': msg['from'],
            'to': msg['to'],
            'date': msg['date'],
            'body': ''
        }

        # Vérifier si le corps du message existe
        body = msg.get_body(preferencelist=('plain',))
        if body:
            email_data['body'] = body.get_content()

        # Ajouter les données de l'email à la liste
        emails_json.append(email_data)

    # Écrire les données JSON dans un fichier
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(emails_json, json_file, ensure_ascii=False, indent=4)

# Exemple d'utilisation
mbox_path = './data/ClubDesk-Résiliés.mbox'
json_path = './data/toto.json'
mbox_to_json(mbox_path, json_path)
