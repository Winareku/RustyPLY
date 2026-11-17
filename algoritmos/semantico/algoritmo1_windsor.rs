// Algoritmo 1 (semántico) - Windsor Estrada
// Pruebas semánticas para operaciones aritméticas compatibles y condiciones de control

fn main() {
    // Operaciones aritméticas válidas con tipos compatibles (i32)
    let a: i32 = 10;
    let b: i32 = 20;
    let suma: i32 = a + b;
    let resta: i32 = b - a;
    let producto: i32 = suma * 2;
    let division: i32 = producto / 2;
    let resto: i32 = division % 3;

    // Operaciones aritméticas válidas con f64
    let x: f64 = 1.5;
    let y: f64 = 2.5;
    let total_flotante: f64 = x + y;

    // Condiciones booleanas válidas en estructuras de control
    let activo: bool = true;
    let mayor: bool = a < b;

    if activo {
        let ok: i32 = 1;
    } else if mayor {
        let ok: i32 = 2;
    } else {
        let ok: i32 = 0;
    }

    let mut contador: i32 = 0;
    while contador < 5 {
        contador = contador + 1;
    }
}
