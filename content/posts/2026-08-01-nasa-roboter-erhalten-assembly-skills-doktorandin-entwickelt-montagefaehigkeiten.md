---
title: 'NASA-Roboter erhalten Assembly-Skills: Doktorandin entwickelt Montagefähigkeiten
  für Weltraumrobotik'
date: '2026-08-01T09:24:59+02:00'
draft: false
tags:
- Weltraumrobotik
- NASA
- Assembly-Skills
categories:
- Forschung
summary: Wie eine Doktorandin NASA-Roboter mit Assembly-Skills ausstattet und damit
  die Zukunft autonomer Weltraummissionen prägt – technische Herausforderungen und
  Potenzial für irdische Anwendungen
ShowToc: true
TocOpen: false
---

Die Entwicklung autonomer Robotersysteme für den Weltraum stellt eine der größten technischen Herausforderungen unserer Zeit dar. Während die meisten Weltraummissionen noch immer auf vorgeplante Abläufe oder direkte Steuerung von der Erde angewiesen sind, arbeiten Forscher weltweit daran, Roboter mit echten Montagefähigkeiten auszustatten. Doch was als reines NASA-Projekt beginnt, könnte weitreichende Folgen für die Robotik auf der Erde haben – denn die Grundlagenforschung an universell einsetzbaren Robotersystemen revolutioniert gerade das gesamte Feld der verkörperten künstlichen Intelligenz.

## Das fundamentale Problem der Robotik

Anders als bei großen Sprachmodellen, die durch Training auf umfangreichen Textdaten zu beeindruckender Leistungsfähigkeit gelangen, fehlt der Robotik bislang ein vergleichbares Erfolgsrezept. Traditionelle Robotersysteme bestehen aus separaten Modulen für Wahrnehmung, Planung und Steuerung, die selten zu einer Intelligenz zusammenwachsen, die von einer Aufgabe zur nächsten oder von einem Roboter zum anderen übertragen werden kann. Das zentrale Problem verkörperter KI ist es, ein äquivalentes Rezept zu finden – doch die Fachwelt ist sich noch nicht einig, wie dieses aussehen soll.

Unternehmen wie das chinesische X Square Robot verfolgen einen expliziten Ansatz: Sie setzen auf einen integrierten Software-Stack, der von den Trainingsdaten über ein Weltmodell zur Vorhersage physikalischer Veränderungen bis hin zu einem Aktionsmodell reicht, das Wahrnehmung, Planung, Argumentation und Entscheidungsfindung zu ausführbarem Roboterverhalten zusammenführt. Die Besonderheit: Dieser Stack wird als Open-Source-Projekt entwickelt, was gerade für ressourcenintensive NASA-Projekte interessante Perspektiven eröffnet.

## Drei Prinzipien für intelligente Roboter

Der Ansatz basiert auf drei fundamentalen Prinzipien, die das traditionelle Verständnis von Roboterdaten herausfordern:

Erstens ist die Grundeinheit von Roboterdaten eine Interaktion, nicht eine Trajektorie. Eine Demonstration gilt nur dann als erfolgreich, wenn sie die Welt wie beabsichtigt verändert – nicht einfach, weil sich die Gelenke bewegt haben. Diese scheinbar simple Unterscheidung hat weitreichende Konsequenzen für die Datenqualität.

Zweitens sollte Vortraining nutzbare Fähigkeiten liefern, nicht nur eine Initialisierung für späteres Finetuning. Ein Roboter sollte bereits nach dem grundlegenden Training einsatzfähig sein, auch wenn er für spezifische Aufgaben weiter optimiert werden kann.

Drittens sollte Verhalten um physikalische Ereignisse herum modelliert werden, nicht um feste Zeitscheiben. Die physikalische Welt verändert sich durch Ereignisse – wenn Kontakt entsteht, ein Griff sich formt oder ein Objekt rutscht – nicht in gleichmäßigen Zeitfenstern.

## Datenqualität statt Datenmenge

Eine der größten Einschränkungen für universell einsetzbare Roboter ist nicht die Anzahl der Parameter, sondern die Kosten und Qualität von Interaktionsdaten. Hier setzt ein besonders innovativer Ansatz an: Statt Roboter fernzusteuern, sammeln menschliche Demonstratoren Daten, indem sie ein tragbares System mit zwei Greifern verwenden. Diese Methode der roboterfreien Datenerfassung ist nicht grundsätzlich neu, doch zwei technische Entscheidungen heben sie hervor.

Die erste ist die Qualitätskontrolle – und sie ist der außergewöhnlichste Teil. Statt aufgezeichnete Trajektorien einfach zu akzeptieren, durchlaufen sie eine Inspektionsschleife mit einem bemerkenswerten Schritt: der physikalischen Wiedergabe. Eine Stichprobe der Trajektorien wird auf dem echten Roboter abgespielt, und nur diejenigen, die die Aufgabe tatsächlich abschließen, gelten als gültig. Das macht die Validitätsrate zu einer messbaren Größe statt zu einer Annahme. Ein Greifer, der eine Sekundenbruchteil zu früh schließt, sieht in den Daten noch immer nach einem Griff aus – physikalisch hat er das Objekt jedoch weggestoßen und sollte nicht als gültig klassifiziert werden.

Die zweite Entscheidung betrifft die Kombination kostengünstiger menschlicher Daten mit knappen Roboterdaten. Das System trainiert zunächst mit einem großen Volumen roboterfreier Demonstrationen, um allgemeine Repräsentationen aufzubauen, und fügt dann eine kleine Menge echter Roboterdaten als Anker für die spezifischen Dynamiken der jeweiligen Maschine hinzu. Berichten zufolge erreicht dieser Ansatz eine Leistung, die mit einem reinen Roboterdatensatz vergleichbar ist, bei etwa zwanzigfach niedrigeren Erfassungskosten.

## Ereignisbasierte Weltmodelle

Bei der Entwicklung von Weltmodellen verfolgen Forscher einen differenzierten Ansatz. Die meisten Aktionsmodelle prognostizieren einen Bewegungsabschnitt fester Länge aus dem aktuellen Bild und der Anweisung. Das ist praktisch, segmentiert aber Verhalten in Fenster fester Dauer, sodass die Grenzen dort fallen, wo die verstrichene Zeit es vorgibt, nicht wo eine Aktion endet und die nächste beginnt.

Stattdessen behandeln moderne Weltmodelle ein aktionsbasiertes semantisches Ereignis als Einheit: ein kohärentes Verhaltensstück wie Erreichen, Greifen oder Platzieren – etwas, das in Sprache benannt, in Video gesehen und als Bewegung ausgeführt werden kann. Diese Modelle koppeln ein Text-zu-Video-Modell mit einem neu initialisierten Aktionsnetzwerk, das aus den Videomerkmalen liest, ohne sie zu überschreiben, was die visuellen Vorkenntnisse bewahrt.

Das Design bietet zwei Modi: Ein Ereignismodus läuft in variablen Segmenten und eignet sich für Argumentationen über lange Zeiträume, während ein Modus fester Länge die stetige Echtzeitausgabe erzeugt, die ein Controller benötigt. Dies platziert solche Systeme zwischen mainstream Chunk-basierten Aktionsmodellen und reinen Video-Weltmodellen.

## Weltraumanwendungen und irdische Perspektiven

Für NASA-Missionen sind diese Entwicklungen von besonderer Bedeutung. Autonome Montagearbeiten im All – sei es beim Aufbau von Raumstationen, der Wartung von Satelliten oder der Konstruktion von Mondbasen – erfordern Roboter, die nicht bei jedem Schritt von der Erde aus gesteuert werden müssen. Die Kommunikationsverzögerung zu Mars oder Mond macht Echtzeitsteuerung unmöglich. Roboter müssen eigenständig entscheiden, wie sie Objekte greifen, montieren und auf unerwartete Situationen reagieren.

Doch die Technologie beschränkt sich nicht auf den Weltraum. Die gleichen Prinzipien, die einen Roboter befähigen, im Vakuum des Alls zu operieren, machen ihn auch für irdische Anwendungen wertvoll. Ein System, das gelernt hat, mit variablen Objekten, unvorhersehbaren Situationen und der Notwendigkeit autonomer Fehlerkorrektur umzugehen, könnte in Haushalten, Pflegeeinrichtungen oder der Industrie eingesetzt werden.

## Die Herausforderung der Zuverlässigkeit

Benchmarks messen Kompetenz – ob ein Modell eine Aufgabe abschließen kann. Reale Umgebungen, ob im Weltraum oder auf der Erde, erfordern jedoch Zuverlässigkeit: sicheren und konsistenten Betrieb über Zeit in einer Umgebung, die sich täglich ändert. Das fehlende Puzzlestück ist nicht eine höhere einmalige Erfolgsquote, sondern robuste Fehlerkorrektur.

Ein zuverlässiger Roboter muss erkennen, wann er unsicher ist, wann er langsamer werden muss, wann er um Hilfe bitten sollte und wie er die Welt nach einem Fehler in einen sicheren Zustand zurückbringt. Im Weltraum kann ein Fehler katastrophale Folgen haben – im Haushalt ebenfalls, wenn auch anderer Natur. In beiden Fällen setzt sich Zuverlässigkeit nicht aus einer einzelnen Fähigkeit zusammen, sondern aus dem Zusammenspiel von Wahrnehmung, Vorhersage, Anpassungsfähigkeit und der Fähigkeit zur Selbstkorrektur.

## Ausblick: Von der Grundlagenforschung zur Anwendung

Die Entwicklung universeller Roboterfähigkeiten steht noch am Anfang. Die derzeitigen Systeme zeigen vielversprechende Ergebnisse in kontrollierten Umgebungen, doch die Übertragung auf unterschiedliche Roboterplattformen, Aufgaben und reale Szenarien mit all ihren Unwägbarkeiten bleibt eine Herausforderung. Die Tatsache, dass führende Unternehmen wie X Square Robot mit Bewertungen von über 2,9 Milliarden US-Dollar auf diese Technologie setzen, zeigt jedoch, dass Investoren Dateninfrastruktur, Grundlagenmodelle und skalierbare Trainingssysteme zunehmend als langfristige Differenzierungsmerkmale in der verkörperten KI betrachten.

Für die NASA und andere Raumfahrtorganisationen bedeutet dies, dass die Vision autonomer Weltraummissionen greifbarer wird. Roboter, die selbstständig komplexe Montageaufgaben durchführen können, würden nicht nur die Kosten senken, sondern auch völlig neue Missionsprofile ermöglichen. Gleichzeitig profitiert die terrestrische Robotik von diesen Fortschritten – ein klassisches Beispiel dafür, wie Weltraumforschung praktische Anwendungen auf der Erde hervorbringt.
