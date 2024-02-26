from libpythonpro.spam.modelos import Usuario
from libpythonpro.tests.test_spam.conftest import sessao


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Gustavo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Gustavo'), Usuario(nome='Luciano')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
