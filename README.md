# UF2_FASTAPI
## Activitat 12
**EL CODI ACTUALITZAT PER L'ACTIVITAT 12 ES TROBA NOMÉS A LA CARPETA ACTIVITAT12.**

**LA CARPETA ACTIVITAT11 NOMÉS CONTÉ CODI DE L'ACTIVITAT ANTERIOR.**

Per aquesta activitat 12, es demana terminar el CRUD de les taules dissenyades al model relacional, i els respectius endpoints.

Hi ha 5 carpetes dins de la carpeta "crud" amb els arxius per crear les taules, consultes select, insert, update i delete.

La decisió a l'hora de pensar si era necessari la consulta o l'endpoint per cada taula o columna a la BBDD la vaig organitzar mitjançant el següent esquema:

| Taules/Columns | GET | POST | PUT | DELETE |
| --- | --- | --- | --- | --- |
| BotoInici | [X] | [_] | [_] | [_] |
| Abecedari | [X] | [_] | [_] | [_] |
| ParaulaSecreta | [X] | [X] | [X] | [_] |
| PARAULES | [X] | [_] | [_] | [_] |
| USUARI | [X] | [X] | [X] | [X] |
| REGISTRE_JOC | [X] | [X] | [X] | [X] |
| HANGMAN | [X] | [X] | [X] | [_] |

## Disseny DB
![cap1](cap1.png)

Justificació: La primera idea per a la BBDD era fer les quatre taules demanades a l'enunciat: usuaris, paraules, registre de joc i informació per pantalla.

Per controlar els futurs usuaris que faràn login i gestionar les seves dades del joc, enllaçarem les taules usuaris i registre de joc amb una foreign key usuari_id.
La taula hangman servirà per emmagatzemar la llista de paths d'imatges del penjat (penjat_0.jpg, etc.) en una sola columna.
Info_pantalla només tindrà una row i múltiples columes pels textos a renderitzar al frontend.

## Endpoints Swagger (/docs)
L'endpoint de /usuari fa servir un schema per renderitzar (donar format) a les dades del jugador en un list[dict].
```
def usuari_schema(usuari) -> dict:
    return {
        "Punts partides actuals": usuari[0],
        "Total partides": usuari[1],
        "Partides guanyades": usuari[2],
        "Partida amb més punts": usuari[3],
    }

def usuaris_schema(usuaris) -> list[dict]:
    return [usuari_schema(usuari) for usuari in usuaris]
```

### GET /boto_inici
![cap2](cap2.png)

### GET /paraula_secreta
![cap3](cap3.png)

### GET /hangman_img
![cap4](cap4.png)

### GET /abecedari
![cap5](cap5.png)

### GET /usuari
![cap6](cap6.png)
