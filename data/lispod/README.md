# Library Science Publications Open Data (LiSPOD)

## Descrizione

Dataset estratto da Wikidata contenente i metadati descrittivi di pubblicazioni scientifiche che a partire dal 2000 hanno affrontato tematiche inerenti alla biblioteconomia e alla scienza dell'informazione.

## Endpoint

Legacy Wikidata Query Service: https://query-legacy-full.wikidata.org/

## Query di estrazione

### Titoli

```sparql
SELECT DISTINCT ?id ?title
WHERE {
  ?id wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38;
           wdt:P31 ?tipo_journal.
  FILTER(?tipo_journal = wd:Q5633421 || ?tipo_journal = wd:Q737498 || ?tipo_journal = wd:Q773668)
  FILTER(LANG(?title) = "it")
}
```

### Date

```sparql
SELECT DISTINCT ?id (GROUP_CONCAT(DISTINCT ?data; SEPARATOR=" | ") AS ?datax)
WHERE {
  ?id wdt:P1433 ?journal;
      rdfs:label ?title.
  OPTIONAL {
    ?id wdt:P577 ?pubDate.
    BIND(YEAR(?pubDate) AS ?data)
  }
  ?journal wdt:P17 wd:Q38;
           wdt:P31 ?tipo_journal.
  FILTER(?tipo_journal = wd:Q5633421 || ?tipo_journal = wd:Q737498 || ?tipo_journal = wd:Q773668)
  FILTER(LANG(?title) = "it")
}
GROUP BY ?id
```

### Journal

```sparql
SELECT DISTINCT ?id ?journal_name 
WHERE {
  ?id wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38;
           wdt:P31 ?tipo_journal.
  FILTER(?tipo_journal = wd:Q5633421 || ?tipo_journal = wd:Q737498 || ?tipo_journal = wd:Q773668)
  OPTIONAL {
    ?journal rdfs:label ?journal_name.
    FILTER(LANG(?journal_name) = "it")
  }
  FILTER(LANG(?title) = "it")
}
```

### Licenze

```sparql
SELECT DISTINCT ?id (GROUP_CONCAT(DISTINCT ?licenza; SEPARATOR="; ") AS ?licenza_journal)
WHERE {
  ?id wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38;
           wdt:P31 ?tipo_journal.
  FILTER(?tipo_journal = wd:Q5633421 || ?tipo_journal = wd:Q737498 || ?tipo_journal = wd:Q773668)
  OPTIONAL {
    ?journal wdt:P275 ?copyright .
    ?copyright rdfs:label ?licenza.
    FILTER(LANG(?licenza) = "en")
  }
  FILTER(LANG(?title) = "it")
}
GROUP BY ?id
```

### Autori

```sparql
SELECT ?id (GROUP_CONCAT(DISTINCT ?autore_completo; SEPARATOR="; ") AS ?autori)
WHERE {
  ?id wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38;
           wdt:P31 ?tipo_journal.
  FILTER(?tipo_journal = wd:Q5633421 || ?tipo_journal = wd:Q737498 || ?tipo_journal = wd:Q773668)
  FILTER(LANG(?title) = "it")
  OPTIONAL {
    {
      ?id wdt:P50 ?a_item .
      ?a_item rdfs:label ?a_name_item .
      FILTER(LANG(?a_name_item) = "it")
      OPTIONAL {
        ?a_item wdt:P21/rdfs:label ?sex_item .
        FILTER(LANG(?sex_item) = "it")
      }
    }
    UNION
    {
      ?id wdt:P2093 ?a_name_str .
    }
  }
  BIND(COALESCE(?a_name_item, ?a_name_str) AS ?real_name)
  BIND(COALESCE(?sex_item, "N/D") AS ?real_sex)
  FILTER(BOUND(?real_name))
  BIND(CONCAT(?real_name, " (", ?real_sex, ")") AS ?autore_completo)
}
GROUP BY ?id
```

### Argomenti

```sparql
SELECT DISTINCT ?id (GROUP_CONCAT(DISTINCT ?argomento; SEPARATOR="; ") AS ?argomenti)
WHERE {
  ?id wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38;
           wdt:P31 ?tipo_journal.
  FILTER(?tipo_journal = wd:Q5633421 || ?tipo_journal = wd:Q737498 || ?tipo_journal = wd:Q773668)
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
SELECT DISTINCT ?id ?pagine
WHERE {
  ?id wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38;
           wdt:P31 ?tipo_journal.
  FILTER(?tipo_journal = wd:Q5633421 || ?tipo_journal = wd:Q737498 || ?tipo_journal = wd:Q773668)
  OPTIONAL {
    ?id wdt:P304 ?pagine .
  }
  FILTER(LANG(?title) = "it")
}
```

### Issue

```sparql
SELECT DISTINCT ?id ?issue
WHERE {
  ?id wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38;
           wdt:P31 ?tipo_journal.
  FILTER(?tipo_journal = wd:Q5633421 || ?tipo_journal = wd:Q737498 || ?tipo_journal = wd:Q773668)
  OPTIONAL {
    ?id wdt:P433 ?issue .
  }
  FILTER(LANG(?title) = "it")
}
```

### Volume

```sparql
SELECT DISTINCT ?id ?volume
WHERE {
  ?id wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38;
           wdt:P31 ?tipo_journal.
  FILTER(?tipo_journal = wd:Q5633421 || ?tipo_journal = wd:Q737498 || ?tipo_journal = wd:Q773668)
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
  ?id wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38;
           wdt:P31 ?tipo_journal.
  FILTER(?tipo_journal = wd:Q5633421 || ?tipo_journal = wd:Q737498 || ?tipo_journal = wd:Q773668)
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
SELECT DISTINCT ?id (GROUP_CONCAT(DISTINCT ?dbLabel; SEPARATOR="; ") AS ?indici)
WHERE {
  ?id wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38;
           wdt:P31 ?tipo_journal.
  FILTER(?tipo_journal = wd:Q5633421 || ?tipo_journal = wd:Q737498 || ?tipo_journal = wd:Q773668)
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
  ?id wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38;
           wdt:P31 ?tipo_journal.
  FILTER(?tipo_journal = wd:Q5633421 || ?tipo_journal = wd:Q737498 || ?tipo_journal = wd:Q773668)
  OPTIONAL {
    ?id wdt:P953 ?url.
  }
  FILTER(LANG(?title) = "it")
}
GROUP BY ?id
```

### DOI

```sparql
SELECT DISTINCT ?id ?doi
WHERE {
  ?id wdt:P1433 ?journal;
      rdfs:label ?title.
  ?journal wdt:P17 wd:Q38;
           wdt:P31 ?tipo_journal.
  FILTER(?tipo_journal = wd:Q5633421 || ?tipo_journal = wd:Q737498 || ?tipo_journal = wd:Q773668)
  OPTIONAL {
    ?id wdt:P356 ?doi.
  }
  FILTER(LANG(?title) = "it")
}
```