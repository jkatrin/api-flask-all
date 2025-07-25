#Importar
from flask import Flask, make_response, jsonify, request
from collections import OrderedDict
from database import get_db_connection


#Instaciar
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#Função está marcada como rota
#@ = decorator | app.route = rota da API
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()

        cursor.close()
        conn.close()

        resposta = OrderedDict()
        resposta["mensagem"] = "Lista de usuarios."
        resposta["dados"] = usuarios

        return make_response(jsonify(resposta),200)
    
    except Exception as e:
        print(str(e))
        return make_response(jsonify(erro="Houve um problema na nossa API."),500)


@app.route('/usuarios', methods=['POST'])
def create_usuarios():
    usuario = request.json

    campos_esperados = ['nome','idade','altura','genero']
    for campo in campos_esperados:
        if campo not in usuario:
            return make_response(
                jsonify(
                    mensagem= f"O campo '{campo}' é obrigatório."
                ),400
            )

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO usuarios (nome, idade, altura, genero)
            VALUES (%s,%s,%s,%s)
        """
        valores = (
            usuario['nome'],
            usuario['idade'],
            usuario['altura'],
            usuario['genero']
        )

        cursor.execute(query, valores)
        conn.commit()

        usuario_id = cursor.lastrowid

        cursor.close()
        conn.close()

        resposta = OrderedDict()
        resposta['mensagem'] = 'Usuario cadastrado com sucesso.'
        resposta['id'] = usuario_id
        resposta['usuario'] = usuario

        return make_response(jsonify(resposta),201)
    
    except Exception as e:
        return make_response(jsonify(erro=str(e)),500)

    

#Start API
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
