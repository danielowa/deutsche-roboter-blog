---
title: 'Kontakt statt Geschicklichkeit: Warum taktile Wahrnehmung die nächste Ära
  der Robotik definieren könnte'
date: '2026-06-10T10:44:43+02:00'
draft: false
tags:
- Physical AI
- Taktile Sensorik
- Dexterous Manipulation
categories:
- Forschung
summary: Analyse des Paradigmenwechsels von rein visueller zu kontaktbasierter Robotik-Wahrnehmung,
  mit Fokus auf neue Benchmark-Plattformen wie RobOmni und die Entwicklung von Physical
  AI als Weiterentwicklung der Embodied AI
ShowToc: true
TocOpen: false
---

Die Robotik hat in den vergangenen Jahrzehnten enorme Fortschritte gemacht – von der industriellen Automation bis hin zu humanoiden Robotern, die komplexe Aufgaben bewältigen können. Doch bei genauerer Betrachtung zeigt sich: Viele dieser Erfolge basieren auf einer fundamentalen Annahme, die zunehmend an ihre Grenzen stößt. Roboter verlassen sich primär auf visuelle Wahrnehmung, während die physische Interaktion mit ihrer Umgebung – der Kontakt selbst – oft vernachlässigt wird. Ein Paradigmenwechsel zeichnet sich ab, der die nächste Ära der Robotik definieren könnte: von der Geschicklichkeit zur taktilen Intelligenz.

## Der Ballon-Hund als technologische Metapher

Auf der IEEE International Conference on Robotics (ICRA) 2026 in Wien zog eine Demonstration besondere Aufmerksamkeit auf sich. Zwei robotische Hände formten einen Ballon-Hund – langsam, präzise und ohne den Ballon platzen zu lassen. Was auf den ersten Blick spielerisch wirkte, offenbarte bei näherer Betrachtung eine der schwierigsten Herausforderungen der modernen Robotik.

Ein Ballon ist leicht, hochgradig deformierbar, rutschig und extrem kraftempfindlich. Jede Drehung verändert seine Geometrie und seinen Innendruck. Für Menschen ist dies intuitiv beherrschbar – wir passen uns kontinuierlich an, ohne bewusst über Kraftregulierung oder Rutschprävention nachzudenken. Für Roboter bleibt diese Anpassungsfähigkeit bemerkenswert schwierig. Die Herausforderung liegt nicht darin, die Finger an die richtige Position zu bewegen, sondern eine stabile Interaktion aufrechtzuerhalten, während sich das Objekt selbst verändert.

Diese Unterscheidung ist entscheidend: Was wie eine Demonstration von Geschicklichkeit aussieht, ist in Wahrheit eine Demonstration über Kontakt. Viele der schwierigsten Probleme in der Robotik beginnen erst, nachdem der Kontakt hergestellt wurde.

## Von der Bewegungs- zur Kontaktintelligenz

Das chinesische Unternehmen AGILINK, das hinter der Ballon-Hund-Demonstration steht, unterscheidet zwischen zwei komplementären Fähigkeiten: Bewegungsintelligenz (Motion Intelligence) und Kontaktintelligenz (Contact Intelligence).

Bewegungsintelligenz umfasst die Fähigkeit, Aktionen zu generieren, beidhändige Verhaltensweisen zu koordinieren und erweiterte Manipulationssequenzen unter realen Unsicherheitsbedingungen auszuführen. Sie bestimmt, was der Roboter tun möchte.

Kontaktintelligenz hingegen beschreibt die Fähigkeit, physische Interaktion herzustellen, aufrechtzuerhalten und anzupassen, während sich Kraftverteilung, Reibung, Verformung und Kontaktgeometrie kontinuierlich verändern. Sie bestimmt, ob der Roboter das Geplante auch tatsächlich durchführen kann.

Für die Entwicklung des Ballon-Hund-Systems sammelte AGILINK zunächst Demonstrationen von professionellen Ballonkünstlern. Menschliche Aktionen wurden auf robotische Hände übertragen, um eine initiale Manipulationsstrategie zu etablieren. Doch erfolgreiche Demonstrationen allein reichten nicht aus. Besonders wertvoll erwies sich das Lernen aus Fehlern: Wann immer Instabilität auftrat, griffen menschliche Operatoren ein und korrigierten die Manipulation in Echtzeit. Diese Interventionen wurden aufgezeichnet und in Reinforcement-Learning-Zyklen integriert.

Dabei zeigte sich: Viele Fehler resultierten nicht aus falschen Aktionssequenzen, sondern aus dem Zusammenbruch des Kontakts selbst. Zwischen einem wegrutschenden und einem platzenden Ballon liegt ein schmaler Stabilitätsbereich – erfolgreiche Manipulation bedeutet, diesen Bereich zu finden und während der gesamten Aufgabe darin zu bleiben.

## Die OmniHand 3 Ultra-M: Hardware für die Kontaktrevolution

Die Erkenntnis, dass Kontaktintelligenz nicht allein durch bessere Lernalgorithmen erreicht werden kann, führte zur Entwicklung neuer Hardware. Auf der ICRA 2026 stellte AGILINK die OmniHand 3 Ultra-M vor – eine robotische Hand, die etwa die Größe einer erwachsenen menschlichen Hand hat und 20 aktive Freiheitsgrade integriert.

Das charakteristische Merkmal ist eine vollständig direktangetriebene Architektur. Im Gegensatz zu herkömmlichen Roboterhänden, die oft auf Getriebe und Untersetzungen ansetzen, ermöglicht der Direktantrieb schnellere und transparentere Kraftregulierung sowie eine höhere Bandbreite in der Kraftregelung. Für kontaktreiche Manipulation kann Reaktionsfähigkeit genauso wichtig sein wie die Sensorik selbst.

Die Plattform integriert taktile Sensoren über nahezu die gesamte Hand. Jede Fingerspitze enthält einen miniaturisierten visionbasierten taktilen Sensor, während mehr als 300 dreidimensionale taktile Messpunkte über die Handfläche verteilt sind. Gemeinsam liefern sie Informationen nicht nur darüber, wo Kontakt stattfindet, sondern auch, wie sich der Kontakt entwickelt.

Das System ist darauf ausgelegt, Druckverteilung, Scherkräfte, lokale Verformung, Rutschtendenzen und andere Interaktionsdynamiken zu erfassen, die für konventionelle positionsbasierte Regelungssysteme oft unsichtbar bleiben. Nach Angaben von AGILINK erreichen die einzelnen Sensoren eine Kraftauflösung von etwa 0,005 Newton – ungefähr vergleichbar mit der Detektion eines auf der Fingerspitze liegenden Blattes Papier. Die räumliche Auflösung liegt bei etwa 0,04 Millimetern, die Sensordichte erreicht rund 50.000 Messpunkte pro Quadratzentimeter.

## RobOmni: Eine Benchmark-Plattform für Physical AI

Parallel zu den Entwicklungen bei AGILINK haben Daimon Robotics und Galbot die gemeinsame Benchmark-Plattform RobOmni vorgestellt. Diese Initiative markiert einen bedeutenden Schritt in der Systematisierung und Vergleichbarkeit von taktiler Wahrnehmung und geschickter Manipulation.

RobOmni reflektiert eine grundlegende Verschiebung in der Embodied AI – der Künstlichen Intelligenz für verkörperte Systeme. Während frühere Ansätze stark vision-zentriert waren, entwickelt sich das Feld zunehmend in Richtung Physical AI. Der Unterschied ist subtil, aber bedeutsam: Embodied AI betont die räumliche Verortung intelligenter Systeme in der physischen Welt. Physical AI geht einen Schritt weiter und stellt die physische Interaktion selbst ins Zentrum – Kontakt, Kraft, Material und Verformung werden zu primären Informationsquellen.

Benchmark-Plattformen wie RobOmni sind essenziell, um Fortschritte quantifizierbar und vergleichbar zu machen. In der Computer Vision existieren etablierte Benchmarks wie ImageNet oder COCO, die den Fortschritt über Jahre hinweg messbar gemacht haben. Für taktile Wahrnehmung und kontaktbasierte Manipulation fehlten bislang äquivalente Standards. RobOmni zielt darauf ab, diese Lücke zu schließen und eine gemeinsame Grundlage für die Bewertung von Physical AI-Systemen zu schaffen.

## Warum Kontakt die Zukunft definiert

Die Bedeutung der Kontaktintelligenz reicht weit über Ballon-Hunde hinaus. Viele Aufgaben, die sich der Automatisierung bisher widersetzen, beinhalten instabile oder deformierbare Interaktionen: Kabelstecken, Textilhandhabung, flexible Verpackungen, Feinmontage, Werkzeugnutzung und Haushaltsmanipulation.

Diese Aufgaben sind nicht deshalb schwierig, weil Roboter die richtige Position nicht erreichen können, sondern weil das Aufrechterhalten stabiler Interaktion nach Kontaktbeginn außerordentlich schwer bleibt. Jahrzehntelang erzielte die Robotik ihre Erfolge durch Reduktion von Unsicherheit. Fabriken wurden so konstruiert, dass robotische Bewegung vorhersagbar, wiederholbar und hochstrukturiert wurde.

Die physische Welt verhält sich anders. Objekte verschieben sich, Materialien verformen sich, Reibung ändert sich, Kontakt entwickelt sich. Reale Umgebungen folgen selten Skripten. Aus dieser Perspektive betrachtet ging es beim Ballon-Hund nie wirklich um den Ballon-Hund. Was bei der ICRA Aufmerksamkeit erregte, war nicht einfach eine visuell beeindruckende Demonstration, sondern ihre Enthüllung: Intelligenz in der physischen Welt wird letztlich durch Interaktion gemessen.

## Ausblick: Von der visuellen zur multimodalen Robotik

Der Paradigmenwechsel von visueller zu kontaktbasierter Wahrnehmung markiert keine vollständige Ablösung, sondern eine Erweiterung. Vision bleibt unverzichtbar für Navigation, Objekterkennung und räumliches Verständnis. Doch für Manipulation – besonders in unstrukturierten Umgebungen – erweist sich taktile Wahrnehmung zunehmend als ebenso fundamental.

Die Integration beider Modalitäten, oft als visuotaktile Wahrnehmung bezeichnet, verspricht Fähigkeiten, die über die Summe ihrer Teile hinausgehen. Vision liefert Kontext und räumliche Information, Taktilsensorik liefert Interaktionsintelligenz. Zusammen ermöglichen sie eine differenziertere Wahrnehmung und Reaktion auf die physische Welt.

Die nächste Ära der Robotik wird wahrscheinlich nicht durch einzelne Durchbrüche definiert, sondern durch die zunehmende Beherrschung von Kontakt – die Fähigkeit, physische Interaktion so flexibel und anpassungsfähig zu gestalten, wie es Menschen intuitiv beherrschen. Plattformen wie die OmniHand 3 Ultra-M und Benchmarks wie RobOmni bilden die Grundlage für diese Entwicklung.

Wenn der Ballon-Hund von Wien eines gezeigt hat, dann dies: Die schwierigsten Probleme der Robotik beginnen genau dort, wo der Kontakt beginnt. Und ihre Lösungen werden bestimmen, wie weit Roboter in die unstrukturierte, deformierbare, unvorhersehbare Welt vordringen können, in der wir leben.
