#!/usr/bin/env python3

import mailbox
import json
import argparse
import os
from email import policy
from email.parser import BytesParser

def mbox_to_json(mbox_path, output_dir):
    # Créer le répertoire de sortie s'il n'existe pas
    os.makedirs(output_dir, exist_ok=True)

    # Ouvrir le fichier mbox
    mbox = mailbox.mbox(mbox_path)

    # Parcourir chaque message dans le fichier mbox
    for i, message in enumerate(mbox):
        try:
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

            # Définir le chemin du fichier JSON pour cet email
            json_path = os.path.join(output_dir, f'email_{i + 1}.json')

            # Écrire les données JSON dans un fichier
            with open(json_path, 'w', encoding='utf-8') as json_file:
                json.dump(email_data, json_file, ensure_ascii=False, indent=4)

            print(f"Email {i + 1} sauvegardé dans {json_path}")

        except Exception as e:
            print(f"Erreur lors du traitement de l'email {i + 1}: {e}")

def main():
    # Configurer l'analyseur d'arguments
    parser = argparse.ArgumentParser(description="Convertir un fichier mbox en fichiers JSON distincts.")
    parser.add_argument("mbox_path", help="Chemin vers le fichier mbox.")
    parser.add_argument("output_dir", help="Répertoire de sortie pour les fichiers JSON.")

    # Analyser les arguments
    args = parser.parse_args()

    # Appeler la fonction de conversion
    mbox_to_json(args.mbox_path, args.output_dir)

if __name__ == "__main__":
    main()
