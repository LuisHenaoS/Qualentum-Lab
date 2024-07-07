package org.example;

public class Calculator {
    private static void validate(int a, int b) {
        if (a < 0 || b < 0) {
            throw new IllegalArgumentException("No se permiten números negativos");
        }
        if (a > 999 || b > 999) {
            throw new IllegalArgumentException("No se permiten números de más de 3 cifras");
        }
    }

    private static int validateResult(int result) {
        if (result > 999) {
            throw new IllegalArgumentException("El resultado no puede tener más de 3 cifras");
        }
        return result;
    }

    public static int suma(int a, int b) {
        validate(a, b);
        return validateResult(a + b);
    }

    public static int resta(int a, int b) {
        validate(a, b);
        return validateResult(a - b);
    }

    public static int multiplica(int a, int b) {
        validate(a, b);
        return validateResult(a * b);
    }

    public static int divide(int a, int b) {
        validate(a, b);
        if (b == 0) {
            throw new IllegalArgumentException("No se puede dividir por cero");
        }
        return validateResult(a / b);
    }
}
