# adobe-tools
Dette er et projekt, der indeholder forskellige værktøjer til at håndtere Adobe brugere på U/NORD med udtræk fra Studsys.

## Installation

### Forudsætninger

- Python 3.11
- Pandas 2.0.2

For at installere de nødvendige pakker, køre:

```bash
pip install -r requirements.txt
```
---

## Brug

### Adobe slette liste

For at finde studerende, der ikke er på UNORD og generere en slette liste fra Studsys eksport funktion, køre:

```bash
python adobe_delete_list.py
```

Dette vil bruge data fra `./csv_adobe_complete/users.csv` og `./csv_studsys_complete/Export.csv` og outputte en ny liste i `./csv_adobe_delete_list/students_not_at_unord.csv`.

### Adobe Tilføj Klasse

For at importere studerende fra studsys og tilføje dem til en klasse i Adobe:

```bash
python adobe_add_class.py
```

Dette vil tage `.csv` filer fra mappen `csv_import`, rense dem og flytte dem til `csv_export`.

For oprette hele klaser kan følgende gøres:

1. Find klassen i studsys
2. Export følgende: Navn, Mailadresse
3. Kopier csv filen til mappen /csv_import
4. Følg skridt 1-5 for alle klasserne der skal oprettes:
5. Kør filen adobe_add_class.py
6. Importer csv filerne fra /csv_export til brugeropretelse: https://adminconsole.adobe.com/3A7C3F955A8FDAEC0A495C1D@AdobeOrg/users
7. Importer csv filerne fra /csv_export til prudukt tilladelse: https://adminconsole.adobe.com/3A7C3F955A8FDAEC0A495C1D@AdobeOrg/products/F548158E1A5DF531DFAA/profiles/57376189/users


## Funktioner i tools.py

Forskellige hjælpefunktioner til håndtering af CSV-filer. Her er nogle eksempler:

- `csv_clean_to_comma(file_name: str)`: Renser en CSV-fil ved at erstatte semikolon med komma.
- `csv_add_column_with_fixed_variable(file_name: str, column_name: str, column_data: str)`: Tilføjer en ny kolonne med en fast værdi.
