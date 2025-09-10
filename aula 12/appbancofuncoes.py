"""
programa de banco
x 1- rodar em loop infinito
x 2- ter conta e senha (validar)
3- encerrar atendimento
4- cheque especial (limite saldo negativo)
x 5- tentar 3 vezes a senha
6- opções (saque, deposito, saldo)
7- mostrar saldo apos saque
8- alterar senha
x 9- dizer o nome do usuario
10- pagar boleto
"""

def banco() -> dict:
    """carregas dados de acesso e configurações"""
    return{
        "usuarios":{
            "123456-7":{
                "senha":"9999",
                "nome": "José",
                "saldo": 1500.00,
                "limite_cheque_especial": 500.00,
            },
        },
        "tentivas_login":3,
        "ultima_conta_base":"123456",
        "digito_verificador":"7",
    }
    
def autenticar_usuario(
    dados_banco:dict,
    conta:str,
    senha:str,
    ) -> tuple[bool, dict| None]:   
    """autentica o usuario com base na conta e senha, retorna status e usuario"""
    usuario_encontrado = dados_banco["usuarios"].get(conta,None) 
    
    if usuario_encontrado and usuario_encontrado["senha"] == senha:
        return True, usuario_encontrado
   
    return False, None 


def verificar_saldo(usuarios:dict) -> None:
    """mostra o saldo atual"""
    print(f"Seu saldo atual é R$ {usuarios["saldo"]:.2f})")
    
    
def cadastrar_cliente(dados_banco:dict) -> None:    
    """cadastrar novo cliente no sotema"""
    