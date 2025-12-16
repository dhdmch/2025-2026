# Visual Arts and Paintings Open Data (VAPOD)

## Descrizione

Dataset estratto da Wikidata contenente i metadati descrittivi di dipinti appartenenti all'arco temporale circoscritto tra il 1400 e il 1999.

## Endpoint

Wikidata Query Service: https://query.wikidata.org/

## Query di estrazione

### Titoli

```sparql
SELECT DISTINCT ?id ?titolo
WHERE { 
  ?id wdt:P31 wd:Q3305213;
            wdt:P17 wd:Q38;
            rdfs:label ?titolo.
  
  FILTER(LANG(?titolo) = "it")   
}
```

### Artisti

```sparql
SELECT DISTINCT ?id ?sesso (GROUP_CONCAT(?artista; SEPARATOR="; ") AS ?artisti)
WHERE {
  ?id wdt:P31 wd:Q3305213;
      wdt:P17 wd:Q38;
      rdfs:label ?titolo.
  FILTER(LANG(?titolo) = "it")
  OPTIONAL {
    ?id wdt:P170 ?creator.
    ?creator rdfs:label ?artista;
             wdt:P21 ?sex.
    ?sex rdfs:label ?sesso.
    FILTER(LANG(?artista) = "it")    
    FILTER(LANG(?sesso) = "it")
  }
}
GROUP BY ?id ?sesso
```

### Date

```sparql
SELECT DISTINCT ?id (GROUP_CONCAT(?data; SEPARATOR=" | ") AS ?datax)
WHERE { 
  ?id wdt:P31 wd:Q3305213;
            wdt:P17 wd:Q38;
            rdfs:label ?titolo.
  OPTIONAL {
    ?id wdt:P571 ?date.
    BIND(YEAR(?date) AS ?data)
  }
  FILTER(LANG(?titolo) = "it")   
}
GROUP BY ?id
```

### Larghezze

```sparql
SELECT DISTINCT ?id (MAX(?width) AS ?larghezza)
WHERE { 
  ?id wdt:P31 wd:Q3305213;
            wdt:P17 wd:Q38;
            rdfs:label ?titolo.
  OPTIONAL {
    ?id wdt:P2049 ?width.
  }
  FILTER(LANG(?titolo) = "it")   
}
GROUP BY ?id
```

### Altezze

```sparql
SELECT DISTINCT ?id (MAX(?height) AS ?altezza)
WHERE { 
  ?id wdt:P31 wd:Q3305213;
            wdt:P17 wd:Q38;
            rdfs:label ?titolo.
  OPTIONAL {
    ?id wdt:P2048 ?height.
  }
  FILTER(LANG(?titolo) = "it")   
}
GROUP BY ?id
```

### Luoghi

```sparql
SELECT DISTINCT ?id (GROUP_CONCAT(?luogo; SEPARATOR="; ") AS ?luoghi)
WHERE { 
  ?id wdt:P31 wd:Q3305213;
            wdt:P17 wd:Q38;
            rdfs:label ?titolo.
  OPTIONAL {
    ?id wdt:P276 ?location.
    ?location rdfs:label ?luogo. 
    FILTER(LANG(?luogo) = "it")
  }
  FILTER(LANG(?titolo) = "it")   
}
GROUP BY ?id
```

### Collezioni

```sparql
SELECT DISTINCT ?id (GROUP_CONCAT(?collezione; SEPARATOR="; ") AS ?collezioni)
WHERE { 
  ?id wdt:P31 wd:Q3305213;
            wdt:P17 wd:Q38;
            rdfs:label ?titolo.
  OPTIONAL {
    ?id wdt:P195 ?collection.
    ?collection rdfs:label ?collezione. 
    FILTER(LANG(?collezione) = "it")
  }
  FILTER(LANG(?titolo) = "it")   
}
GROUP BY ?id
```

### Movimenti

```sparql
SELECT DISTINCT ?id (GROUP_CONCAT(?movimento; SEPARATOR="; ") AS ?movimenti)
WHERE { 
  ?id wdt:P31 wd:Q3305213;
            wdt:P17 wd:Q38;
            rdfs:label ?titolo.
  OPTIONAL {
    ?id wdt:P135 ?movement.
    ?movement rdfs:label ?movimento.
      FILTER(LANG(?movimento) = "it") 
  }
  FILTER(LANG(?titolo) = "it")   
}
GROUP BY ?id
```

### Soggetti

```sparql
SELECT DISTINCT ?id (GROUP_CONCAT(?soggetto; SEPARATOR="; ") AS ?soggetti)
WHERE { 
  ?id wdt:P31 wd:Q3305213;
            wdt:P17 wd:Q38;
            rdfs:label ?titolo.
  OPTIONAL {
    ?id wdt:P921 ?subject.
    ?subject rdfs:label ?soggetto.
      FILTER(LANG(?soggetto) = "it") 
  }
  FILTER(LANG(?titolo) = "it")   
}
GROUP BY ?id
```

### Contenuti

```sparql
SELECT DISTINCT ?id (GROUP_CONCAT(?oggetto_rappresentato; SEPARATOR="; ") AS ?contenuti)
WHERE { 
  ?id wdt:P31 wd:Q3305213;
            wdt:P17 wd:Q38;
            rdfs:label ?titolo.
  OPTIONAL {
    ?id wdt:P180 ?depicted.
    ?depicted rdfs:label ?oggetto_rappresentato.
    FILTER(LANG(?oggetto_rappresentato) = "it")
  }
  FILTER(LANG(?titolo) = "it")   
}
GROUP BY ?id
```

### Generi

```sparql
SELECT DISTINCT ?id (GROUP_CONCAT(?genere; SEPARATOR="; ") AS ?generi)
WHERE { 
  ?id wdt:P31 wd:Q3305213;
            wdt:P17 wd:Q38;
            rdfs:label ?titolo.
  OPTIONAL {
    ?id wdt:P136 ?genre.
    ?genre rdfs:label ?genere.
      FILTER(LANG(?genere) = "it") 
  }
  FILTER(LANG(?titolo) = "it")   
}
GROUP BY ?id
```