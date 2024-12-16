def usuari_schema(usuari) -> dict:
    return {
        "Punts partides actuals": usuari[0],
        "Total partides": usuari[1],
        "Partides guanyades": usuari[2],
        "Partida amb més punts": usuari[3],
    }

def usuaris_schema(usuaris) -> list[dict]:
    return [usuari_schema(usuari) for usuari in usuaris]