from flask import Blueprint, request, jsonify
from services.usuario_services import *
from utils.mensages_erro import erros

usuario_bp = Blueprint('usuarios', __name__)

@usuario_bp.route('/usuarios', methods=['POST'])
def criar():
    dados = request.get_json()   
    novo_usuario, erro = criar_usuario(dados)
    if erro:
        if erro == "EMAIL_DUPLICADO":
            erro_info = erros.get(erro, {"mensagem": "Erro desconhecido", "status_code": 500})
            return jsonify({'error': erro_info['mensagem']}), erro_info['status_code']
    return jsonify(novo_usuario), 201

@usuario_bp.route('/usuarios', methods=['GET'])
def listar():
    return jsonify(listar_usuarios()), 200


@usuario_bp.route('/usuarios/<int:id_usuario>', methods=['GET'])
def buscar(id_usuario):
    usuario, erro = buscar_usuario_por_id(id_usuario)
    if erro:
        erro_info = erros.get(erro, {"mensagem": "Erro desconhecido", "status_code": 500})
        return jsonify({'error': erro_info['mensagem']}), erro_info['status_code']
    return jsonify(usuario.to_dict()), 200

@usuario_bp.route('/usuarios/<int:id_usuario>', methods=['PUT', 'PATCH'])
def atualizar(id_usuario):
    dados = request.get_json()
    if not dados:
        return {'error': 'Dados inválidos'}, 400
    usuario_atualizado, erro = atualizar_usuario(id_usuario, dados)
    if erro:
        erro_info = erros.get(erro, {"mensagem": "Erro desconhecido", "status_code": 500})
        return jsonify({'error': erro_info['mensagem']}), erro_info['status_code']
    return jsonify(usuario_atualizado.to_dict()), 200

@usuario_bp.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def deletar(id_usuario):
    usuario_deletado, erro = deletar_usuario(id_usuario)
    if erro:
        erro_info = erros.get(erro, {"mensagem": "Erro desconhecido", "status_code": 500})
        return jsonify({'error': erro_info['mensagem']}), erro_info['status_code']
    return jsonify({'message': 'Usuário deletado com sucesso'}), 204