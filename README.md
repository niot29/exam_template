# Examination

Individuell examinationsuppgift i kursen Programmering med Python.
<br>
***Det finns uppladdad en inspelade demo på spelet (exam_template.mp4)***


## Frukt Loop

Frukt Loop spelas i terminalen och går ut på att samla olika föremål på spelplanen.

Målet är att på ett så effektivt sätt som möjligt ta sig fram till objekten i spelet. För varje föremål som spelaren samlar in tilldelas poäng enligt följande:

Frukt: 20 poäng
Övriga föremål: 10 poäng

För varje steg spelaren tar utan att plocka upp ett föremål dras 1 poäng från den totala poängen.

---


## Starta projektet

För att starta mitt projekt skriver man följande i terminalen, medan man står i projektets rotmapp.
src.game - starta med  modeul "curses"
```commandline
python -m src.game
```

src.game-test - starta med modeul "curses" - ```src.game-test``` är den kör bar test version
```commandline
python -m src.game-test
```

## Vad jag har gjort
***Del Beskrivning***

Bytt ikonen som rittar upp väggarna, för förtydliga (befinligy oikon blev lite klimpigt i Linux konsolen)
´´´
#wall = "■"   # Tecken för en ogenomtränglig vägg
wall = "|"   # Tecken för en ogenomtränglig vägg
´´´
| **A** | Hämta X- och Y-värden från klassobjektet `g`. Dividera X- och Y-värdena för att beräkna centrum. Skicka sedan resultatet till klassen `Play`.     

| **B** | `directions` används för att mappa tangentnedtryckningar. Spelarens position beräknas genom att addera den nuvarande X- och Y-positionen med värdena i `directions`. Genom att hantera positionsberäkningen på detta sätt undviks kod med många `if`-/`case`-satser och villkor.                                                                                                                                                                  

| **C** | Funktionen `can_move` i klassen `Player` används för att avgöra vilka ytor som inte är väggar. Varje väggobjekt motsvarar en position på spelkartan. Det totala antalet positioner på X-axeln beräknas utan att inkludera start- och slutpositionerna. Samma beräkning gäller för Y-axeln. För att spelpjäsen ska kunna flyttas måste följande villkor uppfyllas. Den nya positionen för spelpjäsen ska ligga inom minimi- och maxvärdena för både X- och Y-axeln. Om villkoret uppfylls returnerar funktionen True. 


| **D/E/F** | Tre nya funktioner har lagts till i klassen `Pickups` <br> - `get_item_score` kontrollerar vilket föremål spelaren har plockat upp och ändrar poängen till **20** om föremålet inte är en frukt (t.ex. en `meatball`).<br>- `pickup_item` lägger de upphämtade föremålen i en lista.<br>- `pickup_print_list` skriver ut innehållet i listan.                                                                                                                                                                   
| **G** | Om spelpjäsens nya position inte sammanfaller med ett fruktobjekt, vilket innebär att ingen frukt plockas upp, görs ett poängavdrag.                                                                                                                                                              


| **H** |  Ny interna väggar skappas, som kontroll att spelpjasen inte skall kunna gå igenom den ny interna väggarn.
