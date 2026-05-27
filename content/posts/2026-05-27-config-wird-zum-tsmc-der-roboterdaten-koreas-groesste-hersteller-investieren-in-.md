---
title: Config wird zum 'TSMC der Roboterdaten' - Koreas größte Hersteller investieren
  in Datenpipeline für lernende Roboter
date: '2026-05-27T10:35:34+02:00'
draft: false
tags:
- Roboterdaten
- Maschinelles Lernen
- Startup
categories:
- Startups
summary: Wie ein koreanisches Startup mit Unterstützung der größten Hersteller des
  Landes den Ansatz verfolgt, nicht Roboter selbst zu bauen, sondern die kritische
  Infrastruktur für Roboterdaten bereitzustellen - ein Paradigmenwechsel in der Robotik-Industrie
ShowToc: true
TocOpen: false
---

Die koreanische Robotik-Industrie erlebt gerade einen bemerkenswerten strategischen Wandel. Während weltweit Unternehmen um die Vorherrschaft bei humanoiden Robotern, Industriearmen und autonomen Systemen wetteifern, setzt ein koreanisches Startup auf einen gänzlich anderen Ansatz: Config will nicht den besten Roboter bauen, sondern die kritische Infrastruktur bereitstellen, die alle Roboter zum Lernen benötigen. Die Analogie liegt nahe – was TSMC für die Chipindustrie ist, möchte Config für die Roboterdatenverarbeitung werden.

## Die Datenfrage als Achillesferse der modernen Robotik

Roboter werden zunehmend intelligenter, aber ihr Lernen steht vor einem grundlegenden Problem: Sie benötigen enorme Mengen an qualitativ hochwertigen Trainingsdaten. Während in der KI-Forschung für Sprachmodelle oder Bilderkennung auf riesige öffentliche Datensätze zurückgegriffen werden kann, existiert für robotische Anwendungen keine vergleichbare Infrastruktur. Jeder Hersteller sammelt seine eigenen Daten, entwickelt eigene Formate und löst die gleichen Probleme immer wieder neu.

Diese Fragmentierung kostet die Industrie nicht nur Ressourcen, sie verlangsamt auch den technologischen Fortschritt erheblich. Ein Roboter, der in einer Fabrik gelernt hat, Bauteile zu greifen, kann dieses Wissen nicht einfach an einen baugleichen Roboter in einer anderen Fabrik weitergeben. Die Datenformate sind inkompatibel, die Kalibrierungen unterschiedlich, die Umgebungsbedingungen verschieden dokumentiert.

## Configs Vision: Eine zentrale Datenpipeline für die Robotik

Genau hier setzt Config an. Das koreanische Startup entwickelt eine standardisierte Infrastruktur für die Erfassung, Verarbeitung, Speicherung und Bereitstellung von Roboterdaten. Die Vision ist ehrgeizig: Eine universelle Plattform zu schaffen, die es Robotern verschiedener Hersteller ermöglicht, aus gemeinsamen Datenpools zu lernen und Erfahrungen auszutauschen.

Das Geschäftsmodell erinnert tatsächlich an TSMC, den taiwanesischen Halbleiterriesen. Während TSMC keine eigenen Chips entwirft, sondern die Fertigungskapazität für andere bereitstellt, fokussiert sich Config darauf, die Dateninfrastruktur zu betreiben, ohne selbst Roboter zu bauen. Diese Spezialisierung erlaubt es dem Unternehmen, neutral zwischen verschiedenen Herstellern zu agieren und sich vollständig auf die Optimierung der Datenpipeline zu konzentrieren.

## Südkoreas Industriegiganten erkennen das strategische Potential

Die Bedeutung dieses Ansatzes haben auch die größten Fertigungskonzerne Südkoreas erkannt. Die jüngsten Investitionsrunden zeigen, dass etablierte Player die strategische Relevanz einer gemeinsamen Dateninfrastruktur verstehen. Anstatt jeweils eigene, proprietäre Systeme zu entwickeln, setzen sie auf einen kollaborativen Ansatz über Config.

Diese Unterstützung ist nicht nur finanzieller Natur. Die beteiligten Konzerne bringen auch ihr tiefes Verständnis für Fertigungsprozesse, ihre Erfahrungen mit Automatisierung und ihre konkreten Anforderungen an robotische Systeme ein. Config profitiert damit von einem direkten Zugang zu realen Produktionsumgebungen und kann seine Plattform anhand tatsächlicher industrieller Bedürfnisse entwickeln.

## Simulation, digitale Zwillinge und die Rolle von Daten

Um die technische Herausforderung zu verstehen, vor der Config steht, lohnt sich ein Blick auf die verschiedenen Ebenen robotischer Datenverarbeitung. In der modernen Robotik spielen sowohl Simulationen als auch digitale Zwillinge eine zentrale Rolle – zwei Konzepte, die oft verwechselt werden, aber unterschiedliche Zwecke erfüllen.

Simulationen dienen primär der Planung und dem Design neuer Systeme. Ingenieure nutzen sie, um verschiedene Roboterkonfigurationen zu testen, Bewegungsabläufe zu optimieren und potenzielle Probleme zu identifizieren, bevor echte Hardware gebaut wird. Die Simulation ist dabei ein "Was-wäre-wenn"-Werkzeug, das verschiedene Szenarien durchspielt.

Digitale Zwillinge hingegen sind virtuelle Abbilder realer, existierender Systeme. Sie werden kontinuierlich mit Echtzeitdaten aus der Produktion gefüttert und spiegeln den aktuellen Zustand wider. Ein digitaler Zwilling einer Fertigungslinie zeigt nicht nur, wie die Linie aufgebaut ist, sondern auch, welche Maschine gerade welchen Auftrag bearbeitet, wo es Engpässe gibt und wann Wartung ansteht.

Für lernende Roboter sind beide Ansätze relevant. In Simulationen können sie gefahrlos Millionen von Trainingsiterationen durchlaufen. Über digitale Zwillinge können sie ihre Erfahrungen aus der realen Welt strukturiert erfassen und für das Training nutzen. Config muss beide Welten verbinden und die Datenströme orchestrieren.

## Die technische Komplexität hinter der Plattform

Die Herausforderungen, die Config meistern muss, sind beträchtlich. Roboterdaten sind nicht nur umfangreich, sondern auch extrem heterogen. Ein Kamerasystem liefert Bildströme, Kraftsensoren erzeugen hochfrequente Messwerte, Greifer melden binäre Zustände, und Navigationssysteme produzieren dreidimensionale Trajektorien. All diese Datentypen müssen synchronisiert, kontextualisiert und in ein einheitliches Format überführt werden.

Hinzu kommt die zeitliche Dimension. Roboterdaten sind nicht statisch wie ein Foto oder ein Text. Sie repräsentieren dynamische Abläufe über die Zeit. Ein Greifvorgang dauert vielleicht zwei Sekunden, aber in dieser Zeit werden Tausende von Datenpunkten erfasst. Die Herausforderung liegt darin, diese temporalen Muster so zu speichern und zu annotieren, dass maschinelle Lernalgorithmen effektiv damit arbeiten können.

Ein weiterer kritischer Aspekt ist die Qualitätssicherung. Nicht alle Roboterdaten sind gleichwertig. Ein erfolgreicher Greifvorgang ist wertvoll für das Training, aber was ist mit einem Fehlversuch? Sollte der Roboter daraus lernen, was nicht funktioniert? Oder verfälschen fehlerhafte Daten nur das Training? Config muss Mechanismen entwickeln, um Datenqualität zu bewerten, zu filtern und zu kuratieren.

## Der Netzwerkeffekt als strategischer Vorteil

Der vielleicht größte Vorteil, den Config aufbauen kann, ist der Netzwerkeffekt. Je mehr Hersteller und Anwender die Plattform nutzen, desto wertvoller wird sie für alle Beteiligten. Ein Roboter, der auf Daten von tausend anderen Robotern trainiert wurde, die ähnliche Aufgaben in unterschiedlichen Kontexten ausgeführt haben, wird deutlich robuster und anpassungsfähiger sein als ein System, das nur auf hauseigene Daten zurückgreifen kann.

Dieser Effekt könnte zu einer selbstverstärkenden Dynamik führen. Frühe Nutzer profitieren von der besseren Dateninfrastruktur, ihre Roboter werden leistungsfähiger, was wiederum neue Nutzer anzieht. Im Idealfall entsteht ein Standard de facto – vergleichbar mit dem, was GitHub für Softwareentwicklung oder AWS für Cloud-Infrastruktur geworden ist.

## Herausforderungen und offene Fragen

Trotz der vielversprechenden Ausgangslage stehen Config und sein Ansatz vor erheblichen Herausforderungen. Die größte ist wahrscheinlich das Thema geistiges Eigentum. Fertigungsunternehmen betrachten ihre Prozessdaten oft als Betriebsgeheimnisse. Die Vorstellung, diese Daten – selbst in anonymisierter Form – mit Wettbewerbern zu teilen, dürfte bei vielen auf Widerstand stoßen.

Config muss daher ausgeklügelte Mechanismen für Datensouveränität und Privacy entwickeln. Federated Learning, bei dem Modelle lokal trainiert und nur die Lernergebnisse geteilt werden, könnte ein Lösungsansatz sein. Auch differenzielle Privacy-Techniken, die garantieren, dass einzelne Datenpunkte nicht rekonstruierbar sind, werden eine Rolle spielen müssen.

Eine weitere Frage ist die Standardisierung. Damit verschiedene Robotersysteme sinnvoll Daten austauschen können, braucht es gemeinsame Ontologien und Datenmodelle. Was bedeutet ein "Greifvorgang" genau? Wie wird die Position eines Objekts im Raum definiert? Solche Standards müssen in Abstimmung mit der gesamten Industrie entwickelt werden – ein politischer ebenso wie ein technischer Prozess.

## Ein Paradigmenwechsel für die Robotik-Industrie

Der Ansatz von Config repräsentiert einen fundamentalen Paradigmenwechsel in der Robotik. Bisher dominierte die Vorstellung, dass Wettbewerbsvorteile primär aus besserer Hardware oder intelligenteren Algorithmen resultieren. Config argumentiert, dass in Zukunft die Dateninfrastruktur der entscheidende Differenzierungsfaktor sein wird.

Diese Perspektive passt zu einer breiteren Entwicklung in der KI-Industrie. Auch dort hat sich gezeigt, dass Datenqualität und -quantität oft wichtiger sind als algorithmische Raffinesse. Die erfolgreichsten KI-Systeme zeichnen sich nicht primär durch neuartige Architekturen aus, sondern durch Zugang zu herausragenden Trainingsdaten und der Infrastruktur, diese effizient zu verarbeiten.

## Ausblick: Die Zukunft datengetriebener Robotik

Sollte Config mit seinem Ansatz erfolgreich sein, könnte dies die Robotik-Industrie nachhaltig verändern. Kleinere Unternehmen und Forschungseinrichtungen, die bisher nicht die Ressourcen hatten, umfangreiche Datensätze zu sammeln, könnten plötzlich auf einen reichen Pool an Trainingsdaten zugreifen. Das könnte Innovation demokratisieren und die Entwicklungszyklen für neue robotische Anwendungen drastisch verkürzen.

Gleichzeitig entstehen neue strategische Fragen. Wenn Dateninfrastruktur zur kritischen Ressource wird, wie wird der Zugang reguliert? Welche Governance-Strukturen braucht es? Und wie verhindert man, dass eine zentrale Plattform selbst zum Monopol wird und die Abhängigkeiten nur verlagert?

Die Entwicklung bleibt spannend zu beobachten. Mit der Unterstützung von Südkoreas größten Herstellern hat Config jedenfalls beste Voraussetzungen, seine Vision einer gemeinsamen Dateninfrastruktur für die Robotik Wirklichkeit werden zu lassen. Ob das Unternehmen tatsächlich zum "TSMC der Roboterdaten" wird, hängt nicht zuletzt davon ab, ob es gelingt, das Vertrauen der Industrie zu gewinnen und technische Exzellenz mit wirtschaftlicher Tragfähigkeit zu verbinden.
