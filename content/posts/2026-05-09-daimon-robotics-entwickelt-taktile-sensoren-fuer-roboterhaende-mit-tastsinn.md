---
title: DAIMON Robotics entwickelt taktile Sensoren für Roboterhände mit Tastsinn
date: '2026-05-09T09:03:46+02:00'
draft: false
tags:
- Sensorik
- Manipulation
- Haptik
categories:
- Forschung
summary: Analyse der technologischen Durchbrüche in der Roboter-Haptik und deren Bedeutung
  für die nächste Generation von Manipulationsaufgaben - von der Forschung zur praktischen
  Anwendung in Industrie und Pflege
ShowToc: true
TocOpen: false
---

Die Revolution des Roboter-Tastsinns: Wie taktile Sensoren die nächste Generation von Roboterhänden ermöglichen

Während sich die Robotikbranche seit Jahren auf künstliche Intelligenz und maschinelles Sehen konzentriert, rückt nun eine oft vernachlässigte Modalität in den Fokus: der Tastsinn. Das in Hongkong ansässige Startup DAIMON Robotics hat im April dieses Jahres mit der Veröffentlichung des Daimon-Infinity-Datensatzes einen bedeutenden Schritt unternommen, um taktiles Feedback als gleichwertige Sinnesmodalität neben dem visuellen Sehen zu etablieren. Die Bedeutung dieses Vorhabens geht weit über ein weiteres technisches Detail hinaus – es könnte den Durchbruch für wirklich geschickte Robotermanipulation markieren.

## Von VLA zu VTLA: Ein Paradigmenwechsel in der Robotik

Das derzeit dominierende Paradigma in der Robotik basiert auf dem Vision-Language-Action-Modell (VLA), das visuelle Wahrnehmung mit sprachbasierten Anweisungen kombiniert, um Roboterhandlungen zu steuern. Professor Michael Yu Wang, Mitgründer und leitender Wissenschaftler bei DAIMON Robotics, hat jedoch einen entscheidenden Mangel dieses Ansatzes identifiziert: die fehlende Sensibilität für physische Interaktionen.

Seine Lösung ist die Vision-Tactile-Language-Action-Architektur (VTLA), die taktile Information auf dieselbe Ebene hebt wie visuelle Daten. "Ohne taktile Sensoren sind Roboter stark eingeschränkt", erklärt Professor Wang. "Sie haben Schwierigkeiten, Objekte in dunklen Umgebungen zu lokalisieren, können ohne Rutscherkennung zerbrechliche Gegenstände wie Glas fallen lassen und scheitern oft an Manipulationsaufgaben, weil sie Kräfte nicht präzise kontrollieren können."

Diese Einschätzung ist nicht nur theoretischer Natur. In der Praxis zeigt sich, dass viele scheinbar einfache Aufgaben – etwa das Herausziehen eines Produkts aus einem dicht gepackten Regal oder das Greifen empfindlicher Materialien – ohne Tastsinn nahezu unmöglich sind.

## Monochromatische Vision: Die technologische Grundlage

DAIMON Robotics hat einen besonderen technischen Ansatz gewählt: monochromatische, bildbasierte taktile Sensoren. Im Gegensatz zu mehrfarbigen optischen Systemen oder einfacheren Kraftsensoren kombiniert diese Technologie hohe Auflösung mit ingenieurtechnischer Robustheit.

Der Sensor packt über 110.000 effektive Sensoreinheiten in ein fingerkuppengroßes Modul – eine bemerkenswerte Dichte, die derzeit weltweit führend ist. Die Technologie erfasst visuelle Bilder der Verformung an der Fingerkuppenoberfläche in Zeitsequenzen. Aus diesen Bildfolgen lassen sich nicht nur Kontaktkräfte ableiten, sondern auch komplexe physikalische Eigenschaften wie Materialbeschaffenheit, Oberflächentextur, Verformung, Slip und Reibung.

Ein entscheidender Vorteil dieser bildbasierten Herangehensweise liegt in der natürlichen Kompatibilität mit bestehenden VLA-Frameworks. Da die taktilen Informationen bereits in visueller Bildform vorliegen, lassen sie sich nahtlos in die auf maschinellem Sehen basierenden Architekturen integrieren – ein pragmatischer Ansatz, der Grundlagenforschung mit praktischer Anwendbarkeit verbindet.

Neben der Sensordichte sind weitere Parameter entscheidend: Die Dynamik des Systems – also Frequenz und Bandbreite – bestimmt, wie schnell Kraftveränderungen erkannt, Signale übertragen und in Echtzeit verarbeitet werden können. Hinzu kommen ingenieurtechnische Aspekte wie Zuverlässigkeit, Drift-Verhalten, Haltbarkeit der weichen Oberfläche und Resistenz gegenüber magnetischen, optischen oder Umwelteinflüssen.

## Der Datensatz als Katalysator

Die Veröffentlichung des Daimon-Infinity-Datensatzes markiert eine strategische Neuausrichtung für das erst zweieinhalbjährige Unternehmen. Dieser wird als größter omni-modaler Robotik-Datensatz für physische KI beschrieben und umfasst hochauflösende taktile Sensorik über ein breites Spektrum von Aufgaben – vom Wäschefalten im Haushalt bis zur Fertigung an Montagelinien.

Das Projekt entstand in Zusammenarbeit mit Partnern aus China und weltweit, darunter Google DeepMind, die Northwestern University und die National University of Singapore. DAIMON hat 10.000 Stunden der Daten als Open Source zur Verfügung gestellt, um die Entwicklung im gesamten Feld der verkörperten KI zu beschleunigen.

Die Strategie dahinter folgt dem "3D-Modell": Devices (Geräte), Data (Daten) und Deployment (Einsatz). DAIMON baut nicht nur Sensoren, sondern ein vollständiges Ökosystem für Datenerfassung und Modelltraining. Das Unternehmen hat dafür das weltweit größte verteilte Datenerfassungsnetzwerk außerhalb klassischer Labore aufgebaut – ein leichtgewichtiges, skalierbares System, das Millionen Stunden Daten pro Jahr in unterschiedlichsten realen Umgebungen sammeln kann.

Dieser Ansatz unterscheidet sich fundamental von zentralisierten "Datenfabriken". Statt Roboter nur in kontrollierten Umgebungen zu trainieren, ermöglicht das verteilte Netzwerk die Erfassung von Daten über 80 verschiedene reale Szenarien und mehr als 2.000 menschliche Fertigkeiten hinweg.

## Von der Forschung zur Anwendung: Realistische Szenarien

Die praktische Relevanz taktiler Sensoren zeigt sich besonders deutlich in spezifischen Anwendungsszenarien. Professor Wang beschreibt das Beispiel eines humanoiden Roboters, der in einem kleinen Convenience-Store eingesetzt werden soll: "Die Regale sind dicht gepackt, der Platz ist knapp. Der Roboter muss in sehr enge Zwischenräume greifen – enger als Bücher in einem Regal – um ein Objekt herauszunehmen. Derzeitige Parallelgreifer mit zwei Backen passen in die meisten dieser Räume nicht hinein."

Die Lösung orientiert sich am menschlichen Vorbild: Man benötigt mindestens drei schlanke Finger, um das Objekt zu berühren, zu sich hin zu rollen und zu sichern. Für solche Aufgaben sind taktile Sensoren unverzichtbar.

Tatsächlich hat China bereits in einem verwandten Bereich beachtliche Fortschritte gemacht. Praktisch jedes größere Hotel im Land verfügt mittlerweile über Lieferroboter – zwar ohne Arme, aber mit autonomer Navigation inklusive Aufzugnutzung. Diese werden als Modell für die schrittweise Einführung humanoider Roboter in spezifischen Bereichen wie Nacht-Apotheken oder Convenience-Stores betrachtet.

Die Entwicklung ähnelt der von autonomen Fahrzeugen: Vollständig autonome Robo-Taxis sind noch nicht flächendeckend im Einsatz, aber in klar definierten Anwendungsbereichen funktionieren autonome Systeme bereits zuverlässig.

## Industrielle und pflegerische Perspektiven

Besonders vielversprechend sind taktile Sensoren für die Fertigungsindustrie und den Pflegebereich. In der Montage ermöglichen sie präzise Kraft-Momenten-Kontrolle, die für Fügeoperationen, Verschraubungen oder den Umgang mit empfindlichen Bauteilen unerlässlich ist. Die hochauflösenden Sensoren können dabei nicht nur die Gesamtkraft messen, sondern die Kraftverteilung über die gesamte Kontaktfläche erfassen – eine Fähigkeit, die kraftbasierte Sensoren alter Bauart nicht besitzen.

Im Pflegebereich könnte taktiles Feedback die sichere physische Interaktion zwischen Robotern und Menschen revolutionieren. Das sanfte Greifen eines Arms, das Unterstützen beim Aufstehen oder das Reichen von Gegenständen erfordert fein abgestimmte Kraftkontrolle, die nur mit entsprechenden Sensoren möglich ist.

## Der lange Weg vom Professor zum Startup-Gründer

Professor Michael Yu Wang kann auf eine beeindruckende Karriere zurückblicken: 40 Jahre in der Wissenschaft, Promotion an der Carnegie Mellon University unter Matt Mason – einem Pionier der Manipulationsforschung –, Gründung des Robotics Institute an der Hong Kong University of Science and Technology, IEEE Fellow und ehemaliger Chefredakteur der IEEE Transactions on Automation Science and Engineering.

Seine Motivation für die Startup-Gründung beschreibt er als Konvergenzmoment: "Elektrische, elektronische und mechatronische Hardware-Technologien haben sich in den letzten zwei Jahrzehnten enorm weiterentwickelt. Roboter sind jetzt vollständig elektrisch und benötigen keine Hydraulik mehr. Moderne Elektronik bietet enorme Bandbreite bei hohen Drehmomenten. Wenn wir Intelligenz in diese Systeme integrieren können, können wir wirklich humanoide Roboter schaffen."

Die KI sei genau zum richtigen Zeitpunkt gereift, so Wang. Große Sprachmodelle würden nun zu Weltmodellen verallgemeinert, die physische KI-Fähigkeiten ermöglichen.

## Ausblick: Die nächste Phase verkörperter Intelligenz

Die Entwicklungen bei DAIMON Robotics und die parallelen Fortschritte in der Branche – etwa das von Hugging Face vorgestellte Agentic Toolkit für den Roboter Reachy Mini, das die Programmierung durch natürlichsprachliche Beschreibungen ermöglicht – deuten auf eine neue Phase der Robotik hin. Es geht nicht mehr nur um einzelne Durchbrüche in Hardware oder Software, sondern um die Integration multimodaler Wahrnehmung mit lernfähiger KI.

"Unsere Vision ist, dass Roboter robuste Manipulationsfähigkeiten erreichen und sich zu verlässlichen Partnern für Menschen entwickeln", fasst Professor Wang zusammen. Der Weg dorthin mag noch lang sein, aber mit taktilen Sensoren, die es Robotern ermöglichen zu fühlen, was sie berühren, ist ein entscheidender Baustein hinzugekommen. Die nächste Generation von Roboterhänden wird nicht nur sehen und verstehen, was sie tun soll – sie wird es auch fühlen können.
