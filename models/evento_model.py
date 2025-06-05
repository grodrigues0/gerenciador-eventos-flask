class Evento():
    def __init__(self, id: int, titulo: str, descricao: str, data: str, localizacao: str, organizador_id: int):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.localizacao = localizacao
        self.organizador_id = organizador_id
    
    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'data': self.data,
            'localizacao': self.localizacao,
            'organizador_id': self.organizador_id
        }