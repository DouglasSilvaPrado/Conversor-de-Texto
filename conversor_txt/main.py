from PyQt5 import QtWidgets, uic

class ConverterTexto:
    def Maiuscula(self):
        dados = conversor.CaixaTexto.toPlainText()
        conversor.CaixaTexto.setText(dados.upper())

    def Minuscula(self):
        dados = conversor.CaixaTexto.toPlainText()
        conversor.CaixaTexto.setText(dados.lower())

    def PrimeiraLetra(self):
        dados = conversor.CaixaTexto.toPlainText()
        conversor.CaixaTexto.setText(dados.title())

    def Inverter(self):
        dados = conversor.CaixaTexto.toPlainText()
        conversor.CaixaTexto.setText(dados[::-1])

    def Apagar(self):
        conversor.CaixaTexto.clear()

    def Copiar(self):
        conversor.CaixaTexto.selectAll()
        conversor.CaixaTexto.copy()

    def Colar(self):
        conversor.CaixaTexto.paste()
   

app = QtWidgets.QApplication([])
conversor = uic.loadUi('conversor.ui')

converter = ConverterTexto()

conversor.btn_maiuscula.clicked.connect(converter.Maiuscula)
conversor.btn_minuscula.clicked.connect(converter.Minuscula)
conversor.btn_primeiraletra.clicked.connect(converter.PrimeiraLetra)
conversor.btn_inverter.clicked.connect(converter.Inverter)
conversor.btn_apagar.clicked.connect(converter.Apagar)
conversor.btn_copiar.clicked.connect(converter.Copiar)
conversor.btn_colar.clicked.connect(converter.Colar)

conversor.show()
app.exec()