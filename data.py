class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def data_formatada(self):
        print('Data Formatada: {}/{}/{}'.format(self.dia, self.mes, self.ano))


