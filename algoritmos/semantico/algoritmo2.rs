// Algoritmo 2 para reglas_israel.py
// Israel Romero

fn main() {

    // PRUEBA 1: Declaraciones validas de distintos tipos
    let edad: i32 = 20;
    let precio: f64 = 15.50;
    let activo: bool = true;
    let mensaje: &str = "Hola";

    // PRUEBA 2: Acceso a variables declaradas
    let copia_edad: i32 = edad;
    let copia_precio: f64 = precio;
    let copia_activo: bool = activo;
    let copia_mensaje: &str = mensaje;

    // PRUEBA 3: Declaracion y reasignacion de variable mutable
    let mut contador: i32 = 0;
    contador = 10;
    contador = 25;

    // PRUEBA 4: Operaciones con tipos numericos iguales
    let suma: i32 = 10 + 5;
    let resta: i32 = 20 - 3;
    let multiplicacion: i32 = 4 * 5;
    let division: i32 = 20 / 2;

    let suma_decimal: f64 = 10.5 + 2.5;
    let resta_decimal: f64 = 15.5 - 5.0;

    // PRUEBA 5: Ambito de bloque
    {
        let variable_local: i32 = 100;
        let copia_local: i32 = variable_local;

        let mut temporal: i32 = 1;
        temporal = 2;
    }

    // PRUEBA 6: Variables mutables de tipo decimal
    let mut saldo: f64 = 100.0;
    saldo = 75.5;

    // PRUEBA 7: Declaraciones inmutables sin reasignacion
    let limite: i32 = 50;
    let limite_copia: i32 = limite;
}
