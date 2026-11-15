// Algoritmo 3 (sintáctico) - César Moreira
// Ingreso de datos mediante read_line

let mut entrada=texto;
io::stdin().read_line(&mut entrada);

//Limpieza de la entrada
let entrada_limpia = entrada.trim();
let numero = entrada_limpia.parse::<i32>().unwrap();


// Definicion de una estructura
struct Persona {
    nombre: String,
    edad: i32,
}

// Instanciación de la estructura
let persona = Persona {
    nombre: "Cesar",
    edad: 20,
};