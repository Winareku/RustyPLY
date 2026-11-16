// Algoritmo 2 (sintáctico) - Israel Romero

// Declaraciones de variables. Ampliar a medida que se agreguen reglas.

let a = 1;
let mut b = 2;
let c: i32 = 3;
let mut d: bool = true;
const K: i32 = 10;
let (x, y) = z;
let nombre: &str = "hola";
let s = String::from;

// Asignaciones

a = 5;
b += 3;
b -= 1;
b *= 2;
b /= 2;
b %= 3;

// Expresiones de comparación y lógicas

let mayor = a > b;
let menor = a < b;
let igual = a == b;
let diferente = a != b;
let mayor_igual = a >= b;
let menor_igual = a <= b;

let condicion1 = a > 0 && b < 10;
let condicion2 = a == 5 || b != 0;
let condicion3 = (a > b) && (b >= 2);

// Vectores y macros

let numeros = vec![1, 2, 3, 4, 5];
let vacio = vec![];
let repetidos = vec![0; 5];

println!("Valor de a: {}", a);
print!("Prueba de impresión");

// Estructura while

let mut contador = 0;
while contador < 10 {
    contador += 1;

    if contador == 5 {
        continue;
    }

    if contador == 8 {
        break;
    }
}

// Estructura loop

let mut intentos = 0;
loop {
    intentos += 1;

    if intentos >= 3 {
        break;
    }
}

// Funciones con parámetros

fn sumar(a: i32, b: i32) {
    let resultado = a + b;
}

fn multiplicar(a: i32, b: i32) -> i32 {
    return a * b;
}

fn obtener_valor() -> i32 {
    return 100;
}

fn verificar(a: i32, b: i32) -> bool {
    return a > b;
}

// Funciones y expresiones combinadas

fn calcular_promedio(a: i32, b: i32, c: i32) -> i32 {
    let suma = a + b + c;
    let promedio = suma / 3;

    return promedio;
}

fn ejecutar() {
    let resultado = calcular_promedio(10, 20, 30);
    let valido = verificar(resultado, 10);
    println!("Resultado: {}", resultado);
    return;
}

//Rangos
    for i in a..b { }
    for i in a..=b { }
 
    //Referencias, acceso y rutas
    let ref1 = &a;
    let ref2 = &mut a;
    let deref = *ref1;
    let campo = punto.x;
    let ruta = std::io::stdin();
    let mapa = HashMap::new();
    mapa.read_line(&mut entrada);
 
    //Flechas
    fn doble(x: bool) -> bool { x }
    match a { b => c, _ => d }
 
    //Clausuras (usan | y ||)
    let cl1 = |a, b| a + b;
    let cl2 = || a;
    let cl3 = |a| a || b;
 
    //Operadores pegados sin espacios
    let p1 = a+b-c*d/e%f;
    let p2 = a<=b&&c>=d||e!=f;
    let p3 = a..=b;
    let p4 = a..b;
    x+=y;
    x-=y;

    //Rangos
    let rango = 0..10;
    let inclusivo = 0..=10;

    //Referencias
    let referencia = &variable;
    let mutable = &mut variable;
    let valor = *referencia;

    //Asignacion a campos e indices
    persona.edad = 20;
    vector[0] = 100;
    *referencia = 30;

    //Variables static
    static MAXIMO: i32 = 100;
    static mut CONTADOR: i32 = 0;
    