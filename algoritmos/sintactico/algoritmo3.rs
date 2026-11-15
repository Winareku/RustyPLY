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

//Acceso a campos de la estructura
let nombre_persona = persona.nombre;
let edad_persona = persona.edad;


// Bloque impl para la estructura Persona
impl Persona {
    // Función asociada para crear una Persona
    fn new(nombre: String, edad: i32) -> Self {
        Self {
            nombre: nombre,
            edad: edad,
        }
    }


    //Metodo que recibe una referencia a self
    fn mostrar_nombre(&self) {
        println!("{}", self.nombre);
    }
}



//Llamada a la funcion asociada
let otra_persona = Persona::new("Ana", 30);



// Llamada al metodo con self
otra_persona.mostrar_nombre();