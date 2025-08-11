# Area destinada a importações 

import os
import platform

def limpar_tela():
    # Verifica o sistema operacional
    if platform.system() == "Windows":
        os.system('cls')  # Comando para Windows
    else:
        os.system('clear')  # Comando para Linux/macOS
