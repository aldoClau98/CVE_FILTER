import csv
import argparse

# Nuove direttive
VALID_AV = {"AV:L", "AV:R", "AV:A"}
VALID_PR = {"PR:L", "PR:N"}
VALID_AC = {"AC:L"}

# Disattivato per ora su richiesta
# def pulisci_severita(raw):
#     """Estrae e pulisce la severity da valori come '7.1 HIGH'"""
#     if not raw:
#         return ""
#     parts = raw.strip().upper().split()
#     for part in parts:
#         if part in {"HIGH", "MEDIUM"}:
#             return part
#     return ""

def vettore_valido(vector):
    """Controlla se il vettore soddisfa AV, PR e AC richiesti"""
    vector = vector.upper()
    return (
        any(av in vector for av in VALID_AV) and
        any(pr in vector for pr in VALID_PR) and
        any(ac in vector for ac in VALID_AC)
    )

def filtro_cve(input_file, output_file):
    risultati_filtrati = []
    total = 0

    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total += 1
            vector = row.get("CVSS Vector", "").strip()

            if not vector:
                continue

            if vettore_valido(vector):
                risultati_filtrati.append(row)
            # else:
            #     print(f"Scartata: {row.get('CVE')} - {vector}")

    with open(output_file, "w", newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(risultati_filtrati)

    print(f"🔎 Analizzate: {total} righe")
    print(f"✅ CVE valide trovate: {len(risultati_filtrati)}")
    print(f"📁 Output salvato in: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Filtra CVE secondo AV, AC, PR richiesti.")
    parser.add_argument("input_csv", help="File CSV di input")
    parser.add_argument("-o", "--output", help="File CSV di output", default="filtered_cve.csv")
    args = parser.parse_args()
    filtro_cve(args.input_csv, args.output)

if __name__ == "__main__":
    main()
