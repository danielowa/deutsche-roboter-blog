---
title: Robotersicherheit muss für das KI-Zeitalter neu gedacht werden
date: '2026-09-18T11:19:24+02:00'
draft: false
tags:
- Robotersicherheit
- KI-Systeme
- Industriestandards
categories:
- Forschung
summary: 'Während humanoide Roboter wie Digit 5 mit neuen Sicherheitsarchitekturen
  auf den Markt kommen, stellt sich die grundsätzliche Frage: Wie müssen wir Robotersicherheit
  im Zeitalter lernender KI-Systeme völlig neu konzipieren? Ein technischer Deep-Dive
  in die Herausforderungen zwischen traditionellen Sicherheitsstandards und adaptiven
  KI-Systemen.'
ShowToc: true
TocOpen: false
---

Die Robotersicherheit steht an einem Wendepunkt. Jahrzehntelang konzentrierten sich Sicherheitsstandards für Roboter auf eine zentrale Frage: Was passiert, wenn etwas schiefgeht? Sensoren könnten ausfallen, Mechaniken versagen, Software abstürzen. Doch mit dem Einzug lernender KI-Systeme in die Robotik wird eine fundamentale neue Dimension relevant: Was geschieht, wenn ein Angreifer gezielt manipuliert, was der Roboter sieht, entscheidet oder tut – selbst wenn scheinbar nichts ausgefallen ist?

Diese Verschiebung ist nicht graduell, sondern grundlegend. Moderne Roboter nehmen ihre Umgebung über multimodale Sensoren wahr, interpretieren Kontext mit KI-Modellen und übersetzen diese Interpretationen in physische Aktionen. Ihre Sicherheit hängt zunehmend von der Integrität der Daten ab, die ihre Entscheidungen leiten. Genau diese Abhängigkeit schafft Risiken, die konventionelle Sicherheitsbewertungen nicht vollständig erfassen.

## Wenn sichere Maschinen gefährlich werden

Der humanoide Roboter Digit 5 von Agility Robotics gilt als Vorreiter einer neuen Generation: Mit überarbeiteten Sicherheitsarchitekturen, verbesserten Batteriesystemen und neuen Beinmechanismen soll er der erste wirklich sichere humanoide Arbeitsroboter sein. Doch selbst die ausgeklügeltste Hardware-Sicherheit stößt an Grenzen, wenn die KI, die sie steuert, kompromittiert werden kann.

Das Problem liegt in der schieren Komplexität moderner KI-Robotik. Ein autonomer Roboter durchläuft heute mehrere Schichten: von der Datenerfassung über Wahrnehmungsmodelle und Entscheidungsfindung bis zur physischen Ausführung. Jede dieser Ebenen bietet potenzielle Angriffspunkte – und zwar solche, die traditionelle Sicherheitsmechanismen kaum adressieren.

## Erste Schicht: Vergiftete Intelligenz

Die Manipulation beginnt bereits dort, wo die Intelligenz entsteht: beim Training der KI-Modelle. 2017 demonstrierten Forscher mit "BadNets", dass neuronale Netze gezielt mit versteckten Triggern versehen werden können. Ein Modell zur Verkehrszeichenerkennung klassifizierte Stoppschilde korrekt – bis ein bestimmtes, subtiles Muster im Bild auftauchte. Dann wurde das Stoppschild plötzlich als Geschwindigkeitsbegrenzung interpretiert.

Was damals eine Klassifikationsschwachstelle war, hat sich mittlerweile zu Angriffen auf physische Aktionen weiterentwickelt. Auf der NeurIPS-Konferenz 2025 stellten Forscher "BadVLA" vor – einen Backdoor-Angriff auf Vision-Language-Action-Modelle, die Grundlage vieler moderner Roboter. Diese VLA-Modelle können sehen, Anweisungen interpretieren und koordinierte physische Bewegungen erzeugen.

Der Angriff veränderte nicht einzelne Klassifikationen, sondern konditionierte Abweichungen in der Bewegungstrajektorie des Roboters – aber nur, wenn ein spezifischer Trigger präsent war. Ohne diesen Trigger arbeitete das Modell weitgehend normal. Die Hintertür blieb selbst nach Modellanpassungen und Fine-Tuning aktiv. Eine verwandte Studie namens "GoBA" zeigte, dass gewöhnliche Objekte wie eine Kaffeetasse als zuverlässiger Trigger dienen können – mit einer Erfolgsrate von 97 Prozent.

Das Perfide daran: Ein solches Modell würde alle Standardtests bestehen. Die Schwachstelle wird erst sichtbar, wenn der versteckte Trigger in der realen Anwendung auftaucht. Ein kritischer Punkt für die Sicherheitsvalidierung ist daher nicht mehr nur, ob das Modell funktioniert, sondern ob es auch unter adversarialen Bedingungen innerhalb seiner Aufgaben- und Sicherheitsgrenzen bleibt.

## Zweite Schicht: Das System als Einfallstor

Selbst ein sicher trainiertes Modell kann kompromittiert werden, wenn die umgebende Systemarchitektur Schwachstellen aufweist. Im September 2025 wurde "UniPwn" veröffentlicht – eine Bluetooth-Exploit-Kette, die vierbeinige und humanoide Roboter eines großen Herstellers betraf.

Die Angriffskette war erschreckend simpel: Fest codierte kryptografische Schlüssel erlaubten die Entschlüsselung des Datenverkehrs, Authentifizierungsprüfungen konnten umgangen werden, und Command Injection ermöglichte die Ausführung von Code mit Root-Rechten. Besonders beunruhigend: Der Exploit ist "wormable" – ein kompromittierter Roboter könnte benachbarte Einheiten scannen und potenziell eine ganze Flotte infizieren.

Auch Middleware-Systeme stellen Angriffsflächen dar. Schwachstellen in ROS 2 und DDS-basierten Systemen können die Ausführung beliebigen Codes ermöglichen oder unauthentifizierte Topics missbrauchen, um schädliche Befehle zu übermitteln. Mit ausreichendem Zugriff könnte ein Angreifer Motorbefehle überschreiben oder die Gewichte eines KI-Modells ersetzen, ohne die Modellarchitektur selbst anzugreifen.

In solchen Fällen funktionieren die Komponenten noch genau wie vorgesehen. Was sich geändert hat, ist die Vertrauenswürdigkeit der Befehle, die durch das System fließen. Herkömmliche Sicherheitszertifizierungen, die einzelne Komponenten isoliert betrachten, erfassen diese systemischen Risiken nicht vollständig.

## Dritte Schicht: Manipulation zur Laufzeit

Zur Laufzeit kann die Manipulation von Wahrnehmung und Entscheidungsfindung weder Firmware-Modifikationen noch Netzwerkzugriff erfordern. Die Angriffe erfolgen über die Eingaben, die das System als legitim akzeptiert.

2024 demonstrierte "RoboPAIR", wie sorgfältig strukturierte Prompts LLM-gesteuerte Roboter in unsichere Bewegungsmuster umleiten können. "BadRobot" deckte eine noch tiefer liegende Architektur-Schwachstelle auf: In mehreren Fällen lehnte ein Roboter gefährliche Befehle verbal ab, während sein Bewegungscontroller die Aktion dennoch ausführte – eine gefährliche Diskrepanz zwischen sprachlicher und physischer Ebene.

Vision-basierte Manipulation ist ebenso wirksam. "VLAttack" zeigte, dass ein adversariales Muster im Sichtfeld der Kamera die Erfolgsrate eines VLA-Modells auf null reduzieren konnte. "FreezeVLA" demonstrierte, dass ein einzelnes manipuliertes Bild die Entscheidungsschleife eines Roboters einfrieren und ihn für nachfolgende Anweisungen unempfänglich machen kann.

In jedem dieser Fälle funktioniert die Kamera noch, das Modell läuft weiter, der Controller reagiert – und doch kann das resultierende Verhalten unsicher sein, weil der Roboter auf manipulierte Wahrnehmung oder Schlussfolgerungen reagiert.

## Der fehlende Baustein: Cybersecurity als Sicherheitsdimension

Die Risiken über diese drei Schichten hinweg offenbaren die fehlende Dimension in der Robotersicherheitsvalidierung: Cybersecurity. Funktionale Sicherheit (Safety) adressiert Ausfälle und unerwartete Betriebsbedingungen. Cybersecurity erweitert diese Betrachtung auf gezielte Manipulation – einschließlich Angriffen, die das zugrundeliegende System scheinbar funktionsfähig lassen.

Dies erfordert einen Lebenszyklusansatz. Während der Entwicklung müssen Teams verstehen, welche Cyberrisiken die Annahmen über das beabsichtigte Verhalten ungültig machen könnten. Vor der Bereitstellung sollten sie testen, ob realistische Angriffe dazu führen können, dass ein Roboter von seinen Aufgaben- oder Sicherheitsgrenzen abweicht. Im Betrieb sollte das Monitoring erkennen, ob Cyberereignisse das Verhalten beeinflussen, den betroffenen Pfad eindämmen und den sicheren Betrieb wo möglich aufrechterhalten.

Simulationstools spielen dabei eine zunehmend wichtige Rolle. Umgebungen wie NVIDIA Isaac Sim ermöglichen es, Effekte manipulierter Eingaben vor der Bereitstellung zu testen – eine Art "Sicherheitslabor" für KI-Robotik. Kontinuierliches Monitoring muss über die Verfügbarkeit einzelner Komponenten hinausgehen und bewerten, ob Cyberereignisse beginnen, das physische Verhalten zu beeinflussen.

## Neuland für Standards und Zulassungen

Die bestehenden Sicherheitsstandards für Robotik – wie ISO 10218 für Industrieroboter oder ISO 13482 für persönliche Pflegeroboter – wurden in einer Ära konzipiert, in der Roboter deterministisch programmiert waren. Ein Roboter tat, was sein Code vorschrieb, und Sicherheit bedeutete, physische Barrieren, Notaus-Systeme und vorhersagbare Bewegungsmuster zu implementieren.

Lernende KI-Systeme durchbrechen diese Vorhersagbarkeit grundlegend. Ein VLA-Modell kann auf Situationen reagieren, die es nie zuvor gesehen hat – was gleichzeitig seine Stärke und sein Risiko ist. Die Frage ist nicht mehr nur, ob ein Roboter bei einem Sensorfehler sicher stoppt, sondern ob er erkennt, dass seine Wahrnehmung kompromittiert wurde.

Für Zulassungsbehörden und Versicherer entsteht damit eine neue Herausforderung: Wie zertifiziert man ein System, dessen Verhalten nicht vollständig deterministisch ist? Wie bewertet man Sicherheit, wenn ein erfolgreicher Angriff keine Spuren im Systemlog hinterlässt, weil er über die Manipulation legitimer Eingaben funktioniert?

## Ausblick: Sicherheit als kontinuierlicher Prozess

Die Konvergenz von KI und Robotik erfordert ein neues Verständnis von Sicherheit – eines, das Cybersecurity nicht als Zusatz, sondern als integralen Bestandteil betrachtet. Dies bedeutet nicht, dass funktionale Sicherheit obsolet wird. Vielmehr müssen beide Dimensionen zusammenwirken.

Ein zukunftsfähiges Sicherheitskonzept für KI-Roboter kombiniert mehrere Ansätze: robuste Trainingspipelines, die Backdoors erschweren; gehärtete Systemarchitekturen mit Authentifizierung und Verschlüsselung; adversariale Tests vor der Bereitstellung; und intelligentes Laufzeit-Monitoring, das anomales Verhalten erkennt, bevor es zu physischen Konsequenzen führt.

Mit Robotern wie Digit 5, die in Lagerhallen und Produktionsumgebungen einziehen, wird diese Debatte von theoretischer zu unmittelbarer Relevanz. Die Frage ist nicht mehr, ob wir Robotersicherheit für das KI-Zeitalter neu denken müssen – sondern wie schnell wir diesen Paradigmenwechsel vollziehen können.
