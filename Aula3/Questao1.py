def analisar_credito():
    print("--- Análise de Solicitação de Crédito ---\n")

    # Entrada de dados
    idade = int(input("Idade: "))
    salario = float(input("Salário mensal (R$): "))
    divida_atual = float(input("Valor da dívida atual (R$): "))
    tempo_emprego = int(input("Tempo de emprego (em meses): "))
    valor_solicitado = float(input("Valor solicitado de empréstimo (R$): "))
    parcelas = int(input("Número de parcelas: "))

    # Cálculos
    comp_atual_pct = (divida_atual / salario) * 100
    valor_parcela = valor_solicitado / parcelas
    comp_nova_parcela_pct = (valor_parcela / salario) * 100
    comp_total_pct = comp_atual_pct + comp_nova_parcela_pct

    # Variáveis de controle do resultado
    resultado = ""
    motivo = ""

    # 1. Teste de aprovação completa
    if (21 <= idade <= 65) and \
            (salario >= 2500.0) and \
            (tempo_emprego >= 12) and \
            (comp_atual_pct <= 30.0) and \
            (comp_nova_parcela_pct <= 25.0):
        resultado = "Aprovada"

    # 2. Teste de aprovação com restrições
    elif (21 <= idade <= 65) and \
            (salario >= 2500.0) and \
            (tempo_emprego >= 6) and \
            (comp_total_pct <= 50.0):
        resultado = "Aprovada com restrições"

    # 3. Reprovação e identificação do motivo principal
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

    # Apresentação dos resultados
    print("\n----------------------------------------")
    print("        RESULTADO DA ANÁLISE            ")
    print("----------------------------------------")
    print(f"Valor da parcela: R$ {valor_parcela:.2f}")
    print(f"Percentual atual de comprometimento: {comp_atual_pct:.2f}%")
    print(f"Novo percentual de comprometimento (com a parcela): {comp_total_pct:.2f}%")
    print(f"Resultado da análise: {resultado}")

    if resultado == "Reprovada":
        print(f"Motivo principal: {motivo}")
    print("----------------------------------------")


# Executa o programa
if __name__ == "__main__":
    analisar_credito()