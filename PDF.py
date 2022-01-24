import os
from fpdf import FPDF

# Criando um PDF
# P = documento na vertical
# L = documento na horizontal
# Medidas do documento = mm, cm, in
# Formatos de documento = A3, A4, A5, Latter e Legal.
pdf = FPDF('P', 'mm', 'A4')

# Criando uma página para o PDF
pdf.add_page()

# Configurando a fonte
# Nome da fonte, formato (B, U, I ou '') e o tamanho
pdf.set_font('Times', '', 16)

# Adicionando texto no PDF
pdf.cell(0, 0, 'Gráfico que detalha a diferença entre casos e óbitos de Araraquara e Bauru')

# Criando uma linha (ex: ------------------------)
pdf.line(0, 0)

# Adicionando as imagens no PDF
pdf.image(name="casos.png")
pdf.image(name="obitos.png")

# Salvando o arquivo PDF
pdf.output('Covid 19.pdf')

print("O PDF foi criado com sucesso!")

os.system("pause")