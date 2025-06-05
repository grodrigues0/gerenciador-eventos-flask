from models.usuario_model import Usuario

usuarios = []
id_usuario = 0

# Utilitário para gerar IDs únicos para usuários
def gerar_id_usuario():
    global id_usuario
    id_usuario += 1
    return id_usuario

# CREATE usuário
def criar_usuario(dados):
    global usuarios
    novo_usuario = Usuario(
        gerar_id_usuario(),
        dados['nome'],
        dados['email'],
        dados['senha']
    )
    usuarios.append(novo_usuario)
    return novo_usuario.to_dict()


# READ usuários
def listar_usuarios():
    global usuarios
    return [usuario.to_dict() for usuario in usuarios]

def buscar_usuario_por_id(id_usuario):
    global usuarios
    for usuario in usuarios:
        if usuario.id == id_usuario:
            return usuario.to_dict()
    return None

# UPDATE usuário
def atualizar_usuario(id_usuario, dados):
    global usuarios
    for usuario in usuarios:
        if usuario.id == id_usuario:
            usuario.nome = dados.get('nome', usuario.nome)
            usuario.email = dados.get('email', usuario.email)
            usuario.senha = dados.get('senha', usuario.senha)
            return usuario.to_dict()
    return None