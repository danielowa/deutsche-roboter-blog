---
title: 'Roboter lernen das Fühlen: Taktile Wahrnehmung als Durchbruch für geschickte
  Manipulation'
date: '2026-09-11T11:18:08+02:00'
draft: false
tags:
- Taktile Sensorik
- Dexterous Manipulation
- Roboterwahrnehmung
categories:
- Forschung
summary: Analyse der aktuellen Entwicklungen in der haptischen Robotik-Sensorik und
  wie taktiles Feedback die größte Hürde für geschickte Manipulation überwindet -
  mit Blick auf technologische Ansätze, Forschungsfortschritte und praktische Anwendungen
ShowToc: true
TocOpen: false
---

Die Revolution des Tastsinns in der Robotik markiert möglicherweise den entscheidenden Durchbruch für geschickte Manipulation. Während Vision-Language-Action-Modelle Robotern bereits ermöglichen, Wäsche zu falten oder Küchengeräte zu bedienen, scheitern sie noch immer an scheinbar einfachen Aufgaben: einen USB-Stecker einführen, einen Schlüssel im Schloss drehen oder ein rohes Ei vorsichtig greifen. Der Grund ist offensichtlich, wenn man ihn erstmal erkannt hat – diese Roboter sind praktisch taub gegenüber einer der wichtigsten Informationsquellen: dem Tastsinn.

## Die Lücke in der sensorischen Wahrnehmung

Aktuelle Vision-Language-Action-Modelle haben die Robotik in den letzten Jahren erheblich vorangebracht. Trainiert auf enormen Mengen an Bildern, Videos und Texten, können sie komplexe Aufgaben bewältigen, selbst wenn sie auf völlig neue Objekte und Umgebungen treffen. Doch bei der feinen Handmotorik stoßen sie an ihre Grenzen – und das ist kein Zufall.

Trevor Darrell, Professor für Informatik an der University of California, Berkeley, bringt es auf den Punkt: "Die meisten geschickten Manipulationen können Menschen mit geschlossenen Augen durchführen." Das Verständnis von Kraft, Rutschbewegungen und präzisem Greifen lässt sich mit herkömmlichen Kamerasensoren nicht adäquat erfassen. Hier zeigt sich eine fundamentale Schwäche aktueller Robotersysteme, die sich fast ausschließlich auf visuelle Informationen verlassen.

## Technische Herausforderungen der taktilen Integration

Die Integration von Tastsensoren in robotische Systeme ist allerdings alles andere als trivial. Taktile Sensordaten unterscheiden sich grundlegend von den Bilddaten, auf denen Vision-Language-Modelle normalerweise trainiert werden. Während visuelle Informationen kontinuierlich und in hoher Bandbreite vorliegen, sind taktile Signale spärlich und intermittierend. Diese strukturelle Differenz führt dazu, dass Modelle dazu neigen, taktile Informationen zu ignorieren – ein Problem, das spezielle Lösungsansätze erfordert.

Darüber hinaus hinkt die Verfügbarkeit von taktilen Datensätzen weit hinter den internetweiten Vision- und Sprachdatensätzen her. Während für visuelle KI-Modelle Milliarden von Bildern zur Verfügung stehen, mussten Forscher im taktilen Bereich bisher mit einigen hundert Stunden Demonstrationsdaten auskommen. Diese Datenlücke stellte lange Zeit das größte Hindernis für Fortschritte dar – eine Situation, die sich nun dramatisch zu ändern beginnt.

## Durchbrüche durch spezialisierte Architekturen

Das Team um Trevor Darrell entwickelte einen innovativen Ansatz, um diese Herausforderungen zu bewältigen. Zunächst wird ein Modell auf bestehenden Datensätzen vortrainiert, bevor es durch ein spezialisiertes Submodell mit Tastsinn ausgestattet wird. Dieses wurde auf 100 Stunden hochwertiger taktiler Daten trainiert, die Demonstrationen alltäglicher Aktionen wie Wischen, Greifen, Drehen oder Gießen mit über 200 verschiedenen Haushaltsobjekten umfassen.

Die eigentliche Innovation liegt jedoch in der Architektur: Das System verwendet separate "Experten"-Submodelle für hochrangige Aktionen und niederrangige taktile Kontrolle. Der Aktionsexperte erstellt Bewegungspläne, während der taktile Experte mit vierfacher Geschwindigkeit arbeitet und in Echtzeit auf Basis des haptischen Feedbacks Anpassungen vornimmt. Diese Aufteilung löst das fundamentale Problem der Reaktionsgeschwindigkeit – taktiles Feedback ist nur dann nützlich, wenn das System schnell genug darauf reagieren kann.

In Tests mit relativ komplexen Manipulationsaufgaben wie dem Einschrauben einer Glühbirne, dem Auftragen von Zahnpasta oder dem Transferieren eines Eis zwischen Schalen erreichte das Modell eine durchschnittliche Erfolgsquote von 65 Prozent über zwölf verschiedene Aufgaben hinweg – nahezu das Doppelte des besten reinen VLA-Modells.

## Die Hardware-Diversität als Hindernis

Eine der größten Herausforderungen in der taktilen Robotikforschung liegt in der enormen Vielfalt der Hardware. Roboterhände reichen von vollständig artikulierten Fünf-Finger-Designs bis zu einfachen Zangen-Greifern. Taktile Sensoren können auf grundlegend unterschiedlichen physikalischen Prinzipien basieren – von der Messung von Widerstandsänderungen bis zur Aufzeichnung von Bildern eines sich verformenden Gel-Pads.

Diese Diversität macht einen Großteil der taktilen KI-Forschung sensor-spezifisch und erschwert den Datenaustausch sowie den Transfer von Erkenntnissen zwischen Forschungsgruppen erheblich. Chengbo Yuan, Masterstudent an der Tsinghua-Universität in Peking, hat dieses Problem frontal angegangen, indem er über 3.000 Stunden taktiler Robotikdaten aus öffentlich verfügbaren Datensätzen aggregierte, die 21 verschiedene Sensortypen und eine Vielzahl von Roboterverkörperungen abdecken.

Yuans Team entwickelte ein hardware-agnostisches Modell, das auf diesen diversen Daten trainieren kann, indem es die Ausgabe jeder Sensorart in ein gemeinsames Format konvertiert und auf beschriftete Positionen einer menschlichen Hand-Vorlage abbildet. Dieser Ansatz erwies sich als deutlich erfolgreicher als Baseline-Modelle, selbst auf Hardware, die während des Trainings nicht verwendet wurde. Yuan führt dies darauf zurück, dass das Modell durch das Training auf so unterschiedlichen Setups "eine Art gesunden Menschenverstand des taktilen Wissens" erworben hat.

## Das Rennen um Datenskalierung

Trotz vielversprechender Ergebnisse sind sich Forscher einig, dass noch deutlich mehr taktile Daten benötigt werden. Die Fudan-Universität in Shanghai und ihr Spin-out NeoteAI haben bereits einen taktilen Datensatz produziert, der eine Größenordnung größer ist als frühere Bemühungen. Mit einem proprietären Sensor, der an verschiedenen Roboterarmen und einem handgeführten Greifer befestigt wurde, haben sie über 30.000 Stunden Demonstrationen mit synchronisierten visuellen und taktilen Daten gesammelt.

Die Forscher nutzten diese Daten, um ein Modell zu trainieren, das nicht nur auf Berührung reagiert, sondern auch proaktiv vorhersagt, was der Roboter fühlen sollte, um Aktionen zu leiten und zu bewerten. Shunlin Lu, Postdoktorand an der Fudan-Universität und CTO von NeoteAI, sieht darin einen klaren Beweis dafür, dass der Zugang zu groß angelegten und diversen taktilen Daten zu signifikanten Leistungssteigerungen führt.

## Alternative Wege zur Datengenerierung

Ein innovativer Ansatz zur Skalierung taktiler Daten könnte darin bestehen, die bereits gesammelten enormen Mengen visueller Robotikdaten zu nutzen. Forscher der University of Southern California haben kürzlich ein Modell veröffentlicht, das gelernt hat, taktile Informationen aus visuellen Daten abzuleiten. Trainiert auf über 2.700 Demonstrationen alltäglicher Manipulationen, lernte das Modell Assoziationen zwischen Bildern des Greifers beim Kontakt mit Objekten und dem Druck, den die taktilen Sensoren in diesem Moment fühlten.

Dies verleiht selbst Robotern ohne taktile Sensoren einen rudimentären Tastsinn, der sich besonders für kontaktreiche Manipulationsaufgaben als nützlich erweist. Die umfassendere Ambition der Forscher besteht jedoch darin, den Generator zu nutzen, um bestehenden visuellen Datensätzen taktile Daten hinzuzufügen – ein Ansatz, der das Datenproblem elegant umgehen könnte.

## Jenseits der reinen Datenmenge

Nicht alle Forscher sind überzeugt, dass Datenskalierung allein die Lösung ist. Long Cheng von der Chinesischen Akademie der Wissenschaften betont: "Daten sind gut, aber wie man sie richtig nutzt, ist eine andere Frage." Das Problem liegt in der Natur der Daten selbst: Vision liefert einen kontinuierlichen, hochbandbreitigen Strom von Pixeln, während taktile Signale spärlich und intermittierend sind – was dazu führt, dass Modelle lernen, sie zu ignorieren.

Chengs Lösung, die auf der IROS 2025 vorgestellt wird, ist ein Modell, das vorhersagt, was ein Roboter allein aus visuellen Informationen fühlen wird, und dies dann mit dem tatsächlichen taktilen Input vergleicht. Eine große Diskrepanz zwischen beiden bedeutet, dass der Sensor etwas erkennt, was der Roboter sonst übersehen würde – diese überraschenden Signale werden verstärkt, während vorhersagbare gedämpft werden. Bei fünf kontaktreichen Aufgaben erreichte dieser Ansatz eine durchschnittliche Erfolgsquote von 62,8 Prozent gegenüber 28,2 Prozent für dasselbe Modell ohne Tastsinn.

## Von der Forschung zur industriellen Anwendung

Die Fortschritte in der akademischen Forschung beginnen nun, den Weg in industrielle Anwendungen zu finden. Mit der Eröffnung des Physical AI Lab von Vention in Montreal entsteht eine Brücke zwischen Grundlagenforschung und skalierbarer Produktionslinien-Implementierung. Solche Initiativen signalisieren, dass die Industrie das Potenzial taktiler Intelligenz für die Fertigung erkannt hat.

## Ausblick: Die nächste Stufe der Physical AI

Wie viele taktile Daten letztlich für echte Durchbrüche bei geschickten Aufgaben erforderlich sein werden, bleibt unklar. Bisher hat das taktile Training hauptsächlich dazu beigetragen, Roboter zu effizienteren Lernenden bei Aufgaben zu machen, die bereits in Reichweite sind, wie das Greifen und Platzieren von Objekten. Yuan vermutet, dass neue Algorithmen erforderlich sein könnten, um Probleme anzugehen, die ohne Tastsinn wirklich unmöglich sind.

Lu ist optimistischer bezüglich der Datenskalierung und schätzt, dass etwa 100.000 Stunden taktiler Daten, gesammelt in variierten, realen Umgebungen statt im Labor, neue Fähigkeiten freischalten könnten. Seine Einschätzung: "Ich denke, taktile Intelligenz ist tatsächlich der nächste Schritt für Physical AI."

Die Entwicklung zeigt bereits jetzt einige frühe Anzeichen dafür, dass größere taktile Datensätze und intelligentere Wege, sie zu nutzen, Robotern einen signifikanten Schub bei einigen der anspruchsvollsten Aufgaben geben können. Der Tastsinn könnte sich als der fehlende Baustein erweisen, der Robotern endlich die Geschicklichkeit verleiht, die sie für den breiten Einsatz in komplexen, realen Umgebungen benötigen.
