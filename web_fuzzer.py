#!/usr/bin/env python3
# ==============================================================================
# Script: web_fuzzer.py
# Descripción: Buscador de rutas ocultas mediante peticiones HTTP GET
# Uso: python3 web_fuzzer.py http://192.168.1.50
# ==============================================================================

import urllib.request
import sys

# Lista de palabras (Wordlist básica para prueba)
wordlist = [
    "admin",
    "login",
    "uploads",
    "backup",
    "config.php",
    "db",
    "robots.txt",
    "api",
    "dashboard",
    "secret"
]

def scan_target(target_url):
    print(f"\n[*] Iniciando Fuzzing en: {target_url}\n" + "-"*40)
    
    for word in wordlist:
        url = f"{target_url.rstrip('/')}/{word}"
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Pentest-Audit-Tool)'}
        )
        try:
            with urllib.request.urlopen(req) as response:
                if response.status == 200:
                    print(f"[+] [200 OK] Ruta encontrada: {url}")
        except urllib.error.HTTPError as e:
            if e.code == 403:
                print(f"[!] [403 Prohibido] Ruta existente pero protegida: {url}")
            elif e.code == 500:
                print(f"[!] [500 Error Interno] Posible falla en la aplicación: {url}")
        except urllib.error.URLError:
            print("[X] Error de conexión con el servidor objetivo.")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Uso: python3 {sys.argv[0]} <URL_OBJETIVO>")
        print("Ejemplo: python3 web_fuzzer.py http://ejemplo.com")
        sys.exit(1)

    scan_target(sys.argv[1])
