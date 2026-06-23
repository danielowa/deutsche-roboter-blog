---
title: 'NVIDIA und FORT Robotics launchen Outside-In Safety: Externe Sensoren verbessern
  Sicherheit und Produktivität autonomer Roboter'
date: '2026-06-23T10:25:16+02:00'
draft: false
tags:
- Sicherheitstechnologie
- NVIDIA
- KI-gestützte Sensorik
categories:
- Industrie
summary: 'Analyse des Paradigmenwechsels in der Robotersicherheit: Wie externe Sensorsysteme
  (''Outside-In'') die bisherigen roboterzentrierten Sicherheitsansätze ergänzen und
  welche Auswirkungen dies auf die Integration von Robotern in Arbeitsumgebungen mit
  Menschen hat. Technische Tiefe zu NVIDIAs Halos-System und praktische Implementierung
  durch FORT Robotics.'
ShowToc: true
TocOpen: false
---

In der Robotik galt bisher eine einfache Grundregel: Ein autonomer Roboter ist für seine eigene Sicherheit verantwortlich. Er muss seine Umgebung wahrnehmen, Hindernisse erkennen und Kollisionen vermeiden – alles mit seinen bordeigenen Sensoren. Doch dieser roboterzentrierte Ansatz stößt zunehmend an seine Grenzen, besonders wenn Menschen und Maschinen eng zusammenarbeiten. NVIDIA und FORT Robotics präsentieren nun einen fundamentalen Paradigmenwechsel: das "Outside-In Safety"-Konzept, bei dem externe Sensorsysteme die Sicherheit autonomer Roboter überwachen und steuern.

## Der Paradigmenwechsel: Von Inside-Out zu Outside-In

Traditionelle Robotersicherheit folgt dem Inside-Out-Prinzip. Der Roboter ist eine in sich geschlossene Einheit, die mit LiDAR, Kameras, Ultraschallsensoren und anderen bordeigenen Systemen ausgestattet ist. Diese Sensoren sammeln Daten, die dann von der Roboter-Steuerung verarbeitet werden, um Entscheidungen über Bewegung, Geschwindigkeit und Sicherheitsabstände zu treffen. Dieses Konzept funktioniert grundsätzlich, bringt aber mehrere Herausforderungen mit sich.

Erstens hat jeder Roboter nur eine begrenzte Perspektive. Tote Winkel, Verdeckungen und die physikalischen Grenzen der Sensorreichweite bedeuten, dass der Roboter nie ein vollständiges Bild seiner Umgebung haben kann. Zweitens erfordert dieser Ansatz, dass jeder einzelne Roboter mit hochentwickelter und teurer Sensorik ausgestattet wird. In Umgebungen mit mehreren autonomen Systemen führt dies zu Redundanzen und hohen Kosten. Drittens fehlt die übergeordnete Koordination: Wenn mehrere Roboter in derselben Umgebung arbeiten, optimiert jeder nur sein eigenes Verhalten, ohne Kenntnis über die Absichten der anderen.

Das Outside-In-Konzept dreht diese Logik um. Statt dass jeder Roboter seine Umgebung beobachtet, beobachtet die Umgebung die Roboter – und die Menschen, die mit ihnen interagieren. Externe Sensoren, strategisch in der Arbeitsumgebung platziert, erfassen ein vollständiges Bild der Situation. Diese Daten werden zentral verarbeitet und können dann verwendet werden, um das Verhalten aller Roboter im System zu koordinieren und zu optimieren.

## NVIDIA Halos: Das technische Fundament

NVIDIA hat mit Halos ein umfassendes System geschaffen, das als technologisches Rückgrat für Outside-In Safety dient. Halos ist keine einzelne Komponente, sondern ein Full-Stack-System, das mehrere Ebenen integriert: KI-Computing, Systemsoftware, Sensordatenverarbeitung, Sicherheitsanwendungen und Überwachungsfunktionen.

Der Name Halos ist dabei durchaus programmatisch – er suggeriert einen schützenden "Heiligenschein" oder eine Hülle, die sich um den gesamten Arbeitsbereich legt. Im Kern nutzt das System NVIDIAs bewährte KI-Infrastruktur, insbesondere die leistungsfähigen Grafikprozessoren und die Software-Frameworks, die bereits in der autonomen Fahrzeugtechnik und anderen sicherheitskritischen Anwendungen erprobt wurden.

Was Halos besonders macht, ist die Integration verschiedener Datenströme in Echtzeit. Kameras, 3D-Sensoren und andere Erfassungssysteme liefern kontinuierlich Daten über die Position und Bewegung von Menschen, Robotern und anderen Objekten im Arbeitsbereich. Diese Daten werden nicht nur aufgezeichnet, sondern in Echtzeit analysiert. KI-Modelle erkennen Muster, antizipieren potenzielle Gefahrensituationen und können präventiv eingreifen, bevor es zu kritischen Situationen kommt.

Die Architektur von Halos folgt dabei den höchsten Sicherheitsstandards. Die Verarbeitung erfolgt deterministisch und nachvollziehbar – eine grundlegende Anforderung in sicherheitskritischen Systemen. Gleichzeitig ist das System modular aufgebaut, sodass es sich an unterschiedliche Arbeitsumgebungen und Anforderungen anpassen lässt.

## FORT Robotics: Praktische Implementierung und funktionale Sicherheit

Während NVIDIA mit Halos die technologische Plattform bereitstellt, bringt FORT Robotics die Expertise in funktionaler Sicherheit und praktischer Implementierung ein. FORT hat sich auf Safety-Systeme für Robotik spezialisiert und bereits umfangreiche Erfahrung mit sicherheitszertifizierten Lösungen gesammelt.

Die Partnerschaft zwischen FORT und NVIDIA kombiniert somit Hardware-beschleunigte KI-Verarbeitung mit robusten Sicherheitsprotokollen. FORT hat einen Blueprint entwickelt, der zeigt, wie Outside-In Safety in realen Produktionsumgebungen umgesetzt werden kann. Dieser Blueprint ist nicht nur theoretisch, sondern bietet konkrete Implementierungsrichtlinien, die den relevanten Sicherheitsstandards wie ISO 13849 oder IEC 61508 entsprechen.

Ein zentraler Aspekt ist dabei die Zuverlässigkeit. Externe Sensorsysteme müssen genauso ausfallsicher sein wie die Sicherheitssysteme der Roboter selbst. FORT adressiert dies durch redundante Sensorarchitekturen und fail-safe-Mechanismen. Wenn ein externer Sensor ausfällt, muss das System dies erkennen und entsprechend reagieren – entweder durch Umschaltung auf alternative Sensoren oder durch einen kontrollierten Übergang in einen sicheren Zustand.

## Praktische Vorteile in der Mensch-Roboter-Kollaboration

Die Auswirkungen von Outside-In Safety auf die praktische Zusammenarbeit zwischen Menschen und Robotern sind erheblich. In traditionellen Setups müssen Roboter oft große Sicherheitsabstände einhalten oder ihre Geschwindigkeit drastisch reduzieren, sobald sich ein Mensch nähert. Dies ist notwendig, weil der Roboter mit seinen bordeigenen Sensoren nicht präzise genug vorhersagen kann, wohin sich der Mensch bewegen wird.

Mit einem Outside-In-System ändert sich diese Dynamik fundamental. Die externen Sensoren können die Bewegungen von Arbeitern präziser verfolgen und deren Absichten besser einschätzen. Moderne KI-Modelle können aus Körperhaltung, Bewegungsrichtung und Geschwindigkeit ableiten, ob eine Person sich dem Roboter nähert oder nur zufällig in der Nähe ist. Dies ermöglicht differenziertere Sicherheitsreaktionen.

Statt starr zu stoppen, wenn jemand einen bestimmten Bereich betritt, kann der Roboter seine Geschwindigkeit graduell anpassen, alternative Routen wählen oder nur bestimmte Bewegungen pausieren, während andere Operationen weiterlaufen. Dies steigert die Produktivität erheblich, ohne Kompromisse bei der Sicherheit einzugehen – im Gegenteil, die Sicherheit wird durch die umfassendere Wahrnehmung sogar verbessert.

## Koordination mehrerer autonomer Systeme

Ein weiterer bedeutender Vorteil zeigt sich in Umgebungen mit mehreren autonomen Robotern. In Lagerhallen oder Produktionsstätten arbeiten oft Dutzende oder sogar Hunderte autonome Fahrzeuge und Manipulatoren parallel. Wenn jedes System nur seine eigene lokale Perspektive hat, kommt es zwangsläufig zu Ineffizienzen: Roboter blockieren sich gegenseitig, müssen auf Vorfahrt warten oder fahren unnötige Umwege.

Ein Outside-In-System fungiert hier als zentraler Verkehrsleiter. Es kennt die Positionen, Ziele und geplanten Routen aller Systeme und kann Konflikte bereits im Voraus erkennen und auflösen. Dies ermöglicht eine Orchestrierung, die weit über das hinausgeht, was dezentrale Systeme leisten können. Die Roboter können dichter zusammenarbeiten, effizienter navigieren und insgesamt mehr Durchsatz erreichen.

## Herausforderungen und offene Fragen

Bei aller Innovation bringt Outside-In Safety auch Herausforderungen mit sich. Die Installation und Kalibrierung eines umfassenden externen Sensorsystems erfordert zunächst höhere Anfangsinvestitionen. Während einzelne Roboter dadurch möglicherweise mit einfacherer Sensorik auskommen, muss die Infrastruktur in der Arbeitsumgebung aufgebaut werden.

Auch die Frage der Verantwortlichkeit wird komplexer. Wenn ein Unfall passiert – liegt die Verantwortung dann beim Roboterhersteller, beim Betreiber der Infrastruktur oder beim Anbieter des Sicherheitssystems? Klare rechtliche Rahmenbedingungen und Zertifizierungsprozesse müssen sich hier noch entwickeln.

Zudem müssen Datenschutzbedenken adressiert werden. Ein System, das kontinuierlich alle Bewegungen in einem Arbeitsbereich erfasst und analysiert, könnte theoretisch auch zur Überwachung von Mitarbeitern missbraucht werden. Transparenz über die Datennutzung und klare Grenzen sind hier unerlässlich.

## Ausblick: Die Zukunft hybrider Sicherheitskonzepte

Die Zukunft der Robotersicherheit liegt vermutlich nicht im vollständigen Ersatz von Inside-Out durch Outside-In, sondern in intelligenten hybriden Ansätzen. Roboter werden weiterhin über eigene Sensoren verfügen, die als Backup und für unmittelbare Reaktionen dienen. Gleichzeitig wird die externe Infrastruktur eine übergeordnete Koordinations- und Optimierungsebene bieten.

Die Zusammenarbeit zwischen NVIDIA und FORT Robotics markiert einen wichtigen Schritt in dieser Richtung. Sie demonstriert, dass die Technologie für Outside-In Safety nicht nur theoretisch möglich, sondern praktisch umsetzbar ist. Mit zunehmender Verbreitung autonomer Systeme in Industrie und Logistik wird dieser Ansatz wahrscheinlich zum Standard werden – nicht als Ersatz, sondern als essenzielle Ergänzung bisheriger Sicherheitskonzepte.

Der Paradigmenwechsel ist damit eingeleitet: Roboter werden nicht mehr als isolierte Einheiten betrachtet, die sich selbst schützen müssen, sondern als Teil eines integrierten Systems, in dem Infrastruktur, KI und Maschinen gemeinsam für Sicherheit und Effizienz sorgen.
