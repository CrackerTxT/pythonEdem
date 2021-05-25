# coding: utf-8

__author__ = "CrackTxt"


# Calculo de retangulo com classe e validação de interação ::
# _VariaveisOcultas
class retangulo:

    def __init__(self, largura, altura):
        self._largura = 0
        self._altura = 0
        self.set_altura(altura)
        self.set_largura(largura)

    def set_altura(self, altura):

        if (not (isinstance(altura, int) and (altura > 0))):
            raise ValueError(f"Altura Invalida: {altura}")
        self.altura = altura

    def set_largura(self, largura):

        if (not (isinstance(largura, int) and (largura > 0))):
            raise ValueError(f"Largura Invalida: {largura}")
        self.largura = largura

    def get_area(self):
        return self.altura * self.largura

r = retangulo(altura=10, largura=10)
a = r.altura
l = r.largura
print(r.get_area())
