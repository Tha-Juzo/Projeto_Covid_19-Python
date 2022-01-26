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

# Configurando a fonte 1
# Nome da fonte, formato (B, U, I ou '') e o tamanho
pdf.set_font('Times', '', 12)

# Adicionando nome de autore no PDF
pdf.cell(0, 0, txt='Nome: Thauany Camile Juzo', align="J")

# Adicionando logo da KICK ao PDF
pdf.image(name="logo.png", w=25, h=10, y=5, x=180)

# Criando uma linha (ex: ------------------------)
pdf.line(5, 15, 205, 15)



# Parte 1
#----------------------------------------------------

# Adicionando título ao PDF
pdf.cell(-190, 20, txt='A Importância do Lockdown', align= 'C')

# Adicionando texto ao PDF
pdf.cell(0, 32, txt='No ano de 2020, fomos surpreendidos por uma pandemia, devido a um vírus reconhecido hoje como SARS-CoV-2,', align= 'J')
pdf.cell(-184, 42, txt='devido as diversas mutações que sofreu ao longo desses dois anos. A doença causada por esse vírus é a COVID-19,', align='C')
pdf.cell(173, 52, txt=' uma infecção respiratória aguda de elevada transmissibilidade, de distribuição global e potencialmente grave.', align= 'C')
pdf.cell(-175, 62, txt='Uma das medidas para combater o alastramento do vírus é o que conhecemos por "Lockdown", podendo ser', align='C')
pdf.cell(191, 72, txt='traduzido como "fechamento total", que se refere a medidas duras tomadas por governos para restringir radicalmente', align='C')
pdf.cell(-195, 82, txt='a circulação de pessoas. Seu objetivo é garantir o distanciamento social - prática defendida por cientistas, governos', align='C')
pdf.cell(161, 92, txt='e a OMS (ou Organização Mundial da Saúde) para reduzir os casos e mortes pelo coronavírus.', align='R')
pdf.cell(-139, 102, txt='Apesar de vários países terem adotado o método, e várias pesquisas sobre a eficácia do lockdown terem sido', align='C')
pdf.cell(140, 112, txt='realizadas, em nosso país, houve diversos estados que não adotaram a medida, e cidades do mesmo estado se ', align='C')
pdf.cell(-136, 122, txt='contradizendo, ou seja, enquanto umas adotavam, houve algumas que recusaram alegando que o método não iria', align='C') 
pdf.cell(6, 132, txt='funcionar em respectivo município.', align='C')
pdf.cell(115, 142, txt='O objetivo desse trabalho é mostrar a importância de aderir ao Lockdown, utilizando dados de duas cidades', align='C')
pdf.cell(-109, 152, txt='brasileiras: Araraquara e Bauru, respectivamente uma que adotou a medida e a outra que optou por não aderir.', align='C')


# Criando uma linha (ex: ------------------------)
pdf.line(5, 92, 205, 92)




# Parte 2
#----------------------------------------------------

# Adicionando título dos gráficos no PDF
pdf.cell(118, 172, txt='Gráfico que detalha a diferença entre casos e óbitos de Araraquara e Bauru', align="C")

# Adicionando as imagens dos gráfico no PDF
pdf.image(name="casos.png", w=210, h=100, y=102, x=5)
pdf.image(name="obitos.png", w=210, h=100, y=202, x=5)




# Parte 3
#----------------------------------------------------

# Adicionando outra página no PDF
pdf.add_page()

# Adicionando nome de autore no PDF
pdf.cell(0, 0, txt='Nome: Thauany Camile Juzo', align="J")

# Adicionando logo da KICK ao PDF
pdf.image(name="logo.png", w=25, h=10, y=5, x=180)

# Criando uma linha (ex: ------------------------)
pdf.line(5, 15, 205, 15)

pdf.cell(-190, 22, txt='Com os gráficos, é possível notar a diferença excessiva tanto do número de casos, quanto do número de óbitos', align='C')
pdf.cell(184, 32, txt='entre as cidades. Araraquara, que decidiu por aderir o Lockdown, seu número de casos contam com 24 mil,', align= 'C')
pdf.cell(-173, 42, txt='enquanto Bauru, seus números ultrapassam a marca de 55 mil casos. No caso de óbitos, Bauru continua liderando', align= 'C')
pdf.cell(80, 52, txt='o maior número com 1250, e Araraquara com 551 mortes.', align='C') 
pdf.cell(15,62, txt='Segundo os dados de 7 de abril divulgados pelo governo estadual em 2021, houve um registro da média de óbitos,', align= 'C')
pdf.cell(-22, 72, txt='que afirma a eficácia do lockdown, afinal em Araraquara houve uma registra média de 11,9 mortes por 100 mil', align= 'C')
pdf.cell(18, 82, txt='habitantes, e a taxa de Bauru no mesmo intervalo de tempo, conseguiu um valor bem mais alto: 26,4 mortes', align= 'C')
pdf.cell(-40, 92, txt='por 100 mil habitantes, sendo que as cidades tem respectivamente 238 mil e 379 mil habitantes.', align= 'C')

# Salvando o arquivo PDF
pdf.output('Covid 19.pdf')

print("O PDF foi criado com sucesso!")

os.system("pause")