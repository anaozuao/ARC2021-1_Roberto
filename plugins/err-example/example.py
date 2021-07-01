from errbot import BotPlugin, botcmd


class Example(BotPlugin):
    """
    apenas uma classe de métodos para aprendizado.
    """

    @botcmd  # flags a command
    def bomdia(self, msg, args):
        """
        Resposnde educadamente ao usuário
        """
        
        argumentos = args.split(' ')
        return "Bom dia quinta-feira"