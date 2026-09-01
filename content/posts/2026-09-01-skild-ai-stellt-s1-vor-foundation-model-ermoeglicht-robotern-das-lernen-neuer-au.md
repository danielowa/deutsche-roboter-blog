---
title: 'Skild AI stellt S1 vor: Foundation Model ermöglicht Robotern das Lernen neuer
  Aufgaben durch Videos'
date: '2026-09-01T11:41:55+02:00'
draft: false
tags:
- Foundation Models
- Robot Learning
- Physical AI
categories:
- KI
summary: Analyse des S1 Foundation Models von Skild AI als potenzieller Durchbruch
  für robotisches Lernen - Vergleich mit bestehenden Ansätzen, technische Bewertung
  der Video-zu-Fähigkeit-Transformation und Einordnung in den aktuellen Wettlauf um
  Robot Foundation Models
ShowToc: true
TocOpen: false
---

Die Robotik steht vor einem fundamentalen Wandel: Während die Hardware längst beeindruckende Fortschritte gemacht hat, warten die mechanischen Körper noch immer auf intelligente Software, die mit der Flexibilität menschlicher Fähigkeiten mithalten kann. Skild AI will diese Lücke nun mit seinem Foundation Model S1 schließen – einem System, das Robotern ermöglichen soll, neue Aufgaben einfach durch das Betrachten von Videos zu erlernen. Die Ankündigung reiht sich ein in einen intensiven Wettlauf um das erste wirklich universelle "Gehirn" für Roboter.

## Das Versprechen: Lernen durch Zuschauen

Das Kernversprechen von Skild AIs S1-Modell klingt verlockend einfach: Ein Roboter sieht ein Video einer Tätigkeit und kann diese anschließend selbst ausführen. Diese Video-zu-Fähigkeit-Transformation würde einen Paradigmenwechsel bedeuten – weg von aufwändiger manueller Programmierung oder zeitintensivem Reinforcement Learning hin zu einem intuitiven Lernprozess, der dem menschlichen Lernen durch Beobachtung ähnelt.

Die Idee ist nicht völlig neu. Schon seit Jahren erforschen Wissenschaftler sogenannte Imitation-Learning-Ansätze, bei denen Roboter durch das Nachahmen menschlicher Demonstrationen lernen. Was S1 von früheren Ansätzen unterscheidet, ist der Anspruch, ein universelles Foundation Model zu sein – ähnlich wie GPT für Sprache, aber eben für physische Manipulation und Bewegung.

Foundation Models zeichnen sich dadurch aus, dass sie auf riesigen Datenmengen vortrainiert werden und dann mit verhältnismäßig wenig zusätzlichem Training für spezifische Aufgaben angepasst werden können. Im Kontext der Robotik bedeutet das: Ein einziges Modell soll unterschiedlichste Roboterplattformen steuern und vielfältige Aufgaben bewältigen können.

## Technische Herausforderungen der Video-Interpretation

Die Transformation von passivem Videomaterial in aktionsfähiges robotisches Wissen ist technisch deutlich komplexer, als es zunächst scheint. Ein Video zeigt lediglich eine zweidimensionale Projektion dreidimensionaler Bewegungen, oft aus einem einzigen Blickwinkel. Verdeckungen, Perspektivenverzerrungen und die fehlende Information über Kraftaufwand oder taktile Rückmeldung machen die Aufgabe anspruchsvoll.

Moderne Ansätze im Bereich Physical AI gehen deshalb zunehmend über einfache Videoaufnahmen hinaus. Wie aktuelle Entwicklungen zeigen, benötigen Frontier-Modelle für physische KI idealerweise multiple Kameraperspektiven, dichte Annotationen und möglicherweise sogar Gehirnwellenmessungen von Menschen während der Aufgabenausführung. Diese neurowissenschaftlichen Daten könnten Aufschluss über Aufmerksamkeitsfokus, Planungsintention und motorische Vorbereitung geben – Informationen, die aus reinem Videomaterial nicht extrahiert werden können.

Es ist unklar, inwieweit S1 auf solche erweiterten Datenquellen zurückgreift oder ob das Modell tatsächlich primär mit konventionellem Videomaterial arbeitet. Die Qualität und Diversität der Trainingsdaten wird letztlich entscheidend sein für die Generalisierungsfähigkeit des Systems.

## Der Entwicklungsstand: Robotik verlässt die "GPT-2-Ära"

Ein aufschlussreicher Vergleich zur Sprachmodell-Entwicklung hilft, den aktuellen Stand der Robot Foundation Models einzuordnen. Während Sprachmodelle mit GPT-4 und darüber hinaus bereits beeindruckende Fähigkeiten demonstrieren, befinden sich die meisten Robotik-Modelle noch in einer früheren Entwicklungsphase – vergleichbar mit der GPT-2-Ära der Sprachverarbeitung.

GPT-2 war bereits beeindruckend in seiner Textgenerierung, zeigte aber noch erhebliche Limitationen in Bezug auf Konsistenz, Faktentreue und komplexes Reasoning. Ähnlich verhält es sich mit aktuellen Robot Foundation Models: Sie zeigen vielversprechende Ansätze, scheitern aber oft noch an der Robustheit und Zuverlässigkeit, die für reale Anwendungen nötig wäre.

Der Sprung von GPT-2 zu GPT-3 und GPT-4 erforderte nicht nur mehr Rechenleistung und Daten, sondern auch architektonische Innovationen und bessere Trainingsmethoden. Für die Robotik steht ein ähnlicher Entwicklungssprung noch bevor. S1 könnte ein Kandidat sein, diesen Sprung zu schaffen – oder zumindest einen wichtigen Schritt in diese Richtung zu markieren.

## Hardware wartet auf Software

Ein bemerkenswerter Aspekt der aktuellen Situation ist die Asymmetrie zwischen Hardware- und Software-Entwicklung. Roboterhardware hat in den letzten Jahren enorme Fortschritte gemacht: Humanoide Roboter von Unternehmen wie Boston Dynamics, Tesla oder Figure AI demonstrieren beeindruckende mechanische Fähigkeiten, Geschicklichkeit und Bewegungsökonomie.

Doch diese ausgefeilten Körper warten noch immer auf intelligente Steuerungssoftware, die ihre Möglichkeiten voll ausschöpfen kann. Die Situation ähnelt einem Hochleistungssportler mit einem unterentwickelten Nervensystem – das Potenzial ist vorhanden, aber nicht nutzbar.

Foundation Models wie S1 könnten diese Lücke schließen, indem sie eine gemeinsame "kognitive Schicht" bereitstellen, die unterschiedliche Roboterplattformen steuern kann. Die Übertragbarkeit zwischen verschiedenen Roboterkörpern ist dabei eine Schlüsselfrage: Kann ein auf einem Roboterarm trainiertes Modell sein Wissen auf einen humanoiden Roboter übertragen? Wie gut generalisiert das Gelernte über unterschiedliche Kinematiken und Aktuatoren hinweg?

## Vergleich mit bestehenden Ansätzen

S1 tritt in ein zunehmend überfülltes Feld ein. Google DeepMind arbeitet an RT-2 und anderen robotischen Transformern, OpenAI hat in der Vergangenheit mit robotischen Systemen experimentiert, und zahlreiche Startups wie Covariant oder Physical Intelligence verfolgen ähnliche Ziele.

Was die verschiedenen Ansätze unterscheidet, sind vor allem die Trainingsdaten, die Modellarchitektur und die Zielhardware. Einige Systeme fokussieren sich auf spezifische Anwendungsbereiche wie Lagerlogistik oder Montageaufgaben, andere streben nach größerer Allgemeinheit.

Der Vorteil spezialisierter Modelle liegt in ihrer Zuverlässigkeit innerhalb eines definierten Aufgabenbereichs. Der Vorteil von Foundation Models wie S1 wäre ihre Flexibilität – vorausgesetzt, sie können das Versprechen der schnellen Anpassbarkeit einlösen.

## Kritische Bewertung und offene Fragen

Bei aller Begeisterung für die Ankündigung bleiben wichtige Fragen offen. Wie robust funktioniert S1 unter realen Bedingungen mit variierender Beleuchtung, unstrukturierten Umgebungen und unvorhergesehenen Störungen? Wie viele Videobeispiele benötigt das System tatsächlich, um eine neue Aufgabe zu erlernen? Und wie konsistent sind die Ergebnisse über verschiedene Versuche hinweg?

Die Geschichte der KI-Robotik ist voll von beeindruckenden Demonstrationen, die sich in kontrollierten Laborbedingungen als funktionsfähig erwiesen, aber bei der Übertragung in die reale Welt scheiterten. Die berühmte "Sim-to-Real-Gap" – die Diskrepanz zwischen simulierter und realer Umgebung – bleibt eine fundamentale Herausforderung.

Zudem stellt sich die Frage der Sicherheit: Ein System, das durch Videos lernt, könnte auch unerwünschte Verhaltensweisen aufnehmen. Welche Mechanismen stellen sicher, dass Roboter keine gefährlichen oder ethisch problematischen Aktionen ausführen?

## Ausblick: Der Weg zum universellen Robotergehirn

Die Entwicklung von Robot Foundation Models steht noch am Anfang, aber die Richtung ist klar. In den kommenden Jahren werden wir wahrscheinlich einen ähnlichen Wettlauf erleben wie bei den Large Language Models – mit schnell steigenden Modellgrößen, Leistungsfähigkeiten und Investitionen.

S1 von Skild AI ist ein interessanter Beitrag zu diesem Wettlauf. Ob es sich als Durchbruch erweist oder als weiterer Entwicklungsschritt in einer längeren Evolutionskette, wird sich in der praktischen Anwendung zeigen müssen. Die wahre Bewährungsprobe liegt nicht in kontrollierten Demonstrationen, sondern im täglichen Einsatz unter realen Bedingungen.

Eines ist jedoch sicher: Die Kombination aus immer leistungsfähigerer Hardware und zunehmend intelligenterer Software bringt uns der Vision universell einsetzbarer, lernfähiger Roboter näher. Die nächsten Jahre werden entscheidend sein für die Frage, ob Foundation Models tatsächlich das fehlende Puzzlestück sind, auf das die Robotik gewartet hat.
