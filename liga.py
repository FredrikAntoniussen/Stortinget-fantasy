class Liga:
    def __init__(self):
        self.LagListe = []
    def legg_til_lag(self,lag):
        self.LagListe.append(lag)

    def hent_liga(self):
        lst = []
        for lag in self.LagListe:
            lst.append(lag._navn)
        return lst