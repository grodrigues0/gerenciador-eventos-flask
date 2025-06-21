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
    for usuario in usuarios:
        if usuario.email == dados['email']:
            return None, "EMAIL_DUPLICADO"
    novo_usuario = Usuario(
        gerar_id_usuario(),
        dados['nome'],
        dados['email'],
        dados['senha']
    )
    usuarios.append(novo_usuario)
    return novo_usuario.to_dict(), None


# READ usuários
def listar_usuarios():
    global usuarios
    return [usuario.to_dict() for usuario in usuarios]

def buscar_usuario_por_id(id_usuario):
    global usuarios
    for usuario in usuarios:
        if usuario.id == id_usuario:
            return usuario, None
    return None, "USUARIO_NAO_ENCONTRADO"

# UPDATE usuário
def atualizar_usuario(id_usuario, dados):
    usuario, erro = buscar_usuario_por_id(id_usuario)
    if erro:
        return None, erro
    
    for u in usuarios:
        if u.id != id_usuario and u.email == dados.get('email'):
            return None, "EMAIL_DUPLICADO"
        
    usuario.nome = dados.get('nome', usuario.nome)
    usuario.email = dados.get('email', usuario.email)
    usuario.senha = dados.get('senha', usuario.senha)
    return usuario.to_dict(), None

# DELETE usuário
def deletar_usuario(id_usuario):
    usuario, erro = buscar_usuario_por_id(id_usuario)
    if erro:
        return False, erro
    usuarios.remove(usuario)
    return True, None
