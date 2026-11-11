
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from decimal import Decimal
import re

app = FastAPI(
    title="API Pix - Projeto 2",
    description="API simulada para validação de transferências Pix",
    version="1.0.0"
)

# Limite máximo permitido para transferência
LIMITE_PIX = Decimal("3000.00")

# Base simulada de chaves Pix cadastradas
CNPJS_CADASTRADOS = {
    "12ABC34501DE35": "Empresa Exemplo Ltda."
}


class PixRequest(BaseModel):
    chave_pix: str = Field(description="CNPJ utilizado como chave Pix")
    valor: Decimal = Field(description="Valor da transferência em reais")


def normalizar_cnpj(cnpj: str) -> str:
    return re.sub(r"[./-]", "", cnpj.strip().upper())


def calcular_digito_verificador(base: str) -> str:
    valores = [ord(caractere) - 48 for caractere in base]

    pesos_dv1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(
        valor * peso
        for valor, peso in zip(valores, pesos_dv1)
    )

    resto = soma % 11
    dv1 = 0 if resto < 2 else 11 - resto

    valores.append(dv1)

    pesos_dv2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(
        valor * peso
        for valor, peso in zip(valores, pesos_dv2)
    )

    resto = soma % 11
    dv2 = 0 if resto < 2 else 11 - resto

    return f"{dv1}{dv2}"


def validar_cnpj(cnpj: str) -> bool:
    if not re.fullmatch(r"[A-Z0-9]{12}[0-9]{2}", cnpj):
        return False

    base = cnpj[:12]
    digitos_informados = cnpj[12:]

    digitos_calculados = calcular_digito_verificador(base)

    return digitos_informados == digitos_calculados


@app.get("/")
def home():
    return {
        "mensagem": "API Pix está funcionando!",
        "status": "ONLINE"
    }


@app.post("/pix")
def realizar_pix(pix: PixRequest):
    cnpj = normalizar_cnpj(pix.chave_pix)

    if not validar_cnpj(cnpj):
        raise HTTPException(
            status_code=400,
            detail="CNPJ inválido ou dígitos verificadores incorretos."
        )

    if pix.valor <= Decimal("0"):
        raise HTTPException(
            status_code=400,
            detail="O valor do Pix deve ser maior que zero."
        )

    if pix.valor > LIMITE_PIX:
        raise HTTPException(
            status_code=403,
            detail="Transação bloqueada: valor acima do limite de R$ 3.000,00."
        )

    if cnpj not in CNPJS_CADASTRADOS:
        raise HTTPException(
            status_code=404,
            detail="Destinatário não encontrado: CNPJ não cadastrado."
        )

    return {
        "status": "AUTORIZADO",
        "mensagem": "Pix realizado com sucesso!",
        "destinatario": CNPJS_CADASTRADOS[cnpj],
        "chave_pix": cnpj,
        "valor": f"{pix.valor:.2f}"
    }
