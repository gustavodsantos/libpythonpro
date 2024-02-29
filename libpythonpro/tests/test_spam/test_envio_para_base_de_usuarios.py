from unittest.mock import Mock

import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Gustavo', email='gustavojuniordos@hotmail.com'),
            Usuario(nome='Luciano', email='luciano@python.pro.com.br')
        ],
        [
            Usuario(nome='Gustavo', email='gustavojuniordos@hotmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gustavojuniordos@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Gustavo', email='gustavojuniordos@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@python.pro.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'luciano@python.pro.com.br',
        'gustavojuniordos@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
