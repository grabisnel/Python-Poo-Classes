from restaurante import Restaurante
from cardapio.bebida import Bebida
from cardapio.prato import Prato


restaurante_praca = Restaurante('praca', 'Gourmet')
bebida_suco = Bebida('Suco de Laranja', 5.0, 'grande')
prato_coxinha = Prato('Coxinha', 2.00, 'Melhor Coxinha da Cidade')


def main():
    print(bebida_suco)
    print(prato_coxinha)

if __name__ == '__main__':
    main()

    