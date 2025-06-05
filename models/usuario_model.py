class Usuario:
    def __init__(self, id: int, nome: str, email: str, senha: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha  
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
        }