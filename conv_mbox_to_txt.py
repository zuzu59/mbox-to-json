#!/usr/bin/env python3

import mailbox
import argparse
from email import policy
from email.parser import BytesParser

def mbox_to_text(mbox_path, txt_path):
    # Ouvrir le fichier mbox
    mbox = mailbox.mbox(mbox_path)

    # Ouvrir le fichier texte pour écrire les résultats
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        # Parcourir chaque message dans le fichier mbox
        for message in mbox:
            # Analyser le message avec la politique par défaut
            msg = BytesParser(policy=policy.default).parsebytes(message.as_bytes())

            # Extraire les informations souhaitées
            subject = msg['subject']
            sender = msg['from']
            recipient = msg['to']
            date = msg['date']

            # Vérifier si le corps du message existe
            body = msg.get_body(preferencelist=('plain',))
            if body:
                body_content = body.get_content()
            else:
                body_content = "Aucun contenu texte trouvé."

            # Écrire les informations de l'email dans le fichier texte
            txt_file.write(f"Sujet: {subject}\n")
            txt_file.write(f"De: {sender}\n")
            txt_file.write(f"À: {recipient}\n")
            txt_file.write(f"Date: {date}\n")
            txt_file.write(f"Corps du message:\n{body_content}\n")
            txt_file.write("-" * 80 + "\n")  # Séparateur entre les emails

def main():
    # Configurer l'analyseur d'arguments
    parser = argparse.ArgumentParser(description="Convertir un fichier mbox en texte.")
    parser.add_argument("mbox_path", help="Chemin vers le fichier mbox.")
    parser.add_argument("txt_path", help="Chemin vers le fichier texte de sortie.")

    # Analyser les arguments
    args = parser.parse_args()

    # Appeler la fonction de conversion
    mbox_to_text(args.mbox_path, args.txt_path)

if __name__ == "__main__":
    main()
