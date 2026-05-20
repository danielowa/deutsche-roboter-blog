---
title: Roboter sollen Elektronikschrott zu Quelle für Legacy-Chips recyceln
date: '2026-05-20T10:21:23+02:00'
draft: false
tags:
- Recycling
- Nachhaltigkeit
- Automatisierung
categories:
- Automatisierung
summary: Wie autonome Robotersysteme das E-Waste-Problem lösen und gleichzeitig die
  Chipknappheit bei älteren Halbleitern adressieren könnten – eine technische und
  wirtschaftliche Analyse der automatisierten Chip-Rückgewinnung
ShowToc: true
TocOpen: false
---

Die Elektronikschrottberge wachsen weltweit unaufhaltsam. Laut dem Global E-Waste Monitor der Vereinten Nationen werden bis 2030 jährlich 82 Millionen Tonnen Elektroschrott anfallen. Weniger als ein Drittel des in diesen weggeworfenen Geräten enthaltenen Metallwerts wird derzeit tatsächlich zurückgewonnen. Während die Regulierungsbehörden zunehmend Druck auf die Recyclingindustrie ausüben – von neuen EU-Abfallversandregeln bis zu Importverboten für Elektronikschrott in Malaysia – könnte eine Lösung ausgerechnet aus der Robotik kommen. Das kalifornische Startup Tuurny entwickelt autonome Systeme, die intakte Halbleiter aus Leiterplatten bergen, bevor diese geschreddert werden. Der Ansatz könnte zwei kritische Probleme gleichzeitig adressieren: die Elektronikschrottflut und die anhaltende Knappheit bei Legacy-Chips.

## Das Problem konventionellen E-Waste-Recyclings

Herkömmliche Elektronikrecyclingverfahren folgen einem destruktiven Prinzip. Leiterplatten werden mitsamt ihren Komponenten geschreddert, die entstehenden Materialströme werden anschließend sortiert und zu Schmelzwerken transportiert. Dieser Ansatz vernichtet systematisch Bauteile, die eigentlich noch funktionsfähig wären. Speicherchips, Prozessoren, Kondensatoren und andere elektronische Komponenten werden zerstört, obwohl sie in Legacy-Systemen wertvoll sein könnten.

Besonders problematisch ist dies bei älteren Halbleitergenerationen. In Telekommunikationssystemen, Luft- und Raumfahrtanwendungen sowie Verteidigungstechnik laufen Geräte oft Jahrzehnte nach dem Ende der kommerziellen Chipproduktion. Ersatzteile werden knapp und teuer. Gleichzeitig landen jährlich Millionen funktionsfähiger RAM-Module und anderer ICs im Schredder, weil die Geräte, in denen sie verbaut sind, veraltet sind.

Die wirtschaftlichen Folgen sind erheblich. Der Wert der in Elektronikschrott enthaltenen Metalle – Kupfer, Aluminium, Tantal und Edelmetalle – wird zum Großteil nicht realisiert. Hinzu kommt, dass die manuelle Demontage von Leiterplatten personalintensiv und schwer skalierbar ist. Robotersysteme könnten hier einen grundlegenden Paradigmenwechsel einleiten.

## Autonome Chip-Rückgewinnung durch Nantul

Das von Tuurny entwickelte Robotersystem Nantul dreht die konventionelle Recyclinglogik um. Statt erst zu schreddern und dann zu sortieren, identifiziert und extrahiert das System wertvolle Komponenten, bevor die Platine mechanisch zerlegt wird. Jede Nantul-Einheit soll laut Unternehmensangaben in der Lage sein, 300 intakte RAM-Integrated-Circuits pro Stunde zu bergen.

Die technische Architektur besteht aus drei integrierten Robotersystemen. Ein Roboterarm versorgt die Entnahmeeinheiten kontinuierlich mit Platinen. Zwei tischgebundene Maschinen, die von der Bauform her an 3D-Drucker oder CNC-Fräsen erinnern, übernehmen die eigentliche Komponentenentnahme. Das Herzstück bildet ein neuronales Netzwerk, das Bauteile auf der Platine identifiziert, katalogisiert und anschließend im Internet nach den thermischen Spezifikationen der Hersteller sucht.

Mit diesen Informationen arbeitet Nantul präzise: Kontrollierte Wärmezufuhr löst das Lot, computergestützte Bildverarbeitung überwacht den Prozess in Echtzeit, und eine Vakuumsaugvorrichtung hebt die Komponente ab. Die geborgenen Chips werden nach Modellnummer und Material sortiert und können entweder zu Testlabors für eine potenzielle Wiederverwendung oder zu Schmelzwerken für die Materialrückgewinnung weitergeleitet werden.

Der Ansatz nutzt modulare, kostengünstige Komponenten und setzt auf Nvidia Jetson Nano-Hardware für die Bildverarbeitung und Steuerung. Gründer Sina Ghashghaei betont, dass die größte technische Herausforderung die Entwicklung der autonomen Computer-Vision- und Robotersteuerung war – nicht die Hardware selbst.

## Technische Herausforderungen der robotergestützten Demontage

Die automatisierte Chip-Rückgewinnung ist technisch anspruchsvoller, als es zunächst scheint. Minghui Zheng, Professor für Maschinenbau an der Texas A&M University und Experte für robotergestützte Demontage, weist auf die zentrale Schwierigkeit hin: Komponenten müssen ohne thermische, mechanische oder elektrische Beschädigung entfernt werden, sodass sie anschließend zuverlässig funktionieren.

Gebrauchte Leiterplatten variieren erheblich in Layout, Beschriftung, Alter, Verschmutzung, Lötzustand und Vorschäden. Ein Robotersystem muss die richtige Komponente identifizieren, eine passende Entnahmestrategie wählen, Wärme lokal und dosiert applizieren, das Bauteil sauber abheben und ausreichend Informationen für nachgelagerte Prüfungen und Wiedervermarktung erfassen.

RAM-Module bieten sich als Einstiegspunkt an, weil sie relativ standardisiert sind und einen hohen Wiederverwendungswert haben. Die Herausforderung skaliert jedoch erheblich, wenn das System auf andere Chiparten erweitert werden soll. Jeder Komponententyp erfordert spezifische Kenntnisse über thermische Profile, mechanische Befestigung und elektrische Empfindlichkeit.

Aus wirtschaftlicher Sicht muss das System adaptiv genug sein, um die enorme Variabilität im Elektronikschrott zu bewältigen, gleichzeitig aber kosteneffizient bleiben. Die geborgenen Komponenten müssen wertvoll genug sein, um die Kosten für Roboter, Sensorik, Prüfung, Wartung, Personal und Skalierung zu rechtfertigen.

## Vom Reparaturassistenten zum Recyclingroboter

Tuurny nahm einen ungewöhnlichen Entwicklungsweg. Das vierköpfige Startup erhielt zunächst eine NASA-Förderung für einen KI-gestützten Reparaturassistenten für Leiterplatten. Dieser setzte Computer Vision und ein spezialisiertes Large Language Model ein, um Techniker anzuleiten. Nach Abschluss dieser Entwicklung entschied sich das Unternehmen für einen Pivot in Richtung Elektronikschrott-Verarbeitung.

Die strategische Neuausrichtung erfolgte aus der Einschätzung, dass der Markt für die Verarbeitung weggeworfener Elektronik größer ist – insbesondere vor dem Hintergrund wachsenden Interesses in den USA an der Rückverlagerung von Produktionskapazitäten für kritische Mineralien und Seltene Erden. Zudem eröffnet der Ansatz die Möglichkeit, Versorgungsprobleme bei Legacy-Chips zu adressieren.

Die erste kommerzielle Anwendung ist bereits in Planung. Tuurny bereitet eine Feldeinführung mit mehreren Dutzend Maschinen bei Areera vor, einem britischen Fernsehrecycler, der monatlich 1.500 Tonnen Fernsehgeräte verarbeitet. Die Inbetriebnahme ist für Anfang 2027 geplant – ein sechsstelliger Vertrag, der das Konzept erstmals im industriellen Maßstab erproben wird.

## Wirtschaftliche und regulatorische Rahmenbedingungen

Die Marktaussichten für automatisierte Chip-Rückgewinnung verbessern sich durch verschärfte Regulierung. In Europa treten neue Abfallversandregeln in Kraft. Kalifornien erweitert Recyclinggebühren auf Produkte mit fest verbauten Batterien. Malaysia verhängt Importverbote für Elektronikschrott. All diese Maßnahmen erhöhen den Druck, mehr Wert aus Elektronikschrott zu extrahieren, bevor er geschreddert oder exportiert wird.

Tuurny verhandelt nach eigenen Angaben mit Legacy-Chip-Lieferanten und strebt Vereinbarungen für die Lieferung von zurückgewonnenem Aluminium und Kupfer an Schmelzwerke und Raffinerien an. Eine neue Lieferkette aus altem Material entsteht – vorausgesetzt, das Unternehmen kann vorhersagbare Materialströme in kommerziellen Volumina bereitstellen.

Ghashghaei räumt ein, dass die Skalierung selbst zu Lieferkettenproblemen führen könnte: Um mehr Roboter zu bauen, benötigt Tuurny ausreichend Komponenten. Die Ironie, dass ein Recycling-Roboter-Startup möglicherweise selbst unter Komponentenknappheit leiden könnte, unterstreicht die Komplexität moderner Produktions- und Kreislaufwirtschaftssysteme.

## Ausblick: Gezielte Wertschöpfung statt Massenverarbeitung

Zheng stuft Tuurnys Ansatz als vielversprechend, aber noch im frühen Stadium ein. Die zentrale Frage sei, ob die robotergestützte Demontage zuverlässig, kosteneffizient und im großen Maßstab funktionieren könne. Realistisch erscheint der Ansatz zunächst als gezielte Rückgewinnungsstrategie für wertvolle Komponenten wie RAM-Module.

Langfristig könnte die Technologie die Recyclingbranche fundamental verändern. Statt undifferenzierter Massenströme könnten selektive Systeme die wertvollsten Komponenten gezielt bergen, bevor der Rest konventionell verarbeitet wird. Dies würde nicht nur die Materialausbeute steigern, sondern auch eine zweite Lebensphase für funktionsfähige Chips ermöglichen.

Die größte Herausforderung bleibt die Skalierung. Ein modulares, kosteneffizientes System, das mit der Variabilität realer Elektronikschrottströme umgehen kann, erfordert fortgeschrittene KI-Systeme, robuste Mechanik und ausgefeilte Prozesssteuerung. Ob Tuurny diese Integration gelingt, wird sich in der geplanten Feldeinführung 2027 zeigen. Sollte das Konzept aufgehen, könnte es einen neuen Standard setzen – und aus Elektronikschrott tatsächlich eine wertvolle Ressourcenquelle machen.
