
import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_pix_realizado_com_sucesso():
    response = client.post(
        "/pix",
        json={
            "chave_pix": "12ABC34501DE35",
            "valor": 100.00
        }
    )

    assert response.status_code == 200
    assert response.json()["status"] == "AUTORIZADO"
    assert response.json()["valor"] == "100.00"


def test_bloquear_pix_acima_do_limite():
    response = client.post(
        "/pix",
        json={
            "chave_pix": "12ABC34501DE35",
            "valor": 3500.00
        }
    )

    assert response.status_code == 403
    assert response.json()["detail"] == (
        "Transação bloqueada: valor acima do limite de R$ 3.000,00."
    )


def test_rejeitar_pix_com_valor_zero():
    response = client.post(
        "/pix",
        json={
            "chave_pix": "12ABC34501DE35",
            "valor": 0
        }
    )

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "O valor do Pix deve ser maior que zero."
    )


def test_rejeitar_cnpj_invalido():
    response = client.post(
        "/pix",
        json={
            "chave_pix": "123456",
            "valor": 100.00
        }
    )

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "CNPJ inválido ou dígitos verificadores incorretos."
    )


def test_rejeitar_destinatario_nao_cadastrado():
    response = client.post(
        "/pix",
        json={
            "chave_pix": "11AAA11101AA66",
            "valor": 100.00
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == (
        "Destinatário não encontrado: CNPJ não cadastrado."
    )
