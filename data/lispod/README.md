# Library Science Publications Open Data (LiSPOD)

## Descrizione

Dataset estratto da Wikidata contenente i metadati descrittivi di pubblicazioni scientifiche italiane.

## Endpoint

Legacy Wikidata Query Service: https://query-legacy-full.wikidata.org/

## Query di estrazione

### Titoli

```sparql
SELECT DISTINCT ?id ?titolo
WHERE {
  ?id wdt:P31 wd:Q13442814;
      wdt:P1433 ?journal;
      rdfs:label ?titolo.
  ?journal wdt:P17 wd:Q38.
  FILTER(LANG(?titolo) = "it")
}
```

### Date

```sparql
SELECT DISTINCT ?id (GROUP_CONCAT(DISTINCT ?data; SEPARATOR=" | ") AS ?data_pubblicazione)
WHERE {
  ?id wdt:P31 wd:Q13442814;
      wdt:P1433 ?journal;
      rdfs:label ?titolo.
  ?journal wdt:P17 wd:Q38.
  OPTIONAL {
    ?id wdt:P577 ?pubDate.
    BIND(YEAR(?pubDate) AS ?data)
  }
  FILTER(LANG(?titolo) = "it")
}
GROUP BY ?id
```

### Riviste

```sparql
SELECT DISTINCT ?id ?rivista
WHERE {
  ?id wdt:P31 wd:Q13442814;
      wdt:P1433 ?journal;
      rdfs:label ?titolo.
  ?journal wdt:P17 wd:Q38.
  OPTIONAL {
    ?journal rdfs:label ?rivista.
    FILTER(LANG(?rivista) = "it")
  }
  FILTER(LANG(?titolo) = "it")
}
```

### Licenze

```sparql
SELECT DISTINCT ?id (GROUP_CONCAT(DISTINCT ?licenza; SEPARATOR="; ") AS ?licenze_rivista)
WHERE {
  ?id wdt:P31 wd:Q13442814;
      wdt:P1433 ?journal;
      rdfs:label ?titolo.
  ?journal wdt:P17 wd:Q38.
  OPTIONAL {
    ?journal wdt:P275 ?copyright .
    ?copyright rdfs:label ?licenza.
    FILTER(LANG(?licenza) = "en")
  }
  FILTER(LANG(?titolo) = "it")
}
GROUP BY ?id
```

### Autori

```sparql
SELECT ?id (GROUP_CONCAT(CONCAT(?autore, " (", ?sesso, ")"); SEPARATOR="; ") AS ?autori)
WHERE {
  ?id wdt:P31 wd:Q13442814;
      wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38.
  FILTER(LANG(?title) = "it")
  OPTIONAL {
      ?id wdt:P50 ?author .
      ?author rdfs:label ?autore .
      FILTER(LANG(?autore) = "it")
      OPTIONAL {
        ?author wdt:P21/rdfs:label ?sesso .
        FILTER(LANG(?sesso) = "it")
      }
  }
}
GROUP BY ?id
```

### Argomenti

```sparql
SELECT DISTINCT ?id (GROUP_CONCAT(DISTINCT ?argomento; SEPARATOR="; ") AS ?argomenti)
WHERE {
  ?id wdt:P31 wd:Q13442814;
      wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38.
  OPTIONAL {
    ?id wdt:P921 ?topic .
    ?topic rdfs:label ?argomento.
    FILTER(LANG(?argomento) = "it")
  }
  FILTER(LANG(?title) = "it")
}
GROUP BY ?id
```

### Pagine

```sparql
SELECT DISTINCT ?id (GROUP_CONCAT(?pages; SEPARATOR="; ") AS ?pagine)
WHERE {
  ?id wdt:P31 wd:Q13442814;
      wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38;
  OPTIONAL {
    ?id wdt:P304 ?pages .
  }
  FILTER(LANG(?title) = "it")
}
GROUP BY ?id
```

### Edizione

```sparql
SELECT DISTINCT ?id ?edizione
WHERE {
  ?id wdt:P31 wd:Q13442814;
      wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38.
  OPTIONAL {
    ?id wdt:P433 ?edizione .
  }
  FILTER(LANG(?title) = "it")
}
```

### Volume

```sparql
SELECT DISTINCT ?id ?volume
WHERE {
  ?id wdt:P31 wd:Q13442814;
      wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38.
  OPTIONAL {
    ?id wdt:P478 ?volume .
  }
  FILTER(LANG(?title) = "it")
}
```

### Editori

```sparql
SELECT DISTINCT ?id (GROUP_CONCAT(DISTINCT ?editore; SEPARATOR="; ") AS ?editori)
WHERE {
  ?id wdt:P31 wd:Q13442814;
      wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38.
  OPTIONAL {
    ?journal wdt:P123 ?publisher .
    ?publisher rdfs:label ?editore.
    FILTER(LANG(?editore) = "it")
  }
  FILTER(LANG(?title) = "it")
}
GROUP BY ?id
```

### Indici

```sparql
SELECT DISTINCT ?id (GROUP_CONCAT(DISTINCT ?dbLabel; SEPARATOR="; ") AS ?basi_dati)
WHERE {
  ?id wdt:P31 wd:Q13442814;
      wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38.
  OPTIONAL {
    ?journal wdt:P8875 ?indexedIn.
    ?indexedIn rdfs:label ?dbLabel.
    FILTER(LANG(?dbLabel) = "it")
  }
  FILTER(LANG(?title) = "it")
}
GROUP BY ?id
```

### URL

```sparql
SELECT DISTINCT ?id (GROUP_CONCAT(DISTINCT ?url; SEPARATOR="; ") AS ?url_disponibili)
WHERE {
  ?id wdt:P31 wd:Q13442814;
      wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38.
  OPTIONAL {
    ?id wdt:P953 ?url.
  }
  FILTER(LANG(?title) = "it")
}
GROUP BY ?id
```

### DOI

```sparql
SELECT DISTINCT ?id (GROUP_CONCAT(DISTINCT ?doi; SEPARATOR="; ") AS ?doi_disponibili)
WHERE {
  ?id wdt:P31 wd:Q13442814;
      wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38;
           wdt:P31 ?tipo_journal.
  OPTIONAL {
    ?id wdt:P356 ?doi.
  }
  FILTER(LANG(?title) = "it")
}
GROUP BY ?id
```