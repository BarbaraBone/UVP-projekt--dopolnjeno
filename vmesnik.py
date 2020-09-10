import bottle
from projekt_model import *

@bottle.get('/')
def osnovna_stran():
    primer = Ploscina([[0,0], [1,1], [3,0], [2,-2]], 2)
    return bottle.template('osnovna_stran.html', primer=primer)



@bottle.post('/izracun/')
def izracun():

    niz = bottle.request.forms['tocke']
    tocke = pretvorba_str_v_list(niz)
    meja = float(bottle.request.forms['meja'])#morda ne dela, če float ne dela uporabi eval
    lik =  Ploscina(tocke, meja)
    return bottle.template('izracun.html', lik=lik, tocke=tocke, meja=meja)

bottle.run(debug=True, reloader=True)