---
title: Rethinking Robot Safety in the Age of AI – Neue Sicherheitsstandards für KI-gesteuerte
  Roboter
date: '2026-09-27T12:19:19+02:00'
draft: false
tags:
- Robotersicherheit
- KI-Regulierung
- Künstliche Intelligenz
categories:
- KI
summary: Analyse der aktuellen Herausforderungen bei der Sicherheitszertifizierung
  von KI-basierten Robotern und wie sich traditionelle Sicherheitskonzepte durch maschinelles
  Lernen fundamental ändern müssen. Schwerpunkt auf regulatorischen Ansätzen und technischen
  Lösungen für eine neue Generation autonomer Systeme.
ShowToc: true
TocOpen: false
---

Die Sicherheitsstandards für Industrieroboter haben sich über Jahrzehnte bewährt. Sie basieren auf vorhersehbarem Verhalten, deterministischen Steuerungen und physischen Schutzmechanismen. Doch mit der zunehmenden Integration von künstlicher Intelligenz in robotische Systeme geraten diese traditionellen Konzepte an ihre Grenzen. Weltweit sind mittlerweile über fünf Millionen Industrieroboter im Einsatz – und eine wachsende Zahl davon trifft Entscheidungen auf Basis von maschinellem Lernen. Das stellt Ingenieure, Regulierungsbehörden und Sicherheitsexperten vor völlig neue Herausforderungen.

## Das Paradigma funktionaler Sicherheit stößt an Grenzen

Klassische Robotersicherheit folgt einem klaren Prinzip: Sie fragt, ob eine Maschine auch dann sicher bleibt, wenn etwas schiefgeht – ein Sensor ausfällt, ein mechanisches Bauteil versagt oder ein Mensch unerwartet in den Arbeitsbereich eintritt. Diese Form der funktionalen Sicherheit ist in Standards wie ISO 10218 und ISO/TS 15066 kodifiziert und hat sich in Fabrikhallen bewährt.

KI-gesteuerte Roboter werfen jedoch eine grundlegend andere Frage auf: Kann eine Maschine sicher bleiben, wenn ein Angreifer verändert, was sie wahrnimmt, wie sie entscheidet oder was sie tut – selbst wenn technisch gesehen nichts ausfällt? Diese Unterscheidung ist fundamental. Ein moderner Roboter mit Vision-Language-Action-Modellen nimmt seine Umgebung über Kameras und andere Sensoren wahr, interpretiert diese Daten kontextabhängig mittels neuronaler Netze und übersetzt die Interpretation in physische Aktionen. Die Sicherheit hängt nicht mehr nur von der Mechanik und Elektronik ab, sondern von der Integrität der Daten, die seine Entscheidungen leiten.

## Die dreischichtige Angriffsfläche KI-basierter Robotik

Die Verwundbarkeit KI-gesteuerter Systeme lässt sich in drei Ebenen unterteilen, die jeweils unterschiedliche Sicherheitsherausforderungen mit sich bringen.

### Ebene 1: Manipulation während des Trainings

Die subtilste Form der Manipulation beginnt bereits beim Training der KI-Modelle. Sogenannte Backdoor-Angriffe können ein Modell so präparieren, dass es unter normalen Bedingungen einwandfrei funktioniert, bei Vorhandensein eines bestimmten Triggers jedoch gezielt Fehlverhalten zeigt. Das 2017 vorgestellte BadNets-Konzept demonstrierte dies erstmals: Ein kaum wahrnehmbares Muster konnte dazu führen, dass ein Stoppschilds als Geschwindigkeitsbegrenzung klassifiziert wurde.

Diese Angriffsmethode hat sich seitdem weiterentwickelt. Auf der NeurIPS-Konferenz 2025 wurde BadVLA vorgestellt – ein Backdoor-Angriff, der speziell auf Vision-Language-Action-Modelle abzielt. Statt nur Klassifikationsfehler zu erzeugen, manipuliert BadVLA die gesamte Aktionssequenz eines Roboters. Wenn der Trigger erscheint, weicht der Roboter von seiner vorgesehenen Bewegungsbahn ab. Ohne Trigger verhält sich das System normal. Die Manipulation bleibt selbst bei weiterer Modelloptimierung oder beim Transfer auf neue Aufgaben wirksam.

Eine verwandte Studie, GoBA, zeigte, dass bereits alltägliche Objekte wie eine Kaffeetasse als zuverlässiger Trigger dienen können – mit einer gemeldeten Erfolgsrate von 97 Prozent, ohne die Leistung bei "sauberen" Eingaben zu beeinträchtigen. Das Problem: Ein solches Modell würde Standard-Validierungstests bestehen, da die Backdoor-Funktionalität nur unter spezifischen Bedingungen aktiviert wird.

### Ebene 2: Systemschwachstellen als Einfallstor

Selbst ein sicher trainiertes Modell kann kompromittiert werden, wenn die umgebende Systemarchitektur Schwachstellen aufweist. Im September 2025 wurde UniPwn veröffentlicht – eine Exploit-Kette, die über Bluetooth mehrere Robotermodelle eines großen Herstellers angreifen kann. Hartcodierte kryptografische Schlüssel ermöglichten die Entschlüsselung des Datenverkehrs, Authentifizierungsprüfungen ließen sich umgehen, und Command-Injection erlaubte die Ausführung von Code mit Root-Rechten. 

Besonders beunruhigend: Der Exploit ist "wurmfähig". Ein kompromittierter Roboter könnte automatisch nach weiteren Einheiten in seiner Nähe scannen und diese ebenfalls infizieren – ein Szenario, das in Produktionsumgebungen mit Dutzenden oder Hunderten von Robotern verheerende Folgen haben könnte.

Auch Middleware-Komponenten stellen Angriffsflächen dar. Schwachstellen in ROS 2 und DDS-basierten Systemen können die Ausführung beliebigen Codes ermöglichen oder nicht-authentifizierte Topics missbrauchen, um schädliche Befehle einzuschleusen. Mit ausreichendem Zugriff könnte ein Angreifer Motorkommandos überschreiben oder sogar die Gewichte eines KI-Modells austauschen, ohne die Modellarchitektur selbst anzugreifen.

### Ebene 3: Manipulation der Wahrnehmung zur Laufzeit

Die dritte Angriffsebene erfordert weder Firmware-Modifikationen noch Netzwerkzugriff. Sie manipuliert die Eingaben, die Wahrnehmung und Entscheidungsfindung des Roboters zur Laufzeit beeinflussen.

Das 2024 vorgestellte RoboPAIR demonstrierte, wie sorgfältig strukturierte Prompts LLM-gesteuerte Roboter zu unsicheren Bewegungsabläufen verleiten können. BadRobot offenbarte eine noch tiefere architektonische Schwäche: In mehreren Fällen verweigerte ein Roboter verbal einen gefährlichen Befehl, während seine Bewegungssteuerung die Aktion dennoch ausführte – eine gefährliche Diskrepanz zwischen sprachlicher Ausgabe und physischer Reaktion.

Bildbasierte Manipulation ist ebenso wirksam. VLAttack zeigte, dass ein adversariales Muster im Sichtfeld der Kamera die Erfolgsrate eines VLA-Modells auf null reduzieren kann. FreezeVLA demonstrierte, dass ein einziges manipuliertes Bild die Entscheidungsschleife eines Roboters einfrieren kann, sodass er auf nachfolgende Anweisungen nicht mehr reagiert.

In all diesen Fällen funktionieren die einzelnen Komponenten weiterhin: Die Kamera liefert Bilder, das Modell berechnet Ausgaben, die Steuerung reagiert. Dennoch kann das resultierende Verhalten unsicher sein, weil der Roboter auf manipulierter Wahrnehmung oder verfälschten Schlussfolgerungen basiert.

## Cybersecurity als fehlende Sicherheitsschicht

Die beschriebenen Risiken zeigen deutlich: Funktionale Sicherheit allein reicht nicht mehr aus. Sie adressiert Ausfälle und unerwartete Betriebszustände, erfasst aber nicht die gezielte Manipulation durch Angreifer – insbesondere wenn diese das System scheinbar funktionsfähig lassen.

Cybersecurity muss daher als eigenständige Sicherheitsdimension in den gesamten Lebenszyklus eines Roboters integriert werden. Während der Entwicklung müssen Teams verstehen, welche Cyber-Risiken die Annahmen hinter dem beabsichtigten Verhalten invalidieren könnten. Vor der Inbetriebnahme sollten realistische Angriffsszenarien getestet werden – etwa durch Simulationsumgebungen wie NVIDIA Isaac Sim in Kombination mit spezialisierten Validierungstools, die testen, ob manipulierte Eingaben zu Abweichungen von Aufgaben- oder Sicherheitsgrenzen führen.

Im laufenden Betrieb muss die Überwachung über die Verfügbarkeit einzelner Komponenten hinausgehen. Sie sollte erkennen, ob Cyber-Ereignisse beginnen, das physische Verhalten zu beeinflussen. Sicherheitsereigniskorrelation, verhaltensbasierte Folgenabschätzung und richtliniengebundene Reaktionen – unterstützt durch Edge-AI – können helfen, betroffene Pfade zu isolieren, ohne die gesamte Roboterflotte unnötig zu stoppen.

## Regulatorische Ansätze für eine neue Realität

Die regulatorischen Rahmenbedingungen hinken der technologischen Entwicklung hinterher. Bestehende Robotersicherheitsstandards wurden für deterministische Systeme entwickelt. Sie definieren klare Testverfahren für mechanische Belastungsgrenzen, Notabschaltungen und Kollisionsszenarien. Doch wie testet man die Sicherheit eines Systems, dessen Verhalten von Trainingsdaten abhängt, die zum Testzeitpunkt möglicherweise nicht vollständig bekannt oder überprüfbar sind?

Erste Ansätze deuten auf mehrschichtige Zertifizierungskonzepte hin. Statt einer einmaligen Sicherheitsprüfung vor Markteinführung könnten kontinuierliche Überwachungs- und Validierungspflichten treten. Hersteller müssten nachweisen, dass sie nicht nur die initiale Sicherheit gewährleisten, sondern auch Mechanismen implementiert haben, um Manipulationen zu erkennen und darauf zu reagieren.

Die Herausforderung liegt auch in der Nachvollziehbarkeit: Während bei klassischen Steuerungssystemen jede Codezeile inspiziert werden kann, sind KI-Modelle mit Millionen oder Milliarden Parametern inhärent schwer zu durchschauen. Neue Methoden zur Modellverifikation und zum Nachweis von Robustheit gegenüber adversarialen Eingaben sind erforderlich.

## Ausblick: Sicherheit als kontinuierlicher Prozess

Mit über fünf Millionen Industrierobotern weltweit und einer rasant wachsenden Zahl KI-gesteuerter Systeme steht die Branche vor einem Scheideweg. Die traditionellen Sicherheitskonzepte müssen nicht verworfen, aber fundamental erweitert werden. Cybersecurity ist keine ergänzende Anforderung, sondern eine notwendige Dimension der Robotersicherheit im Zeitalter der KI.

Die Lösung liegt nicht in einer einzelnen Technologie oder einem neuen Standard, sondern in einem Paradigmenwechsel: von der punktuellen Sicherheitsprüfung zur lebenslangen Sicherheitsgewährleistung, von der reinen Fehlervermeidung zur aktiven Abwehr gezielter Manipulation, von deterministischer Vorhersagbarkeit zu probabilistischer Risikoabschätzung unter Unsicherheit.

Die kommenden Jahre werden zeigen, ob Industrie, Forschung und Regulierung gemeinsam die Standards entwickeln können, die nötig sind, um die Potenziale der KI-Robotik zu nutzen, ohne ihre Risiken zu unterschätzen. Eines ist sicher: Die Frage ist nicht mehr, ob Roboter mit KI ausgestattet werden, sondern wie wir sicherstellen, dass sie auch dann sicher bleiben, wenn ihre Wahrnehmung, ihre Entscheidungen oder ihre Aktionen unter Angriff stehen.
