# Library Science Publications Open Data (LiSPOD)

## Descrizione

Dataset estratto da Wikidata contenente i metadati descrittivi di pubblicazioni scientifiche che a partire dal 2000 hanno affrontato tematiche inerenti alla biblioteconomia e alla scienza dell'informazione.

## Endpoint

Scholarly Wikidata Query Service: https://query-scholarly.wikidata.org/

## Query di estrazione

```sparql
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wd: <http://www.wikidata.org/entity/>


SELECT ?item ?title (YEAR(?pubDate) AS ?date) ?authorLabel ?langLabel ?sexLabel ?countryLabel ?employerLabel ?journalLabel (YEAR(?journalDate) AS ?journalInception) ?publisherLabel ?dbLabel ?topicLabel ?workTitle ?volume ?issue ?pages
WHERE {
  {
    ?item wdt:P921 wd:Q13420675 .
  }
  UNION
  {
    ?item wdt:P921 wd:Q199655 .
  }
  UNION
  {
    ?item wdt:P921 wd:Q16387 .
  }
  UNION
  {
    ?item wdt:P921 wd:Q4027615 .
  }
  UNION
  {
    ?item wdt:P921 wd:Q180160 .
  }
  ?item wdt:P1476 ?title .
  ?item wdt:P577 ?pubDate .
  ?item wdt:P1433 ?journal .
  ?item wdt:P921 ?topic .
  ?item wdt:P478 ?volume .
  ?item wdt:P433 ?issue .
  ?item wdt:P304 ?pages .
  ?item wdt:P50 ?author .
  ?item wdt:P407 ?lang .
  
  OPTIONAL { ?item wdt:P2860 ?work . ?work wdt:P1476 ?workTitle . }
  
  FILTER(YEAR(?pubDate) >= 2000)
    
  SERVICE wdsubgraph:wikidata_main {
    ?author rdfs:label ?authorLabel .
    ?author wdt:P21 ?sex .
    ?author wdt:P27 ?country .
    ?sex rdfs:label ?sexLabel .
    ?topic rdfs:label ?topicLabel .
    ?country rdfs:label ?countryLabel .
    ?journal rdfs:label ?journalLabel .
    ?journal wdt:P123 ?publisher .
    ?publisher rdfs:label ?publisherLabel .
    
    ?lang rdfs:label ?langLabel .
    OPTIONAL { ?author wdt:P108 ?employer . ?employer rdfs:label ?employerLabel . }
    OPTIONAL { ?journal wdt:P571 ?journalDate . }
    OPTIONAL { ?journal wdt:P8875 ?indexedIn . ?indexedIn rdfs:label ?dbLabel . }
    
    FILTER(LANG(?authorLabel) = "en")
    FILTER(LANG(?sexLabel) = "it")
    FILTER(LANG(?employerLabel) = "en")
    FILTER(LANG(?journalLabel) = "en")
    FILTER(LANG(?publisherLabel) = "en")
    FILTER(LANG(?dbLabel) = "en")
    FILTER(LANG(?topicLabel) = "it")
    FILTER(LANG(?countryLabel) = "it")
    FILTER(LANG(?langLabel) = "it")
  }
}
```