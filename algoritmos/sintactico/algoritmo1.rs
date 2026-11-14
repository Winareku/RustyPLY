// Algoritmo 1 (sintáctico) - Windsor Estrada
// Impresión, aritmética, arreglos, tuplas, if/else, fn sin retorno y clausuras.

fn main() {
    // Datos: tuplas y arreglos
    let datos = (10, 20);
    let unidad = ();
    let uno = (5,);
    let primero = datos.0;
    let arreglo = [1, 2, 3, 4, 5];
    let ceros = [0; 5];
    let x = arreglo[0];
    let tipado: [i32; 3] = [1, 2, 3];
    let par: (i32, bool) = (1, true);

    // Expresiones aritméticas
    let suma = 1 + 2 * 3 - 4 / 2 % 3;
    let neg = -suma;
    let agrupada = (1 + 2) * -3;
    let conv = suma as f64;

    // Impresión
    println!("Suma: {}", suma);
    print!("Hola");
    println!();

    // Control
    if activo {
        println!("activo");
    } else if otro {
        println!("otro");
    } else {
        println!("ninguno");
    }
    let v = if activo { 1 } else { 2 };

    // Clausuras
    let cl1 = |a, b| a + b;
    let cl2 = || 5;
    let cl3 = move |n: i32| { n * 2 };

    {
        let interno = arreglo[1] + datos.1;
    }
}

fn saludar() {
    println!("Hola");
}
