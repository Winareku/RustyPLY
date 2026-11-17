// Casos de error semántico - César Moreira
// Reglas: Structs y Funciones

struct Persona {
    nombre: &str,
    edad: i32,
}

// Error 1: Duplicación de struct en el mismo ámbito
struct Persona {
    id: i32,
}

fn saludar(nombre: &str, edad: i32) -> &str {
    return nombre;
}

// Error 2: Duplicación de función en el mismo ámbito
fn saludar() {}

fn main() {
    // Error 3: Instanciación con campos faltantes, campos extra y tipos incorrectos
    let persona: Persona = Persona {
        nombre: 25,
        activo: true,
    };

    // Error 4: Llamada con cantidad incorrecta de argumentos
    let s1 = saludar("Ana");

    // Error 5: Llamada con tipos incompatibles en los argumentos
    let s2 = saludar(123, "veinte");

    // Error 6: Llamada a función no declarada
    let no_existe = funcion_inexistente();
}
