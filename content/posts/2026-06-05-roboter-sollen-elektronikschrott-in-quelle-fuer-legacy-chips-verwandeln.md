---
title: Roboter sollen Elektronikschrott in Quelle für Legacy-Chips verwandeln
date: '2026-06-05T10:39:46+02:00'
draft: false
tags:
- Recycling-Robotik
- Kreislaufwirtschaft
- Chip-Versorgung
categories:
- Forschung
summary: Wie autonome Recycling-Roboter die Chip-Knappheit durch E-Waste-Mining lösen
  könnten und welche technischen Herausforderungen dabei zu bewältigen sind
ShowToc: true
TocOpen: false
---

Die Welt steht vor einem wachsenden Elektronikschrottproblem: Bis 2030 werden jährlich schätzungsweise 82 Millionen Tonnen E-Waste anfallen. Gleichzeitig kämpfen viele Industrien mit einer anhaltenden Knappheit an Legacy-Chips – jenen älteren Halbleiterbausteinen, die in Telekommunikation, Luft- und Raumfahrt oder Verteidigungssystemen noch Jahrzehnte nach ihrer ursprünglichen Markteinführung benötigt werden. Ein kalifornisches Start-up namens Tuurny versucht nun, beide Probleme mit einer Lösung anzugehen: autonome Recycling-Roboter, die intakte Chips aus ausrangierten Elektronikgeräten bergen, bevor diese geschreddert werden.

## Verschwendetes Potenzial in der Schrottpresse

Die Vereinten Nationen schätzen, dass heute weniger als ein Drittel des in Elektronikschrott enthaltenen Metallwerts tatsächlich zurückgewonnen wird. Ein Großteil dieses Verlusts entsteht nicht etwa durch ineffiziente Schmelzprozesse, sondern bereits viel früher: beim Schreddern. Konventionelle Recyclingverfahren vermischen Prozessoren, Speicherchips, Kondensatoren und Edelmetalle zu einem heterogenen Materialstrom und zerstören dabei systematisch Komponenten, die eigentlich noch funktionsfähig wären.

Genau hier setzt Tuurny an. Statt Leiterplatten direkt zu zerkleinern, identifiziert und entfernt das System zunächst wiederverwendbare Bauteile – insbesondere RAM-Chips. Erst danach wird das verbleibende Material zur weiteren Verarbeitung zerkleinert. Das Unternehmen hat ein robotisches System namens Nantul entwickelt, das nach eigenen Angaben 300 intakte RAM-ICs pro Stunde bergen kann.

## Wie die Roboter arbeiten

Die technische Herausforderung ist beträchtlich. Nantul besteht aus drei miteinander verbundenen Robotersystemen: einem Zuführarm und zwei tischgroßen Maschinen, die an 3D-Drucker oder CNC-Fräsen erinnern. Der Prozess beginnt mit Computer Vision: Ein neuronales Netzwerk analysiert die Leiterplatte, identifiziert Bauteile und katalogisiert sie. Anschließend durchsucht das System das Internet nach den Wärmeprofilspezifikationen der Hersteller – entscheidend für die schonende Entfernung.

Mit einer Kombination aus gezielter Hitze, Unterdruck und präziser robotischer Steuerung werden die Chips dann von der Platine gelöst. Die Kunst besteht darin, die Lötstellen zu verflüssigen, ohne den Chip selbst zu beschädigen. Nach der Bergung sortiert das System die Komponenten nach Modellnummer und Material. "Wir schaffen eine neue Lieferkette aus altem Material, die es bisher nicht gab", erklärt Sina Ghashghaei, Gründer von Tuurny.

Minghui Zheng, der an der Texas A&M University robotische Demontagesysteme erforscht, hält den Ansatz für grundsätzlich machbar, betont aber die Schwierigkeiten: "RAM ist ein guter Ausgangspunkt, weil es einen relativ hohen Wiederverwendungswert hat und standardisierter ist als viele andere elektronische Bauteile. Die größere Herausforderung besteht jedoch darin, Chips ohne thermische, mechanische oder elektrische Schäden zu entfernen und sicherzustellen, dass sie anschließend noch zuverlässig funktionieren."

## Die Variabilität des Elektroschrotts

Jede ausrangierte Leiterplatte ist ein Unikat. Layout, Beschriftung, Alter, Verschmutzungsgrad, Lötzustand und vorherige Beschädigungen variieren erheblich. Ein autonomes System muss in Echtzeit die richtige Komponente identifizieren, eine Entfernungsstrategie wählen, Wärme lokal applizieren, das Bauteil sauber abheben und dabei genug Informationen für spätere Tests und Wiedervermarktung bewahren.

Zheng sieht genau hier die größte Hürde für die kommerzielle Skalierung: "Jedes Elektronikprodukt ist anders, und gebrauchte Platinen können beschädigt, verschmutzt oder unterschiedlich angeordnet sein. Der Roboter muss die richtigen Teile finden, sie vorsichtig entfernen und Schäden in Echtzeit vermeiden, was erhebliche Herausforderungen für robotische Wahrnehmung, Entscheidungsfindung, Planung und Manipulation schafft."

## Der Weg zur Serienreife

Tuurny setzt auf einen modularen Ansatz mit Standardkomponenten, maßgeschneiderten Steuerungen und Nvidia Jetson Nano-Hardware, um die Kosten niedrig zu halten. Das vierköpfige Team hat seine größten technischen Herausforderungen in der autonomen Bildverarbeitung und robotischen Steuerung gesehen. Ursprünglich entwickelte das Unternehmen mit NASA-Förderung einen KI-gestützten Reparaturassistenten für Leiterplatten, schwenkte dann aber auf E-Waste-Verarbeitung um, nachdem sich abzeichnete, dass der Markt für die Rückgewinnung kritischer Materialien deutlich größer ist.

Im April 2025 kündigte Tuurny einen sechsstelligen Deal mit Areera an, einem britischen TV-Recycler, der monatlich 1.500 Tonnen Fernsehgeräte verarbeitet. Der Einsatz mehrerer Dutzend Nantul-Maschinen ist für Anfang 2027 geplant – ein entscheidender Test für die Praxistauglichkeit der Technologie. Parallel führt das Unternehmen Gespräche mit Legacy-Chip-Lieferanten und potentiellen Abnehmern für zurückgewonnenes Aluminium und Kupfer.

## Open-Source-Bewegung als Beschleuniger

Die Entwicklung solcher Systeme wird durch eine parallele Revolution in der Robotik erleichtert: die zunehmende Verfügbarkeit von Open-Source-Tools für künstliche Intelligenz. Was mit dem Robot Operating System (ROS) 2007 begann – der Standardisierung grundlegender Robotikinfrastruktur –, setzt sich nun auf der Ebene der KI-gestützten Entscheidungsfindung fort.

Unternehmen wie Nvidia, Hugging Face und Alibaba haben in den letzten zwei Jahren bedeutende Open-Source-Plattformen für Robotik-KI veröffentlicht. Nvidias Cosmos-Weltmodelle generieren synthetische Trainingsdaten, während die GR00T-Modelle Robotern komplexes Denken ermöglichen. Hugging Face hat mit LeRobot seit Mai 2024 eine Community-Plattform geschaffen, auf der die Zahl der Robotik-Datensätze von 1.145 Ende 2024 auf über 58.000 explodiert ist.

Diese Demokratisierung der Technologie senkt die Einstiegshürden dramatisch. Spencer Huang, Nvidias Direktor für Robotik-Produkte, betont: "Um in die Robotik einzusteigen, braucht man heute keinen Doktortitel mehr." Computer Vision, einst ein schwieriges Problem, lässt sich mittlerweile mit wenigen Codezeilen umsetzen.

## Wirtschaftliche Realitäten

Dennoch bleiben fundamentale Fragen offen. Zheng betont, dass die wirtschaftliche Tragfähigkeit entscheidend ist: "Die zurückgewonnenen Teile sollten wertvoll genug sein, um die Kosten für Roboter, Sensorik, Tests, Wartung, Personal und Skalierung zu rechtfertigen." Für Schmelzen und Raffinerien stellt sich die Frage, ob Tuurny vorhersehbare Materialströme in kommerziell relevanten Mengen liefern kann.

Ghashghaei selbst räumt ein, dass die Skalierung an eigenen Lieferkettenbeschränkungen scheitern könnte – paradoxerweise beim Versuch, genug Komponenten zu beschaffen, um mehr Roboter zu bauen. Hinzu kommen regulatorische Entwicklungen: Neue europäische Abfallversandregeln, erweiterte Recyclinggebühren in Kalifornien für Produkte mit fest verbauten Batterien und E-Waste-Importverbote in Malaysia erhöhen 2026 den Druck, mehr Wert aus Elektronikschrott zu gewinnen.

## Ausblick: Vom Nischenprodukt zur Kreislaufwirtschaft?

Zheng bezeichnet Tuurnys Ansatz als vielversprechend, aber noch früh im Entwicklungsstadium: "Vorerst ist es realistischer als gezielte Rückgewinnungsstrategie für wertvolle Komponenten wie RAM. Die Schlüsselfrage ist, ob die robotische Demontagetechnologie zuverlässig, erschwinglich und im großen Maßstab funktionieren kann."

Der Erfolg solcher Systeme könnte weitreichende Folgen haben. Sie würden nicht nur die Verfügbarkeit schwer beschaffbarer Legacy-Chips verbessern und wertvolle Materialien zurückgewinnen, sondern auch grundsätzlich demonstrieren, dass hochpräzise robotische Sortierung im Recycling wirtschaftlich tragfähig ist. Das könnte den Weg für eine neue Generation von Kreislaufwirtschaftssystemen ebnen, die den Wert in unseren Produkten weit über deren erste Nutzungsphase hinaus bewahren – ein dringend benötigter Paradigmenwechsel in einer Welt, die jährlich Millionen Tonnen funktionsfähiger Elektronik verschrottet.
