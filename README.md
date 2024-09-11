# Sorteringsverktøyet
Persiske tepper er utrolig fine og veldige spesielle. Noe av det som gjør dem veldig spesielle er at hvert teppe er håndknyttet og unikt. Dette er noe av årsaken til at de er så verdifulle, men samtidig er det også en årsak til at det kan være vanskelig å finne dem (spesielt om du du er en teppeforhandler med 100-vis av persiske tepper). 

Motivasjonen bak dette prosjektet har vært å gjøre det enklere for deltidsansatte/sommervikarer å finne frem tepper i min familie sin teppeforetning. Tanken er at man skal kunne få opplysninger fra en intressent(hovedsakelig pris og størrelse) og basert på dette finne frem potensielle tepper som kan passe.

I tillegg til å kunne hjelpe familieforetningen ønsket jeg å lære meg et nytt rammeverk og lære mer om webutvikling. 


---

## Data

For å få denne ideen til å realiseres har jeg brukt data om tepper som er lastet opp på nettsiden til foretningen. Shopify har en funksjon hvor man kan laste ned produktene som CSV. Selv om dette var veldig fint, var det det 2 hovedutfordringer som måtte løses: 1. Hvordan skal man overføre produktene fra CSV-filen til Django sin ORM/Database og 2. Hvordan rengjøre CSV-filen? Denne utfordringen høres kanskje litt rar ut, men det var nemlig slik at det fantes veldig mange duplikater av samme produkt pga. hvordan de hadde blitt lagt til i Shopify. I tillegg var ikke størrelsen en egen kolonne, men den var heldigvis utledbar fra tittilen til produktet (selv om formatet ikke var gjevnt tvers over linja)

---

Opprinnelig var prosjektet hostet på en Linux-server gjennom OceanCloud, men nå kjøres det på localhost når det brukes og jeg har derfor laget en kort videodemonstrasjon for å vise hvordan nettsiden fungerer.

[Video Demo](youtube.com) // kommer snart



