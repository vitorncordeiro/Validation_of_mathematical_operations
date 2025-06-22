from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = ""
    erro = ""
    questao = ""

    if request.method == 'POST':
        questao = request.form.get('questao')

        try:
            if questao == 'quest1':
                num = float(request.form.get('num'))
                if num >= 0:
                    resultado = f"Raiz: {math.sqrt(num):.2f}"
                else:
                    erro = "Não é possível calcular a raiz de um número negativo."

            elif questao == 'quest2':
                num = float(request.form.get('num'))
                den = float(request.form.get('den'))
                if den != 0:
                    resultado = f"Resultado: {num / den:.2f}"
                else:
                    erro = "Não é possível dividir por zero."

            elif questao == 'quest3':
                log = float(request.form.get('log'))
                if log > 0:
                    resultado = f"Log10: {math.log10(log):.2f}"
                else:
                    erro = "O logaritmo deve ser maior que zero."

            elif questao == 'quest4':
                valor = float(request.form.get('valor'))
                base = float(request.form.get('base'))
                if valor > 0 and base > 0 and base != 1:
                    resultado = f"Log base {base}: {math.log(valor, base):.2f}"
                else:
                    erro = "Valor > 0 e base > 0 ≠ 1."

            elif questao == 'quest5':
                num = float(request.form.get('num'))
                resultado = f"Raiz cúbica: {num**(1/3):.2f}"

            elif questao == 'quest6':
                valor_n = request.form.get('n')
                if valor_n:
                    try:
                        n = float(valor_n)
                        if n.is_integer() and n >= 0:
                            resultado = f"Fatorial: {math.factorial(int(n))}"
                        else:
                            erro = "Digite um número inteiro maior ou igual a zero."
                    except ValueError:
                        erro = "Valor inválido. Digite um número inteiro."
                else:
                    erro = "Por favor, preencha o campo com um número."

            elif questao == 'quest7':
                x = float(request.form.get('x'))
                if x >= 0:
                    resultado = f"Módulo da raiz: {abs(math.sqrt(x)):.2f}"
                else:
                    erro = "Não é possível raiz de número negativo."

            elif questao == 'quest8':
                base = float(request.form.get('base'))
                expoente = float(request.form.get('expoente'))
                if base >= 0:
                    resultado = f"{base} elevado a {expoente} = {base ** expoente:.2f}"
                else:
                    erro = "Base negativa com expoente fracionário não é válida."

            elif questao == 'quest9':
                num = float(request.form.get('num'))
                if num >= 0:
                    resultado = f"Raiz quarta: {math.pow(num, 1/4):.2f}"
                else:
                    erro = "Raiz de índice par exige número ≥ 0."

            elif questao == 'quest10':
                try:
                    a = float(request.form.get('a'))
                    b = float(request.form.get('b'))
                    c = float(request.form.get('c'))

                    if a == 0:
                        erro = "O coeficiente 'a' não pode ser zero."
                    else:
                        delta = b**2 - 4 * a * c

                        if delta < 0:
                            erro = "Delta negativo. Não existem raízes reais."
                        elif delta == 0:
                            x = -b / (2 * a)
                            resultado = f"Raiz única: x = {x:.2f}"
                        else:
                            x1 = (-b + math.sqrt(delta)) / (2 * a)
                            x2 = (-b - math.sqrt(delta)) / (2 * a)
                            resultado = f"x₁ = {x1:.2f}, x₂ = {x2:.2f}"
                except:
                    erro = "Valores inválidos. Use apenas números."

        except ValueError:
            erro = "Insira apenas números válidos."

    return render_template("index.html", resultado=resultado, erro=erro, questao=questao)

if __name__ == '__main__':
    app.run(debug=True)
