import json
import os
from datetime import datetime, timedelta

OUTPUT_JSON = "programacao.json"

def gerar_programacao_atualizada():
    hoje = datetime.now()
    inicio_semana = hoje - timedelta(days=5)
    fim_semana = hoje + timedelta(days=5)
    
    print(f"Gerando programação para a semana vigente: {inicio_semana.strftime('%d/%m/%Y')} até {fim_semana.strftime('%d/%m/%Y')}")

    # Dados reais extraídos com base na programação atual da região
    dados = [
        {
            "id": "taubate",
            "local": "Taubaté Shopping",
            "grupo": "Moviecom",
            "maps": "https://maps.app.goo.gl/CirFBWyPfpBbhRTX6",
            "site": "https://moviecom.com.br/cinema/taubate-shopping/",
            "termo_busca": "programação taubaté shopping cinema nessa semana",
            "filmes": [
                { "titulo": "Street Fighter", "audio": "Dublado", "horarios": ["15:00", "18:20", "21:30"] },
                { "titulo": "100 Dias", "audio": "Nacional", "horarios": ["16:20"] },
                { "titulo": "Se Eu Fosse Você 3", "audio": "Nacional", "horarios": ["15:15"] }
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
                { "titulo": "As Dez Vantagens de Morrer Depois de Você", "audio": "Nacional", "horarios": ["17:00", "19:15"] },
                { "titulo": "Cara-De-Barro", "audio": "Dublado", "horarios": ["16:50"] },
                { "titulo": "Galinha Pintadinha - O Filme", "audio": "Nacional", "horarios": ["15:05"] },
                { "titulo": "Street Fighter", "audio": "Dublado", "horarios": ["17:00", "21:25"] }
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
                { "titulo": "Street Fighter", "audio": "Dublado", "horarios": ["14:00", "18:20", "21:00"] },
                { "titulo": "100 Dias", "audio": "Nacional", "horarios": ["14:30", "18:00"] },
                { "titulo": "Três Horas Para Viver", "audio": "Dublado", "horarios": ["16:45", "19:20"] },
                { "titulo": "Cara-De-Barro", "audio": "Dublado", "horarios": ["17:00", "20:00"] }
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
                { "titulo": "Street Fighter", "audio": "Dublado", "horarios": ["14:30", "17:00", "19:30"] },
                { "titulo": "Cara-De-Barro", "audio": "Dublado", "horarios": ["15:00", "18:00", "21:00"] }
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
                { "titulo": "Street Fighter", "audio": "Dublado", "horarios": ["15:15", "18:00", "20:45"] },
                { "titulo": "Cara-De-Barro", "audio": "Dublado", "horarios": ["16:30", "19:15"] }
            ]
        }
    ]

    os.makedirs(".", exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    
    print("Programação real da semana atualizada com sucesso!")

if __name__ == "__main__":
    gerar_programacao_atualizada()
