---
title: General Robotics setzt auf modulare Intelligenz statt ein einzelnes Roboter-Gehirn
date: '2026-09-28T13:22:02+02:00'
draft: false
tags:
- KI-Architektur
- Modulare Robotik
- Foundation Models
categories:
- KI
summary: Analyse des neuen Ansatzes der modularen, spezialisierten KI-Fähigkeiten
  gegenüber universellen Modellen – welche Vorteile bietet die Komposition spezialisierter
  Fähigkeiten für die praktische Robotik-Anwendung und wie unterscheidet sich dieser
  Ansatz von aktuellen Foundation-Model-Strategien?
ShowToc: true
TocOpen: false
---

## Der Paradigmenwechsel in der Roboter-KI

Die Robotikbranche steht vor einer strategischen Weichenstellung: Während viele Unternehmen auf immer größere, universelle KI-Modelle setzen, verfolgt General Robotics einen fundamental anderen Ansatz. Statt eines einzelnen "Roboter-Gehirns" setzt das Unternehmen auf modulare Intelligenz – ein Konzept, das spezialisierte Fähigkeiten wie Bausteine kombiniert. Diese Entscheidung wirft grundlegende Fragen über die Zukunft der Robotik auf: Ist größer wirklich besser, oder liegt der Schlüssel zum Erfolg in der intelligenten Komposition spezialisierter Systeme?

Die aktuelle Debatte erinnert an frühere Architekturdebatten in der Informatik. Während Foundation Models – große, auf riesigen Datenmengen vortrainierte Modelle – in der Bild- und Sprachverarbeitung beeindruckende Erfolge feiern, zeigen sich in der praktischen Robotik zunehmend deren Grenzen. General Robotics setzt dagegen auf einen Ansatz, der spezialisierte KI-Module für unterschiedliche Aufgaben entwickelt und diese je nach Bedarf kombiniert.

## Die Grenzen universeller Modelle in der Robotik

Vision-Language-Action (VLA) Modelle haben in den letzten Jahren erhebliche Fortschritte ermöglicht. Diese auf gewaltigen Mengen von Bildern, Videos und Text vortrainierten Systeme, die anschließend mit kleineren Datensätzen aus robotischen Demonstrationen feinabgestimmt werden, können Roboter durch eine wachsende Bandbreite alltäglicher Aufgaben führen – vom Wäschefalten über das Aufräumen von Wohnzimmern bis zum Bedienen von Küchengeräten.

Doch diese beeindruckenden Fähigkeiten täuschen über eine fundamentale Schwäche hinweg: VLAs verlassen sich nahezu ausschließlich auf visuelle Information. Bei Aufgaben, die feinmotorische Kontrolle erfordern – das Einstecken eines USB-Kabels, das Drehen eines Schlüssels im Schloss oder das Handhaben verformbarer Materialien – stoßen sie an ihre Grenzen. Der Grund liegt auf der Hand: Menschen nutzen für solche Aufgaben primär den Tastsinn, nicht das Sehen.

Trevor Darrell, Professor für Informatik an der University of California in Berkeley, bringt es auf den Punkt: "Die meisten geschickten Manipulationen können Menschen mit geschlossenen Augen durchführen." Das Verständnis von Kraft, Schlupf und präzisem Greifen lässt sich mit traditionellen visuellen Sensoren nicht zufriedenstellend erfassen.

## Modulare Experten statt Alleskönner

Hier setzt der modulare Ansatz an, den verschiedene Forschungsgruppen mittlerweile verfolgen. Darrells Team hat ein System entwickelt, das verschiedene spezialisierte Submodelle – sogenannte "Experten" – für unterschiedliche Aspekte einer Aufgabe einsetzt. Ein Experte übernimmt die hochrangigen Aktionen und Bewegungspläne, während ein taktiler Experte, der viermal schneller arbeitet, diese Pläne in Echtzeit basierend auf haptischem Feedback anpasst.

Diese Architektur löst ein grundlegendes Problem: Die Reaktionszeiten. Große VLA-Modelle arbeiten zu langsam, um taktile Signale sinnvoll zu nutzen. Ein Roboter, der eine Glühbirne einschraubt oder Zahnpasta auf eine Zahnbürste aufträgt, muss seine Bewegungen in Millisekunden anpassen können. Das gesamte Modell für solche Geschwindigkeiten zu optimieren wäre ineffizient – spezialisierte Module erlauben es, jedes für seine spezifische Aufgabe zu optimieren.

Die Ergebnisse sprechen für sich: Bei zwölf komplexen Manipulationsaufgaben erreichte das modulare System eine durchschnittliche Erfolgsquote von 65 Prozent – fast doppelt so viel wie das beste VLA-Modell.

## Die Herausforderung der Datenvielfalt

Ein wesentlicher Vorteil des modularen Ansatzes zeigt sich im Umgang mit Hardwareunterschiede. Roboterhände reichen von vollständig artikulierten fünffingrigen Designs bis zu einfachen Zangengreifern. Taktile Sensoren basieren auf grundlegend unterschiedlichen physikalischen Prinzipien – manche messen Widerstandsänderungen, andere zeichnen Bilder eines sich verformenden Gel-Pads auf.

Chengbo Yuan von der Tsinghua-Universität in Peking hat über 3.000 Stunden taktiler Roboterdaten aus öffentlich verfügbaren Datensätzen aggregiert, die 21 Sensortypen und verschiedene Roboter-Embodiments abdecken. Sein Team entwickelte ein hardware-agnostisches Modell, das auf diesen diversen Daten trainiert, indem es die Ausgaben jeder Sensortype in ein gemeinsames Format konvertiert und auf vordefinierten Positionen einer menschlichen Hand-Vorlage abbildet.

Das modulare Prinzip zeigt hier seine Stärke: Statt ein riesiges Modell auf allen möglichen Kombinationen von Hardware und Sensoren zu trainieren, können spezialisierte Module für verschiedene Sensortypen entwickelt und nach Bedarf ausgetauscht werden. Yuan führt den Erfolg darauf zurück, dass das System "eine Art gesunden Menschenverstand taktilen Wissens" durch das Training auf so unterschiedlichen Setups erwirbt.

## Praktische Vorteile der Modularität

Der modulare Ansatz bietet mehrere konkrete Vorteile gegenüber monolithischen Foundation Models:

**Effizienz beim Training**: Spezialisierte Module benötigen deutlich weniger Daten für ihre spezifische Aufgabe. Während Darrells Team nur 100 Stunden hochqualitativer taktiler Daten sammelte, würde ein universelles Modell möglicherweise um Größenordnungen mehr benötigen.

**Anpassungsfähigkeit**: Roboter können für verschiedene Aufgaben und Umgebungen durch Austausch oder Rekonfiguration von Modulen angepasst werden, ohne das gesamte System neu zu trainieren. Ein Restaurant-Roboter könnte die gleichen Basismodule wie ein Lager-Roboter nutzen, aber mit aufgabenspezifischen Experten kombinieren.

**Interpretierbarkeit**: Wenn ein modulares System versagt, lässt sich leichter identifizieren, welches Modul das Problem verursacht. Bei einem großen, monolithischen Modell ist die Fehleranalyse deutlich komplexer.

**Ressourceneffizienz**: Nicht jede Aufgabe erfordert die volle Rechenleistung eines großen Modells. Module können je nach Anforderung aktiviert werden, was Energie spart und Latenz reduziert.

## Die Datenfrage bleibt zentral

Trotz dieser Vorteile betonen Experten, dass Datenqualität und -quantität weiterhin entscheidend bleiben. NeoteAI, ein Spin-out der Fudan-Universität in Shanghai, hat bereits einen Datensatz produziert, der eine Größenordnung über bisherigen Bemühungen liegt: über 30.000 Stunden Demonstrationen mit synchronisierten visuellen und taktilen Daten.

Shunlin Lu, Postdoc-Forscher an der Fudan-Universität und CTO von NeoteAI, schätzt, dass möglicherweise 100.000 Stunden Daten nötig sein könnten, um neue Fähigkeiten freizuschalten – allerdings aus variablen, realen Umgebungen gesammelt statt aus dem Labor.

Hier zeigt sich ein weiterer Vorteil modularer Systeme: Daten können gezielter gesammelt werden. Statt zu versuchen, alle möglichen Szenarien in einem universellen Datensatz abzudecken, können für spezifische Module hochqualitative, fokussierte Datensätze erstellt werden.

## Die Rolle überraschender Signale

Long Cheng von der Chinesischen Akademie der Wissenschaften in Peking weist auf ein subtiles, aber bedeutendes Problem hin: Vision liefert einen kontinuierlichen, hochbandbreitigen Strom von Pixeln, während taktile Signale spärlich und intermittierend sind. Daher lernen Modelle, sie zu ignorieren.

Seine Lösung, die auf der IROS 2026 vorgestellt wird, verwendet ein Modell, das vorhersagt, was ein Roboter allein aufgrund visueller Information fühlen sollte, und vergleicht dies mit tatsächlichem taktilem Input. Eine große Diskrepanz bedeutet, dass der Sensor etwas erfasst, das der Roboter sonst übersehen würde – diese überraschenden Signale werden verstärkt, während vorhersagbare gedämpft werden.

Dieser Ansatz verkörpert ein Kernprinzip modularer Intelligenz: Verschiedene Informationsquellen optimal zu kombinieren, indem man ihre jeweiligen Stärken nutzt und Schwächen kompensiert.

## Ausblick: Komplementäre Strategien statt Entweder-oder

Die Debatte zwischen modularer und universeller Intelligenz muss nicht als Entweder-oder betrachtet werden. Wahrscheinlicher ist, dass beide Ansätze ihre Berechtigung haben und sich in der Praxis ergänzen werden.

Foundation Models könnten die Basis bilden – sie liefern grundlegendes Weltwissen, Sprachverständnis und visuelle Verarbeitung. Darauf aufbauend könnten spezialisierte Module für haptisches Feedback, Kraftregelung oder domänenspezifische Aufgaben die Fähigkeiten für konkrete Anwendungen verfeinern.

General Robotics' Wette auf modulare Intelligenz ist weniger eine Ablehnung großer Modelle als vielmehr eine pragmatische Antwort auf die Anforderungen realer Robotik-Anwendungen. In einer Welt, in der Roboter in Fabriken, Krankenhäusern, Restaurants und Haushalten arbeiten sollen, könnte die Fähigkeit, spezialisierte Fähigkeiten flexibel zu kombinieren, wichtiger sein als ein einzelnes, alles beherrschendes Modell.

Die kommenden Jahre werden zeigen, welcher Ansatz sich in der Praxis durchsetzt – oder ob, wie so oft in der Technologiegeschichte, eine hybride Lösung den größten Erfolg verspricht.
