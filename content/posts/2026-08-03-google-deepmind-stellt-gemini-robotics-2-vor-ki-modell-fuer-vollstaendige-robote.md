---
title: 'Google DeepMind stellt Gemini Robotics 2 vor: KI-Modell für vollständige Roboterkörper-Kontrolle'
date: '2026-08-03T10:23:06+02:00'
draft: false
tags:
- Foundation Models
- Google DeepMind
- Physical AI
categories:
- KI
summary: Technische Tiefenanalyse des neuen Gemini Robotics 2-Modells von Google DeepMind,
  das Robotern ermöglicht, jede Bewegung durchzudenken und ein breites Aufgabenspektrum
  zu bewältigen. Einordnung in den Kontext der Foundation Models für Physical AI und
  Vergleich mit konkurrierenden Ansätzen wie General Intuition und Reimagine Robotics.
ShowToc: true
TocOpen: false
---

Die Robotik steht vor einem Paradigmenwechsel, der dem Durchbruch der Large Language Models im Bereich der künstlichen Intelligenz ähnelt. Während Sprachmodelle wie GPT und Claude durch umfangreiches Vortraining auf breiten Datenmengen zu erstaunlich vielseitigen Systemen heranwuchsen, fehlte der Robotik bislang ein vergleichbares Erfolgsrezept. Google DeepMind präsentiert mit Gemini Robotics 2 nun einen Ansatz, der genau diese Lücke schließen soll – ein Foundation Model, das Robotern ermöglicht, jede einzelne Bewegung zu durchdenken und eine vollständige Körperkontrolle zu erreichen.

## Das fundamentale Problem der Roboter-Intelligenz

Robotersysteme wurden traditionell aus separaten Komponenten für Wahrnehmung, Planung und Steuerung zusammengesetzt – Bausteine, die selten zu einer Intelligenz verschmolzen, die sich von einer Aufgabe zur nächsten oder von einer Maschine zur anderen übertragen ließ. Das zentrale Problem der verkörperten KI bestand darin, das Äquivalent zum erfolgreichen Rezept der Sprachmodelle zu finden. Während die Community noch über den richtigen Ansatz debattiert, präsentiert Google DeepMind mit Gemini Robotics 2 eine klare Vision: ein integriertes Modell, das nicht nur einzelne Bewegungen generiert, sondern jeden Schritt im physischen Kontext versteht und plant.

Das Besondere an Gemini Robotics 2 ist die Fähigkeit zur vollständigen Körperkontrolle – ein Ansatz, der über die bisherigen fragmentierten Systeme hinausgeht. Statt separate Subsysteme für Armsteuerung, Greifplanung und Bewegungskoordination zu verwenden, ermöglicht das Modell ein ganzheitliches Verständnis des Roboterkörpers und seiner Interaktion mit der Umwelt.

## Foundation Models für Physical AI: Der aktuelle Wettlauf

Gemini Robotics 2 ist nicht der einzige Versuch, Foundation Models für die Robotik zu entwickeln. Ein aufschlussreicher Vergleich zeigt sich im Ansatz des chinesischen Unternehmens X Square Robot, das einen besonders expliziten Architektur-Stack vorgeschlagen hat. Dieser umfasst die Daten, von denen ein Roboter lernt, ein Weltmodell zur Vorhersage physischer Veränderungen sowie ein Aktionsmodell, das Wahrnehmung, Planung, Reasoning und Entscheidungsfindung integriert.

Der Stack von X Square Robot basiert auf drei Kernprinzipien: Erstens ist die grundlegende Einheit der Roboterdaten eine Interaktion, nicht eine Trajektorie – eine Demonstration gilt nur dann als erfolgreich, wenn sie die Welt wie beabsichtigt verändert. Zweitens sollte das Vortraining nutzbare Fähigkeiten erzeugen, nicht nur eine Initialisierung für späteres Fine-Tuning. Drittens sollte Verhalten um physische Ereignisse modelliert werden, nicht um fixe Zeitabschnitte.

Reimagine Robotics verfolgt einen weiteren alternativen Ansatz mit dem Schwerpunkt auf "learning on the job" – Roboter, die während des Einsatzes kontinuierlich dazulernen. Diese verschiedenen Philosophien zeigen, wie unterschiedlich die Community das grundlegende Problem angeht.

## Gemini Robotics 2: Durchdenken statt Nachahmen

Was unterscheidet Gemini Robotics 2 von bestehenden Ansätzen? Nach Angaben von Google DeepMind liegt der Kern in der Fähigkeit des Modells, Bewegungen nicht nur auszuführen, sondern zu durchdenken. Dies impliziert eine Form des Reasoning, die über simple Muster-Erkennung hinausgeht.

Während traditionelle Aktionsmodelle typischerweise eine fixe Bewegungssequenz aus dem aktuellen Bild und einer Instruktion vorhersagen, deutet die Beschreibung von Gemini Robotics 2 auf eine tiefere Integration von Planung und Ausführung hin. Das Modell könnte beispielsweise antizipieren, wie sich Objekte durch Kontakt verändern, welche Griffstrategie für ein bestimmtes Material optimal ist, oder wie Fehler während der Ausführung korrigiert werden können.

## Die Datenfrage: Qualität schlägt Quantität

Ein kritischer Faktor, den verschiedene Ansätze unterschiedlich angehen, ist die Qualität der Trainingsdaten. X Square Robot hat beispielsweise ein ausgeklügeltes Qualitätskontrollsystem entwickelt: Statt aufgezeichnete Trajektorien einfach zu akzeptieren, durchläuft das System eine physische Überprüfungsschleife. Eine Stichprobe der Trajektorien wird auf einem echten Roboter abgespielt, und nur diejenigen, die die Aufgabe tatsächlich erfüllen, gelten als gültig. Das Unternehmen berichtet von einer Validitätsrate von etwa 85 Prozent.

Diese Herangehensweise ist bemerkenswert, denn Fehler in Roboterdaten sind weitaus kostspieliger als in Sprachdaten. Ein kleiner Timing- oder Kontaktfehler kann die Bedeutung einer Demonstration völlig verändern. Wenn ein Greifer eine Sekundenbruchteil zu früh schließt, sieht die Bewegung in den Daten immer noch wie ein Greifen aus, physisch hat sie das Objekt jedoch weggestoßen.

Für Gemini Robotics 2 hat Google DeepMind vermutlich ebenfalls umfangreiche Überlegungen zur Datenqualität angestellt, auch wenn spezifische Details zur Datensammlung noch nicht öffentlich sind. Die Fähigkeit zur vollständigen Körperkontrolle setzt voraus, dass das Modell aus hochwertigen, diversen Demonstrations-Daten gelernt hat.

## Ereignis-basiertes Lernen: Eine neue Perspektive

Ein innovativer Ansatz in der Robotik-KI ist die Organisation von Verhalten um Ereignisse statt um fixe Zeitfenster. Die physische Welt verändert sich durch Ereignisse – wenn Kontakt entsteht, ein Griff sich formt oder ein Objekt rutscht – nicht in festgelegten Frame-Fenstern. Ereignis-basierte Modelle konzentrieren die Aufmerksamkeit auf diese Momente und sind besonders wichtig für Aufgaben mit langem Horizont, wie das Abräumen eines Tisches, bei denen Fortschritt eine Sequenz semantischer Ereignisse ist statt eines glatten Ablaufs.

Ob Gemini Robotics 2 einen ähnlichen ereignis-basierten Ansatz verfolgt oder eine andere Architektur verwendet, ist noch nicht im Detail bekannt. Die Betonung auf "durchdachte" Bewegungen deutet jedoch auf eine Form der hierarchischen Planung hin, die möglicherweise zwischen übergeordneten Intentionen und detaillierten Ausführungen unterscheidet.

## Cross-Embodiment: Die Herausforderung der Übertragbarkeit

Ein zentrales Versprechen von Foundation Models ist die Übertragbarkeit. Bei Gemini Robotics 2 stellt sich die Frage, inwieweit die erlernte vollständige Körperkontrolle von einem Robotertyp auf einen anderen übertragen werden kann. Roboter unterscheiden sich in Steuerfrequenz, Verzögerung, Nachgiebigkeit, Präzision der Sensorik und Kontaktdynamik.

Cross-Embodiment-Lernen benötigt eine intermediäre Abstraktion – niedriger als Sprache, aber höher als Gelenkwinkel. Es geht darum, wie man sich einem Objekt nähert, wie man Kontakt herstellt, wie man Kraft aufbringt und wie man sich von Fehlern erholt. Diese Fähigkeiten müssen so abstrahiert werden, dass sie sich auf verschiedene kinematische Konfigurationen übertragen lassen.

## Der Markt reagiert: Bewertungen in Milliardenhöhe

Der Wettlauf um Foundation Models für Robotik ist nicht nur eine akademische Übung. X Square Robot etwa hat kürzlich eine Bewertung von über 20 Milliarden Yuan (etwa 2,9 Milliarden US-Dollar) erreicht. Investoren betrachten Dateninfrastruktur, Foundation Models und skalierbare Trainingssysteme zunehmend als langfristige Differenzierungsmerkmale in der verkörperten KI.

Google DeepMind bringt in diesen Wettlauf immense Ressourcen und Expertise aus der Entwicklung von Gemini, dem multimodalen KI-System, ein. Die Erweiterung auf Robotik mit Gemini Robotics 2 ist ein logischer Schritt, der die Stärken in Vision, Sprache und Reasoning mit physischer Ausführung verbindet.

## Ausblick: Von der Demonstration zur Zuverlässigkeit

Die entscheidende Frage für alle Foundation Models in der Robotik ist nicht, ob sie beeindruckende Demonstrationen liefern können, sondern ob sie zuverlässig genug für den Alltagseinsatz sind. Benchmarks messen Kompetenz – ob ein Modell eine Aufgabe abschließen kann. Der echte Einsatz erfordert jedoch Zuverlässigkeit: sichere und konsistente Leistung über die Zeit in einer Umgebung, die sich täglich ändert.

Das fehlende Element ist robuste Fehlerbehandlung. Ein zuverlässiger Roboter muss erkennen, wann er unsicher ist, wann er langsamer werden sollte, wann er um Hilfe bitten muss, und wie er die Umgebung nach einem Fehler in einen sicheren Zustand zurückbringen kann. In einer echten Wohnung ist die Fähigkeit zur Fehlerbehebung wichtiger als die Erfolgsquote bei Einzelaufgaben, denn die Umgebung setzt sich nicht selbst zurück.

Gemini Robotics 2 markiert einen wichtigen Meilenstein auf diesem Weg. Die vollständige Körperkontrolle durch ein integriertes Foundation Model könnte der Durchbruch sein, den die Robotik benötigt. Gleichzeitig zeigen die parallelen Entwicklungen bei X Square Robot, Reimagine Robotics und anderen, dass verschiedene Architekturansätze um die beste Lösung konkurrieren. Die nächsten Monate werden zeigen, welcher Ansatz sich in der Praxis bewährt – und ob die Robotik ihr GPT-Moment tatsächlich gefunden hat.
