n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {0} é {1}. O triplo de {0} é {2}. A raiz quadrada de {0} é {3:.2f}.'.format(n, d, t, r))

# outra forma de fazer:
print('Outra forma de fazer:')

print('O dobro de {0} é {1}. \nO triplo de {0} é {2}. \nA raiz quadrada de {0} é {3:.2f}.'
      .format(n, (n*2), (n*3), (n ** (1/2))))
