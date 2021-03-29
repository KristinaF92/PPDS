# PPDS - H2O

V tomto tyzdni som si vybrala riesit problem skladania molekuly vody.
Problem sa riesi pomocou trojice vlakien, ktore kontroluje bariera. Pre jednotlive
molekuly kyslika a vodika mame definovane pocitadla a mutex ktory chrani ich integritu.
Riesenie modelujeme pomocou silnych semaforov(fronty) na ktorych budu cakat vlakna kysliku a vodiku.
Experiment bezi v nekonecnom cykle. Kde sa nahodne vytvaraju vlakna vodika a kyslika.
Funkcia bond spracuje molekulu pri dostatocnom pocte kyslika a vodikov.

