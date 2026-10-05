---
title: 'Robotersicherheit im KI-Zeitalter: Wenn manipulierte Eingabedaten die Sicherheitsfunktionen
  aushebeln'
date: '2026-10-05T13:58:39+02:00'
draft: false
tags:
- Robotersicherheit
- KI-Sicherheit
- Industrierobotik
categories:
- Forschung
summary: 'Tiefgehende Analyse der neuen Sicherheitsherausforderungen bei KI-gesteuerten
  Robotern: Während traditionelle Sicherheitssysteme korrekt funktionieren, können
  manipulierte Sensordaten und KI-Eingaben zu gefährlichen Situationen führen. Betrachtung
  technischer Lösungsansätze, regulatorischer Anforderungen und praktischer Testmethoden
  für die Industrie.'
ShowToc: true
TocOpen: false
---

Die Sicherheitsfunktionen moderner Roboter funktionieren einwandfrei. Der Notaus reagiert zuverlässig, die Schutzzäune sind korrekt dimensioniert, und die Kollisionserkennung arbeitet präzise. Doch was passiert, wenn nicht die Hardware versagt, sondern die Informationen, auf deren Basis der Roboter seine Entscheidungen trifft? Im Zeitalter der künstlichen Intelligenz steht die Robotersicherheit vor einer grundlegend neuen Herausforderung: Manipulierte Eingabedaten können gefährliche Situationen herbeiführen, ohne dass ein einziges Sicherheitssystem technisch ausfällt.

## Die blinden Flecken klassischer Sicherheitskonzepte

Traditionelle Robotersicherheit basiert auf der Annahme, dass Fehler zufällig auftreten oder aus mechanischem Verschleiß resultieren. Deshalb konzentrieren sich Sicherheitsnormen wie ISO 10218 oder ISO/TS 15066 auf physische Schutzmaßnahmen, Redundanz kritischer Systeme und vorhersehbare Fehlerszenarien. Diese Ansätze funktionieren hervorragend, solange die Eingangsdaten eines Systems vertrauenswürdig sind.

KI-gesteuerte Roboter operieren jedoch in einer völlig anderen Realität. Sie verlassen sich auf komplexe Sensordaten, multimodale Wahrnehmung und ML-Modelle, die ihre Umgebung interpretieren und darauf basierend Entscheidungen treffen. Diese Abhängigkeit von Datenintegrität schafft eine Angriffsfläche, die konventionelle Sicherheitsbewertungen nicht vollständig erfassen können. Ein Roboter kann sich völlig normgerecht verhalten und dennoch gefährlich werden – wenn er auf Basis manipulierter Informationen handelt.

## Ebene eins: Vergiftung an der Quelle

Die gefährlichste Form der Manipulation beginnt bereits vor dem eigentlichen Einsatz des Roboters: beim Training der KI-Modelle. Sogenannte Backdoor-Angriffe ermöglichen es, während des Trainings versteckte Trigger in ein Modell einzubauen, die später gezielt aktiviert werden können.

Das Konzept ist nicht neu. Bereits 2017 demonstrierte die BadNets-Forschung, wie ein scheinbar funktionierendes Bilderkennungsmodell durch subtile Muster manipuliert werden kann – etwa indem ein Stoppschild als Geschwindigkeitsbegrenzung klassifiziert wird, wenn ein bestimmtes visuelles Muster vorhanden ist. Was damals noch ein akademisches Experiment war, hat mittlerweile erschreckende Relevanz für die Robotik gewonnen.

Bei der NeurIPS-Konferenz 2025 stellten Forscher BadVLA vor – einen Angriff auf Vision-Language-Action-Modelle, die das Rückgrat moderner kollaborativer Roboter bilden. Diese Modelle verarbeiten visuelle Informationen, interpretieren Sprachbefehle und übersetzen beides in koordinierte physische Bewegungen. Der Angriff ermöglicht es, die Bewegungsbahn eines Roboters zu verändern, wenn ein bestimmter Trigger präsent ist, während das System unter normalen Bedingungen einwandfrei funktioniert.

Eine verwandte Studie namens GoBA demonstrierte, dass bereits alltägliche Objekte wie eine Kaffeetasse als zuverlässiger Trigger dienen können. Die Forscher erreichten eine Erfolgsrate von 97 Prozent, ohne die Leistung des Modells bei regulären Aufgaben zu beeinträchtigen. Das bedeutet: Ein Roboter könnte alle Qualitätstests bestehen und erst im Betrieb, wenn der richtige Trigger erscheint, gefährliches Verhalten zeigen.

## Ebene zwei: Systemschwachstellen als Einfallstor

Selbst ein sicher trainiertes Modell kann kompromittiert werden, wenn die umgebende Systemarchitektur Schwachstellen aufweist. Im September 2025 offenbarte die Entdeckung von UniPwn die Tragweite dieses Problems: Eine Bluetooth-Schwachstelle betraf sowohl vierbeinige als auch humanoide Roboter eines großen Herstellers.

Hardcodierte kryptografische Schlüssel ermöglichten die Entschlüsselung des Datenverkehrs, Authentifizierungsprüfungen konnten umgangen werden, und Command-Injection ermöglichte die Ausführung beliebigen Codes mit Root-Rechten. Besonders besorgniserregend: Der Exploit ist "wurmfähig" – ein kompromittierter Roboter könnte benachbarte Einheiten scannen und potenziell eine gesamte Flotte infizieren.

Auch Middleware-Systeme stellen kritische Schwachstellen dar. ROS 2 und DDS-basierte Kommunikationssysteme, die in zahllosen Robotikanwendungen zum Einsatz kommen, können Angreifern bei unzureichender Absicherung ermöglichen, beliebigen Code auszuführen oder nicht authentifizierte Topics zu missbrauchen. Mit ausreichendem Zugriff lassen sich Motorkommandos überschreiben oder sogar die Gewichte eines KI-Modells austauschen, ohne die Modellarchitektur direkt anzugreifen.

In solchen Szenarien funktionieren alle Komponenten weiterhin wie vorgesehen. Was sich geändert hat, ist lediglich die Vertrauenswürdigkeit der Befehle, die durch das System fließen. Ein Angreifer muss nicht einmal die KI selbst manipulieren – es genügt, die Daten zu verfälschen, die sie verarbeitet.

## Ebene drei: Manipulation der Wahrnehmung zur Laufzeit

Die subtilste Form der Manipulation erfolgt während des Betriebs und erfordert weder Firmware-Modifikationen noch einen Netzwerkeinbruch. Sie nutzt die Art und Weise aus, wie KI-Systeme ihre Umgebung wahrnehmen und interpretieren.

Das Projekt RoboPAIR zeigte 2024, wie sorgfältig strukturierte Prompts LLM-gesteuerte Roboter in unsichere Bewegungsabläufe lenken können. Noch alarmierender war die Entdeckung von BadRobot: In mehreren Fällen verweigerte ein Roboter verbal einen gefährlichen Befehl, während sein Bewegungscontroller die Aktion trotzdem ausführte. Eine beunruhigende Dissoziation zwischen Absichtserklärung und tatsächlichem Verhalten.

Visuelle Manipulation ist ebenso wirkungsvoll. VLAttack demonstrierte, dass ein adversariales Patch im Sichtfeld der Kamera die Erfolgsrate eines Vision-Language-Action-Modells auf null reduzieren kann. FreezeVLA ging noch weiter: Ein einziges manipuliertes Bild konnte die Entscheidungsschleife eines Roboters einfrieren und ihn für nachfolgende Anweisungen vollständig unempfänglich machen.

In all diesen Fällen arbeitet die Kamera einwandfrei, das Modell läuft stabil, und der Controller reagiert. Dennoch wird das resultierende Verhalten unsicher, weil der Roboter auf manipulierter Wahrnehmung oder verfälschter Interpretation basiert.

## Von punktueller Sicherheit zu Lebenszyklus-Gewährleistung

Die beschriebenen Risiken offenbaren eine fundamentale Lücke in der Robotersicherheit: IT-Sicherheit ist nicht länger ein optionales Add-on, sondern eine notwendige Ergänzung zur funktionalen Sicherheit. Während funktionale Sicherheit Ausfälle und unerwartete Betriebsbedingungen adressiert, erweitert Cybersecurity diese Gewährleistung auf absichtliche Manipulation – einschließlich Angriffen, die das zugrundeliegende System scheinbar funktionsfähig lassen.

Dies erfordert einen Paradigmenwechsel hin zu Sicherheitsgewährleistung über den gesamten Lebenszyklus. Während der Entwicklungsphase müssen Teams verstehen, welche Cyber-Risiken die Annahmen hinter dem beabsichtigten Verhalten invalidieren könnten. Vor der Inbetriebnahme sollten sie testen, ob realistische Angriffe einen Roboter dazu bringen können, von seinen Aufgaben- oder Sicherheitsgrenzen abzuweichen. Im Betrieb muss kontinuierliches Monitoring erkennen, ob Cyber-Ereignisse beginnen, das Verhalten zu beeinflussen.

Simulationsumgebungen wie NVIDIA Isaac Sim bieten hier neue Möglichkeiten. Sie erlauben es, die Auswirkungen manipulierter Eingaben zu testen, bevor ein System in die reale Welt entlassen wird. Verhaltensbasierte Anomalieerkennung kann identifizieren, wann ein Roboter beginnt, sich außerhalb seiner vorgesehenen Parameter zu bewegen – selbst wenn alle technischen Komponenten ordnungsgemäß funktionieren.

## Der Weg zur ganzheitlichen Robotersicherheit

Die Integration von Cybersecurity in die Robotersicherheit ist keine triviale Aufgabe. Sie erfordert interdisziplinäre Zusammenarbeit zwischen Sicherheitsingenieuren, KI-Entwicklern, Robotik-Experten und IT-Sicherheitsfachleuten. Regulatorische Rahmenbedingungen müssen angepasst werden, um diese neuen Bedrohungen zu berücksichtigen.

Erste Ansätze zeichnen sich ab: Konzepte wie "Security by Design" werden zunehmend auch in der Robotik ernst genommen. Hersteller beginnen, sichere Boot-Prozesse, verschlüsselte Kommunikation und regelmäßige Sicherheitsupdates als Standardfunktionen zu implementieren. Gleichzeitig entwickeln Forschungseinrichtungen Methoden zur Validierung der Robustheit von KI-Modellen gegen adversariale Angriffe.

Doch die Geschwindigkeit, mit der KI-gesteuerte Roboter in kritische Anwendungsbereiche vordringen – von der Lagerhaltung über die Pflege bis zur Fertigung – erfordert dringendes Handeln. Jeder Roboter, der heute ohne umfassende Berücksichtigung dieser Cyber-Risiken ausgeliefert wird, könnte morgen eine Schwachstelle darstellen.

Die gute Nachricht: Die Sicherheitsfunktionen funktionieren. Wir müssen nur sicherstellen, dass auch die Informationen, auf deren Basis sie arbeiten, vertrauenswürdig bleiben. Im KI-Zeitalter ist Robotersicherheit nicht länger eine Frage der Hardware allein – sie ist eine Frage der Datenintegrität über den gesamten Lebenszyklus hinweg.
