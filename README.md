V tomto tyzdni sa snazime demonstrovat efektivnost asynchronneho programovania.
Vyuzitim asyncio modulu a neblokujúcich IO funkcii môžeme dosiahnut asynchronne spracovanie kodu.
Experiment vytvara 5 volani funkcie pocitaj ktora kazda trva sekundu. Dokazali sme stiahnut cas pocitania
piatich volani na dobu cakania na sekundu oproti synchronnej verzii ktora trvala 5sekund.