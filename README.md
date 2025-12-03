# KI-gestützte E-Mail-Klassifikation  
**Prototyp zur automatisierten Themenzuordnung**

## Thema des Projekts
Dieses Projekt entsteht im Rahmen meines IHK-Abschlussprojekts 2025/2026.  
Ziel ist die Entwicklung eines Prototyps, der eingehende E-Mails automatisch analysiert, in inhaltliche Kategorien einordnet (z. B. Mitarbeiterangelegenheiten, Zahlungen, Support) und anschließend eine Weiterleitungsentscheidung simuliert.

## Projektbeschreibung
Der Prototyp soll:
- E-Mails einlesen und vorverarbeiten  
- deren Inhalt thematisch klassifizieren  
- die Klassifikation evaluieren (Genauigkeit, F1-Score usw.)  
- verschiedene Modelle vergleichen  

### Datenbasis
Die Trainingsdaten bestehen aus:
- **übersetzten Enron-E-Mails** (EN → DE),  
- **selbst generierten E-Mails**, um deutsche Syntax und typische Formulierungen abzudecken,  
- **öffentlich verfügbaren Beispieldaten**, soweit zulässig.

Alle Daten werden anonymisiert oder synthetisch erzeugt, sodass keine personenbezogenen Informationen enthalten sind.

### Hinweis zu großen Datensätzen
Der Enron-Datensatz kann hier nicht hochgeladen werden.  
Er ist unter folgendem Link verfügbar:

🔗 **https://www.kaggle.com/datasets/wcukierski/enron-email-dataset**

---

## Fortschritt

### **Tag 1**
**Schritt 1:** Projektstruktur angelegt  
<img width="742" height="380" alt="Baumstruktur" src="https://github.com/user-attachments/assets/201bdfa0-9237-4d9c-bcbb-329b1256f26c" />

**Schritt 2:** Mini-Dataset erstellt  
Für erste Funktionstests wurde ein kleines Test-Dataset mit  
„Betreff“, „Body“ und „Abteilung“ erstellt.

---

### **Tag 2**

- Änderungen im Code vorgenommen:
  - 5.000 E-Mails aus dem Enron-Datensatz eingelesen und in neue CSV-Dateien exportiert.
  - 5.000 E-Mails bereinigt und geparst.

- **Ergebnis:**
  Der Enron-Datensatz ist für die KI-Automatisierung ungeeignet. Er enthält viele spezifische Header und Sonderzeichen. Außerdem besteht er nicht nur aus geschäftlichen E-Mails, sondern auch aus privaten Nachrichten zwischen Mitarbeitenden.  
  Daher haben wir uns entschieden, auf synthetisch erstellte E-Mails umzusteigen.
  Code wurde trotzdem in Projekt drin gelassen, falls in Zukunft ähnliche Art von Code gebraucht wird.

- **Entscheidung:**
  Ab sofort wird ausschließlich der Spam-Datensatz verwendet; Enron-Daten werden nicht weiter genutzt.  
  Zusätzlich wurde im Ordner `data` eine lizenzfreie `spam.csv` eingefügt, die etwa 5.500 E-Mails enthält.

### **Tag 3**




