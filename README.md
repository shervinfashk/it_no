# Sorteringsverktøyet

Persiske tepper er utrolig vakre og svært spesielle. Noe av det som gjør dem unike er at hvert teppe er håndknyttet og derfor helt unikt. Dette bidrar til deres høye verdi, men samtidig gjør det dem også vanskeligere å finne – spesielt hvis du er en teppeforhandler med hundrevis av persiske tepper.

Motivasjonen bak dette prosjektet har vært å gjøre det enklere for deltidsansatte og sommervikarer å finne frem tepper i min families teppeforretning. Målet er at man skal kunne få opplysninger fra en interessent (hovedsakelig pris og størrelse) og basert på disse finne frem til potensielle tepper som kan passe.

I tillegg til å hjelpe familieforretningen, ønsket jeg også å lære meg et nytt rammeverk og utforske mer om webutvikling.

---

## Data

For å realisere denne ideen har jeg brukt data om tepper som er lastet opp på forretningens nettside. Shopify har en funksjon som lar deg laste ned produktene som en CSV-fil. Selv om dette var veldig nyttig, møtte jeg to hovedutfordringer:

1. Hvordan overføre produktene fra CSV-filen til Djangos ORM/database?
2. Hvordan rengjøre CSV-filen?

Den andre utfordringen kan virke litt spesiell, men det var mange duplikater av produkter på grunn av måten de var lagt til i Shopify. I tillegg var ikke teppets størrelse en egen kolonne, men heldigvis kunne den utledes fra produktets tittel, selv om formatet ikke var konsekvent.

---

Opprinnelig ble prosjektet hostet på en Linux-server via DigitalOcean, men nå kjøres det på localhost når det brukes. Jeg har derfor laget en kort videodemonstrasjon som viser hvordan nettsiden fungerer.

[Video Demo](youtube.com) // kommer snart
