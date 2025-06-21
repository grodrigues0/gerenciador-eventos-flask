from evento_services import Evento

eventos = []
id_evento = 0

# Utilitário para gerar IDs únicos para usuários
def gerar_id_evento():
    global id_evento
    id_evento += 1
    return id_evento

# CREATE ingresso
def criar_ingresso(dados):
    global eventos
    novo_evento = Evento(
        gerar_id_evento(),
        dados['titulo'],
        dados['descricao'],
        dados['data'],
        dados['localizacao'],
        dados['organizador_id']
    )
    eventos.append(novo_evento)
    return novo_evento.to_dict()