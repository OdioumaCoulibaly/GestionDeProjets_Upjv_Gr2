#!/usr/bin/env python3
import speech_recognition as sr
import logging


def Rec():
    # Initialisation du recognizer
    r = sr.Recognizer()
    # Écouter l'audio avec le microphone
    logging.getLogger('speech_recognition').setLevel(logging.ERROR)
    with sr.Microphone() as source:
        print("Dites quelque chose :")
        audio = r.listen(source)

    # Essayer de reconnaître le texte à partir de l'audio enregistré
    try:
        text = r.recognize_google(audio, language="fr-FR")
        print(f"Vous avez dit : {text}")
        # Ouvrir le fichier en mode "append" (ajouter à la fin du fichier)
        return text

    except sr.UnknownValueError:
        print("Je n'ai pas compris ce que vous avez dit")
    except sr.RequestError as e:
        print(f"Erreur lors de la reconnaissance vocale : {e}")
