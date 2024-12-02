class Usuario:
    """
    Classe que representa um usuário no sistema.
    """

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __repr__(self):
        return f"Usuario(nome={self.nome}, email={self.email})"
