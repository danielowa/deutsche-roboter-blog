---
title: Forscherin entwickelt Methode für Roboter, um mit unvollständigen Informationen
  fundierte Vermutungen anzustellen
date: '2026-06-16T12:02:54+02:00'
draft: false
tags:
- Künstliche Intelligenz
- Maschinelles Lernen
- Robotik-Forschung
categories:
- Forschung
summary: Wie probabilistische Ansätze und maschinelles Lernen Robotern ermöglichen,
  in unsicheren Umgebungen bessere Entscheidungen zu treffen – eine Schlüsseltechnologie
  für den Einsatz außerhalb kontrollierter Laborbedingungen
ShowToc: true
TocOpen: false
---

Die größte Herausforderung für Roboter liegt nicht in der perfekten Ausführung vorprogrammierter Aufgaben, sondern im Umgang mit dem Unerwarteten. In Laboren mögen Robotersysteme zuverlässig funktionieren, doch sobald sie in die unvorhersehbare reale Welt entlassen werden, stoßen sie an ihre Grenzen. Eine neue Forschungsarbeit von Yen-Ling Kuo, Assistenzprofessorin für Informatik an der University of Virginia, zeigt nun einen vielversprechenden Weg auf, wie Roboter lernen können, fundierte Vermutungen anzustellen – eine Fähigkeit, die den Unterschied zwischen einem hilflosen Stillstand und einer erfolgreichen Aufgabenbewältigung ausmachen kann.

## Das Problem der Unsicherheit in der Robotik

Roboter haben traditionell mit einem fundamentalen Problem zu kämpfen: Sie sind darauf trainiert, in bekannten Situationen zu agieren. Sobald sich die Umgebung ändert – sei es ein Objekt in einer unerwarteten Position oder eine unbekannte Griffposition – können kleine Fehler schnell zu einem kompletten Systemausfall führen. Ein Roboter, der gelernt hat, einen Apfel in einer bestimmten Ausrichtung zu schneiden, scheitert möglicherweise vollständig, wenn der Apfel nur leicht gedreht ist.

Diese Limitierung hat ihre Wurzeln in der Art und Weise, wie Roboter lernen. Historisch gesehen erfolgte das Training durch direkte Nachahmung: Ein Forscher führte den Roboter manuell durch eine Aufgabe, und die Maschine wiederholte diese Bewegungen. Doch diese Methode ist nur so robust wie die Trainingsszenarien es zulassen. In einer Welt voller Variabilität ist das schlicht nicht ausreichend.

## Von DAgger zu Diff-DAgger: Ein evolutionärer Sprung

Um diese Herausforderung anzugehen, entwickelten Forscher die Dataset Aggregation-Methode, kurz DAgger. Dabei überwacht ein menschlicher Operator den Roboter während der Aufgabenausführung und greift in Echtzeit ein, wenn unerwartete Situationen auftreten. Diese Korrekturdaten werden kontinuierlich dem Modell hinzugefügt, sodass der Roboter lernt, sich von Fehlern zu erholen.

Eine Weiterentwicklung dieses Ansatzes war das robot-gated DAgger, bei dem Roboter selbst entscheiden können, wann sie menschliche Hilfe benötigen. Die gängigste Methode dafür: Das Training mehrerer Modelle, die bei Entscheidungen zu Rate gezogen werden. Stimmen alle Modelle überein, führt der Roboter die Aktion aus. Bei Uneinigkeit signalisiert er Unsicherheit und fordert Unterstützung an.

Doch dieser Ansatz hat entscheidende Schwächen. Mit zunehmender Komplexität der Modelle wird es praktisch unmöglich, mehrere Kopien parallel zu trainieren. Noch grundlegender ist das Problem, dass Uneinigkeit zwischen Modellen nicht zwingend Unsicherheit bedeutet – sie könnte lediglich verschiedene gültige Lösungswege für dieselbe Aufgabe repräsentieren.

## Diff-DAgger: Unsicherheit als Signal nutzen

Hier setzt Kuos preisgekrönte Forschungsarbeit an. Ihre Methode, Diff-DAgger genannt, baut auf der sogenannten Diffusion Policy auf – einer Technik, die Robotern hilft, verschiedene mögliche Ausführungswege für eine Aufgabe zu berücksichtigen. Die Innovation besteht darin, den sogenannten Diffusion Loss, ein Signal, das Roboter während des Trainings zur Modellverbesserung nutzen, als Echtzeit-Vertrauensindikator umzufunktionieren.

Während der Aufgabenausführung berechnet der Roboter dieses Signal kontinuierlich und vergleicht es mittels statistischer Tests mit Werten aus den Trainingsdaten. Steht die Maschine vor einer unbekannten Situation und ist unsicher, wie sie vorgehen soll, schnellt das Signal in die Höhe. Ist die aktuelle Aktion jedoch nah an dem, was während des Trainings gelernt wurde, bleibt das Signal unauffällig.

Diese Spike-Erkennung ermöglicht es dem Roboter, drohende Fehler selbst zu diagnostizieren. Menschliches Eingreifen wird nur dann ausgelöst, wenn das Signal tatsächlich anschlägt – ansonsten kann der Roboter autonom weiterarbeiten.

## Beeindruckende Ergebnisse in der Praxis

Die Resultate dieser Methode sind bemerkenswert: Die Vorhersage von Fehlern verbesserte sich um 39 Prozent. Die Erfolgsquote bei der Aufgabenerledigung stieg um 20 Prozent, und Aufgaben wurden nahezu achtmal schneller abgeschlossen. Diese Zahlen belegen nicht nur eine theoretische Verbesserung, sondern einen praktischen Durchbruch für die Robotik.

Besonders beeindruckend ist die Effizienzsteigerung bei der Datensammlung. Weniger menschliche Überwachung bedeutet, dass Roboter schneller und kostengünstiger trainiert werden können – ein entscheidender Faktor für die Skalierung robotischer Systeme in der realen Welt.

## Probabilistische Ansätze als Schlüsseltechnologie

Kuos Arbeit steht exemplarisch für einen größeren Trend in der Robotik: die Integration probabilistischer Ansätze und maschinellen Lernens zur Bewältigung von Unsicherheit. Anstatt zu versuchen, jede mögliche Situation vorherzusehen und zu programmieren, lernen moderne Robotersysteme, mit Wahrscheinlichkeiten umzugehen und informierte Entscheidungen zu treffen, auch wenn nicht alle Informationen verfügbar sind.

Diese Fähigkeit ist fundamental für den Einsatz von Robotern außerhalb kontrollierter Laborbedingungen. Ob in der häuslichen Pflege, in der Lagerhaltung oder bei Außeneinsätzen – überall begegnen Roboter unvorhersehbaren Variablen. Die Fähigkeit, Unsicherheit zu quantifizieren und darauf angemessen zu reagieren, ist daher keine optionale Erweiterung, sondern eine Grundvoraussetzung für praktische Anwendungen.

## Theory of Mind: Der nächste Schritt

Kuos Forschung geht jedoch noch weiter. An der University of Virginia arbeitet sie an der Entwicklung von Computational Models, die Robotern helfen sollen, sowohl direkte Daten als auch subtile Signale zu interpretieren – von Sprache über Bewegungen bis hin zu Blickrichtungen. Ihr Ansatz basiert auf der „Theory of Mind", einem Konzept aus der Kognitionswissenschaft, das die Fähigkeit beschreibt, mentale Zustände anderer zu verstehen und deren Verhalten vorherzusagen.

Ein Beispiel verdeutlicht das Potenzial: Wenn zwei Studierende gemeinsam in ein Wohnheim einziehen, koordinieren sie ihre Aktivitäten oft stillschweigend. Sie interpretieren gegenseitige Verhaltensweisen und Signale, um Entscheidungen zu treffen und Aufgaben zu erledigen – ohne viele Worte. Genau diese natürliche Zusammenarbeit soll auch zwischen Mensch und Roboter möglich werden.

## Ausblick: Roboter als soziale Akteure

Die Kombination aus verbesserten Unsicherheitsschätzungen und Theory-of-Mind-Reasoning könnte Robotern den Weg in den sozialen Raum ebnen. Servicerobots und autonome Fahrzeuge würden nicht nur technisch kompetenter, sondern auch intuitiver in der Interaktion mit Menschen.

Die Anerkennung von Kuos Arbeit – sowohl durch den IEEE Robotics and Automation Society Award als auch durch das National Science Foundation Career Award – unterstreicht die Bedeutung dieser Forschungsrichtung. Mit einem fünfjährigen Fördervolumen von 665.000 US-Dollar kann sie ihre Vision weiterverfolgen: Roboter zu entwickeln, die nicht nur technisch versiert sind, sondern die auch als langfristige Begleiter im Alltag fungieren können.

Der Weg dorthin führt über die Fähigkeit, mit Unsicherheit umzugehen – eine zutiefst menschliche Kompetenz, die nun Schritt für Schritt auch Maschinen vermittelt wird.
