from errbot import BotPlugin, botcmd
from random import randint


class Dados(BotPlugin):
    """
    Rolar os dados para suporte a jogos de RPG de mesa.
    Tem o rolar de n dados com m faces, entre outros comandos.
    """

    @botcmd(split_args_with=' ')
    def rolar(self, msg, args):
        """
        Informar quantos dados e faces.
        Forma de usar:
        !rolar <dados> <faces>
        onde <dados> e <faces> são números inteiros.
        """

        try:
            dados = int(args[0])
            faces = int(args[1])
        except:
            yield "Por favor, informe dados e faces como números inteiros"
            yield "na seguinte forma:"
            yield "!rolar <dados> <faces>"
        else:
            somatorio = 0
            for parada in range(1, dados + 1):
                dado = randint(1, faces)
                somatorio = somatorio + dado
                yield "Dado " + str(parada) + " = " + str(dado)
            yield "Somatório = " + str(somatorio)