class Lag:
    def __init__(self, navn):
        self._navn = navn
        self._politiker_liste = []
        self._penger = 100000
    def kjop_spiller(self,politiker):
        self._politiker_liste.append(politiker)
        self._penger -= politiker._pris
    def selg_spiller(self,politiker):
        self._politiker_liste.remove(politiker)
        self._penger += politiker._pris
    def hent_lag(self):
        lst = []
        for politiker in self._politiker_liste:
            lst.append(politiker._navn)
        return lst


    def hent_budsjett(self):
        return self._penger

