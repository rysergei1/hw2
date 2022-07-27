print('С клавиатуры задайте сумму займа:')
s = int(input())
print('Напишите количество лет займа:')
n = int(input())
print('Под какой процент хотите займ?')
p = int(input()) / 100
m = round((s * p * (1 + p) ** n) / (12 * ((1 + p) ** n - 1)))
total_amount = m * n * 12
overpayment = total_amount - s
print(f'Месячная выплата по займу составит: {m}, за весь срок: {total_amount}, сумма переплат: {overpayment}')
