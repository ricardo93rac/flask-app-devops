from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__, static_folder='static')

def conectar_db():
    return sqlite3.connect('database.db')

with conectar_db() as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY, nombre TEXT, precio REAL)")
    
#Ruta Principal para mostrar prodcutos

@app.route('/')
def mostrar_productos():
    conn = conectar_db()
    productos = conn.execute("SELECT * FROM productos").fetchall()
    conn.close()
    return render_template('index.html', productos=productos)

#Agregar un producto
@app.route('/agregar', methods=['POST'])
def agregar_producto():
    nombre = request.form['nombre']
    precio = request.form['precio']
    
    conn = conectar_db()
    conn.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", (nombre, precio))
    conn.commit()
    conn.close()    
    return redirect(url_for('mostrar_productos'))

#Eliminar un producto
@app.route('/eliminar/<int:id>')
def eliminar_producto(id):
    conn = conectar_db()
    conn.execute("DELETE FROM productos WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('mostrar_productos'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)