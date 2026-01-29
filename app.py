from flask import Flask, render_template, request , redirect , url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'Proyecto2'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/registro', methods = ['POST', 'GET'])
def agregarcuenta():
    if request.method == 'GET':
        return render_template('registro.html')
    
    elif request.method == "POST":
        id = request.form['id']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        mail = request.form['mail']
        contraseña = request.form['contraseña']
        telefono = request.form['telefono']
        edad = request.form['edad']
        localidad = request.form['localidad']
        dni = request.form['dni']
        genero = ['genero']
        cursor = mysql.connection.cursor()
        cursor.execute('insert into usuario () values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                    (id,nombre,apellido,mail,contraseña,telefono,edad,localidad,dni,genero))
        mysql.connection.commit()
        return redirect(url_for('cuenta'))

@app.route('/usuario')
def cuenta():
    cursor = mysql.connection.cursor()
    sql = ('SELECT * from usuario;')
    cursor.execute(sql)
    cuenta1 = cursor.fetchall()
    return render_template('cuenta.html', cuenta = cuenta1)

@app.route('/eliminar/cuenta/<string:id>')
def eliminar_cuenta(id):
    cursor = mysql.connection.cursor()
    sql = ('delete FROM usuario WHERE id = {0}'.format(id))
    cursor.execute(sql)
    mysql.connection.commit()
    return redirect(url_for('cuenta'))

@app.route('/editar/cuenta/<id>')
def editar(id):
    cursor = mysql.connection.cursor()
    sql = ('select * from usuario where id = {0}'.format(id))
    cursor.execute(sql)
    rpta = cursor.fetchall()
    return render_template('editar.html', datos = rpta[0])

@app.route('/actualizar/cuenta/<id>', methods = ['POST'])
def actualizar(id):
    if request.method == "POST":
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        mail = request.form['mail']
        contraseña = request.form['contraseña']
        telefono = request.form['telefono']
        localidad = request.form['localidad']
        genero = request.form['genero']
        cursor = mysql.connection.cursor()
        cursor.execute('''update usuario set 
                    nombre = %s,
                    apellido = %s,
                    mail = %s,
                    contraseña = %s,
                    telefono = %s,
                    localidad = %s,
                    genero = %s
                    where id = %s''', (nombre,apellido,mail,contraseña,telefono,localidad,genero,id))
        mysql.connection.commit()
        return redirect(url_for('cuenta'))

@app.route('/roomie/<id>', methods = ['POST', 'GET'])
def agregarroomie(id):
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        sql = ('SELECT * from usuario where id = {0}'.format(id))
        cursor.execute(sql)
        cuenta1 = cursor.fetchall()
        return render_template('fperfil.html', cuenta = cuenta1[0])
    
    elif request.method == "POST":
        descripcion = request.form['descripcion']
        redes = request.form['redes']
        ide = request.form['id']
        ocupacion = request.form['ocupacion']
        estudios = request.form['estudios']
        presupuesto = request.form['presupuesto']
        lugartiempo = request.form['lugartiempo']
        condiciones = request.form['condiciones']
        idiomas = request.form['idiomas']
        hijos = request.form['hijos']
        mascotas = request.form['mascotas']
        situacion = request.form['situacion']
        acompañante = request.form['acompañante']
        cursor = mysql.connection.cursor()
        cursor.execute('insert into roomie () values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                    (descripcion,redes,ide,ocupacion,estudios,presupuesto,lugartiempo,condiciones,idiomas,hijos,mascotas,situacion,acompañante))
        mysql.connection.commit()
        return redirect(url_for('perfil'))

@app.route('/perfil')
def perfil():
    cursor = mysql.connection.cursor()
    sql = ('SELECT * from usuario;')
    cursor.execute(sql)
    cuenta1 = cursor.fetchall()

    cursor = mysql.connection.cursor()
    sql = ('SELECT * from roomie;')
    cursor.execute(sql)
    perfiles1 = cursor.fetchall()
    return render_template('perfil.html', cuenta = cuenta1[0], perfiles = perfiles1)

@app.route('/verperfil/<id>', methods = ['GET'])
def verperfil(id):
    cursor = mysql.connection.cursor()

    cursor.execute(f'Select * from usuario where id = {id}')
    
    cuenta1 = cursor.fetchall()
    
    cursor.execute(f'Select * from roomie where id = {id}')
    perfil1 = cursor.fetchall()
    
    return render_template('verperfil.html', cuenta = cuenta1[0] , perfil = perfil1)

@app.route('/eliminar/perfil/<string:id>')
def eliminar_perfil(id):
    cursor = mysql.connection.cursor()
    sql = ('delete FROM roomie WHERE id = {0}'.format(id))
    cursor.execute(sql)
    mysql.connection.commit()
    return redirect(url_for('perfil'))

@app.route('/editar/perfil/<id>')
def editar_roomie(id):
    cursor = mysql.connection.cursor()
    sql = ('SELECT * from usuario where id = {0}'.format(id))
    cursor.execute(sql)
    cuenta1 = cursor.fetchall()

    cursor = mysql.connection.cursor()
    sql = ('SELECT * from roomie where id = {0}'.format(id))
    cursor.execute(sql)
    roomie1 = cursor.fetchall()
    return render_template('eroomie.html', roomie = roomie1, cuenta = cuenta1)

@app.route('/actualizar/perfil/<id>', methods = ['POST'])
def actualizar_roomie(id):
    if request.method == "POST":
        descripcion = request.form['descripcion']
        redes = request.form['redes']
        id = request.form['id']
        ocupacion = request.form['ocupacion']
        estudios = request.form['estudios']
        presupuesto = request.form['presupuesto']
        lugartiempo = request.form['lugartiempo']
        condiciones = request.form['condiciones']
        idiomas = request.form['idiomas']
        hijos = request.form['hijos']
        mascotas = request.form['mascotas']
        situacion = request.form['situacion']
        acompañante = request.form['acompañante']
        cursor = mysql.connection.cursor()
        cursor.execute('''update roomie set 
                    descripcion = %s,
                    redes = %s,
                    ocupacion = %s,
                    estudios = %s,
                    presupuesto = %s,
                    lugartiempo = %s,
                    condiciones = %s,
                    idiomas = %s,
                    hijos = %s,
                    mascotas = %s,
                    situacion = %s,
                    acompañante = %s
                    where id = %s''', (descripcion,redes,ocupacion,estudios,presupuesto,lugartiempo,condiciones,idiomas,hijos,mascotas,situacion,acompañante,id))
        mysql.connection.commit()
        return redirect(url_for('perfil'))

@app.route('/registro/inmueble/<id>', methods = ['GET','POST'])
def agregarinmueble(id):
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        sql = ('select * from usuario where id = {0}'.format(id))
        cursor.execute(sql)
        cuenta1 = cursor.fetchall()
        return render_template('finmueble.html', cuenta = cuenta1)
    
    elif request.method == 'POST':
        id = request.form['id']
        direccion = request.form['direccion']
        descripcion = request.form['descripcion']
        ambientes = request.form['ambientes']
        motivo = request.form['motivo']
        precio = request.form['precio']
        gastos = request.form['gastos']
        tiempo = request.form['tiempo']
        condiciones = request.form['condiciones']
        huespedes = request.form['huespedes']
        cursor = mysql.connection.cursor()
        cursor.execute('insert into inmueble () values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                    (id,direccion,descripcion,ambientes,motivo,precio,gastos,tiempo,condiciones,huespedes))
        mysql.connection.commit()
        return redirect(url_for('inmueble'))

@app.route('/inmueble')
def inmueble():
    cursor = mysql.connection.cursor()
    sql = ('SELECT * from usuario;')
    cursor.execute(sql)
    cuenta1 = cursor.fetchall()

    cursor = mysql.connection.cursor()
    sql = ('SELECT * from inmueble;')
    cursor.execute(sql)
    inmueble1 = cursor.fetchall()
    return render_template('inmueble.html', inmueble = inmueble1, cuenta = cuenta1)

@app.route('/verinmueble/<id>')
def verinmueble(id):
    cursor = mysql.connection.cursor()
    sql = ('select * from usuario where id = {0}'.format(id))
    cursor.execute(sql)
    cuenta1 = cursor.fetchall()

    cursor = mysql.connection.cursor()
    sql = ('select * from inmueble where id = {0}'.format(id))
    cursor.execute(sql)
    inmueble1 = cursor.fetchall()
    return render_template('verinmueble.html', inmueble = inmueble1, cuenta = cuenta1[0])

@app.route('/editar/inmueble/<id>')
def editar_inmueble(id):
    cursor = mysql.connection.cursor()
    sql = ('SELECT * from usuario where id = {0}'.format(id))
    cursor.execute(sql)
    cuenta1 = cursor.fetchall()

    cursor = mysql.connection.cursor()
    sql = ('SELECT * from inmueble where id = {0}'.format(id))
    cursor.execute(sql)
    inmueble1 = cursor.fetchall()
    return render_template('einmueble.html', inmueble = inmueble1, cuenta = cuenta1)

@app.route('/actualizar/inmueble/<id>', methods = ['POST'])
def actualizar_inmueble(id):
    if request.method == "POST":
        id = request.form['id']
        direccion = request.form['direccion']
        descripcion = request.form['descripcion']
        ambientes = request.form['ambientes']
        motivo = request.form['motivo']
        precio = request.form['precio']
        gastos = request.form['gastos']
        tiempo = request.form['tiempo']
        condiciones = request.form['condiciones']
        huespedes = request.form['huespedes']
        cursor = mysql.connection.cursor()
        cursor.execute('''update inmueble set 
                    direccion = %s,
                    descripcion = %s,
                    ambientes = %s,
                    motivo = %s,
                    precio = %s,
                    gastos = %s,
                    tiempo = %s,
                    condiciones = %s,
                    huespedes = %s
                    where id = %s''', (direccion,descripcion,ambientes,motivo,precio,gastos,tiempo,condiciones,huespedes,id))
        mysql.connection.commit()
        return redirect(url_for('inmueble'))

@app.route('/eliminar/inmueble/<string:id>')
def eliminar_inmueble(id):
    cursor = mysql.connection.cursor()
    sql = ('delete FROM inmueble WHERE id = {0}'.format(id))
    cursor.execute(sql)
    mysql.connection.commit()
    return redirect(url_for('inmueble'))

@app.route('/buscar', methods=['POST', 'GET'])
def buscar():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT roo.*, usu.nombre from roomie roo join usuario usu on roo.id = usu.id')
        roomie1 = cursor.fetchall()

        cursor = mysql.connection.cursor()
        sql = ('SELECT inm.*, usu.nombre from inmueble inm join usuario usu on inm.id = usu.id')
        cursor.execute(sql)
        inmueble1 = cursor.fetchall()
        return render_template('buscar.html', per = roomie1, inm = inmueble1)

    elif request.method == 'POST':
        ingreso1 = request.form['ingreso1'].strip()
        if not ingreso1:
            return render_template('buscar.html')        
        cursor = mysql.connection.cursor()
        cursor.execute('''SELECT * FROM roomie WHERE   
            roomie.descripcion LIKE %s OR
            roomie.redes LIKE %s OR
            roomie.id LIKE %s OR
            roomie.ocupacion LIKE %s OR
            roomie.estudios LIKE %s OR
            roomie.presupuesto LIKE %s OR
            roomie.lugartiempo LIKE %s OR
            roomie.condiciones LIKE %s OR
            roomie.idiomas LIKE %s OR
            roomie.situacion LIKE %s ''', ( f"%{ingreso1}%", f"%{ingreso1}%", f"%{ingreso1}%", f"%{ingreso1}%", f"%{ingreso1}%",f"%{ingreso1}%", f"%{ingreso1}%", f"%{ingreso1}%", f"%{ingreso1}%", f"%{ingreso1}%"))
        respuesta = cursor.fetchall()

        cursor = mysql.connection.cursor()
        cursor.execute('''SELECT * FROM inmueble WHERE   
            direccion LIKE %s OR
            descripcion LIKE %s OR
            ambientes LIKE %s OR
            motivo LIKE %s OR
            precio LIKE %s OR
            gastos LIKE %s OR
            tiempo LIKE %s OR
            condiciones LIKE %s OR
            huespedes LIKE %s OR
            id LIKE %s''', (f"%{ingreso1}%", f"%{ingreso1}%", f"%{ingreso1}%", f"%{ingreso1}%", f"%{ingreso1}%", f"%{ingreso1}%",f"%{ingreso1}%", f"%{ingreso1}%", f"%{ingreso1}%", f"%{ingreso1}%"))
        respuesta2 = cursor.fetchall()

        return render_template('buscador.html', per=respuesta, inm = respuesta2)
if __name__ == '__main__':
    app.run(port=3000, debug=True)

        # ide = respuesta[0]
        # idee = ide[2] 
        # cursor = mysql.connection.cursor()
        # cursor.execute('SELECT nombre, apellido FROM usuario WHERE usuario.id = %s', (idee))
        # respuesta3 = cursor.fetchall()