def palindromo(palavra):
    aux = ''
    for i in range(len(palavra)):
        for j in range(len(palavra), i, -1):
            if palavra[i:j] == ''.join(reversed(palavra[i:j])):
                if len(aux) < len(palavra[i:j]):
                    aux = palavra[i:j]
    return aux

print(palindromo("bolovo"))