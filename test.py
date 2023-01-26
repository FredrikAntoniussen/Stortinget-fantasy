from lag import Lag 
from politikere import Politikere
from liga import Liga

def hovedprogram():
    erna = Politikere("Erna Solberg","Høyre",20000)
    jonas = Politikere("Jonas Gahr Støre","Arbeiderpartiet",12000)
    vedum = Politikere("Trygve Slagsvold Vedum","Senterpartiet",5000)
    
    fantasy_lag = Lag("fantasy1")
    fantasy_lag.kjop_spiller(erna)
    fantasy_lag.kjop_spiller(jonas)
    fantasy_lag.kjop_spiller(vedum)

    print(fantasy_lag.hent_budsjett())
    print(fantasy_lag.hent_lag())

    fantasy_lag2 = Lag("fantasy2")
    fantasy_lag2.kjop_spiller(erna)
    fantasy_lag2.kjop_spiller(jonas)
    liga = Liga()
    liga.legg_til_lag(fantasy_lag)
    liga.legg_til_lag(fantasy_lag2)
    print(liga.hent_liga())

    
hovedprogram()