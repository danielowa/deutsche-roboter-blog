---
title: Roboter-Finger mit farbsensitiver Tastfähigkeit vereint haptische und visuelle
  Wahrnehmung
date: '2026-08-24T07:31:54+02:00'
draft: false
tags:
- Sensorik
- Taktile Wahrnehmung
- Robotermanipulation
categories:
- Forschung
summary: Analyse einer neuen Sensortechnologie, die Robotern ermöglicht, Oberflächentexturen
  und Farben gleichzeitig zu erfassen - ein Durchbruch für feinfühlige Manipulationsaufgaben
  in Industrie und Servicerobotik
ShowToc: true
TocOpen: false
---

Wenn Menschen mit den Fingern über eine Oberfläche streichen, nehmen sie gleichzeitig eine Vielzahl von Informationen auf: die Textur des Materials, seine Temperatur, die Form von Erhebungen und Vertiefungen – und natürlich auch seine Farbe. Für Roboter stellte diese multisensorische Wahrnehmung bislang eine erhebliche Herausforderung dar. Ein europäisches Forschungsteam hat nun einen Roboterfinger entwickelt, der haptische und visuelle Wahrnehmung auf neuartige Weise vereint: Eine farbsensitive künstliche Haut verändert ihre optischen Eigenschaften bei mechanischer Verformung und ermöglicht damit hochauflösende Tastwahrnehmung in Echtzeit.

## Das Prinzip der mechanochromischen Sensorhaut

Das Herzstück dieser Innovation ist ein sogenannter Bragg-Reflektor – eine Struktur, die aus dem Bereich der Optik bekannt ist und nun erstmals für taktile Sensorik eingesetzt wird. Giacomo Sasso, Postdoktorand an der Queen Mary University of London, kam auf die Idee, nachdem er eine Publikation über mechanochromische Materialien gelesen hatte. Solche Materialien ändern ihre Farbe bei mechanischer Belastung – ein Phänekt, das auch in der Natur vorkommt.

Die Herstellung des Sensors ist bemerkenswert präzise: Ein lichtempfindlicher Film wird sieben Minuten lang einem 5-Megawatt-Laser ausgesetzt, dessen Wellenlänge bei 635 Nanometern (rot) liegt. Der Laserstrahl erzeugt ein Interferenzmuster, das den Film in alternierenden Dichten polymerisieren lässt. Dadurch entstehen Schichten mit unterschiedlichen Brechungsindizes – die charakteristische Struktur eines Bragg-Reflektors.

Diese Schichtstruktur reflektiert spezifische Wellenlängen des Lichts. Wird der Reflektor durch Kontakt mit einem Objekt verformt, dehnen sich die Schichten, werden dünner und reflektieren Licht einer anderen Wellenlänge. Das Farbspektrum reicht von Rot bei geringer Verformung über Grün bis zu Blau bei maximaler Verformung. Sasso benötigte weniger als eine Woche, um das Material im Labor zu reproduzieren – ein Hinweis auf die praktische Umsetzbarkeit der Technologie.

## Aufbau und Optimierung des Roboterfingers

Der fertige Roboterfinger besteht aus mehreren funktionalen Schichten: Der Bragg-Reflektor ist zwischen einer schützenden Silikonschicht an der Außenseite und einem transparenten, fingerförmigen Silikonkörper eingebettet. Im Inneren des Fingers befinden sich eine Kamera und eine LED-Lichtquelle. Das LED-Licht durchdringt das transparente Polymer, und wenn der Finger ein Objekt berührt, reflektiert der verformte Bragg-Reflektor das Licht zurück zur Kamera – mit Wellenlängen, die dem Grad der Verformung entsprechen.

Um die Leistungsfähigkeit zu maximieren, nahm das Forschungsteam mehrere Optimierungen vor. Die äußere Silikonschicht wurde schwarz eingefärbt, um den Farbkontrast zu erhöhen und der Kamera eine präzisere Zuordnung von Farbe zu Morphologie zu ermöglichen. Zusätzlich verstärkt die Steifigkeit der im Finger eingebetteten Kamera die Verformung des Reflektors, was zu größeren Unterschieden in den reflektierten Wellenlängen führt.

Diese Optimierungen zahlen sich aus: Der Sensor erreicht eine Auflösung von 100 Mikrometern – das entspricht etwa dem Durchmesser eines menschlichen Haares – und das ohne rechnerische Latenz. Die Echtzeitverarbeitung ist ein entscheidender Vorteil für Anwendungen, bei denen schnelle Reaktionen erforderlich sind.

## Quantitative Messung statt relativer Topografie

Was den neuen Ansatz von bisherigen Lösungen unterscheidet, ist die Fähigkeit, quantitative Informationen über Tiefe und Größe aus den topologischen Karten zu extrahieren. Während die meisten taktilen Sensoren lediglich relative Größenverhältnisse von Objektmerkmalen erfassen können, liefert die farbbasierte Methode absolute Messwerte.

Rich Walker, Direktor von Shadow Robot, einem der führenden Unternehmen für Roboterarme in Großbritannien, zeigt sich beeindruckt von diesem grundlegend anderen Ansatz. Das Team hat den Sensor bereits erfolgreich eingesetzt, um detaillierte Karten eines menschlichen Fingers, eines US-Pennys mit seinen erhabenen Buchstaben und Lincolns Profil sowie eines Blattes zu erstellen.

Ein weiterer konzeptioneller Vorteil liegt in der Integration der Sensorik direkt ins Material. Anders als bei taxelbasierten Systemen, die Kraft oder Druck an diskreten räumlichen Punkten messen, ist hier das Material selbst das sensorische Element. Die Kamera dient lediglich als hochoptimierte Schnittstelle, die das Verhalten des Materials in digitale Signale übersetzt. Dieser Ansatz könnte die räumliche Auflösung weiter skalierbar machen, ohne zusätzliche elektronische Komponenten in den Finger integrieren zu müssen.

## Herausforderungen und praktische Validierung

Trotz der vielversprechenden Eigenschaften gibt es auch kritische Stimmen. Michael Wang, Mitgründer und Chefwissenschaftler bei Daimon Robotics, betont die Bedeutung von Langzeittests in realen Anwendungen. Weiche Materialien, wie sie in diesem Sensor verwendet werden, stehen oft vor Herausforderungen bezüglich der Haltbarkeit. Wenn Silikon durch wiederholte Nutzung erodiert oder beschädigt wird, könnten die Sensorsignale die tatsächliche Objekttopografie zunehmend ungenau wiedergeben.

Besonders problematisch wird es, wenn die Elektronik direkt in die Materialschicht eingebettet ist – ein Ingenieurproblem, für das es bislang kaum zufriedenstellende Lösungen gibt. Wang weist darauf hin, dass er nur wenige weiche elektronische Materialien kennt, die längeren Nutzungsperioden wirklich standhalten.

Die Forscher haben dieses Problem jedoch antizipiert: Da der Bragg-Reflektor nicht in direktem Kontakt mit Objekten steht, dient die äußere Silikonschicht als Schutzbarriere. Zudem lässt sich Silikon durch spezielle chemische Beschichtungen widerstandsfähiger machen. Diese Designentscheidung könnte den Unterschied zwischen einem Labordemonstrator und einem industrietauglichen Produkt ausmachen.

## Anwendungsperspektiven in Industrie und Medizin

Das Forschungsteam ist bereits in Gesprächen mit Unternehmen, die den Sensor potenziell einsetzen könnten. Die Anwendungsmöglichkeiten reichen von feinfühliger Montage in der Industrie über Servicerobotik bis hin zu medizinischen Instrumenten. Besonders vielversprechend erscheint der Einsatz in chirurgischen Werkzeugen, die eine präzise Kontaktkartierung von Gewebe und Organen erfordern.

Allerdings arbeitet das Team noch an Verbesserungen für die Erfassung von Objekten, die nicht flach auf Oberflächen liegen. Diese Erweiterung würde das Einsatzspektrum erheblich erweitern und komplexere Greif- und Manipulationsaufgaben ermöglichen.

Federico Carpi, der das Projekt an der Queen Mary University of London leitet, zeigt sich optimistisch: "Es gibt bedeutende Entwicklungen, die wir erwarten, mit einem klaren Pfad zur Überführung in reale Anwendungen." Die Kombination aus hoher räumlicher Auflösung, Echtzeitverarbeitung und dem Potenzial für quantitative Messungen macht die Technologie für verschiedene Bereiche attraktiv.

## Ausblick: Ein neues Kapitel der Robotersensorik

Die Entwicklung zeigt exemplarisch, wie interdisziplinäre Ansätze – in diesem Fall die Verbindung von Optik, Materialwissenschaft und Robotik – zu innovativen Lösungen führen können. Während klassische Ansätze versuchen, möglichst viele diskrete Sensoren in einen Roboterfinger zu integrieren, geht dieser Weg in die entgegengesetzte Richtung: Das Material selbst wird zum Sensor.

Ob sich die Technologie durchsetzen wird, hängt von mehreren Faktoren ab: der Langzeitstabilität unter realen Bedingungen, den Herstellungskosten und der Integration in bestehende Robotiksysteme. Die nächsten Jahre werden zeigen, ob der farbsensitive Roboterfinger den Sprung vom Labor in die Praxis schafft – und damit möglicherweise einen neuen Standard für taktile Wahrnehmung in der Robotik setzt.
