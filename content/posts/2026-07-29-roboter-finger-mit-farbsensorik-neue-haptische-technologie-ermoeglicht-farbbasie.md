---
title: 'Roboter-Finger mit Farbsensorik: Neue haptische Technologie ermöglicht farbbasiertes
  Tasten'
date: '2026-07-29T09:38:45+02:00'
draft: false
tags:
- Sensortechnik
- Haptik
- Robotergreifer
categories:
- Forschung
summary: Analyse der neuartigen Sensortechnologie, die Robotern ermöglicht, Oberflächen
  nicht nur zu ertasten, sondern auch deren Farbe zu erfühlen - ein Durchbruch für
  präzisere Manipulation und Objekterkennung in der Robotik
ShowToc: true
TocOpen: false
---

## Wenn Roboter Farben fühlen: Revolution in der taktilen Sensorik

Unsere menschliche Haut ist ein Wunderwerk der Natur. Sie nimmt Druck, Temperatur, Textur und Vibration gleichzeitig wahr und verarbeitet diese Informationen zu einem komplexen Bild der Umgebung. Robotikern bereitet die Nachbildung dieser Fähigkeiten seit jeher Kopfzerbrechen. Nun hat ein europäisches Forschungsteam einen bemerkenswerten Durchbruch erzielt: einen Roboterfinger, der Oberflächen nicht nur ertasten, sondern dabei auch deren Verformung in Farben übersetzen kann – eine völlig neue Herangehensweise an das Problem der taktilen Wahrnehmung.

Die von Wissenschaftlern der Queen Mary University London, der Universitäten Florenz, Triest und Trient entwickelte Technologie nutzt ein mechanochromisches Material, das seine Farbe abhängig von mechanischer Verformung ändert. Das Ergebnis: hochauflösende topologische Karten von berührten Objekten, die in Echtzeit und ohne Rechenverzögerung erstellt werden – mit einer beeindruckenden Auflösung von 100 Mikrometern.

## Das Prinzip: Bragg-Reflektoren und Lichtwellen

Das Herzstück der Innovation ist ein sogenannter Bragg-Reflektor, eine Struktur aus abwechselnd dichten Polymerschichten mit unterschiedlichen Brechungsindizes. Die Herstellung dieses Materials ist überraschend elegant: Ein lichtempfindlicher Film wird für sieben Minuten einem hochleistungsfähigen roten Laser mit 5 Megawatt Leistung und 635 Nanometer Wellenlänge ausgesetzt. Der Laserstrahl erzeugt ein Interferenzmuster, das den Film in alternierenden Dichten polymerisieren lässt.

Diese geschichtete Struktur reflektiert spezifische Wellenlängen des Lichts. Wenn der Reflektor durch Kontakt mit einem Objekt verformt wird, werden seine Schichten gedehnt und dünner – und reflektieren dadurch Licht anderer Wellenlängen. Für Giacomo Sasso, den Postdoktoranden im Labor von Federico Carpi, der die Idee entwickelte, war dies der Schlüssel: Die Farbe allein reicht aus, um die Topologie von Objekten zu erfassen.

## Aufbau des sensorischen Roboterfingers

Der praktische Aufbau ist ebenso durchdacht wie das Grundprinzip. Der Bragg-Reflektor ist zwischen zwei Silikonschichten eingebettet: Eine äußere, schützende Schicht und ein transparenter, fingerförmiger Silikonkörper, in dem eine Kamera und eine LED-Lichtquelle eingebettet sind.

Die Funktionsweise: Das LED-Licht durchdringt das klare Polymer des Fingers. Wenn die Fingerspitze durch ein Objekt verformt wird, reflektiert der Bragg-Reflektor Licht zur Kamera zurück – mit Wellenlängen, die vom Grad der Verformung abhängen. Rot signalisiert geringe Verformung, die Farbe wechselt über Grün zu Blau bei stärkster Deformation.

Mehrere Optimierungen erhöhen die Sensitivität des Systems: Die äußere Silikonschicht ist schwarz gefärbt, um den Farbkontrast zu verstärken und der Kamera die Interpretation der Farbinformation zu erleichtern. Die Steifigkeit der im Finger eingebetteten Kamera verstärkt zudem die Verformung des Reflektors und erzeugt größere Unterschiede in den reflektierten Wellenlängen.

## Die Herausforderung: Was brauchen Roboterfinger wirklich?

Die Entwicklung wirft eine grundlegende Frage auf, die Rich Walker, Direktor von Shadow Robot, einem der führenden britischen Unternehmen für Roboterhände, auf den Punkt bringt: Welcher Sensortyp sollte in einem Roboterfinger verbaut werden, wenn der Platz begrenzt ist und nicht alle gewünschten Sensortypen gleichzeitig integriert werden können?

"Die Antwort darauf ist... das ist eine wirklich schwierige Frage. Niemand weiß es genau", räumt Walker ein. Gerade deshalb sei die Arbeit des Teams so wertvoll: Sie präsentiert eine weitere Option, mit der Robotiker experimentieren können.

Tatsächlich hebt sich die Technologie von bisherigen Ansätzen ab. Während andere weiche Materialien für taktile Sensorik bereits erforscht wurden, kann das neue System quantitative Informationen über Tiefe und Größe aus den erzeugten topologischen Karten extrahieren. Die meisten anderen Sensoren liefern lediglich topologische Karten, die relative Größen von Objektmerkmalen zeigen, aber keine absoluten Messungen ermöglichen.

Ein weiterer konzeptioneller Unterschied: Anstatt Taxel zu verwenden – einzelne Messpunkte, die Kraft oder Druck an bestimmten räumlichen Positionen erfassen – ist die taktile Erfassung direkt in das Material des Fingers eingebettet. "Der Kernaspekt des Sensors ist, dass wir im Wesentlichen in Richtung eines Sensorelementes auf Materialebene gehen", erklärt Sasso. Die Kamera fungiert dabei als hochoptimiertes elektronisches Bauteil, das die Reaktionen des Materials direkt in digitale Signale übersetzt.

## Kritische Stimmen und praktische Herausforderungen

Nicht alle Experten sind jedoch gleichermaßen überzeugt von der praktischen Anwendbarkeit. Michael Wang, Mitbegründer und leitender Wissenschaftler bei Daimon Robotics, einem Unternehmen, das primär auf visionsbasierte Sensorik setzt, äußert sich vorsichtig optimistisch. Zwar begrüßt auch er die Erforschung neuer Sensormethoden, weist aber auf eine zentrale Schwäche weicher Materialien hin: ihre Haltbarkeit.

"Die praktischen und nützlichen Vorteile, besonders im Kontext von Roboterhänden, müssen noch getestet und validiert werden", betont Wang. Das Problem: Wenn weiche Sensormaterialien wie das verwendete Silikon durch wiederholte Nutzung abgenutzt oder beschädigt werden, spiegeln die gemessenen Signale möglicherweise nicht mehr korrekt die Topographie der Objekte wider.

Besonders herausfordernd wird es, wenn die Elektronik direkt in die Materialschicht eingebettet ist. "Ich habe noch nicht viele gute weiche Elektronik-Materialien gesehen, die wirklich langen Nutzungsperioden standhalten können", gibt Wang zu bedenken.

Sasso kontert diese Bedenken mit einem konstruktiven Argument: Da der Bragg-Reflektor nicht in direktem Kontakt mit den Objekten steht, wirkt die äußere Silikonschicht als Schutzbarriere. Zudem könne das Silikon durch bestimmte chemische Beschichtungen haltbarer gemacht werden, ergänzt Wang.

## Anwendungsperspektiven und Zukunftspotenzial

Die Forschungsgruppe hat bereits Gespräche mit Unternehmen aufgenommen, die den neuen Sensor potenziell einsetzen könnten. Die bisherigen Demonstrationen – das Abtasten eines menschlichen Fingers, eines US-Penny und eines Blattes – zeigen eindrucksvoll die Vielseitigkeit der Technologie.

Die nächste Entwicklungsstufe sieht vor, den Sensor so zu verbessern, dass er auch Objekte erfassen kann, die nicht flach auf Oberflächen liegen. Dies könnte besonders für chirurgische Instrumente interessant sein, die eine präzise Kontaktkartierung von Gewebe und Organen erfordern. Die medizinische Robotik könnte von der Fähigkeit profitieren, während minimalinvasiver Eingriffe gleichzeitig Oberflächentopologie und mechanische Eigenschaften von biologischem Gewebe zu erfassen.

Doch auch für die industrielle Manipulation verspricht die Technologie Fortschritte. Die Fähigkeit, Objekte nicht nur zu greifen, sondern ihre Oberflächenbeschaffenheit in Echtzeit zu kartieren, könnte die Präzision bei Montageaufgaben erheblich steigern. Besonders bei der Handhabung empfindlicher oder unregelmäßig geformter Objekte – etwa in der Lebensmittelverarbeitung oder Elektronikfertigung – wäre dies ein Gewinn.

## Ein neues Kapitel der Roboter-Haptik

Die Entwicklung des farbbasierten taktilen Sensors markiert einen konzeptionellen Wandel in der Robotersensorik: weg von diskreten Messpunkten, hin zu einer kontinuierlichen, materialbasierten Erfassung. Die Eleganz liegt in der Einfachheit – ein optisches Phänomen wird zur Grundlage hochpräziser Messungen.

Ob sich die Technologie in der rauen Realität industrieller Anwendungen bewähren wird, muss die Zeit zeigen. Die Herausforderungen bezüglich Langlebigkeit und Robustheit sind real und nicht trivial. Doch wie Federico Carpi betont: "Es gibt signifikante Entwicklungen, die wir erwarten, mit einem klaren Pfad zur Übertragung in reale Anwendungen."

In einer Zeit, in der humanoide Roboter und komplexe Manipulationsaufgaben zunehmend an Bedeutung gewinnen, könnte diese farbbasierte Tastsinntechnologie ein wichtiger Baustein sein. Sie zeigt, dass Innovation in der Robotik manchmal bedeutet, völlig neue Wege zu gehen – und dabei die Grenzen zwischen optischer und haptischer Wahrnehmung kreativ zu verwischen.
