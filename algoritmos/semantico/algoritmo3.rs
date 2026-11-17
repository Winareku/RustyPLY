// Algoritmo 3 (semántico) - César Moreira
// Pruebas válidas de definición/instanciación de structs y llamadas a funciones

struct Persona {
    nombre: &str,
    edad: i32,
}

fn calcular_doble(numero: i32) -> i32 {
    let res: i32 = numero * 2;
    return res;
}

fn saludar(nombre: &str) {
    let mensaje: &str = nombre;
}

fn main() {
    let persona: Persona = Persona {
        nombre: "Carlos",
        edad: 28,
    };

    let doble_edad: i32 = calcular_doble(persona.edad);
    saludar(persona.nombre);
}
