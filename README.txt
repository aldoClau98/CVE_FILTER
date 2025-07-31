
################################# CVE Vector Filter Tool #############################


Questo strumento analizza un file .csv contenente informazioni sulle vulnerabilità (CVE) e filtra solo quelle che rispettano criteri specifici del vettore CVSS.
L’obiettivo è individuare le vulnerabilità potenzialmente più sfruttabili, secondo parametri tecnici come complessità, privilegi richiesti e vettore d'attacco.


################################# Come si usa #################################

Esecuzione base:

python filtro_cve.py input.csv -o output_filtrato.csv

Parametri:

input.csv: CSV contenente l'elenco delle CVE e i relativi vettori CVSS.

-o output.csv: (opzionale) nome del file CSV filtrato. Default: filtered_cve.csv

################################# Cosa fa lo script #################################

Prende in input un file CSV generato da uno scraper (es. dallo script principale che estrae CVE da nvd.nist.gov).

Legge riga per riga le informazioni e analizza il campo "CVSS Vector".

Applica un filtro preciso basato su:

AC:L (Attack Complexity: Low)

PR:L o PR:N (Privilege Required: Low o None)

AV:L, AV:R, AV:A (Attack Vector: Local, Remote o Adjacent)

Genera un nuovo CSV contenente solo le vulnerabilità che soddisfano tutti questi criteri.

################################# Formato del file CSV di input #################################

Il file CSV deve avere un header e deve includere almeno le seguenti colonne:

CVE | CVSS Vector | Fonte | Descrizione | Severity

Esempio di riga:

CVE-2022-33742,CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:H,NVD (crawl),Linux disk/nic frontends data leaks,7.1 HIGH

################################# Requisiti #################################

Lo script richiede Python 3.6 o superiore.

################################# Dipendenze #################################

L’unica dipendenza esterna usata è argparse, che è inclusa nella libreria standard di Python.

Per sicurezza puoi installare tutto con:

pip install -r requirements.txt

Nota: il file requirements.txt è opzionale. Se vuoi crearlo manualmente, puoi lasciarlo vuoto o includere solo argparse per chiarezza.


################################# Criteri di filtro (hardcoded) #################################

Lo script considera valide solo le CVE che contengono nel campo “CVSS Vector”:

AC:L (Attack Complexity: Low)

PR:L oppure PR:N (Privilege Required: Low o None)

AV:L, AV:R oppure AV:A (Attack Vector: Local, Remote o Adjacent)

Esempio accettato:
CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

Esempio scartato:
CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:C/C:L/I:L/A:N

################################# Esclusione del filtro severity #################################

Il filtro basato sulla Severity (HIGH / MEDIUM) è stato disattivato su richiesta,
 ma è commentato nello script e può essere facilmente riattivato.


################################# Output #################################

Lo script genera un file CSV contenente solo le CVE che superano il filtro.
Mantiene tutte le colonne originali.

Esempio output (filtered_cve.csv):

CVE,CVSS Vector,Fonte,Descrizione,Severity
CVE-2022-33742,CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:H,NVD (crawl),Linux disk/nic frontends data leaks,7.1 HIGH