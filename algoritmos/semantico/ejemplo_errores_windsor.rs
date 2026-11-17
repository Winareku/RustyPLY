// Casos de error semántico - Windsor Estrada

fn main() {
    let entero: i32 = 10;
    let flotante: f64 = 3.5;
    let texto: &str = "hola";
    let activo: bool = true;

    // Regla 1: Tipos incompatibles en operaciones aritméticas (+, -, *, /, %)
    let err1 = entero + flotante;
    let err2 = entero - texto;
    let err3 = activo * entero;

    // Regla 2: Condición en if / while no booleana
    if entero {
        let x: i32 = 1;
    }

    if flotante {
        let y: i32 = 2;
    }

    while 100 {
        let z: i32 = 3;
    }
}
