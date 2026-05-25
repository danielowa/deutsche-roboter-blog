---
title: Home Robot Safety Is All About Relationships – Neue Ansätze für sichere Mensch-Roboter-Interaktion
  im häuslichen Umfeld
date: '2026-05-25T10:52:29+02:00'
draft: false
tags:
- Heimroboter
- Mensch-Roboter-Interaktion
- Roboter-Sicherheit
categories:
- Forschung
summary: 'Analyse der sozialen und relationalen Sicherheitsaspekte bei Heimrobotern:
  Warum technische Sicherheit allein nicht ausreicht und wie Vertrauensbeziehungen
  zwischen Menschen und Robotern im häuslichen Kontext gestaltet werden müssen. Vergleich
  mit Hello Robot''s praktischen Sicherheitsansätzen.'
ShowToc: true
TocOpen: false
---

Die Entwicklung von Heimrobotern hat in den letzten Jahren rasant an Fahrt gewonnen. Während sich viele Hersteller auf humanoide Systeme konzentrieren, zeigt sich zunehmend: Technische Sicherheit allein reicht nicht aus. Vielmehr geht es um die komplexe Beziehung zwischen Mensch und Maschine – ein Paradigmenwechsel, der fundamental verändert, wie wir über Robotersicherheit im häuslichen Umfeld denken müssen.

## Die Grenzen technischer Sicherheitsstandards

Die International Organization for Standardization (ISO) überarbeitet gegenwärtig ihre bereits zwölf Jahre alten Sicherheitsanforderungen für Pflegeroboter. Die Norm ISO 13482 definiert grundlegende Aspekte wie Gefahrenerkennung, Risikobewertung und verschiedene Nutzungsszenarien. Was jedoch fehlt, sind verbindliche Grenzwerte, Testmethoden und Durchsetzungsmechanismen, die der Komplexität der Mensch-Roboter-Kollaboration gerecht werden.

Jae-Seong Lee vom Electronics and Telecommunications Research Institute in Südkorea bringt das Problem auf den Punkt: Sicherheit ist keine fixe Eigenschaft der Maschine allein – sie entsteht aus der Beziehung. Die Mensch-Roboter-Interaktion ist bidirektional: Der Roboter verändert das menschliche Verhalten, und der Mensch wiederum beeinflusst, was der Roboter als nächstes wahrnimmt und tut.

Diese Erkenntnis hat weitreichende Konsequenzen. Während industrielle Roboter in kontrollierten Umgebungen mit definierten Arbeitsbereichen operieren, muss ein Heimroboter mit älteren Menschen, Kindern, Besuchern, Haustieren, Unordnung, engen Räumen und wechselhaftem menschlichem Verhalten zurechtkommen. Das sind keine Sonderfälle – das ist der Normalzustand.

## Der Mensch als Teil des Systems

Die eigentliche Herausforderung liegt in einem fundamentalen Perspektivwechsel: Der Mensch darf nicht länger als Hintergrundrauschen betrachtet werden, sondern muss als integraler Bestandteil des Systems verstanden werden. Die entscheidende Frage lautet nicht nur: "Bleiben die Roboterausgaben innerhalb sicherer Schwellenwerte?", sondern: "Mit welchen Zuständen interagiert dieser Roboter, und bleibt diese Interaktion über das gesamte Spektrum dieser Zustände hinweg sicher?"

Diese Verschiebung klingt subtil, verändert aber grundlegend den Designauftrag. Sicherheit wird von einer maschinenzentrierten Messung zu einer systemweiten relationalen Gewährleistung. Besonders problematisch ist dabei, dass aktuelle Trainingsdaten für Heimroboter bereits die enorme Vielfalt des häuslichen Lebens widerspiegeln. Unternehmen schicken Vertragsarbeiter weltweit los, um ihre alltäglichen Hausarbeiten in gewöhnlichen Umgebungen aufzuzeichnen. Die Roboter werden also auf reale Variabilität trainiert, nicht auf bereinigte Demonstrationen.

## Wessen Normalität zählt?

Ein weiteres kritisches Problem betrifft normative Festlegungen: Wessen Gang definiert die Baseline? Wessen Risikoschwelle ist akzeptabel? Wessen Definition von sicherem Urteilsvermögen wird in die Anforderungssprache eingeschrieben? Diese Fragen sind Werturteile, keine rein ingenieurtechnischen Entscheidungen.

Lee weist darauf hin, dass die am stärksten betroffenen Personen – insbesondere ältere Menschen, die oft die primären Nutzer häuslicher Pflegeroboter sind – in den Arbeitsgruppen, die den Standard entwickeln, nicht systematisch vertreten sind. Ihre Bewegungsmuster und kognitiven Zustände fließen nicht direkt in den Standardisierungsprozess ein. Die aktuelle Überarbeitung erkennt zwar die schwierigsten Probleme an, schiebt aber ungelöste Fragen in beratende Formulierungen, unverbindliche Leitlinien oder zukünftige Revisionen.

## Der praktische Ansatz von Hello Robot

Während internationale Gremien über Standards diskutieren, verfolgt das amerikanische Unternehmen Hello Robot einen pragmatischeren Weg. Mit dem kürzlich vorgestellten Stretch 4 demonstriert das Unternehmen, wie sichere und praktische Heimroboter bereits heute realisierbar sind – und zwar ohne den Umweg über humanoide Systeme.

Der Stretch 4 verzichtet bewusst auf Beine, Arme, Hände und Gesichter im humanoiden Sinne. Stattdessen konzentriert sich das Design auf das Wesentliche: Mobilität und Manipulation. Die wichtigste Neuerung ist eine omnidirektionale Basis, die es dem Roboter ermöglicht, sich in jede Richtung zu bewegen, ohne sich erst drehen zu müssen. Dies vereinfacht die Bedienung erheblich, insbesondere für unerfahrene Nutzer.

Die Sensorkopf-Einheit wurde grundlegend überarbeitet und umfasst nun hemisphärische Lidare, spezielle Kameras für Vision und Navigation sowie eine am Handgelenk montierte Tiefenkamera für Manipulation. Das System läuft auf einem Intel NUC 15, ergänzt durch einen Nvidia Jetson Orin NX für KI-basierte visuelle Verarbeitung.

## Die Philosophie des Menschen in der Schleife

Hello Robots Autonomie-Philosophie ist bemerkenswert: Sie setzt auf den Menschen in der Schleife – in verschiedensten Formen von direkter Kontrolle bis zu rein überwachender Steuerung. Der Roboter wird mit grundlegenden autonomen Fähigkeiten ausgeliefert, darunter Kartierung, Navigation, selbstständiges Aufladen und Greiffunktionen. Anders als andere Robotikfirmen strebt Hello Robot jedoch nicht danach, riesige Datenmengen zu sammeln in der vagen Hoffnung, dass daraus irgendwann kommerzielle Autonomie erwächst.

Mitgründer und CTO Charlie Kemp erklärt: "Ich wäre viel lieber die Plattform, auf die Foundation-Model-Entwickler abzielen." Diese Haltung spiegelt ein nüchternes Verständnis der eigenen Stärken wider und vermeidet die gefährliche Überschätzung, die viele humanoide Roboterprojekte kennzeichnet.

## Warum nicht humanoid?

Die Entscheidung gegen eine humanoide Form ist nicht willkürlich, sondern folgt klaren Überlegungen. Henry Evans, der seit etwa 15 Jahren Roboter in seinem Zuhause testet, stellt die entscheidende Frage: "Welchen Vorteil bietet ein zweibeiniger Roboter für eine Person, die nicht gehen kann?" Evans ist gelähmt und kann nicht sprechen – seine Umgebung ist vollständig auf Rollstühle und rollende Systeme ausgelegt.

Seine Argumentation ist überzeugend: Automobile haben keine Beine, und Heimroboter sollten sie auch nicht haben. Räder sind günstig, stabil, präzise, erfordern nur wenige Steuerelemente und müssen nicht erst erfunden werden. Zudem können humanoide Roboter dutzende Freiheitsgrade gleichzeitig erfordern – eine gelähmte Person, die nicht sprechen kann, kann mit heutigen Steuerungsmechanismen bestenfalls ein oder zwei Gelenke gleichzeitig kontrollieren.

Ein weiterer kritischer Aspekt ist die Sicherheit. Wenn ein Roboter auf Rädern im Notfall gestoppt wird, friert er an Ort und Stelle ein. Ein zweibeiniger Roboter hingegen würde auf alles darunter zusammenbrechen – einschließlich des Patienten. Charlie Kemp bringt es deutlich auf den Punkt: "Der Sicherheitsaspekt von Humanoiden im Haushalt macht mir Angst. Ich weiß nicht, wie man bei einem Humanoiden im Haus selbstbewusst über Sicherheit nachdenken kann."

## Bezahlbarkeit als Schlüsselfaktor

Ein oft übersehener Aspekt ist die Wirtschaftlichkeit. Der Stretch 4 kostet 29.950 US-Dollar – für einen mobilen Manipulator sehr erschwinglich. Hello Robot plant, durch Pilotprojekte in Privathaushalten Erkenntnisse zu sammeln, um die nächste Version für den kommerziellen Verkauf zu optimieren. Bei der bisherigen Entwicklungsgeschwindigkeit könnte Stretch 5 innerhalb eines Jahres verfügbar sein – als erster praktischer, bezahlbarer Assistenzroboter für den Heimgebrauch.

## Ausblick: Relationale Sicherheit als Grundlage

Die Zukunft der Heimrobotik liegt nicht in der Perfektion einzelner technischer Komponenten, sondern im Verständnis und der Gestaltung komplexer Beziehungssysteme. Sicherheit muss über das gesamte Spektrum menschlicher Zustände hinweg gewährleistet sein, denen der Roboter tatsächlich begegnen wird. Das erfordert einen Rahmen, der den Menschen nicht als Störfaktor, sondern als Teil der Definition des Sicherheitsbereichs behandelt.

Der Kontrast zwischen den theoretischen Diskussionen um Sicherheitsstandards und Hello Robots pragmatischem Ansatz zeigt: Während die eine Seite noch debattiert, schafft die andere bereits Tatsachen. Beides ist notwendig – aber letztendlich werden es die praktischen Lösungen sein, die zeigen, was funktioniert und was nicht. Die Beziehung zwischen Mensch und Roboter ist keine zu lösende Gleichung, sondern eine zu gestaltende Realität.
