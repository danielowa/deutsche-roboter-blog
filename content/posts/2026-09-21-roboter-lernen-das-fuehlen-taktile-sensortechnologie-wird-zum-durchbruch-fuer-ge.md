---
title: 'Roboter lernen das Fühlen: Taktile Sensortechnologie wird zum Durchbruch für
  geschickte Manipulation'
date: '2026-09-21T12:20:34+02:00'
draft: false
tags:
- Taktile Sensorik
- Manipulation
- KI
categories:
- Forschung
summary: Eine tiefgehende Analyse, wie neue haptische Sensorsysteme und KI-gestützte
  taktile Wahrnehmung die größte Barriere der Robotik überwinden – die geschickte
  Manipulation von Objekten. Der Artikel beleuchtet aktuelle Forschungsansätze, technologische
  Herausforderungen und das transformative Potenzial für Industrie und Servicerobotik.
ShowToc: true
TocOpen: false
---

Die geschickte Manipulation von Objekten gehört seit Jahrzehnten zu den größten Herausforderungen der Robotik. Während Roboter in strukturierten Industrieumgebungen längst Präzisionsarbeit leisten, scheitern sie noch immer an vermeintlich einfachen Alltagsaufgaben: Ein USB-Kabel einstecken, einen Schlüssel im Schloss drehen oder ein rohes Ei vorsichtig handhaben – für Menschen trivial, für Roboter bislang eine nahezu unlösbare Aufgabe. Der Grund liegt auf der Hand, oder besser gesagt: in ihr. Menschen verlassen sich bei feinmotorischen Tätigkeiten primär auf ihren Tastsinn, nicht auf ihre Augen. Diese fundamentale Erkenntnis führt zu einem Paradigmenwechsel in der Robotik: Taktile Sensortechnologie, kombiniert mit KI-gestützter Verarbeitung, könnte die Lösung für das Manipulationsproblem sein.

## Die Vision-Lücke: Warum Sehen allein nicht ausreicht

Vision-Language-Action-Modelle haben in den vergangenen Jahren beeindruckende Fortschritte ermöglicht. Diese VLAs, trainiert auf riesigen Mengen an Bildern, Videos und Texten, können Roboter durch komplexe Aufgaben leiten – vom Wäschefalten über das Aufräumen von Wohnräumen bis zur Bedienung von Küchengeräten. Doch bei allen Erfolgen bleibt eine kritische Schwäche: Aufgaben, die feinmotorische Handkontrolle erfordern, überfordern diese Systeme systematisch.

Trevor Darrell, Professor für Informatik an der University of California, Berkeley, bringt es auf den Punkt: "Die meisten geschickten Manipulationen können Menschen mit geschlossenen Augen ausführen. Kraft, Rutschen und präzises Greifen zu verstehen, ist mit herkömmlichen visuellen Sensoren nicht gut möglich." Die Lösung liegt in der Integration taktiler Sensoren – doch deren praktische Umsetzung ist alles andere als trivial.

## Das Datenproblem: Taktile Informationen als neue Dimension

Eine der größten Hürden auf dem Weg zu tastenden Robotern ist der eklatante Mangel an Trainingsdaten. Während VLAs auf internet-weite Datensätze zurückgreifen können, existieren für taktile Informationen nur vergleichsweise winzige Datensammlungen. Die Charakteristika taktiler Daten unterscheiden sich fundamental von Bildinformationen: Sie sind spärlich, intermittierend und hochgradig hardwarespezifisch.

Das Team um Darrell entwickelte einen innovativen Ansatz, um diese Herausforderung zu bewältigen. Sie trainierten zunächst ein Modell auf bestehenden visuellen Datensätzen und erweiterten es dann durch ein spezialisiertes Untermodell, das auf 100 Stunden hochwertiger taktiler Daten basiert. Diese Daten umfassen Demonstrationen gängiger Aktionen wie Wischen, Greifen, Drehen und Gießen mit über 200 verschiedenen Haushaltsgegenständen.

Die praktische Umsetzung erforderte jedoch einen ausgeklügelten technischen Kniff. Das Problem: Taktiles Feedback muss in Echtzeit verarbeitet werden, um effektiv zu sein. Die meisten Vision-Language-Modelle arbeiten jedoch zu langsam für diese schnellen Reaktionszeiten. Die Lösung bestand in der Entwicklung eines Zwei-Experten-Systems: Ein "Action Expert" erstellt übergeordnete Bewegungspläne, während ein "Tactile Expert", der viermal schneller operiert, diese Pläne in Echtzeit anhand des haptischen Feedbacks anpasst.

## Beeindruckende Ergebnisse in der Praxis

Die Ergebnisse des Systems sind vielversprechend. Bei komplexen Manipulationsaufgaben wie dem Einschrauben einer Glühbirne, dem Auftragen von Zahnpasta auf eine Zahnbürste oder dem Übertragen eines Eis zwischen Schalen erreichte das Modell eine durchschnittliche Erfolgsrate von 65 Prozent über zwölf verschiedene Aufgaben hinweg – nahezu doppelt so hoch wie das beste reine VLA-Modell ohne taktile Komponente.

Dennoch räumt Darrell eine wichtige Einschränkung ein: Die Daten stammen von einer einzigen Roboterhardware-Konfiguration. Roboterhände variieren erheblich – von vollständig artikulierten Fünf-Finger-Designs bis zu einfachen Zangengreifern. Auch taktile Sensoren basieren auf grundlegend unterschiedlichen physikalischen Prinzipien: Manche messen Widerstandsänderungen, andere zeichnen Bilder von sich deformierenden Gel-Pads auf. Diese Heterogenität macht den Großteil der taktilen KI-Forschung sensorspezifisch und erschwert den Datenaustausch zwischen Forschungsgruppen erheblich.

## Hardware-Agnostik als Lösungsansatz

Chengbo Yuan, Masterstudent an der Tsinghua-Universität in Peking, erkannte diese Problematik und entwickelte einen innovativen Ansatz zur Überwindung der Hardware-Fragmentierung. Sein Team aggregierte über 3.000 Stunden taktiler Roboterdaten aus öffentlich verfügbaren Datensätzen, die 21 verschiedene Sensortypen und diverse Roboter-Verkörperungen abdecken.

Die Inspiration kam von Initiativen wie der Open X-Embodiment Collaboration, die Daten von zahlreichen Robotern zusammenführte und zu Modellen führte, die auf in der Trainingsphase nicht verwendeter Hardware generalisieren konnten. Yuans Team entwickelte ein hardware-agnostisches Modell, das auf diesen diversen Daten trainiert, indem es die Ausgabe jedes Sensors in ein gemeinsames Format konvertiert und auf beschriftete Positionen einer menschlichen Hand-Vorlage abbildet.

Das Ergebnis war bemerkenswert: Das Modell erwies sich als deutlich erfolgreicher als Basisliniensysteme, selbst auf Hardware, die es während des Trainings nie gesehen hatte. Yuan führt dies darauf zurück, dass das System durch das Training auf derart vielfältigen Setups "eine Art Allgemeinwissen über taktiles Wissen" erworben hat.

## Der Wettlauf um Datenmenge

Trotz der vielversprechenden Resultate ist Yuan überzeugt, dass noch mehr taktile Daten benötigt werden. Seine Gruppe leitet mittlerweile eine Zusammenarbeit von 80 Institutionen, um einen größeren Satz teleoperierter Demonstrationen mit einem standardisierten Ansatz zur taktilen Datenerfassung und -verarbeitung zusammenzustellen.

Während diese Bemühungen noch laufen, hat die Fudan-Universität in Shanghai gemeinsam mit ihrem Spin-out NeoteAI bereits einen taktilen Datensatz erstellt, der eine Größenordnung umfangreicher ist als bisherige Bemühungen. Mit einem proprietären Sensor, der an verschiedenen Roboterarmen und einem handgeführten Greifer befestigt wurde, sammelten sie über 30.000 Stunden Demonstrationen mit synchronisierten visuellen und taktilen Daten.

Die Forscher nutzten diese Daten, um ein Modell zu trainieren, das nicht nur auf Berührungen reagiert, sondern auch proaktiv vorhersagt, was der Roboter fühlen sollte, um Aktionen zu leiten und zu bewerten. Shunlin Lu, Postdoc-Forscher an der Fudan-Universität und CTO von NeoteAI, betrachtet die Ergebnisse als klaren Beweis dafür, dass der Zugang zu umfangreichen und vielfältigen taktilen Daten zu signifikanten Leistungssteigerungen führt.

## Alternative Wege: Synthetische Taktilität

Ein alternativer Ansatz zur Skalierung taktiler Daten könnte darin bestehen, die bereits vorhandenen enormen Mengen visueller Robotikdaten zu nutzen. Forscher der University of Southern California entwickelten kürzlich ein Modell, das gelernt hat, taktile Informationen aus visuellen Daten abzuleiten. Das System wurde auf über 2.700 Demonstrationen alltäglicher Manipulationen trainiert, bei denen ein handgeführter Greifer sowohl taktile Daten als auch Bilder einer am Gerät befestigten Kamera aufzeichnete.

Das Modell lernte Assoziationen zwischen Bildern des Greifers beim Kontakt mit Objekten und dem in diesem Moment von den taktilen Sensoren gefühlten Druck. Dies verleiht selbst Robotern ohne taktile Sensoren einen rudimentären Tastsinn, der sich als besonders nützlich für kontaktreiche Manipulationsaufgaben erwies. Die weitergehende Ambition der Forscher besteht darin, den Generator zu nutzen, um bestehenden visuellen Datensätzen taktile Daten hinzuzufügen.

## Die Bedeutung intelligenter Algorithmen

Wie viele taktile Daten für Durchbrüche bei geschickten Manipulationsaufgaben erforderlich sind, bleibt unklar. Bisher bestand der Hauptbeitrag des taktilen Trainings laut Yuan darin, Roboter zu effizienteren Lernenden bei Aufgaben zu machen, die bereits in Reichweite liegen, wie das Greifen und Platzieren von Objekten. Er vermutet, dass neue Algorithmen erforderlich sein könnten, um Probleme anzugehen, die ohne Tastsinn wirklich unmöglich sind.

Long Cheng von der Chinesischen Akademie der Wissenschaften in Peking teilt diese Einschätzung. "Daten sind gut", sagt er. "Aber wie man sie richtig nutzt, ist eine andere Frage." Das Problem besteht darin, dass visuelle Informationen einen kontinuierlichen Datenstrom mit hoher Bandbreite liefern, während taktile Signale spärlich und intermittierend sind – mit der Folge, dass Modelle lernen, sie zu ignorieren.

Chengs Lösung, die auf der IROS 2026 präsentiert wird, besteht in einem Modell, das allein aus visuellen Informationen vorhersagt, was ein Roboter fühlen wird, und dies dann mit dem tatsächlichen taktilen Input vergleicht. Eine große Diskrepanz zwischen Vorhersage und Realität bedeutet, dass der Sensor etwas erfasst, das der Roboter sonst übersehen würde. Solche überraschenden Signale werden verstärkt, während vorhersehbare gedämpft werden. Bei fünf kontaktreichen Aufgaben erreichte dieser Ansatz eine durchschnittliche Erfolgsrate von 62,8 Prozent gegenüber 28,2 Prozent für dasselbe Modell ohne Tastsinn.

## Ausblick: Die Zukunft der physischen KI

Lu zeigt sich zuversichtlicher bezüglich des Potenzials der Datenskalierung und vermutet, dass näher an 100.000 Stunden – gesammelt in vielfältigen, realen Umgebungen statt im Labor – neue Fähigkeiten erschließen könnten. Unabhängig davon gibt es nun erste Anzeichen dafür, dass größere taktile Datensätze und intelligentere Methoden zu ihrer Nutzung Robotern einen signifikanten Schub bei einigen der anspruchsvollsten Aufgaben verleihen können.

Die Integration taktiler Intelligenz markiert möglicherweise den nächsten evolutionären Schritt in der Robotik. Während Vision-Language-Modelle Robotern geholfen haben, die Welt zu verstehen, könnte der Tastsinn ihnen ermöglichen, wirklich mit ihr zu interagieren. Für Industrieanwendungen bedeutet dies präzisere Montagearbeiten und den Umgang mit empfindlichen Materialien. In der Servicerobotik eröffnen sich völlig neue Einsatzfelder – von der Altenpflege über Haushaltsaufgaben bis hin zu chirurgischen Assistenzsystemen.

Die größte Transformation könnte jedoch konzeptueller Natur sein: Der Übergang von Robotern, die die Welt beobachten und darauf reagieren, zu Systemen, die sie aktiv ertasten und verstehen. Dieser Paradigmenwechsel könnte letztlich den Unterschied ausmachen zwischen Maschinen, die in kontrollierten Umgebungen funktionieren, und solchen, die sich wirklich in der unstrukturierten Komplexität unserer alltäglichen physischen Welt bewegen können.
