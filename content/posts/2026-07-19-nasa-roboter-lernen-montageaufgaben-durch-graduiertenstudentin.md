---
title: NASA-Roboter lernen Montageaufgaben durch Graduiertenstudentin
date: '2026-07-19T09:24:02+02:00'
draft: false
tags:
- NASA
- Weltraumrobotik
- Montageautomatisierung
categories:
- Forschung
summary: Wie eine Doktorandin NASA-Robotern fortgeschrittene Montagefähigkeiten beibringt
  und damit die Zukunft autonomer Weltraummissionen mitgestaltet - ein Einblick in
  die Verbindung von akademischer Forschung und Raumfahrttechnologie
ShowToc: true
TocOpen: false
---

Die Robotik steht vor einer ähnlichen Revolution, wie sie die künstliche Intelligenz mit großen Sprachmodellen erlebt hat. Während GPT und ähnliche Systeme durch massives Vortraining auf breiten Datensätzen zu generalistischen Fähigkeiten gelangten, suchte die Robotik bislang vergeblich nach einem vergleichbaren Rezept. Zu lange bestand die Automatisierung aus isolierten Modulen für Wahrnehmung, Planung und Steuerung – Komponenten, die selten zu einer Intelligenz verschmolzen, die von einer Aufgabe zur nächsten oder von einem Roboter zum anderen übertragbar wäre. Doch nun formiert sich ein vielversprechender Ansatz, der zeigt, wie eine integrierte Architektur die Zukunft autonomer Systeme prägen könnte.

## Der Systemansatz: Mehr als die Summe der Teile

Das chinesische Unternehmen X Square Robot verfolgt eine ungewöhnlich explizite Strategie. Statt auf ein einzelnes übergreifendes Modell zu setzen, entwickelt das Unternehmen einen integrierten Stack, der drei zentrale Ebenen miteinander verbindet: die Datengrundlage, aus der Roboter lernen, ein Weltmodell zur Vorhersage physikalischer Veränderungen und ein Aktionsmodell, das Wahrnehmung, Planung, Entscheidungsfindung und ausführbares Roboterverhalten vereint.

Was diesen Ansatz zusammenhält, sind nicht komplexe Algorithmen, sondern drei grundlegende Prinzipien. Erstens: Die elementare Einheit von Roboterdaten ist eine Interaktion, keine Trajektorie. Eine Demonstration gilt nur dann als erfolgreich, wenn sie die Welt wie beabsichtigt verändert – nicht einfach, weil sich Gelenke bewegt haben. Zweitens: Das Vortraining sollte bereits nutzbare Fähigkeiten hervorbringen, nicht nur eine Initialisierung für späteres Feintuning. Drittens: Verhalten sollte um physikalische Ereignisse herum modelliert werden, nicht um feste Zeitscheiben.

Diese Prinzipien machen die Schichten voneinander abhängig. Die roboterfreien Daten, die das Aktionsmodell trainieren, sind gleichzeitig so strukturiert, dass sie das Weltmodell speisen. Beide Modelle werden als komplementäre, aber unabhängige Modellfamilien beschrieben, die eine gemeinsame Codebasis teilen und Teil des breiteren "World Unified Model" sind – einer Architektur zum gemeinsamen Training von Vision, Sprache, Aktion und physikalischer Vorhersage.

## Datenqualität statt Datenmenge

Eine der größten Einschränkungen für Allzweckroboter ist nicht die Anzahl der Parameter, sondern die Kosten und Qualität von Interaktionsdaten. X Square Robot hat dafür ein System zur Datenerfassung entwickelt, das auf einem innovativen Ansatz basiert: Menschen tragen einen Aufbau mit zwei Greifern und demonstrieren Aufgaben direkt, ohne einen Roboter fernzusteuern.

Das klingt zunächst nicht revolutionär, doch die Umsetzung macht den Unterschied. Der entscheidende Schritt ist die Qualitätskontrolle durch physische Wiedergabe. Eine Stichprobe der aufgezeichneten Trajektorien wird auf dem echten Roboter abgespielt, und nur diejenigen, die die Aufgabe tatsächlich vollenden, gelten als gültig. Die Validitätsrate wird damit zu einer messbaren Größe statt einer Annahme. Ein Greifer, der eine Sekundenbruchtel zu früh schließt, sieht in den Daten wie ein Griff aus – doch physisch hat er das Objekt weggeschoben. Solche Fehler würden ohne Überprüfung ins Training einfließen und Mehrdeutigkeit statt Geschicklichkeit lehren.

Die Kombination aus kostengünstigen menschlichen Demonstrationen und knappen Roboterdaten folgt einer klaren Strategie: Vortraining auf einem großen Volumen roboterfreier Demonstrationen baut allgemeine Repräsentationen auf, dann verankert eine kleine Menge echter Roboterdaten das Modell in der Dynamik der spezifischen Maschine. Das Unternehmen berichtet von einer Leistung, die mit einem reinen Roboterdatensatz vergleichbar ist – bei etwa zwanzigfach niedrigeren Erfassungskosten. Der resultierende Datensatz ist bewusst modellunabhängig formatiert und kann sowohl Aktions- als auch Weltmodelle speisen.

## Ereignisse statt Zeitfenster

Das Weltmodell WALL-WM von X Square Robot verfolgt einen differenzierten Ansatz. Die meisten Aktionsmodelle sagen aus dem aktuellen Bild und der Anweisung einen Bewegungsabschnitt fester Länge voraus. Das ist praktisch, segmentiert aber Verhalten in zeitlich fixierte Fenster, deren Grenzen fallen, wo die verstrichene Zeit es vorgibt – nicht dort, wo eine Aktion endet und die nächste beginnt.

WALL-WM behandelt stattdessen ein aktionsbasiertes semantisches Ereignis als seine Einheit: ein kohärentes Verhaltensstück wie Greifen, Fassen oder Platzieren – etwas, das in Sprache benannt, in Video gesehen und als Bewegung ausgeführt werden kann. Das Design reflektiert eine spezifische Sorge: nicht zu verwerfen, was große Videomodelle bereits wissen. Um das zu erreichen, wird ein Text-zu-Video-Modell mit einem frisch initialisierten Aktionsnetzwerk gekoppelt, das aus den Videomerkmalen liest, ohne sie zu überschreiben.

Aus diesem einen Prozess ergeben sich zwei Modi. Ein Ereignismodus läuft in variabel langen Segmenten und eignet sich für Überlegungen über lange Horizonte, während ein Modus fester Länge die stetige Echtzeitausgabe produziert, die ein Controller benötigt. Das positioniert WALL-WM zwischen üblichen chunk-basierten Aktionsmodellen und reinen Video-Weltmodellen – es behält den prädiktiven Charakter eines Weltmodells bei und liefert dennoch ausführbare Steuerung.

## Bedeutungsvolle Aktions-Tokens

Die Aktionsschicht trägt zwei verbundene Ideen. Die erste ist eine Anforderung, die sich das Unternehmen selbst setzt: Das vortrainierte Modell sollte auf einem echten Roboter laufen, bevor jegliches aufgabenspezifisches Feintuning stattfindet. Das Interesse liegt weniger in den Punktzahlen als im dahinterliegenden Design. Das Modell trainiert drei Ziele gemeinsam: diskrete Aktions-Tokens, Sprachverankerung und kontinuierliche Aktionsgenerierung. Dabei lässt es Gradienten durch alle hindurchfließen, statt Teile des Netzwerks einzufrieren.

Die zweite Idee ist die Aktionsschnittstelle selbst, genannt X-Tokenizer. Die meisten Systeme, die kontinuierliche Bewegung in diskrete Tokens übersetzen, produzieren Codes, die das Sprachmodell nicht interpretieren kann. X-Tokenizer rahmt die Tokenisierung als Lernen einer semantischen Schnittstelle neu, sodass der Code auf oberster Ebene für die Absicht einer Bewegung steht, während Codes niedrigerer Ebene feinere Details tragen – alle ausgerichtet auf die eigenen Merkmale des Sprachmodells.

Eine nützliche Konsequenz ist Stabilität. Das Hinzufügen von Rauschen zu einer Aktion bewegt den Absichtscode kaum, was es ermöglicht, einen Tokenizer über Roboter hinweg wiederzuverwenden, ohne ihn neu abzustimmen. Zusammen geben die beiden Ideen der Aktionsschicht etwas ziemlich Mächtiges: Fähigkeit, die übertragbar ist.

## Die Bewährungsprobe: Von der Forschung zur Praxis

X Square Robot setzt darauf, dass sein einzigartiger Ansatz sich von anderen Architekturen für verkörperte KI abheben wird. Der physische Wiedergabeschritt, der Datenqualität verankert, ist ungewöhnlich und sinnvoll. Die Neuformulierung der Weltmodellierung um Ereignisse herum, mit einem Rückgrat, das sowohl Überlegung als auch Steuerung dient, ist ein wirklich eigenständiger Ansatz. Und die Paarung eines einsetzbaren Vortrainingsstandards mit einem als semantische Schnittstelle konzipierten Tokenizer verleiht der Aktionsschicht ungewöhnliche Kohärenz.

Die nächste Phase wird eine breitere Validierung bringen. Ein Großteil der aktuellen Evidenz stammt von X Square Robots eigenen Robotern und Benchmarks. Mit der nun öffentlich gemachten Weltmodell-Code werden die berichteten Fähigkeiten über mehr Roboter, Aufgaben und Umgebungen hinweg getestet werden.

Die jüngsten Finanzierungsrunden des Unternehmens spiegeln ähnliches Vertrauen wider. Die Bewertung ist auf über 20 Milliarden Yuan (etwa 2,9 Milliarden US-Dollar) geklettert, was darauf hindeutet, dass Investoren Dateninfrastruktur, Grundlagenmodelle und skalierbare Trainingssysteme zunehmend als langfristige Differenzierungsmerkmale in der verkörperten KI betrachten.

## Die fehlende Zutat für den Alltag

Trotz aller Fortschritte fehlt noch eine entscheidende Fähigkeit, bevor Roboter in Haushalten zuverlässig werden können: robuste Fehlerbehandlung. Benchmarks messen Kompetenz – ob ein Modell eine Aufgabe beenden kann. Haushalte erfordern Zuverlässigkeit: sicheren und konsistenten Betrieb über Zeit in einer Umgebung, die sich täglich ändert.

Das fehlende Puzzleteil ist nicht eine höhere einmalige Erfolgsrate, sondern die Fähigkeit zur Wiederherstellung. Ein zuverlässiger Haushaltsroboter muss wissen, wann er unsicher ist, wann er verlangsamen, wann er um Hilfe bitten sollte und wie er die Welt nach einem Fehler in einen sicheren Zustand zurückbringt. In einem echten Haushalt ist die Fehlerbehandlung wichtiger als roher Erfolg, weil sich der Haushalt nicht selbst zurücksetzt.

Die Veröffentlichung der Komponenten als Open Source zeigt, dass X Square Robot den längeren Weg wählt: Verkörperte Intelligenz kann nicht von einer Organisation allein gelöst werden. Sie braucht viele Verkörperungen, viele reale Aufgaben und breites Feedback. Das langfristige Ziel ist ein Stack, der weiterlernt und Roboter letztlich von Labordemonstration zu zuverlässiger Alltagsnutzung führt.
