class Calculadora():

    def coleta_notas():
        """
        Método que coletas as notas disponíveis.
        """
        x = 0
        lista = []
        # caso adicionem o valor -1 o laço é interrompide e é retornada uma lista
        # com as notas já adicionadas
        while x != -1:
            x = int(input(
            'Adicione um valor inteiro para uma nova nota ou "-1" para sair:  '))
            if x not in lista:
                lista.append(x)
        return lista

    def coleta_valor(self):
        """
        Método que coleta o valor a ser trocado.
        """
        x = int(input('Adicione um valor inteiro para saber como troca-lo '
                            'com as notas disponíveis ou "-1" para sair:  '))
        return x


    def ordena_lista(lista):
        """
        Método que ordena lista.
        """
        return sorted(lista)

    def response(self, notas, valor):
        """
        Metodo que recebe como parâmetros notas e o valor ser trocado e retorna
        dict de resposta e um valor restante.
        """
        # primeiramente a lista de notas é ordenada
        notas = self.ordena_lista(notas)
        # inicio o dict de resposta
        response = {}
        # enquanto a lista de notas estiver populada executo
        while notas != []:
            # se o ultimo da lista for menor que o valor restante
            if notas[-1] < valor:
                # adiciono um item no dict de respostas com a key(nota) e value(quantidade)
                # fazendo uma divisão truncada para saber o quantidade maxima de
                # notas deste valor a serem utilizadas
                response[notas[-1]] = valor // max(notas)
                # e tranformo a variável valor no resto dessa msm divisão
                valor = valor % max(notas)
            # este if deve ser ignorado, for uma "gambiarra por falta de tempo"
            if valor == 1 and 1 in notas:
                response['1'] = valor
                valor = 0
            # removo o ultimo valor da lista de notas no fim de cada laço
            notas.remove(notas[-1])
        # retorno o dict de respostas e o resto do valor
        return response, valor
