from flask import Flask, jsonify, request

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="banco"
)

app = Flask(__name__)

#Create
@app.route('/api/notas', methods=['POST'])
def add_nota():
    cursor = db.cursor()
    title = request.json['title']
    content = request.json['content']
    cursor.execute("INSERT INTO notas (title, content) VALUES (%s, %s)", (title, content))
    db.commit()
    return jsonify({'message': 'Nota adicionada com sucesso'})


#Read
@app.route('/api/notas', methods=['GET'])
def get_notas():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM notas")
    notas = cursor.fetchall()
    return jsonify(notas)

#Update
@app.route('/api/notas/<int:id>', methods=['PUT'])
def update_nota(id):
    cursor = db.cursor()
    title = request.json['title']
    content = request.json['content']
    cursor.execute("UPDATE notas SET title=%s, content=%s WHERE id=%s", (title, content, id))
    db.commit()
    return jsonify({'message': 'Nota atualizada com sucesso'})

#Delete
@app.route('/api/notas/<int:id>', methods=['DELETE'])
def delete_nota(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM notas WHERE id=%s", (id,))
    db.commit()
    return jsonify({'message': 'Nota deletada com sucesso'})

if __name__ == '__main__':
    app.run(debug=True)
