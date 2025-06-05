class Ingresso:
    def __init__(self, id: int, usuario_id: int, evento_id: int, tipo: str, valor: float):
        self.id = id
        self.usuario_id = usuario_id
        self.evento_id = evento_id
        self.tipo = tipo
        self.valor = valor

    def to_dict(self):
        return {
            'id': self.id,
            'usuario_id': self.usuario_id,
            'evento_id': self.evento_id,
            'tipo': self.tipo,
            'valor': self.valor
        }