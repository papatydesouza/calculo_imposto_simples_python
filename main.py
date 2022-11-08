def soma_imposto (imposto, custo):
    valor = (custo + (custo * (imposto/100)))
    return valor

imposto = float(input("Digite o percentual de imposto a ser considerado no produto: "))
custo = float(input("Digite o custo cheio (sem impostos) do produto: "))
print("O valor final do produto com o imposto é de R${}" .format(soma_imposto(imposto, custo)))