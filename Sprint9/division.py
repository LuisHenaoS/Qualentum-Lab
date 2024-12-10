def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

if __name__ == "__main__":
    print(dividir(5, 3))