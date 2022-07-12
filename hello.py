#!/usr/bin/env python3
"""Hello World Multi Languages.

Depending on the language configured in the environment, the program displays the corresponding message.

Usage:

Have the LANG variable properly configured ex:

    export LANG=pt_BR

Execution:

    python3 hello.py
    or
    ./hello.py
"""
__version__= "0.1.3"
__author__= "Francisco Wesley"
__license__= "Unlicense"

import os 
import sys

arguments = {"lang": None,"count": 1,}

for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input ("Choose a language ? ")

current_language = current_language[:5]

msg = {

    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_iT": "Ciao, Mondo!",
    "es_ES": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language] * int(arguments["count"]))