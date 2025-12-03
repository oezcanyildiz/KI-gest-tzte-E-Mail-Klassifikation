import pandas as pd
import re
import os

INPUT = "projekt/data/enron_5000.csv"
OUTPUT = "projekt/data/enron_parsed.csv"


# -----------------------------------------------------
# 1. SUBJECT extrahieren
# -----------------------------------------------------

def extract_subject(text: str):
    if pd.isna(text):
        return None

    match = re.search(r"Subject:\s*(.*)", text, flags=re.IGNORECASE)
    if match:
        return match.group(1).strip()

    first_line = text.split("\n", 1)[0]
    return first_line.strip()[:120]


# -----------------------------------------------------
# 2. BODY extrahieren
# -----------------------------------------------------

def extract_body(text: str):
    if pd.isna(text):
        return ""

    parts = re.split(r"Subject:.*", text, maxsplit=1, flags=re.IGNORECASE)
    if len(parts) > 1:
        body = parts[1]
    else:
        body = text

    return body.strip()


# -----------------------------------------------------
# 3. BODY reinigen
# -----------------------------------------------------

def clean_body(text: str):
    if pd.isna(text):
        return ""

    text = re.sub(r"-{2,}\s*Original Message\s*-{2,}.*", "", text, flags=re.IGNORECASE | re.DOTALL)

    # 2. Enron-spezifische Header entfernen
    header_patterns = [
        r"X-From:.*?\n",
        r"X-To:.*?\n",
        r"X-cc:.*?\n",
        r"X-bcc:.*?\n",
        r"X-Folder:.*?\n",
        r"X-Origin:.*?\n",
        r"X-FileName:.*?\n",
        r"Content-Type:.*?\n",
        r"Content-Transfer-Encoding:.*?\n",
        r"Mime-Version:.*?\n",
        r"Message-ID:.*?\n",
        r"<<.*?>>",    
        r"_{5,}.*",    
    ]
    for pattern in header_patterns:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)

    text = re.sub(r"Subject:.*", "", text, flags=re.IGNORECASE)

    text = re.sub(r"^[A-Z]\s*\n", "", text)          # einzelne Buchstaben
    text = re.sub(r"BX?-X?-X?.*\n", "", text)        # Enron-Artefakte

    # 5. einfache E-Mail-Signatur entfernen
    text = re.sub(r"(Best regards|Regards|Sincerely|Thank you|All the best|Cynthia|PL|Take care)\b.*", "",
                  text, flags=re.IGNORECASE | re.DOTALL)

    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


# -----------------------------------------------------
# Hauptfunktion
# -----------------------------------------------------

def parse_enron():
    print("📥 Lade Enron-Datei:", INPUT)

    df = pd.read_csv(INPUT)

    print("📌 Einträge geladen:", len(df))

    # STEP 1: subject extrahieren
    print("✂️  Extrahiere Subject ...")
    df["subject_parsed"] = df["message"].astype(str).apply(extract_subject)

    # STEP 2: body extrahieren
    print("✂️  Extrahiere Body ...")
    df["body_raw"] = df["message"].astype(str).apply(extract_body)

    # STEP 3: Cleanup
    print("🧹 Reinige Body ...")
    df["body_clean"] = df["body_raw"].apply(clean_body)

    # STEP 4: leere / unbrauchbare Einträge entfernen
    df = df[df["body_clean"].str.len() > 20]

    # STEP 5: finale struktur
    final = df[["subject_parsed", "body_clean"]].rename(
        columns={"subject_parsed": "subject", "body_clean": "body"}
    )

    print("✨ Verbleibende Emails nach Reinigung:", len(final))

    print("💾 Speichere:", OUTPUT)
    final.to_csv(OUTPUT, index=False, encoding="utf-8")

    print("🎉 Fertig! Ausgabe gespeichert:", OUTPUT)


if __name__ == "__main__":
    parse_enron()
