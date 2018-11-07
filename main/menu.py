from core.utils import Calculadora
from core.exceptions import ParametroNegativoException

class Body():



    def iniciar(Body):
        """
        Método que chama a função main, fzd um laço para que o usuário faça várias
        até que decida parar.
        """
        while main() != -1:
            self.main()
        return 'Fim'

    def main(notas=None, valor=None):
        """
        Metodo principal, chama as funções de coleta e retorna lista com respostas
        """
        print('CADASTRE AS NOTAS DISPONÍVEIS:')
        # inicio lista de resposta
        resp = []
        # caso notas sejam nulas, faço coleta de informações do usuário
        if notas == None:
            notas = Calculadora.coleta_notas()
            valor = Calculadora.coleta_valor()
        try:
            if valor < 0:
                raise ParametroNegativoException('Valor negativo!')
        except ParametroNegativoException as e:
            return e
        # função response retorna response do valor trocado e o valor resto, caso exista
        response, resto = Calculadora.response(Calculadora, notas, valor)
        # para cada item no dict response é construia uma str
        for item in response.items():
            resp.append('Nota: {}, quantidade: {}'.format(item[0], item[1]))
        # essa str é adicionada na lista resp para ser retornada para o usuário
        resp.append('resto: {}'.format(resto))
        return resp
