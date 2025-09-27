# Visual Arts and Paintings Open Data (VAPOD)

## Descrizione

Dataset estratto da Wikidata contenente i metadati descrittivi di dipinti appartenenti all'arco temporale circoscritto tra il 1400 e il 1999.

## Endpoint

Wikidata Query Service: https://query.wikidata.org/

## Query di estrazione

### 1400-1499

```sparql
SELECT ?item ?title (YEAR(?date) AS ?year) ?genreLabel ?creatorLabel ?countryLabel ?subjectLabel ?depictsLabel ?collectionLabel ?movementLabel ?materialLabel ?width ?height ?commissionerLabel ?creatorSexLabel ?collectionOwnerLabel ?commissionerSexLabel
WHERE
{
  ?item wdt:P31 wd:Q3305213 .
  ?item wdt:P1476 ?title .
  ?item wdt:P571 ?date .
  ?item wdt:P136 ?genre .
  ?item wdt:P17 ?country .
  ?item wdt:P921 ?subject .
  ?item wdt:P180 ?depicts .
  ?item wdt:P2049 ?width .
  ?item wdt:P2048 ?height .
  ?item wdt:P186 ?material .
  
  OPTIONAL { ?item wdt:P195 ?collection . ?collection wdt:P127 ?collectionOwner . }
  OPTIONAL { ?item wdt:P135 ?movement . }
  OPTIONAL { ?item wdt:P170 ?creator . ?creator wdt:P21 ?creatorSex . }
  OPTIONAL { ?item wdt:P88 ?commissioner . ?commissioner wdt:P21 ?commissionerSex . }
  
  FILTER(LANG(?title) = "en")
  FILTER(YEAR(?date) >= 1400 && YEAR(?date) < 1500)
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "it". }
}
```