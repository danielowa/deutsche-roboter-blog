---
title: Radar-Sensoren messen menschliche Muskelkraft nicht-invasiv für Exoskelette
date: '2026-07-31T09:45:58+02:00'
draft: false
tags:
- Exoskelette
- Radar-Sensorik
- Mensch-Maschine-Interaktion
categories:
- Forschung
summary: Wie neue Radar-Technologie die Entwicklung von Exoskeletten und robotischen
  Mobilitätshilfen revolutioniert, indem sie präzise Muskelkraftmessung ohne implantierte
  Sensoren ermöglicht – eine Analyse der technischen Möglichkeiten und Anwendungen
ShowToc: true
TocOpen: false
---

Die Entwicklung von Exoskeletten und robotischen Mobilitätshilfen steht vor einem grundlegenden Durchbruch: Forscher haben eine Methode entwickelt, die es ermöglicht, Muskelkraft präzise und in Echtzeit zu messen – ganz ohne invasive Sensoren oder Elektroden auf der Haut. Die Lösung liegt in einer Technologie, die uns aus völlig anderen Bereichen bekannt ist: Radarsensoren. Was zunächst wie Science-Fiction klingt, könnte die Art und Weise revolutionieren, wie Exoskelette mit ihren Trägern kommunizieren und deren Bewegungsabsichten verstehen.

## Das fundamentale Problem der Mensch-Maschine-Schnittstelle

Robotische Assistenzsysteme wie Exoskelette stehen seit Jahren vor einer zentralen Herausforderung: Wie kann eine Maschine die Bewegungsabsichten eines Menschen schnell genug erkennen, um synchron und unterstützend zu reagieren? Bisherige Lösungen waren immer mit Kompromissen verbunden. Oberflächenelektroden zur Messung der Elektromyographie (EMG) sind anfällig für Störungen durch Schweiß, Bewegungsartefakte und müssen präzise platziert werden. Kraftsensoren in den Gelenken reagieren erst, wenn bereits eine Bewegung begonnen hat – oft zu spät für eine wirklich intuitive Steuerung. Implantierte Sensoren wiederum sind invasiv, bergen Infektionsrisiken und kommen nur für spezifische medizinische Anwendungen infrage.

Die neue Radar-basierte Methode verspricht, diese Limitierungen zu überwinden. Sie ermöglicht es, die Kontraktion von Muskeln durch Kleidung hindurch zu erfassen, ohne direkten Hautkontakt und mit einer Präzision, die bisher nur invasive Verfahren erreichten.

## Wie Radar in den Muskel blickt

Die Grundlage der Technologie bilden hochfrequente elektromagnetische Wellen im Millimeterwellenbereich. Diese Radarsignale werden auf den Körper gerichtet und von den verschiedenen Gewebeschichten reflektiert. Der entscheidende Effekt: Wenn sich ein Muskel kontrahiert, verändert sich seine Geometrie und Dichte. Der Muskel wird dicker, die Muskelfasern verdichten sich, und die umliegenden Gewebeschichten verschieben sich minimal.

Diese winzigen Veränderungen – oft nur wenige Millimeter – führen zu messbaren Unterschieden in den reflektierten Radarsignalen. Moderne Radarsysteme können solche Verschiebungen mit einer Auflösung im Submillimeterbereich erfassen. Durch die Analyse der Laufzeitunterschiede und Phasenverschiebungen der reflektierten Wellen lässt sich nicht nur feststellen, dass sich ein Muskel bewegt, sondern auch wie stark die Kontraktion ist.

## Von der Signalverarbeitung zur Kraftschätzung

Die eigentliche Innovation liegt jedoch nicht nur in der Hardware, sondern in der intelligenten Signalverarbeitung. Die Rohdaten eines Radarsensors sind komplex und enthalten Informationen über viele verschiedene Bewegungen gleichzeitig – Atmung, Herzschlag, Körperbewegungen und eben auch Muskelkontraktionen. Moderne Algorithmen, häufig basierend auf maschinellem Lernen, müssen diese Signale trennen und die relevanten Informationen extrahieren.

Forscher trainieren neuronale Netze darauf, spezifische Muster in den Radardaten zu erkennen, die mit bestimmten Muskelaktivitäten korrelieren. In einer Kalibrierungsphase wird das System mit bekannten Kraftwerten trainiert – beispielsweise indem Probanden gegen kalibrierte Kraftsensoren drücken, während gleichzeitig die Radardaten aufgezeichnet werden. Das trainierte Modell kann dann in Echtzeit aus neuen Radardaten die Muskelkraft schätzen.

Die Genauigkeit dieser Methode ist bemerkenswert: In ersten Studien erreichen Radar-basierte Systeme eine Korrelation mit tatsächlichen Kraftmessungen von über 90 Prozent. Die zeitliche Auflösung liegt im Bereich von Millisekunden, schnell genug für die Steuerung von Exoskeletten in Echtzeit.

## Praktische Vorteile für Exoskelette

Für die Entwicklung von Exoskeletten eröffnet diese Technologie völlig neue Möglichkeiten. Ein fundamentaler Vorteil ist die Robustheit gegenüber Umwelteinflüssen. Anders als EMG-Elektroden funktionieren Radarsensoren auch durch Kleidung, bei Feuchtigkeit und über längere Zeiträume ohne Neupositionierung. Das macht sie ideal für den Alltagseinsatz, wo Zuverlässigkeit und Benutzerfreundlichkeit entscheidend sind.

Ein weiterer Aspekt ist die Möglichkeit zur vorausschauenden Steuerung. Muskelkontraktionen beginnen bereits Millisekunden bevor eine tatsächliche Bewegung ausgeführt wird. Ein Radarsensor kann diese frühen Anzeichen der Bewegungsabsicht erfassen und das Exoskelett vorpositionieren, noch bevor der Träger die Bewegung vollständig initiiert hat. Dies führt zu einer natürlicheren, flüssigeren Interaktion zwischen Mensch und Maschine.

Für Rehabilitationsanwendungen bietet die Technologie zusätzliche diagnostische Möglichkeiten. Ärzte und Therapeuten können die Muskelaktivität ihrer Patienten objektiv quantifizieren und den Therapiefortschritt präzise dokumentieren – und das alles nicht-invasiv und ohne aufwendige Verkabelung.

## Technische Herausforderungen und Lösungsansätze

Trotz des vielversprechenden Potenzials bleiben technische Herausforderungen bestehen. Die Individualisierung ist komplex: Körperbau, Fettverteilung und Muskelarchitektur variieren stark zwischen Personen. Ein System, das für eine Person kalibriert wurde, funktioniert nicht ohne Weiteres bei einer anderen. Moderne Ansätze arbeiten mit adaptiven Algorithmen, die sich kontinuierlich an den jeweiligen Nutzer anpassen.

Auch die Mehrdeutigkeit der Signale ist ein Problem. Wenn mehrere Muskelgruppen gleichzeitig aktiv sind, überlagern sich ihre Signaturen im Radarsignal. Hier kommen Arrays aus mehreren Radarsensoren zum Einsatz, die aus verschiedenen Winkeln messen und so die räumliche Auflösung verbessern. Beamforming-Techniken, bekannt aus der Kommunikationstechnik, ermöglichen es, bestimmte Muskeln gezielt zu "fokussieren".

Die Energieeffizienz ist ein weiterer kritischer Faktor. Tragbare Exoskelette sind auf Batterien angewiesen, und leistungsstarke Radarsensoren können den Energiebedarf deutlich erhöhen. Aktuelle Entwicklungen zielen auf ultra-niedrig-leistende Radarchips ab, die mit wenigen Milliwatt auskommen und trotzdem ausreichende Genauigkeit bieten.

## Ausblick: Von der Forschung zur Anwendung

Die Radarsensorik für Muskelkraftmessung befindet sich am Übergang von der Grundlagenforschung zu ersten praktischen Anwendungen. Mehrere Forschungsgruppen weltweit arbeiten an Prototypen, die die Technologie in funktionsfähige Exoskelette integrieren. Besonders vielversprechend sind Anwendungen in der industriellen Unterstützung, wo Arbeiter schwere Lasten heben müssen, sowie in der medizinischen Rehabilitation nach Schlaganfällen oder Rückenmarksverletzungen.

Die Kombination mit anderen Sensortechnologien – Inertialsensoren für die Orientierung, Kraftsensoren in den Gelenken, optische Systeme zur Umgebungswahrnehmung – wird Exoskelette entstehen lassen, die ihre Träger intuitiver und effektiver unterstützen als je zuvor. Die Radar-basierte Muskelkraftmessung ist dabei ein entscheidendes Puzzleteil, das eine nahtlose Mensch-Maschine-Symbiose ermöglicht.

In den nächsten Jahren dürfte die Miniaturisierung der Radarsensoren weiter voranschreiten, während gleichzeitig die Algorithmen durch größere Trainingsdatensätze präziser werden. Die Vision von Exoskeletten, die sich so natürlich anfühlen wie eine Erweiterung des eigenen Körpers, rückt damit in greifbare Nähe – ermöglicht durch eine Technologie, die durch die Haut blickt, ohne sie zu berühren.
