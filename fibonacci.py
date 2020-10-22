number = int(input("Digite o número a ser avaliado: "))

def fibonacci(number):
    if number < 0 or number > 60 :
        print("Esse número não é valido. Digite um número entre 1 e 60.")
    elif number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return (fibonacci(number-1)+fibonacci(number-2))


print("Fib("+str(number)+") = "+ str(fibonacci(number)))