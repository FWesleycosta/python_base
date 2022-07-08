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
__version__= "0.0.1"
__author__= "Francisco Wesley"
__license__= "Unlicense"

import os 

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "en_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"

print(msg)