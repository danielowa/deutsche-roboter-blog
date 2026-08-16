---
title: 'Robotischer Finger mit Farbfühlsensor: Neuer Tastsensor ermöglicht Robotern
  farbbasiertes haptisches Feedback'
date: '2026-08-16T07:20:51+02:00'
draft: false
tags:
- Sensorik
- Haptik
- Greiftechnologie
categories:
- Forschung
summary: Detaillierte technische Analyse des neuen Sensorsystems, das Robotern erlaubt,
  Texturen über Farbinformationen zu erfassen - ein Durchbruch für die haptische Wahrnehmung
  in der Robotik mit Potenzial für Anwendungen in Industrie, Medizin und präziser
  Manipulation
ShowToc: true
TocOpen: false
---

Die Robotik sucht seit langem nach der perfekten Lösung für das Problem der haptischen Wahrnehmung. Während Menschen mühelos mit ihren Fingerspitzen Oberflächen abtasten und dabei die feinsten Details wahrnehmen können, stehen Robotersysteme vor erheblichen Herausforderungen. Nun präsentiert ein europäisches Forscherteam einen unkonventionellen Ansatz: einen robotischen Finger, dessen synthetische Haut ihre Farbe ändert, wenn sie deformiert wird – und damit präzise haptische Information liefert.

## Das Prinzip der mechanochromischen Wahrnehmung

Der von Wissenschaftlern der Queen Mary University of London, der Universitäten von Florenz, Triest und Trento entwickelte Sensor basiert auf einem faszinierenden physikalischen Phänomen. Das Herzstück bildet ein sogenannter Bragg-Reflektor – eine Struktur mit alternierenden Schichten unterschiedlicher Brechungsindizes. Giacomo Sasso, Postdoktorand im Labor von Federico Carpi, entwickelte die Idee nach der Lektüre einer Arbeit in der Fachzeitschrift Nature über mechanochromische Materialien.

Die Herstellung des Reflektors erfolgt durch ein präzises Belichtungsverfahren: Ein lichtempfindlicher Film wird sieben Minuten lang einem 5-Megawatt-Laser mit einer Wellenlänge von 635 Nanometern ausgesetzt. Der Laserstrahl erzeugt ein Interferenzmuster, das die Polymerisation des Films in alternierenden Dichten bewirkt. Diese Schichten mit unterschiedlichen Brechungsindizes reflektieren spezifische Wellenlängen des Lichts.

Das Besondere: Wenn dieser Reflektor durch Kontakt mit einem Objekt verformt wird, werden seine Schichten gedehnt und dünner. Dadurch ändert sich die reflektierte Lichtwellenlänge – von Rot bei geringer Deformation über Grün bis hin zu Blau bei stärkerer Verformung. Diese Farbänderung ist nicht nur ein visueller Effekt, sondern ein präzises Messverfahren für mechanische Belastung.

## Aufbau und Funktionsweise des Sensorsystems

Der robotische Finger besteht aus mehreren sorgfältig aufeinander abgestimmten Schichten. Der Bragg-Reflektor ist zwischen einer schützenden Silikonschicht und einem transparenten, fingerförmigen Silikonkörper eingebettet. Im Inneren dieses transparenten Fingers befinden sich eine Kamera und eine LED-Lichtquelle.

Die LED strahlt Licht durch das klare Polymer des Fingers. Wenn die Fingerspitze durch ein Objekt deformiert wird, reflektiert der Bragg-Reflektor das Licht zur Kamera zurück – mit Wellenlängen, die vom Grad der Verformung abhängen. Die Kamera erfasst diese Farbinformationen und wandelt sie in topografische Karten um, die nicht nur die Oberflächenstruktur, sondern auch Dehnung und Kontaktdruck abbilden.

Um die Sensitivität zu maximieren, nahmen die Forscher wichtige Optimierungen vor. Die äußere Silikonschicht ist schwarz eingefärbt, um den Farbkontrast zu erhöhen und der Kamera die Unterscheidung feiner Farbunterschiede zu erleichtern. Zusätzlich verstärkt die Steifigkeit der im Finger eingebetteten Kamera die Verformung des Reflektors und erzeugt dadurch größere Unterschiede in den reflektierten Wellenlängen.

Das Resultat dieser Optimierungen ist bemerkenswert: Der Sensor erreicht eine räumliche Auflösung von 100 Mikrometern – ohne rechnerische Latenz. Das Team konnte bereits erfolgreich detaillierte topografische Karten eines menschlichen Fingers, eines US-Cent-Stücks und eines Blattes erstellen, wobei selbst feinste Oberflächenstrukturen wie die erhabenen Buchstaben auf der Münze oder die Riffelung der Lincoln-Memorial-Säulen sichtbar wurden.

## Quantitative Tiefenmessung als Alleinstellungsmerkmal

Was diesen Ansatz von anderen taktilen Sensoren unterscheidet, ist die Fähigkeit zur quantitativen Analyse. Während viele bestehende Systeme lediglich relative topografische Karten generieren können, extrahiert dieser Sensor tatsächliche Informationen über Tiefe und Größe von Objektmerkmalen. 

Rich Walker, Direktor von Shadow Robot, einem der führenden britischen Roboterhersteller mit Fokus auf robotische Hände, zeigte sich beeindruckt von diesem „deutlich anderen Ansatz". Die Besonderheit liegt in der Integration der taktilen Wahrnehmung direkt in das Material des Fingers, anstatt diskrete Kraftsensoren – sogenannte Taxels – an bestimmten räumlichen Punkten zu verwenden.

Sasso betont diesen Aspekt: Die Messelemente befinden sich auf Materialebene, während die Kamera als hochoptimierte elektronische Komponente lediglich übersetzt, was das Material bereits physikalisch leistet. Dies unterscheidet sich fundamental von konventionellen Ansätzen, bei denen Arrays von Drucksensoren verwendet werden müssen.

## Herausforderungen und kritische Betrachtung

Trotz der vielversprechenden Eigenschaften gibt es auch kritische Stimmen. Michael Wang, Mitgründer und leitender Wissenschaftler bei Daimon Robotics, weist auf eine zentrale Herausforderung hin: die Langzeitbeständigkeit weicher Materialien. Wenn Silikon durch wiederholten Gebrauch erodiert oder beschädigt wird, können die Sensorsignale die tatsächliche Topografie von Objekten nicht mehr präzise wiedergeben.

Dies ist ein grundsätzliches Problem bei weichen Sensoren. Besonders wenn die Elektronik direkt in die Materialschicht eingebettet ist, entsteht ein anspruchsvolles technisches Problem. Wang merkt an, dass bisher nur wenige weiche elektronische Materialien existieren, die längeren Nutzungsperioden standhalten.

Das Forscherteam begegnet dieser Kritik mit einem konstruktiven Argument: Der Bragg-Reflektor steht nicht in direktem Kontakt mit den abgetasteten Objekten. Die äußere Silikonschicht fungiert als Schutzbarriere. Zudem lässt sich Silikon durch spezielle chemische Beschichtungen deutlich haltbarer machen, wie Wang selbst einräumt.

Ein weiterer Punkt betrifft die räumlichen Einschränkungen robotischer Finger. Menschliche Haut verarbeitet eine Vielzahl taktiler Informationen gleichzeitig – Temperatur, Textur, Druck und Vibration. In einem robotischen Fingerspitze ist jedoch oft nicht genug Platz für mehrere Sensortypen. Walker formuliert es treffend: Die Frage, welcher Sensortyp verwendet werden sollte, sei „eine wirklich schwierige Frage. Niemand weiß es noch."

## Anwendungsperspektiven und Zukunftsausblick

Die praktische Relevanz dieser Technologie wird sich in der Integration in reale Roboterhände zeigen müssen. Das Team befindet sich bereits in Gesprächen mit Unternehmen über potenzielle Anwendungen. Ein besonders vielversprechendes Einsatzgebiet sehen die Forscher in der Medizintechnik: Chirurgische Instrumente, die präzises Kontakt-Mapping von Gewebe und Organen erfordern, könnten von dieser Technologie profitieren.

Derzeit arbeitet das Team an Verbesserungen, um auch Objekte erfassen zu können, die nicht flach auf Oberflächen liegen. Dies würde den Anwendungsbereich erheblich erweitern und die Technologie für komplexere Manipulationsaufgaben qualifizieren.

Carpi zeigt sich zuversichtlich: „Es gibt bedeutende Entwicklungen, die wir erwarten, mit einem klaren Pfad zur Übertragung in reale Anwendungen." Diese Aussage unterstreicht, dass es sich nicht um Grundlagenforschung ohne praktischen Bezug handelt, sondern um eine Technologie mit konkretem Anwendungspotenzial.

In der Industrierobotik könnte der Sensor präzise Montageaufgaben ermöglichen, bei denen subtile Oberflächeneigenschaften erkannt werden müssen. In der Servicerobotik würde er Robotern helfen, empfindliche Objekte sicher zu greifen. Die fehlende Latenz ist dabei ein entscheidender Vorteil für Echtzeitanwendungen.

Die Entwicklung zeigt exemplarisch, wie interdisziplinäre Forschung – in diesem Fall die Verbindung von Optik, Materialwissenschaft und Robotik – zu innovativen Lösungen führen kann. Ob sich dieser farbenbasierte Ansatz durchsetzen wird, hängt letztlich von der Bewährung in praktischen Anwendungen ab. Doch bereits jetzt erweitert er das Repertoire verfügbarer Technologien für die haptische Wahrnehmung in der Robotik.
