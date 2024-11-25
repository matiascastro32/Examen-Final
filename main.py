from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])

        # Calcular el precio total
        precio_por_tarro = 9000  # Cada tarro cuesta $9000
        total_sin_descuento = cantidad_tarros * precio_por_tarro

        # Calcular el descuento según la edad
        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15  # 15% de descuento
        elif edad > 30:
            descuento = total_sin_descuento * 0.25  # 25% de descuento
        else:
            descuento = 0  # No hay descuento para menores de 18 años

        # Calcular el total con descuento
        total_con_descuento = total_sin_descuento - descuento

        # Renderizar la plantilla con los resultados
        return render_template('ejercicio1.html',
                               nombre=nombre,
                               total_sin_descuento=total_sin_descuento,
                               descuento=descuento,
                               total_con_descuento=total_con_descuento)

    # Si el método es GET, mostrar el formulario vacío
    return render_template('ejercicio1.html',
                           nombre=None,
                           total_sin_descuento=None,
                           descuento=None,
                           total_con_descuento=None)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    usuarios = {
        'juan': 'admin',
        'pepe': 'user'
    }

    mensaje = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario in usuarios and usuarios[usuario] == contrasena:
            if usuario == 'juan':
                mensaje = f"Bienvenido administrador {usuario}"
            else:
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
