// Casos de error semántico - Israel Romero
// Reglas: Inmutabilidad y compatibilidad de tipos en asignación y declaración

fn main() {
    // Regla 1: Intento de reasignación a una variable inmutable
    let inmutable: i32 = 10;
    inmutable = 20;

    let mensaje: &str = "hola";
    mensaje = "mundo";

    // Regla 2: Incompatibilidad de tipos en declaración
    let texto: i32 = "cadena";
    let valor_bool: f64 = true;

    // Regla 2: Incompatibilidad de tipos en reasignación de variable mutable
    let mut numero: i32 = 5;
    numero = true;
    numero = "otro texto";

    let mut decimal: f64 = 1.25;
    decimal = false;
}
