// Casos de error semántico generales (Grupo 11)
// Incluye pruebas para las 6 reglas semánticas:
// - Windsor: Aritmética y Condiciones de control
// - Israel: Mutabilidad y Asignación de tipos
// - César: Structs y Funciones

struct Punto {
    x: i32,
    y: i32,
}

struct Punto {
    z: i32,
}

fn duplicada() {}
fn duplicada() {}

fn operar(val: i32) -> i32 {
    let res: i32 = val + 1;
    return res;
}

fn main() {
    // === REGLAS DE WINDSOR ===
    // 1. Tipos incompatibles en operaciones aritméticas
    let a: i32 = 10;
    let b: f64 = 2.5;
    let err_arit1 = a + b;
    let err_arit2 = a - "texto";

    // 2. Condición en if/while no booleana
    if a {
        let x: i32 = 1;
    }
    while b {
        let y: i32 = 2;
    }

    // === REGLAS DE ISRAEL ===
    // 1. Reasignación de variable inmutable
    let inmutable: i32 = 100;
    inmutable = 200;

    // 2. Asignación de tipo incompatible
    let tipo_malo: i32 = "cadena";
    let mut numero: i32 = 10;
    numero = false;

    // === REGLAS DE CÉSAR ===
    // 1. Errores en instanciación de structs
    let p = Punto {
        x: "cien",
        w: 50,
    };

    // 2. Errores en llamadas a funciones
    let call1 = operar();
    let call2 = operar("texto");
    let call3 = no_declarada();
}
