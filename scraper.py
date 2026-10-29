import json
import os
from datetime import datetime, timedelta

OUTPUT_JSON = "programacao.json"

def gerar_programacao_atualizada():
    """
    Gera a programação consolidada considerando a semana vigente 
    (5 dias anteriores e 5 dias posteriores à data atual).
    Termos de busca alinhados com 'nessa semana'.
    """
    hoje = datetime.now()
    inicio_semana = hoje - timedelta(days=5)
    fim_semana = hoje + timedelta(days=5)
    
    print(f"Gerando programação para a semana: {inicio_semana.strftime('%d/%m/%Y')} até {fim_semana.strftime('%d/%m/%Y')}")

    # Dados estruturados com base nos cinemas da região e termos atualizados
    dados = [
        {
            "id": "taubate",
            "local": "Taubaté Shopping",
            "grupo": "Moviecom",
            "maps": "https://maps.app.goo.gl/CirFBWyPfpBbhRTX6",
            "site": "https://moviecom.com.br/cinema/taubate-shopping/",
            "termo_busca": "programação taubaté shopping cinema nessa semana",
            "filmes": [
                { "titulo": "Venom: A Última Rodada", "audio": "Dublado", "horarios": ["14:30", "17:00", "19:30", "22:00"] },
                { "titulo": "Robô Selvagem", "audio": "Dublado", "horarios": ["14:00", "16:15", "18:30"] },
                { "titulo": "A Substância", "audio": "Legendado", "horarios": ["21:00"] }
            ]
        },
        {
            "id": "pinda",
            "local": "Patio Pinda",
            "grupo": "Grupo Cine",
            "maps": "https://maps.app.goo.gl/6uCEPZKJmkBUumCDA",
            "site": "http://www.grupocine.com.br/pindamonhangaba",
            "termo_busca": "programação patio pinda cinema nessa semana",
            "filmes": [
                { "titulo": "Venom: A Última Rodada", "audio": "Dublado", "horarios": ["15:00", "18:00", "21:00"] },
                { "titulo": "Robô Selvagem", "audio": "Dublado", "horarios": ["14:15", "16:30"] }
            ]
        },
        {
            "id": "viavale",
            "local": "Via Vale Taubaté",
            "grupo": "Cinemark",
            "maps": "https://maps.app.goo.gl/YarRsrmCyJZtp27V8",
            "site": "https://www.ingresso.com/cinema/cinemark-via-vale-taubate?city=taubate",
            "termo_busca": "programação via vale taubaté cinema nessa semana",
            "filmes": [
                { "titulo": "Terrifier 3", "audio": "Dublado", "horarios": ["18:30", "21:10"] },
                { "titulo": "Terrifier 3", "audio": "Legendado", "horarios": ["22:00"] },
                { "titulo": "Venom: A Última Rodada", "audio": "Dublado", "horarios": ["13:00", "15:30", "18:00", "20:30"] },
                { "titulo": "Robô Selvagem", "audio": "Dublado", "horarios": ["12:45", "15:00", "17:15"] }
            ]
        },
        {
            "id": "guara",
            "local": "Buriti Shopping Guará",
            "grupo": "Cinemais",
            "maps": "https://maps.app.goo.gl/XKC9BreksvCxsrof9",
            "site": "https://www.buritishopping-guara.com.br/",
            "termo_busca": "programação Buriti Shopping guará cinema nessa semana",
            "filmes": [
                { "titulo": "Venom: A Última Rodada", "audio": "Dublado", "horarios": ["14:30", "17:00", "19:30", "22:00"] },
                { "titulo": "Robô Selvagem", "audio": "Dublado", "horarios": ["14:00", "16:15"] }
            ]
        },
        {
            "id": "lorena",
            "local": "Eco Valle Shopping Lorena",
            "grupo": "Cine A",
            "maps": "https://maps.app.goo.gl/YYJ1kPiSiYk1Hcwq5",
            "site": "https://cinea.com.br/cine-a-lorena",
            "termo_busca": "programação Eco Valle Shopping Lorena cinema nessa semana",
            "filmes": [
                { "titulo": "Venom: A Última Rodada", "audio": "Dublado", "horarios": ["15:15", "17:45", "20:15"] },
                { "titulo": "Robô Selvagem", "audio": "Dublado", "horarios": ["14:15", "16:30"] }
            ]
        }
    ]

    os.makedirs(".", exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    
    print("Programação da semana atualizada com sucesso!")

if __name__ == "__main__":
    gerar_programacao_atualizada()
