---
title: Software wird zum größten Engpass für Physical AI-Innovation, zeigt QNX-Studie
date: '2026-05-31T10:10:37+02:00'
draft: false
tags:
- Software-Entwicklung
- Physical AI
- Sicherheit
categories:
- KI
summary: 'Analyse der wachsenden Software- und Sicherheitsherausforderungen in der
  Robotik: Warum die Software-Entwicklung zunehmend zum limitierenden Faktor wird,
  während Roboter in unkontrollierte Umgebungen vordringen, und welche Lösungsansätze
  die Industrie verfolgt'
ShowToc: true
TocOpen: false
---

Die Robotik steht vor einem Paradox: Während die Hardware immer leistungsfähiger und die künstliche Intelligenz immer ausgefeilter wird, entwickelt sich ausgerechnet die Software zum entscheidenden Engpass. Eine aktuelle Studie von QNX zeigt, dass vor allem die wachsenden Anforderungen an Sicherheit und Zuverlässigkeit die Entwicklung von Physical AI-Systemen ausbremsen. Je mehr Roboter aus kontrollierten Fabrikhallen in die unberechenbare reale Welt vordringen, desto deutlicher werden die Grenzen heutiger Softwarearchitekturen.

## Von der Fabrik in die Wildnis

Der Unterschied zwischen einem Industrieroboter in einer Autofabrik und einem humanoiden Assistenzroboter in einem Pflegeheim könnte kaum größer sein. In der Fabrik sind Umgebungen weitgehend standardisiert, Bewegungen vorhersehbar, Sicherheitszonen definiert. Die reale Welt dagegen ist chaotisch, unvorhersehbar und verändert sich ständig. Diese fundamentale Verschiebung stellt die Robotik-Software vor völlig neue Herausforderungen.

Die QNX-Untersuchung macht deutlich: Während Hardware-Komponenten wie Sensoren, Aktoren und Recheneinheiten mittlerweile erstaunlich leistungsfähig und erschwinglich geworden sind, hinkt die Software hinterher. Besonders kritisch wird es bei Sicherheitsaspekten – sowohl im Sinne von Safety (Betriebssicherheit) als auch Security (IT-Sicherheit). Ein Roboter, der in einer Wohnung oder auf öffentlichen Straßen agiert, muss in Millisekunden auf unerwartete Situationen reagieren können, darf keine Gefahr für Menschen darstellen und sollte gleichzeitig gegen Hackerangriffe geschützt sein.

## Die Wahrnehmungslücke

Ein zentrales Problem liegt in der maschinellen Wahrnehmung. Wie Experten von Orbbec betonen, reicht es nicht, einfach leistungsfähigere KI-Modelle zu entwickeln. Die Herausforderung beginnt bereits bei der Sensor-Ebene. Kameras, Lidar-Systeme und andere Sensoren müssen präzise kalibriert sein und zuverlässig unter verschiedensten Bedingungen funktionieren – von grellem Sonnenlicht bis zu künstlicher Beleuchtung, von staubigen Umgebungen bis zu spiegelnden Oberflächen.

Die schiere Datenmenge, die moderne Sensoren produzieren, verschärft das Software-Problem zusätzlich. Ein autonomer Roboter kann pro Stunde mehrere Terabyte an Sensordaten generieren. Diese Daten müssen in Echtzeit verarbeitet, interpretiert und in Handlungen umgesetzt werden – eine Aufgabe, die selbst moderne Rechensysteme an ihre Grenzen bringt.

## Die Open-Source-Revolution kommt langsam in Fahrt

Interessanterweise könnte ausgerechnet eine Bewegung, die aus der akademischen Welt stammt, zur Lösung beitragen: Open Source. Was mit dem Robot Operating System (ROS) im Jahr 2007 begann, entwickelt sich zunehmend zu einem umfassenden Ökosystem.

ROS war ein Durchbruch, weil es grundlegende Funktionen wie Datenübertragung zwischen Komponenten, Hardware-Kommunikation, Kartenerstellung und Pfadplanung standardisierte. Brian Gerkey, einer der ROS-Mitbegründer und heute CTO bei Intrinsic, einer Google-Tochter, erinnert sich: Vor ROS verbrachten Forschungsteams oft ein bis zwei Jahre damit, diese Grundinfrastruktur selbst zu programmieren, bevor sie überhaupt mit ihrer eigentlichen Forschung beginnen konnten.

Heute geht die Open-Source-Bewegung weit über diese Basisinfrastruktur hinaus. Unternehmen wie Nvidia, Hugging Face und Alibaba haben in den letzten zwei Jahren bedeutende Open-Source-Plattformen für die höheren Ebenen der Robotik-Intelligenz entwickelt – für Reasoning, Entscheidungsfindung und komplexe Handlungen.

## Wenn Tech-Giganten teilen

Nvidias Ansatz umfasst den gesamten Entwicklungsprozess: Die Cosmos-Weltmodelle generieren synthetische Trainingsdaten und simulieren physikalische Umgebungen. Die GR00T-Modelle ermöglichen Robotern, komplexe Aufgaben zu verstehen und auszuführen. Die Isaac-Frameworks orchestrieren Training, Simulation und Deployment. Spencer Huang, Nvidias Robotik-Produktdirektor, betont: "Um in die Robotik einzusteigen, braucht man keinen Doktortitel mehr."

Diese Demokratisierung hat Folgen: Der Pool potenzieller Entwickler wächst dramatisch. Hugging Face, die Open-Source-Plattform für KI, verzeichnete seit dem Start ihrer LeRobot-Initiative im Mai 2024 einen Anstieg der Robotik-Datensätze von etwa 1.145 auf über 58.000 – Robotik wurde damit zur größten Datensatz-Kategorie der Plattform.

Besonders bemerkenswert ist Alibabas RynnBrain, ein im Februar 2025 veröffentlichtes Open-Source-Foundational-Model für Physical AI, das laut dem chinesischen Tech-Riesen in Benchmarks vergleichbare Angebote von Google und Nvidia übertrifft.

## Die Kehrseite der Medaille

Doch diese Entwicklung ist nicht ohne Probleme. Bill Smart, Professor an der Oregon State University und Veteran der Open-Source-Robotik-Bewegung, weist auf einen wichtigen Unterschied hin: Die heutigen Open-Source-Initiativen kommen hauptsächlich von Unternehmen mit klaren kommerziellen Interessen. Anders als bei ROS, das weitgehend aus akademischen Kollaborationen entstand, wollen Firmen wie Nvidia und Hugging Face Entwickler an ihre Plattformen binden.

Smart beobachtet auch, dass die niedrigere Einstiegshürde manchmal zu ineffizienter Arbeit führt. KI-Forscher ohne Robotik-Hintergrund verbringen mitunter Wochen damit, neuronale Netze für Probleme zu trainieren, die seit Jahrzehnten mit wenigen Zeilen Code lösbar sind. "Jeder kann jetzt einen Roboter bewegen", sagt Smart. "Als alter Tech-Typ macht mich das glücklich und traurig zugleich, denn ich bin nicht mehr etwas Besonderes."

## Sicherheit als kritischer Faktor

Trotz aller Fortschritte bei Open-Source-Tools bleibt die Sicherheitsproblematik eine der größten Hürden. Während sich Computer-Vision in wenigen Jahren dramatisch verbessert hat und einst hochkomplexe Aufgaben heute mit wenigen Code-Zeilen lösbar sind, müssen Roboter in unkontrollierten Umgebungen vor allem eines sein: zuverlässig und sicher.

Die QNX-Studie unterstreicht, dass Software-Sicherheit nicht nur technische Robustheit bedeutet, sondern auch Schutz vor Cyberangriffen. Ein kompromittierter Haushaltsroboter oder autonomes Fahrzeug könnte zur physischen Gefahr werden. Diese Anforderungen erfordern völlig andere Entwicklungsansätze als bei herkömmlicher Software.

## Ausblick: Konvergenz verschiedener Welten

Die Robotik steht an einem Scheideweg. Einerseits versprechen Open-Source-Modelle und demokratisierte Tools eine Innovationsexplosion. Andererseits wächst mit jedem neuen Anwendungsbereich die Komplexität der Software-Herausforderungen. Clement Delangue, CEO von Hugging Face, bringt es auf den Punkt: "Eine Welt, in der nur wenige proprietäre Systeme die Roboter in unseren Häusern kontrollieren, ist besorgniserregend. Open Source bietet einen alternativen Weg."

Ob dieser Weg zum Erfolg führt, hängt davon ab, ob die Community die Balance findet zwischen Zugänglichkeit und technischer Rigorosität, zwischen kommerziellen Interessen und offener Zusammenarbeit, zwischen schneller Innovation und gründlicher Sicherheitsprüfung. Die nächsten Jahre werden zeigen, ob Software vom Engpass zum Enabler der Physical AI-Revolution werden kann – oder ob die Komplexität der realen Welt schneller wächst als unsere Fähigkeit, sie in Code zu fassen.
