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
*(Fortschritt wird hier täglich ergänzt.)*

