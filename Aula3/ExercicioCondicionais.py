#Questão 1

print("========== Sistema de classificação de crédito ==========")
idade = int(input("Digite a idade: "))
salario = float(input("Salário mensal R$: "))
divida_atual = float(input("Valor da dívida atual R$: "))
tempo_emprego = int(input("Tempo de emprego (em meses): "))
valor_solicitado = float(input("Valor solicitado de empréstimo R$: "))
parcelas = int(input("Número de parcelas: "))

comp_atual_pct = (divida_atual / salario) * 100
valor_parcela = valor_solicitado / parcelas
comp_nova_parc_pct = (valor_parcela / salario) * 100
comp_total_pct = comp_nova_parc_pct + comp_atual_pct

resultado = ""
motivo = ""

if 21 <= idade <= 65 and salario >= 2500.0 and tempo_emprego >= 12 and comp_atual_pct <= 30.0 and comp_nova_parcela_pct <= 25.0:
    resultado = "Aprovada"

elif 21 <= idade <= 65 and salario >= 2500.0 and tempo_emprego >= 6 and comp_total_pct <= 50.0:
    resultado = "Aprovada com restrições"

else:
    resultado = "Reprovada"

    if not (21 <= idade <= 65):
        motivo = f"Idade ({idade} anos) fora da faixa permitida (21 a 65 anos)."
    elif salario < 2500.0:
        motivo = f"Salário (R$ {salario:.2f}) inferior ao mínimo exigido (R$ 2.500,00)."
    elif tempo_emprego < 6:
        motivo = f"Tempo de emprego ({tempo_emprego} meses) inferior ao mínimo de 6 meses."
    elif comp_total_pct > 50.0:
        motivo = f"Comprometimento total ({comp_total_pct:.1f}%) excede o limite máximo de 50% do salário."
    else:
        motivo = "Política interna de risco de crédito não atendida."

    print("=====RESULTADO DA ANÁLISE=====")
    print(f"Valor da parcela: R$ {valor_parcela:.2f}")
    print(f"Percentual atual de comprometimento: {comp_atual_pct:.2f}%")
    print(f"Novo percentual de comprometimento (com a parcela): {comp_total_pct:.2f}%")
    print(f"Resultado da análise: {resultado}")
    if resultado == "Reprovada":
        print(f"Motivo principal: {motivo}")

#Questão 2

print("=====Cálculo completo de imposto de renda=====")

salario_bruto = float(input("Informe seu salario bruto: R$ "))
qtd_dependentes = int(input("Informe a quantidade de dependentes: "))
previdencia =  float(input("Valor pago em Previdencia: R$ "))
pensao = float(input("Valor pago em Pensão: R$ "))

deducao_dependentes = qtd_dependentes * 250.0
total_deducoes = previdencia + pensao + deducao_dependentes

if total_deducoes > salario_bruto:
    base_calculo = 0.0
    aliquota_str = "Isento"
    imposto = 0.0
    motivo_alerta = "Aviso: O deduções supera o salario bruto."

else:
    base_calculo = salario_bruto - total_deducoes
    motivo_alerta = None

if base_calculo <= 2500.0:
    aliquota_pct = 0.0
    aliquota_str = "Isento"
elif base_calculo <= 3500.0:
    aliquota_pct = 7.5
    aliquota_str = "7,5%"
elif base_calculo <= 5000.0:
    aliquota_pct = 15.0
    aliquota_str = "15,0%"
elif base_calculo <= 7500.0:
    aliquota_pct = 22.5
    aliquota_str = "22,5%"
else:
    aliquota_pct = 27.5
    aliquota_str = "27,5%"

imposto = base_calculo * (aliquota_pct / 100)

salario_liquido = salario_bruto - previdencia - pensao - imposto

print("=====RESUMO DO CÁLCULO=====")
print(f"Salário Bruto:R$ {salario_bruto:.2f}")
print(f"Total de Deduções:R$ {total_deducoes:.2f}")
print(f"Base de Cálculo:R$ {base_calculo:.2f}")
print(f"Alíquota:{aliquota_str}")
print(f"Imposto a Pagar:R$ {imposto:.2f}")
print(f"Salário Líquido:R$ {salario_liquido:.2f}")

if motivo_alerta:
    print(f"\n{motivo_alerta}")

#Questao 3

print("=====Sistema de avaliação academica=====")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
frequencia = float(input("Digite o percentual de frequencia (0 a 100): "))
atividade_entregue = int(input("Digite quantas atividades foram entregues: "))
total_atividade = int(input("Digite o total de atividades: "))

media = (nota1 + nota2 + nota3) / 3
pct_atividade_entregue = (total_atividade/atividade_entregue) * 100

print(f"\nMédia: {media:.2f}")
print(f"\nAtividades: {pct_atividade_entregue:.1f}%")

if media >= 9 and frequencia >= 90 and pct_atividade_entregue >= 100:
    print("Aprovado com excelência")
    print("Motivo: Atingiu o nível máximo em tudo!")
elif media >= 7 and frequencia >= 75 and pct_atividade_entregue >= 70:
    print("Aprovado")
    print("Motivo para não ter Excelência: Média abaixo de 9, frequência abaixo de 90% ou faltou entregar atividades.")
elif media >= 5 and media <= 6.99 and frequencia >= 75:
    print("Recuperação")
    print("Motivo para não ter Aprovado: Média abaixo de 7 ou entregou menos de 70% das atividades.")
elif frequencia < 75:
    print("Reprovado por frequencia")
    print("Motivo: Frequência abaixo de 75%.")
elif media < 5:
    print("Reprovado por nota")
    print("Motivo: Média abaixo de 5.")

#Questao 4

peso = float(input("Peso da encomenda (kg): "))
distancia = float(input("Distância (km): "))
tipo_entrega = input("Tipo de entrega (normal, expressa, urgente): ").strip().lower()
assinante = input("Cliente é assinante? (sim/nao): ").strip().lower() == "sim"
valor_compra = float(input("Valor da compra (R$): "))

frete_gratis = assinante and valor_compra >= 2000 and tipo_entrega == "normal" and peso <= 10

if frete_gratis:
    frete_final = 0.0
    taxa_peso = 0.0
    taxa_distancia = 0.0
    adicional_tipo = 0.0
    adicional_peso_extra = 0.0
    adicional_distancia_extra = 0.0
    desconto_aplicado_pct = 0.0
    valor_desconto = 0.0
else:
    taxa_peso = peso * 2.50
    taxa_distancia = distancia * 0.30
    subtotal_base = taxa_peso + taxa_distancia

    if tipo_entrega == "expressa":
        adicional_tipo = subtotal_base * 0.30
    elif tipo_entrega == "urgente":
        adicional_tipo = subtotal_base * 0.60
    else:
        adicional_tipo = 0.0

    adicional_peso_extra = 80.0 if peso > 30 else 0.0
    adicional_distancia_extra = 100.0 if distancia > 500 else 0.0

    subtotal_bruto = subtotal_base + adicional_tipo + adicional_peso_extra + adicional_distancia_extra

    desconto_pct = 0.0
    if assinante:
        desconto_pct += 15.0
    if valor_compra > 1000:
        desconto_pct += 10.0

    desconto_aplicado_pct = min(desconto_pct, 20.0)
    valor_desconto = subtotal_bruto * (desconto_aplicado_pct / 100)

    frete_final = subtotal_bruto - valor_desconto

print("\n--- COMPONENTES DO CÁLCULO ---")
if frete_gratis:
    print("FRETE GRÁTIS APLICADO! (Atende a todos os critérios de isenção)")
else:
    print(f"Taxa por peso ({peso} kg): R$ {taxa_peso:.2f}")
    print(f"Taxa por distância ({distancia} km): R$ {taxa_distancia:.2f}")
    print(f"Adicional tipo de entrega ({tipo_entrega}): R$ {adicional_tipo:.2f}")
    print(f"Adicional de peso extra (>30kg): R$ {adicional_peso_extra:.2f}")
    print(f"Adicional de distância longa (>500km): R$ {adicional_distancia_extra:.2f}")
    print(f"Subtotal Bruto: R$ {subtotal_bruto:.2f}")
    print(f"Desconto aplicado: {desconto_aplicado_pct:.0f}% (-R$ {valor_desconto:.2f})")

print(f"\nValor Total do Frete: R$ {frete_final:.2f}")

#Questao 5

# Entrada de dados
renda = float(input("Digite sua renda mensal (R$): "))

print("\n--- INFORME SEUS GASTOS MENSAIS ---")
moradia = float(input("Gastos com moradia: R$ "))
alimentacao = float(input("Gastos com alimentação: R$ "))
transporte = float(input("Gastos com transporte: R$ "))
saude = float(input("Gastos com saúde: R$ "))
educacao = float(input("Gastos com educação: R$ "))
lazer = float(input("Gastos com lazer: R$ "))
dividas = float(input("Gastos com dívidas: R$ "))

# Cálculos
total_despesas = moradia + alimentacao + transporte + saude + educacao + lazer + dividas
saldo_mensal = renda - total_despesas

if renda > 0:
    pct_comprometido = (total_despesas / renda) * 100
    pct_dividas = (dividas / renda) * 100
else:
    pct_comprometido = 0.0
    pct_dividas = 0.0

# Regras de Classificação
# 1. Insolvência: Despesas maiores que a renda e saldo negativo superior a 20% da renda (comprometimento > 120%)
if saldo_mensal < 0 and pct_comprometido > 120:
    situacao = "Insolvência"
    recomendacao = (
        "SITUAÇÃO DE EMERGÊNCIA: Seu orçamento está em déficit severo.\n"
        "- Busque renegociar imediatamente as dívidas com os credores.\n"
        "- Liste todos os gastos variáveis (lazer, compras) e corte-os temporariamente.\n"
        "- Procure fontes de renda extra para cobrir o déficit antes de recorrer a mais empréstimos."
    )

# 2. Crítica: Comprometimento acima de 85% OU dívidas acima de 35% (ou saldo negativo)
elif pct_comprometido > 85 or pct_dividas > 35 or saldo_mensal < 0:
    situacao = "Crítica"
    recomendacao = (
        "ALERTA VERMELHO: O comprometimento da sua renda está muito alto.\n"
        "- Reduza imediatamente os gastos não essenciais (lazer e supérfluos).\n"
        "- Priorize a quitação das dívidas de juros mais altos (como cartão de crédito e cheque especial).\n"
        "- Evite assumir qualquer novo parcelamento ou financiamento."
    )

# 3. Atenção: Comprometimento total entre 70% e 85%
elif 70 <= pct_comprometido <= 85:
    situacao = "Atenção"
    recomendacao = (
        "CUIDADO: Seu orçamento está equilibrado no limite, mas vulnerável a imprevistos.\n"
        "- Reavalie assinaturas, serviços de streaming e refeições fora de casa para abrir margem.\n"
        "- Comece a montar uma reserva de emergência guardando uma pequena quantia todo mês.\n"
        "- Acompanhe de perto suas faturas para o comprometimento não ultrapassar 85%."
    )

# 4. Saudável: Comprometimento até 70% e dívidas até 20%
else:
    situacao = "Saudável"
    recomendacao = (
        "PARABÉNS! Suas finanças estão bem organizadas.\n"
        "- Mantenha ou amplie sua reserva de emergência (de 3 a 6 meses do seu custo de vida).\n"
        "- Avalie opções de investimento para objetivos de médio e longo prazo (CDBs, Tesouro Direto, etc.).\n"
        "- Siga mantendo as dívidas abaixo do limite de 20% da sua renda."
    )

# Apresentação dos resultados
print("\n" + "="*40)
print("        DIAGNÓSTICO FINANCEIRO        ")
print("="*40)
print(f"Renda Mensal:             R$ {renda:.2f}")
print(f"Total de Despesas:        R$ {total_despesas:.2f}")
print(f"Saldo Mensal:             R$ {saldo_mensal:.2f}")
print(f"Renda Comprometida:       {pct_comprometido:.1f}%")
print(f"Comprometido com Dívidas: {pct_dividas:.1f}%")
print("-" * 40)
print(f"Classificação: {situacao}")
print("-" * 40)
print("Recomendação:")
print(recomendacao)
print("="*40)