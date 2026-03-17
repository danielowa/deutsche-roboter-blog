---
title: 'Militärische Drohnentechnologie als Wegbereiter für autonomes Fahren: Erkenntnistransfer
  zwischen Verteidigungsforschung und ziviler Mobilität'
date: '2026-03-17T06:55:00+01:00'
draft: false
tags:
- Autonomes Fahren
- Drohnentechnologie
- Technologietransfer
categories:
- Forschung
summary: Analyse wie bewährte Technologien aus der militärischen Drohnenentwicklung
  - insbesondere Sensorfusion, Pfadplanung und Entscheidungsfindung unter Unsicherheit
  - die Entwicklung selbstfahrender Autos beschleunigen können. Diskussion der technischen
  Parallelen, ethischen Implikationen des Technologietransfers und industrieller Kooperationen
  zwischen Verteidigungs- und Automobilsektor.
ShowToc: true
TocOpen: false
---

## Wenn Kriegsdrohnen Autos das Fahren beibringen

Die Geschichte autonomer Systeme ist älter als die der selbstfahrenden Autos. Während Tesla, Waymo und andere Automobilhersteller seit gut einem Jahrzehnt an vollautonomen Fahrzeugen arbeiten, sammelt das US-Militär bereits seit den 1980er Jahren Erfahrungen mit ferngesteuerten unbemannten Luftfahrzeugen. Diese jahrzehntelange Praxis hat eine umfangreiche Wissensbasis geschaffen – doch die zivile Automobilindustrie scheint die teuer erkauften Lektionen aus der Verteidigungsforschung weitgehend zu ignorieren.

Die Parallelen zwischen militärischen Drohnen und selbstfahrenden Autos sind offensichtlicher als es zunächst scheinen mag. Beide Systeme müssen in unvorhersehbaren Umgebungen operieren, Entscheidungen unter Unsicherheit treffen und – entscheidend – benötigen sie menschliche Überwachung aus der Ferne, wenn die Autonomie an ihre Grenzen stößt. Während ein Predator-Drohne über Afghanistan kreist, kommuniziert sie mit Piloten in Nevada. Wenn ein Waymo-Fahrzeug in San Francisco nicht weiterkommt, greift ein Operator – mittlerweile aus den Philippinen – ein. Doch die technischen und operationellen Herausforderungen dieser Fernüberwachung wurden vom Militär bereits durchlebt und dokumentiert.

## Die fünf Kardinalfehler der Fernsteuerung

Die militärische Drohnenentwicklung hat fünf zentrale Problemfelder identifiziert, die direkt auf autonome Fahrzeuge übertragbar sind: Latenz, Arbeitsplatzgestaltung, Arbeitsbelastung, Training und Notfallplanung.

**Latenz** – die Verzögerung bei der Datenübertragung – ist das gravierendste Problem. Selbst unter idealen Bedingungen benötigt ein Mensch 200 bis 500 Millisekunden, um auf neue Informationen zu reagieren. Diese neuromuskuläre Verzögerung addiert sich zur Netzwerklatenz. In den Anfangstagen der Drohnenkriegführung versuchten US-Luftwaffenpiloten in Las Vegas, Drohnen im Nahen Osten per Fernsteuerung starten und landen zu lassen. Mit mindestens zwei Sekunden Verzögerung zwischen Befehl und Reaktion war die Unfallrate sechzehnmal höher als bei bemannten Kampfjets auf denselben Missionen. Das Militär stellte schließlich auf lokale Operatoren und vollautomatisierte Start- und Landeprozeduren um.

Selbstfahrende Autos verlassen sich typischerweise auf Mobilfunknetze für Befehle. Diese sind in Städten unzuverlässig und anfällig für Verzögerungen. In einem dokumentierten Vorfall wies ein Waymo-Operator ein Fahrzeug an, bei einer vermeintlich gelben Ampel links abzubiegen – doch aufgrund der Netzwerklatenz war die Ampel in der Realität bereits rot. Nachdem Waymo sein Fernsteuerungszentrum von den USA auf die Philippinen verlegte, hat sich die Latenz noch weiter erhöht. Die räumliche Distanz zwischen Operator und Fahrzeug ist nicht nur ein technisches, sondern auch ein Sicherheitsproblem.

## Interface-Design: Wenn Knöpfe Leben kosten

Schlechtes Interface-Design hat zu zahlreichen Drohnenabstürzen geführt. Die Streitkräfte lernten auf die harte Tour, dass verwirrende Bedienelemente, schwer lesbare Anzeigen und unklare Autonomiemodi katastrophale Folgen haben können. Je nach UAV-Plattform wurden zwischen 20 und 100 Prozent der durch menschliches Versagen verursachten Abstürze bei Army und Air Force bis 2004 auf mangelhaftes Interface-Design zurückgeführt.

Ein besonders eindringliches Beispiel: Bei manchen Drohnen waren die Bedienelemente so angeordnet, dass Operatoren versehentlich das Triebwerk abschalteten, wenn sie eigentlich eine Rakete abfeuern wollten. Diese Designfehler führten zu mehreren Abstürzen.

Die selbstfahrende Fahrzeugindustrie zeigt vergleichbare Probleme. Einige autonome Shuttle-Busse verwenden handelsübliche Gaming-Controller – die zwar kostengünstig, aber niemals für Fahrzeugsteuerung konzipiert waren. Die zweckentfremdete Nutzung solcher Controller kann zu Modusverwechslungen führen, die zu Unfällen beigetragen haben. Intensive Tests mit menschlichen Operatoren sind unerlässlich, nicht nur vor der Systemeinführung, sondern auch nach größeren Software-Updates.

## Arbeitsbelastung: Zwischen Langeweile und Überforderung

Drohnenmissionen umfassen typischerweise lange Überwachungsphasen mit gelegentlichen Einsätzen. Diese Missionen können sich über Tage hinziehen, während das Militär beispielsweise darauf wartet, dass eine Zielperson ein Gebäude verlässt. Die Operatoren erleben dadurch extreme Schwankungen in der Arbeitsbelastung: von erdrückender Langeweile bis zu überwältigender Intensität. Beide Zustände können zu Fehlern führen.

Bei Fernsteuerung ist die Arbeitsbelastung hoch und Ermüdung setzt schnell ein. Übernimmt die Bordautonomie jedoch die meiste Arbeit, können Operatoren gelangweilt, selbstgefällig und unaufmerksam werden. Dieses Muster ist in der UAV-Forschung gut dokumentiert.

Die Betreiber selbstfahrender Autos erleben wahrscheinlich ähnliche Probleme – von der Interpretation verwirrende Verkehrszeichen bis zur Unterstützung von Fahrzeugen, die in Sackgassen festsitzen. In einfachen Szenarien droht Langeweile, in Notfällen – etwa beim Fahren in überschwemmte Gebiete oder während stadtweiter Stromausfälle – kann schnell Überforderung eintreten.

Das Militär versuchte jahrelang, einen einzelnen Operator mehrere Drohnen gleichzeitig überwachen zu lassen, da dies deutlich kosteneffizienter wäre. Doch die kognitiven Umschaltkosten – das Wiedererlangen des Situationsbewusstseins nach dem Wechsel zwischen Drohnen – führen zu Arbeitsspitzen und hohem Stress. Gekoppelt mit zunehmend komplexen Schnittstellen und Kommunikationsverzögerungen erwies sich dies als äußerst schwierig.

Selbstfahrende Autounternehmen stehen vor denselben Hindernissen. Sie müssen die Arbeitsbelastung der Operatoren modellieren und zuverlässig vorhersagen können, wie viele Fahrzeuge eine einzelne Person effektiv überwachen kann, insbesondere bei Notfalleinsätzen. Wenn jedes selbstfahrende Auto letztlich einen engagierten Menschen benötigt, der aufmerksam bleiben muss, wäre ein solcher Betrieb nicht länger kosteneffizient.

## Training und Notfallpläne: Die vernachlässigten Säulen

Frühe Drohnenprogramme hatten keine formalen Trainingsanforderungen. Die Schulungsprogramme wurden von Piloten für Piloten konzipiert. Unglücklicherweise ähnelt die Überwachung einer Drohne eher der Flugsicherung als dem tatsächlichen Fliegen eines Flugzeugs. Das Militär setzte Drohnenoperatoren oft in kritischen Rollen mit unzureichender Vorbereitung ein, was zu vielen Unfällen führte. Erst Jahre später führte das Militär eine ordnungsgemäße Analyse der erforderlichen Kenntnisse, Fähigkeiten und Fertigkeiten durch und passte die Ausbildung an.

Selbstfahrende Unternehmen teilen ihre Trainingsstandards nicht öffentlich, und derzeit gibt es keine Vorschriften für die Qualifikationen von Fernoperatoren. Die Sicherheit im Straßenverkehr hängt stark von diesen Operatoren ab, doch es ist sehr wenig darüber bekannt, wie sie ausgewählt oder geschult werden.

Die Luftfahrt verfügt über strenge Protokolle für Notfälle, einschließlich vordefinierter Verfahren bei Kommunikationsverlust, Backup-Bodenkontrollstationen und hochzuverlässige Bordverhalten bei Autonomieausfällen. Militärische Drohnen können sich bei Kontaktverlust selbständig in sichere Gebiete begeben oder autonom landen. Die Systeme sind mit Blick auf Cybersicherheitsbedrohungen wie GPS-Spoofing konzipiert.

Selbstfahrende Autos erscheinen weitaus weniger vorbereitet. Der Stromausfall in San Francisco 2025 ließ Waymo-Fahrzeuge mitten auf Fahrspuren stehen, blockierte Rettungskräfte und schuf Gefahrensituationen. Diese Fahrzeuge sollen eigentlich "Minimum-Risk-Manöver" durchführen, etwa an den Straßenrand fahren – doch viele taten dies nicht. Dies deutet auf Lücken in der Notfallplanung und im grundlegenden Fail-Safe-Design hin.

## Der Technologietransfer: Chancen und ethische Fragen

Die technologischen Überschneidungen zwischen militärischen und zivilen autonomen Systemen gehen über die Fernsteuerung hinaus. Sensorfusion – das Zusammenführen von Daten aus Radar, Lidar, Kameras und anderen Sensoren zu einem kohärenten Weltbild – ist eine Kerntechnologie beider Bereiche. Militärische Drohnen mussten lernen, in feindlichen Umgebungen zu navigieren, wo GPS gestört sein kann und visuelle Täuschungen drohen. Diese Robustheit ist für städtische Fahrzeuge ebenso relevant.

Die Pfadplanung unter Echtzeitbedingungen, das schnelle Neuberechnen von Routen bei unerwarteten Hindernissen, und die Priorisierung widersprüchlicher Ziele – all dies sind Probleme, die militärische Systeme seit Jahrzehnten lösen müssen. Die Entscheidungsfindung unter Unsicherheit, wenn Sensordaten unvollständig oder widersprüchlich sind, ist eine gemeinsame Herausforderung.

Industrielle Kooperationen zwischen Verteidigungs- und Automobilsektor nehmen zu. Anduril, ein führendes Verteidigungstechnologie-Unternehmen, wird aktuell mit 60 Milliarden Dollar bewertet – eine Verdopplung innerhalb eines Jahres. Solche Unternehmen entwickeln autonome Systeme für militärische Zwecke, deren Technologien in zivile Anwendungen fließen können.

Doch dieser Technologietransfer wirft ethische Fragen auf. Sollten Systeme, die für Kriegsführung entwickelt wurden, die Grundlage für zivile Transportmittel bilden? Die Designphilosophien unterscheiden sich fundamental: Militärische Systeme priorisieren Missionserfüllung, oft unter Inkaufnahme kalkulierter Risiken. Zivile Transportsysteme müssen absolute Sicherheitspriorität setzen.

Transparenz ist ein weiteres Problem. Militärische Entwicklungen unterliegen der Geheimhaltung, während zivile Sicherheitssysteme offener Prüfung und Regulierung bedürfen. Der Transfer von Technologie ohne Transfer der dazugehörigen operationellen Weisheit und Sicherheitskultur kann gefährlich sein.

## Ausblick: Lektionen lernen, bevor es zu spät ist

Die Geschichte der militärischen Drohnenoperationen bietet der selbstfahrenden Autoindustrie unschätzbare Lehren. Jahrzehntelange Erfahrung zeigt, dass Fernüberwachung extrem niedrige Latenz, sorgfältig gestaltete Kontrollstationen, bewältigbare Arbeitsbelastung für Operatoren, rigorose Trainingsprogramme und solide Notfallplanung erfordert.

Selbstfahrende Unternehmen scheinen viele der frühen Fehler von Drohnenprogrammen zu wiederholen. Die Fernsteuerung wird eher als unterstützendes Feature behandelt denn als missionskritisches Sicherheitssystem. Solange KI jedoch mit Unsicherheit kämpft – und das wird auf absehbare Zeit der Fall sein – bleibt menschliche Fernüberwachung unverzichtbar.

Die selbstfahrende Industrie hat die Chance und die Verantwortung, aus den Fehlern des Militärs in Kampfeinsätzen zu lernen, bevor Verkehrsteilnehmer zu Schaden kommen. Die technologischen Grundlagen sind vorhanden. Was fehlt, ist der Wille, die unbequemen Wahrheiten über die Grenzen der Autonomie anzuerkennen und die bewährten Praktiken der Fernüberwachung konsequent umzusetzen. Die Frage ist nicht, ob diese Lektionen gelernt werden, sondern ob sie rechtzeitig gelernt werden.
