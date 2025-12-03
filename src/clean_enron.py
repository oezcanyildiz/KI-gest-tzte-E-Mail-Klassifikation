import pandas as pd
import re


# -----------------------------------------------------------
# SUBJECT extrahieren
# -----------------------------------------------------------
def extract_subject(raw):
    if not isinstance(raw, str):
        return ""

    # nimm die erste Subject-Zeile
    match = re.search(r"Subject:\s*(.*)", raw, flags=re.IGNORECASE)
    if match:
        subject = match.group(1).strip()
        # manchmal endet die Subject-Zeile mitten im Satz → abschneiden bei Doppelpunkt
        subject = subject.split("Message-ID")[0].strip()
        return subject

    return ""


# -----------------------------------------------------------
# BODY extrahieren
# -----------------------------------------------------------
def extract_body(raw):
    if not isinstance(raw, str):
        return ""

    # Teile die Mail nach dem ersten Subject:
    parts = re.split(r"Subject:.*", raw, maxsplit=1, flags=re.IGNORECASE)
    if len(parts) < 2:
        return raw.strip()

    body = parts[1]

    # Header entfernen
    body = re.sub(
        r"^(From|To|Cc|Bcc|Date|Message-ID|Mime-Version|Content-Type|Content-Transfer-Encoding|X-\S+):.*$",
        "",
        body,
        flags=re.MULTILINE | re.IGNORECASE,
    )

    # Forward-Ketten entfernen
    body = re.split(
        r"-{2,}.*Original Message.*-{2,}", 
        body, 
        flags=re.IGNORECASE
    )[0]

    # Disclaimer entfernen
    body = re.sub(
        r"(This e-mail.*?Thank you\.)", 
        "", 
        body, 
        flags=re.DOTALL | re.IGNORECASE
    )

    # HTML-Tags entfernen
    body = re.sub(r"<[^>]+>", " ", body)

    # URLs entfernen
    body = re.sub(r"http\S+|www.\S+", " ", body)

    # Sonderzeichen entfernen
    body = body.replace("\\n", " ")
    body = body.replace("\\r", " ")
    body = re.sub(r"\s+", " ", body)

    return body.strip()


# -----------------------------------------------------------
# Hauptfunktion
# -----------------------------------------------------------
def clean_enron(input_path="projekt/data/enron_5000.csv", output_path="projekt/data/enron_clean.csv"):
    print("Lade Enron-Daten ...")

    df = pd.read_csv(input_path)

    if "message" not in df.columns:
        print("Die Datei enthält keine 'message'-Spalte. Bitte prüfen.")
        print("Gefundene Spalten:", df.columns)
        return

    # SUBJECT extrahieren
    print("Extrahiere subject ...")
    df["subject"] = df["message"].apply(extract_subject)

    # BODY extrahieren
    print("Bereinige body ...")
    df["body"] = df["message"].apply(extract_body)

    # Leere & sehr kurze Einträge entfernen
    df = df[df["body"].str.len() > 20]

    # Ausgabe speichern
    df[["subject", "body"]].to_csv(output_path, sep=";", index=False)

    print(f"Bereinigung abgeschlossen. Gespeichert unter: {output_path}")


if __name__ == "__main__":
    clean_enron()