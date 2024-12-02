import pytest
from models.py import Usuario

@pytest.fixture
def usuario_service():
    """Cria uma instância do serviço de usuários para ser usada nos testes."""
    return UsuarioService()

# Testes para Cadastro de Usuário
def test_cadastrar_usuario_valido(usuario_service):
    usuario = usuario_service.cadastrar_usuario("João", "joao@dominio.com", "senha1234")
    assert usuario.nome == "João"
    assert usuario.email == "joao@dominio.com"

def test_cadastrar_usuario_email_duplicado(usuario_service):
    usuario_service.cadastrar_usuario("João", "joao@dominio.com", "senha1234")
    with pytest.raises(ValueError, match="Email inválido ou já cadastrado."):
        usuario_service.cadastrar_usuario("Maria", "joao@dominio.com", "senha5678")

def test_cadastrar_usuario_senha_curta(usuario_service):
    with pytest.raises(ValueError, match="A senha deve ter pelo menos 8 caracteres e conter ao menos um número."):
        usuario_service.cadastrar_usuario("João", "joao@dominio.com", "12345")

def test_cadastrar_usuario_email_invalido(usuario_service):
    with pytest.raises(ValueError, match="Email inválido ou já cadastrado."):
        usuario_service.cadastrar_usuario("João", "emailinvalido", "senha1234")

# Testes para Login de Usuário
def test_login_bem_sucedido(usuario_service):
    usuario_service.cadastrar_usuario("João", "joao@dominio.com", "senha1234")
    usuario = usuario_service.login("joao@dominio.com", "senha1234")
    assert usuario.nome == "João"

def test_login_email_nao_cadastrado(usuario_service):
    usuario_service.cadastrar_usuario("João", "joao@dominio.com", "senha1234")
    with pytest.raises(ValueError, match="Email ou senha incorretos."):
        usuario_service.login("maria@dominio.com", "senha1234")

def test_login_senha_incorreta(usuario_service):
    usuario_service.cadastrar_usuario("João", "joao@dominio.com", "senha1234")
    with pytest.raises(ValueError, match="Email ou senha incorretos."):
        usuario_service.login("joao@dominio.com", "senhaerrada")

# Testes adicionais (testando limites e exceções)
def test_cadastrar_usuario_nome_vazio(usuario_service):
    with pytest.raises(ValueError, match="O nome não pode estar vazio."):
        usuario_service.cadastrar_usuario("", "joao@dominio.com", "senha1234")

def test_login_email_vazio(usuario_service):
    usuario_service.cadastrar_usuario("João", "joao@dominio.com", "senha1234")
    with pytest.raises(ValueError, match="Email ou senha incorretos."):
        usuario_service.login("", "senha1234")
