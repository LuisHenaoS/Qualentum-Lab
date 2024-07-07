import static org.junit.jupiter.api.Assertions.*;

import org.example.Calculator;
import org.junit.jupiter.api.Test;

public class CalculatorTest {

    @Test
    void testSumaValida() {
        assertEquals(579, Calculator.suma(123, 456));
    }

    @Test
    void testSumaConNumeroNegativo() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            Calculator.suma(-123, 456);
        });
        assertEquals("No se permiten números negativos", exception.getMessage());
    }

    @Test
    void testSumaConNumeroMayorATresCifras() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            Calculator.suma(1000, 1);
        });
        assertEquals("No se permiten números de más de 3 cifras", exception.getMessage());
    }

    @Test
    void testSumaConResultadoMayorATresCifras() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            Calculator.suma(500, 501);
        });
        assertEquals("El resultado no puede tener más de 3 cifras", exception.getMessage());
    }

    @Test
    void testRestaValida() {
        assertEquals(300, Calculator.resta(500, 200));
    }

    @Test
    void testRestaConNumeroNegativo() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            Calculator.resta(-500, 200);
        });
        assertEquals("No se permiten números negativos", exception.getMessage());
    }

    @Test
    void testMultiplicacionValida() {
        assertEquals(990, Calculator.multiplica(10, 99));
    }

    @Test
    void testMultiplicacionConNumeroNegativo() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            Calculator.multiplica(-10, 99);
        });
        assertEquals("No se permiten números negativos", exception.getMessage());
    }

    @Test
    void testMultiplicacionConResultadoMayorATresCifras() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            Calculator.multiplica(10, 100);
        });
        assertEquals("El resultado no puede tener más de 3 cifras", exception.getMessage());
    }

    @Test
    void testDivisionValida() {
        assertEquals(10, Calculator.divide(100, 10));
    }

    @Test
    void testDivisionPorCero() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            Calculator.divide(100, 0);
        });
        assertEquals("No se puede dividir por cero", exception.getMessage());
    }

    @Test
    void testDivisionConNumeroNegativo() {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            Calculator.divide(-100, 10);
        });
        assertEquals("No se permiten números negativos", exception.getMessage());
    }

}
