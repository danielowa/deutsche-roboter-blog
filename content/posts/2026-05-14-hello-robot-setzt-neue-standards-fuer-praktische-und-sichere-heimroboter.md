---
title: Hello Robot setzt neue Standards für praktische und sichere Heimroboter
date: '2026-05-14T09:38:22+02:00'
draft: false
tags:
- Serviceroboter
- Heimroboter
- Robotersicherheit
categories:
- Forschung
summary: Analyse wie Hello Robot mit seinem Stretch-Roboter den Spagat zwischen Forschungsplattform
  und alltagstauglichem Heimroboter meistert - ein Blick auf Design-Philosophie, Sicherheitskonzepte
  und die Vision bezahlbarer Serviceroboter für zu Hause
ShowToc: true
TocOpen: false
---

Die Robotik für den Heimbereich durchläuft gerade einen bemerkenswerten Paradigmenwechsel. Während humanoidale Roboter mit Beinen und menschenähnlichen Händen derzeit viel Aufmerksamkeit und immense Investitionssummen anziehen, verfolgt das kalifornische Startup Hello Robot einen radikal pragmatischeren Ansatz. Mit dem Stretch-Roboter, dessen vierte Generation jetzt vorgestellt wurde, demonstriert das Unternehmen, dass der Traum vom Heimroboter nicht zwingend auf zwei Beinen gehen muss – und möglicherweise gerade deshalb realistischer ist als je zuvor.

## Minimalismus als Designphilosophie

Hello Robot wurde von Aaron Edsinger und Charlie Kemp gegründet, zwei Robotikexperten mit jahrzehntelanger Erfahrung – auch im Bereich humanoider Systeme. Ihre bewusste Entscheidung gegen die Komplexität humanoider Roboter und für ein minimalistisches Design ist keine technische Kapitulation, sondern eine strategische Fokussierung auf das Wesentliche: Mobilität und Manipulation.

"Wir haben das Unternehmen auf der Grundlage gegründet, einfache, minimalistische Roboter zu bauen", erklärt Kemp. "Jedes Mal, wenn wir Komplexität hinzufügten, war das eine emotionale Herausforderung." Diese Philosophie resultierte in einem Roboter, der bewusst auf überflüssige Freiheitsgrade verzichtet und stattdessen die für Alltagsaufgaben wirklich notwendigen Funktionen optimiert.

Der Stretch 4 verfügt über eine omnidirektionale Basis, die es dem Roboter ermöglicht, sich in jede Richtung zu bewegen, ohne sich erst drehen zu müssen. Diese scheinbar simple Verbesserung gegenüber der Vorgängerversion macht die Bedienung deutlich intuitiver – besonders für unerfahrene Nutzer. Die technische Umsetzung war allerdings alles andere als trivial: Sechs Monate konzentrierter Entwicklungsarbeit waren nötig, um neu entwickelte Omnidirektionalräder aus dem Bereich motorisierter Rollstühle zu integrieren.

## Durchdachtes Sensorkonzept statt Sensorfülle

Der ausziehbare Arm des Stretch kann Gegenstände in verschiedenen Höhen erreichen, während ein neu gestalteter Sensorkopf für Wahrnehmung und Navigation sorgt. Anders als ursprünglich geplant, setzt Hello Robot nicht auf eine Vielzahl günstiger Kameras nach Tesla-Vorbild, sondern auf ein reichhaltigeres Sensor-Setup, das an Waymos Ansatz erinnert.

"Je reichhaltiger und zuverlässiger deine Daten sind, desto sicherer und intelligenter kann der Roboter sein", begründet Edsinger die Entscheidung. Der Sensorkopf vereint hemisphärische Lidare, Luxonis-Kameras für Vision und Navigation sowie eine am Handgelenk montierte Tiefenkamera für Manipulationsaufgaben. Die Rechenleistung liefert ein Intel NUC 15 als Hauptsystem, ergänzt durch einen Nvidia Jetson Orin NX für visuelle Verarbeitung und KI-Anwendungen.

## Der Mensch im Regelkreis

Die Autonomie-Philosophie von Hello Robot unterscheidet sich fundamental von vielen anderen Robotik-Unternehmen. Statt möglichst viele Daten zu sammeln in der vagen Hoffnung, daraus irgendwann kommerzielle Autonomie zu generieren, setzt das Unternehmen auf eine Kombination aus Basisautonomie und menschlicher Kontrolle.

Stretch 4 wird mit grundlegenden autonomen Fähigkeiten ausgeliefert: Kartierung, Navigation, selbstständiges Aufladen und demonstrationsreife Funktionen wie autonomes Greifen. Die Kontrolle durch den Menschen kann dabei von direkter Steuerung bis zu rein überwachender Kontrolle reichen. "Ich würde viel lieber die Plattform sein, die Foundation-Model-Entwickler anvisieren", sagt Kemp und positioniert Stretch damit als Hardwareplattform für andere Entwickler, statt selbst in den KI-Wettlauf einzusteigen.

## Praxistest mit klarer Zielgruppe

Während frühere Versionen primär als Forschungsplattformen konzipiert waren, wurde Stretch 4 explizit für Pilotprojekte in den Wohnungen von Menschen mit schweren Mobilitätseinschränkungen entwickelt. Diese Ausrichtung ist mehr als nur eine Marktnische – sie ist eine fundierte Entscheidung, die auf jahrelanger Zusammenarbeit mit Henry Evans basiert.

Evans ist gelähmt und kann nicht sprechen, nutzt jedoch seit etwa 15 Jahren Roboter als Assistenz in seinem Zuhause. Seine Perspektive auf humanoide Heimroboter ist ernüchternd: "Die Frage ist: Welchen Nutzen bietet ein zweibeiniger Roboter einer Person, die nicht laufen kann? Ihre gesamte Umgebung wurde für Rollstühle angepasst. Autos haben keine Beine, und Heimroboter sollten das auch nicht haben."

Evans weist auch auf praktische Sicherheitsaspekte hin: "Wenn ein Roboter auf Rädern gestoppt wird, friert er an Ort und Stelle ein. Wenn ein zweibeiniger Roboter gestoppt wird, stürzt er auf alles darunter, einschließlich des Patienten." Diese Beobachtung unterstreicht einen fundamentalen Vorteil nicht-humanoider Roboter im häuslichen Umfeld.

## Sicherheit durch Design, nicht durch Hoffnung

Kemp und Edsinger, beide mit umfangreicher Erfahrung im Bereich humanoider Robotik, teilen Evans' Bedenken. "Der Sicherheitsaspekt von Humanoiden in einem Zuhause beunruhigt mich", erklärt Kemp. "Ich verstehe nicht, wie jemand zuversichtlich über Sicherheit nachdenken kann bei einem Humanoiden zu Hause."

Stretch hingegen ist von Grund auf für Sicherheit konzipiert. Der niedrige Schwerpunkt, die stabile Radbasis und die inhärente Stabilität machen den Roboter vorhersehbar. Bei einem Notaus bleibt er einfach stehen – keine Sturzgefahr, keine unkontrollierten Bewegungen. Diese passive Sicherheit ist ein oft unterschätzter, aber entscheidender Vorteil gegenüber laufenden Systemen.

## Bezahlbarkeit als Markteintrittsbarriere senken

Mit einem Preis von 29.950 US-Dollar ist Stretch 4 für einen mobilen Manipulator außergewöhnlich erschwinglich. Das ist immer noch eine erhebliche Investition, aber sie liegt in einem Bereich, der für Forschungseinrichtungen, Unternehmen und mittelfristig auch für den Heimgebrauch realistisch ist.

Hello Robot plant, die Erkenntnisse aus den Pilotprojekten zu nutzen, um die nächste Generation – Stretch 5 – als kommerziell verkäufliches Assistenzsystem für den Heimbereich zu etablieren. Bei der bisherigen Entwicklungsgeschwindigkeit könnte das bereits innerhalb des nächsten Jahres Realität werden.

## Vision trifft auf Pragmatismus

Der Ansatz von Hello Robot könnte als Gegenentwurf zur aktuellen Robotik-Hysterie verstanden werden, ist aber vielmehr eine Rückbesinnung auf die Grundprinzipien erfolgreicher Robotik: Löse ein konkretes Problem mit der einfachsten möglichen technischen Lösung, und optimiere diese bis zur Perfektion.

Kemp bringt es auf den Punkt: "Es gibt Anwendungen, wo die menschliche Form fundamental ist. Aber für viele Anwendungen ist der Wert der menschlichen Form unklar oder sogar problematisch." Die strukturierten Innenräume, die wir bereits geschaffen haben, bieten Chancen, die verloren gehen, wenn man vorschnell zum Schluss kommt, dass Roboter humanoid sein müssen.

Stretch mag nicht wie Rosie aus den Jetsons aussehen, aber er verspricht etwas Wertvolleres: Er funktioniert, ist sicher, und er ist verfügbar. In einer Branche, die oft große Versprechen macht und selten liefert, könnte dieser pragmatische Ansatz genau der richtige Weg sein, um Heimroboter endlich aus dem Labor in unsere Wohnzimmer zu bringen.
