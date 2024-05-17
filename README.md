# Driftende waterstofisotopen in ITER
_Idse Bayu Tromp_

De wanden van kernfusiereactoren als ITER worden gebombardeerd door hete deeltjes uit het plasma. Dit komt doordat het magneetveld met 1/r afneemt, waarbij r de afstand is t.o.v. het midden van de reactor. Deze afname zorgt ervoor dat de ladingen in het plasma een minder grote lorentzkracht ondervinden Bij deze simulatie is geprobeerd om ITER zo goed mogelijk na te maken, d.m.v. bijvoorbeeld het gebruiken van de echte straal en magneetveld van de reactor. Desalniettemin is het niet gelukt om drift te zien te krijgen bij een toroïdaal magneetveld. M.b.v. Excel is gekeken naar of er wellicht wel drifts optreden die niet goed zichtbaar zijn doordat de drift erg klein is. Hoewel hieruit voort kwam dat er wel een soort van drift optreet, komt dit niet door een goed werkend model, maar door een (te) grote tijdsstapgrootte. Door het model wat aan te passen is geprobeerd om het effect van de drifts groter te maken (nl. B = basevalue \* 1/r veranderen naar B = basevalue \* 1/(r^4)), ook dit mocht echter niet baten.

Het is wel gelukt om drifts te zien te krijgen bij een linear magneetveld.

## Afbeeldingen

Bij het project zitten enkele afbeeldingen van resultaten van het model. _linearDrifts_ laat drifts zien van deeltjes (twee met positieve lading, één met negatieve lading) in een linear veld. _toroidalPandT_ toont hoe een proton (H-1-kern) (paars) en een tritiumkern (rood) een ander pad volgen door hun verschil in lading en massa, ondanks dat ze in hetzelfde punt beginnen.

De afbeeldingen _WhatN_ laten zien dat het leven van een programmeur niet makkelijk is.

## Referenties

Voor de gegevens van ITER is gebruikgemaakt van de volgende bron: \
ITER. (n.d.). _Magnets._ <https://www.iter.org/mach/Magnets>

Verder is benoemingswaardig dat de Geachte Dr.ir. M.F.M. Steenbakkers mij meerdere malen buiten lestijden om de tijd heeft genomen om mij de wiskunde uit te leggen en op het juiste pad te sturen.
