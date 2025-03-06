#!/usr/bin/env python3

import mailbox
from email import policy
from email.parser import BytesParser

def mbox_to_text(mbox_path):
    # Ouvrir le fichier mbox
    mbox = mailbox.mbox(mbox_path)

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

        # Afficher les informations de l'email
        print("Sujet:", subject)
        print("De:", sender)
        print("À:", recipient)
        print("Date:", date)
        print("Corps du message:\n", body_content)
        print("-" * 80)  # Séparateur entre les emails

# Exemple d'utilisation
mbox_path = './data/ClubDesk-Résiliés.mbox'
mbox_to_text(mbox_path)

