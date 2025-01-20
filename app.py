from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def buscar_tareas(palabra_clave, archivo_csv):
    resultados = []
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        encabezados = next(reader)  # Leer la primera fila como encabezados
        for fila in reader:
            if any(palabra_clave in columna for columna in fila):  # Verificar todas las columnas
                resultados.append(fila)
    return resultados, encabezados

def mostrar_resultados(resultados, encabezados):
    return render_template('index.html', resultados=resultados, encabezados=encabezados)

@app.route('/', methods=['GET', 'POST'])
def home():
    resultados = []
    encabezados = []
    if request.method == 'POST':
        palabra_clave = request.form['palabra_clave'].upper()
        archivo_csv = request.form['archivo_csv']
        resultados, encabezados = buscar_tareas(palabra_clave, archivo_csv)
    return mostrar_resultados(resultados, encabezados)

if __name__ == '__main__':
    app.run(debug=True)