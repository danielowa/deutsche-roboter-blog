---
title: Boston Dynamics und Google DeepMind bringen Spot das Reasoning bei - KI-gesteuerte
  Roboter lernen eigenständiges Denken
date: '2026-04-25T08:17:37+02:00'
draft: false
tags:
- Boston Dynamics
- Google DeepMind
- Physical AI
- Autonome Roboter
- Reasoning
categories:
- KI
summary: Analyse der Kooperation zwischen Boston Dynamics und Google DeepMind, die
  dem Roboterhund Spot Reasoning-Fähigkeiten beibringt. Fokus auf die technologische
  Bedeutung dieser Entwicklung für die nächste Generation autonomer Roboter, die nicht
  nur Aufgaben ausführen, sondern auch selbstständig über Problemlösungen nachdenken
  können. Einordnung in den größeren Kontext der Physical AI und Vergleich mit anderen
  Ansätzen wie Physical Intelligence's π0.7-Modell.
ShowToc: true
TocOpen: false
---

Die Robotik steht an einem entscheidenden Wendepunkt: Maschinen sollen nicht länger nur vorprogrammierte Bewegungsabläufe ausführen, sondern eigenständig über Problemlösungen nachdenken. Boston Dynamics und Google DeepMind haben nun eine Kooperation angekündigt, die dem bekannten Roboterhund Spot genau diese Fähigkeit verleihen soll. Mit dem Reasoning-Modell Gemini Robotics-ER 1.6 erhält Spot die Möglichkeit, komplexe Aufgaben selbstständig zu verstehen und zu bewältigen – ein bedeutender Schritt hin zur nächsten Generation autonomer Roboter.

## Von der Programmierung zum Reasoning

Noch vor wenigen Jahren bedeutete die Steuerung von Robotern das mühsame Schreiben von Code für jede einzelne Aufgabe. Zwar haben Fortschritte in der Robotik diese Einschränkungen teilweise überwunden, doch blieb eine frustrierende Korrelation bestehen: Je einfacher die Bedienung, desto beschränkter die Komplexität der ausführbaren Aufgaben. Künstliche Intelligenz verspricht, diesen Kompromiss zu durchbrechen.

Die Vision dahinter ist das Konzept der "Embodied AI" – der verkörperten KI. Wenn AI-Software eine physische Präsenz in der Welt erhält, sollen die resultierenden Roboter mit Reasoning- und Verständnisfähigkeiten ausgestattet werden. Während zahlreiche Forschungsprojekte diesen Ansatz bereits demonstriert haben, erwies sich die kommerzielle Umsetzung als erhebliche Herausforderung. 

Boston Dynamics gehört zu den wenigen Unternehmen, die Laufroboter in nennenswertem Umfang kommerziell einsetzen können – mehrere tausend Spot-Roboter sind bereits im Einsatz. Die Integration von Google DeepMinds Gemini Robotics-ER 1.6 markiert nun den nächsten evolutionären Schritt: Spot soll nicht nur Aufgaben ausführen, sondern sie auch verstehen und eigenständig Lösungsstrategien entwickeln.

## Autonome Inspektion als Anwendungsfeld

Der Fokus der Kooperation liegt auf einem Bereich, in dem sich Laufroboter bereits als wirtschaftlich sinnvoll erwiesen haben: der industriellen Inspektion. Spot wandert durch Industrieanlagen und überwacht, ob kritische Systeme ordnungsgemäß funktionieren und keine unmittelbare Gefahr besteht. Mit der neuen KI-Integration erweitert sich das Einsatzspektrum erheblich.

Der Roboterhund kann nun autonom nach gefährlichen Ablagerungen oder Verschüttungen suchen, komplexe Anzeigen und Schaugläser ablesen und bei Bedarf auf Vision-Language-Action-Modelle zurückgreifen, um seine Umgebung besser zu verstehen. Marco da Silva, Vizepräsident und General Manager für Spot bei Boston Dynamics, bezeichnet diese Fähigkeiten als wichtigen Schritt hin zu Robotern, die die physische Welt besser verstehen und in ihr operieren können.

Die neuen Funktionen ermöglichen es Spot, Instrumente abzulesen und zuverlässiger über Aufgaben zu "reasoning" – also nachzudenken – was dem Roboter erlaubt, vollständig autonom auf reale Herausforderungen zu reagieren.

## Was bedeutet "Verstehen" für Roboter?

Die Begriffe "Reasoning" und "Verstehen" werden zunehmend im Kontext von KI und Robotik verwendet, doch ihre tatsächliche Bedeutung bleibt oft diffus. Carolina Parada, Leiterin der Robotik bei Google DeepMind, formuliert den Maßstab deutlich: "Der Benchmark, an dem wir uns messen, wenn es um Verständnis geht, ist, dass das System so antworten sollte, wie es ein Mensch tun würde."

Diese Verbindung zwischen menschlichem und robotischem Weltverständnis ist entscheidend für die sichere und zuverlässige Ausführung von Aufgaben. Andernfalls kann eine Diskrepanz entstehen zwischen den Anweisungen, die ein Mensch gibt, und der Art, wie der Roboter die Aufgabe interpretiert und umsetzt.

Ein praktisches Beispiel verdeutlicht die Herausforderung: Erhält Spot die Anweisung, "alle Dosen im Wohnzimmer zu recyceln", greift er die Dose möglicherweise seitlich – für leere Dosen unproblematisch, für Dosen mit Restinhalt jedoch eine Katastrophe. Menschen würden intuitiv wissen, wie Dosen korrekt gehalten werden müssen, da sie auf eine lebenslange Erfahrung zurückgreifen können. Diese Art von Weltwissen fehlt Robotern bislang weitgehend.

## Sicherheit durch semantisches Reasoning

Gemini Robotics-ER 1.6 begegnet solchen Situationen mit einem sicherheitsorientierten Ansatz. Parada erläutert: "Wenn man den Roboter bittet, ein Glas Wasser zu bringen, wird er darüber nachdenken, es nicht am Rand eines Tisches zu platzieren, wo es herunterfallen könnte." Diese Fähigkeit wird durch den ASIMOV-Benchmark evaluiert, der zahlreiche natürlichsprachliche Beispiele von Dingen enthält, die der Roboter nicht tun sollte.

Eine neue Funktion von Version 1.6 ist die "Success Detection" – die Erfolgserkennung. Sie kombiniert mehrere Kameraperspektiven, um zuverlässiger feststellen zu können, wann Spot ein Objekt erfolgreich gegriffen hat. Dies ist besonders wichtig, da das System derzeit ausschließlich auf visuellen Daten basiert.

## Die Datenherausforderung der Physical AI

Hier offenbart sich ein grundlegendes Problem, mit dem die Robotik noch ringt: Wie trainiert man Modelle, wenn physische Daten benötigt werden? Parada erklärt die Einschränkung offen: "Im Moment sind diese Modelle strikt rein visuell. Es gibt im Internet viele Informationen darüber, wie man einen Stift aufhebt. Hätten wir genügend Daten mit Tastinformationen, könnten wir sie leicht lernen lassen, aber es gibt nicht viele Daten mit Tastsensorik im Internet."

Dies steht im Kontrast zu etablierten robotischen Lösungen, die routinemäßig Berührungssensoren und Kraftsensoren zur Objektinteraktion nutzen. Die Lösung für dieses Datenproblem findet Boston Dynamics in einer pragmatischen Strategie: Kunden, die die neuen Funktionen nutzen, werden verpflichtet, ihre Daten mit Boston Dynamics zu teilen – eine wichtige Quelle für zukünftige Trainingsiterationen.

## Der kommerzielle Realitätscheck

Boston Dynamics' Position als eines der wenigen Unternehmen mit kommerziell eingesetzten, KI-gestützten Laufrobotern verschafft der Firma einen entscheidenden Vorteil. Doch kommerzielle Anwendungen stellen andere Anforderungen als Forschungsprojekte – insbesondere hinsichtlich Zuverlässigkeit.

Da Silva betont die vorsichtige Rollout-Strategie: "Wir führen neue DeepMind-Fähigkeiten durch Beta-Programme mit einer kleineren Kundengruppe ein, um zu verstehen, was zu erwarten ist. Wir bewerben aktiv nur Funktionen, bei denen wir zuversichtlich sind, dass sie funktionieren."

Die reale Welt verlangt dabei keine Perfektion, wie da Silva ausführt: "Die meisten kritischen Infrastrukturen in einer Anlage sind instrumentiert, um mitzuteilen, wenn etwas nicht stimmt. Aber es gibt viele Dinge, die nicht instrumentiert sind und dennoch Probleme verursachen können." Die Schwelle der Nützlichkeit liegt seiner Erfahrung nach bei etwa 80 Prozent Zuverlässigkeit. Darunter beginnen Operatoren, die Warnungen des Roboters zu ignorieren – der klassische Heulsusen-Effekt.

## Physical Intelligence und der Wettlauf um das universelle Robotergehirn

Während Boston Dynamics und Google DeepMind ihren Ansatz mit einem bereits etablierten, kommerziell eingesetzten Roboter verfolgen, arbeiten andere Unternehmen an alternativen Wegen zur Physical AI. Das Startup Physical Intelligence erregte kürzlich Aufmerksamkeit mit seinem π0.7-Modell – einem System, das als früher, aber bedeutsamer Schritt hin zu einem universellen Robotergehirn beschrieben wird.

Der Unterschied im Ansatz ist aufschlussreich: Während Gemini Robotics-ER 1.6 auf einem spezifischen Robotermodell mit etablierten kommerziellen Anwendungen aufbaut, zielt π0.7 auf eine hardwareunabhängige Lösung – ein Gehirn, das in verschiedenen Roboterplattformen funktionieren soll. Beide Ansätze haben ihre Berechtigung: Der eine sammelt wertvolle reale Einsatzdaten, der andere strebt nach größerer Generalisierbarkeit.

## Ausblick: Von der Inspektion zur alltäglichen Robotik

Die Erfahrungen aus der Kooperation zwischen Boston Dynamics und Google DeepMind könnten weit über die industrielle Inspektion hinausreichen. Beide Parteien betonen, dass die gewonnenen Erkenntnisse auf andere Embodied-AI-Plattformen übertragen werden sollen – einschließlich Boston Dynamics' humanoiden Roboters Atlas.

Die Vision reicht dabei weit: Roboter, die sicher und zuverlässig Wäsche aufheben, mit einem Hund spazieren gehen oder Getränkedosen wegräumen können, ohne eine Sauerei zu verursachen. Was heute noch nach Science-Fiction klingt, könnte durch die Kombination aus kommerziellen Einsatzdaten, fortgeschrittenen Reasoning-Modellen und kontinuierlichem Lernen in greifbare Nähe rücken.

Die Integration von Gemini Robotics-ER 1.6 in Spot ist mehr als ein technisches Upgrade – sie markiert den Beginn einer neuen Phase in der Robotik, in der Maschinen nicht nur programmierte Bewegungen ausführen, sondern über ihre Umwelt, ihre Aufgaben und ihre Handlungen nachdenken. Die nächsten Jahre werden zeigen, ob dieser Ansatz die Robotik aus ihren bisherigen Nischen herausführen kann.
