from flask import Flask, request, abort, url_for, make_response

app = Flask(__name__)

@app.route('/')  #declarando o caminho raiz
def home(): #declarando a função
    return f'''                                                     #usa o f pois usarei parametros
            <h1>Avaliação contínua: Aula 030</h1>                 #Declarando o titulo que estara na pgina
                <ul>                                              #declarando lista
                    <li><a href="{url_for('home')}">Home</a></li> #item da lista chamado nome e vai direcionar para a url Home 
                    <li><a href="{url_for('identificacao', nome='Lais Gabriele', prontuario='PT3025993', instituicao='IFSP')}">Identificação</a></li>   #Item da lista chamado identificação, que direcionara para url, essa url vai ter a função identificação e os paramtros colocados
                    <li><a href="{url_for('contexto_requisicao')}">Contexto da requisição</a></li>   #a url direcionara para função contextorequisiçao
                </ul>
            '''

#Aqui eu declaro as funções e o que ela vai conter 
@app.route("/user/<nome>/<prontuario>/<instituicao>")
def identificacao(nome, prontuario, instituicao):
    return f'''
        <h1>Avaliação contínua: Aula 030</h1>
        <h2><b>Aluno:</b> {nome}</h2>
        <h2><b>Prontuário:</b> {prontuario}</h2>
        <h2><b>Instituição:</b> {instituicao}</h2>
        <p><a href="{url_for('home')}">Voltar</a></p>
        '''

@app.route("/contextorequisicao") 
def contexto_requisicao():
    user_agent = request.headers.get("User-Agent")
    remote_ip = request.remote_addr 
    host = request.host

    return f'''
        <h1>Avaliação contínua: Aula 030</h1>
        <h2><b>Seu navegador é:</b> {user_agent}</h2>
        <h2><b>O IP do computador remoto é:</b> {remote_ip}</h2>
        <h2><b>O host da aplicação é:</b> {host}</h2>
        <p><a href="{url_for('home')}">Voltar</a></p>
        '''

@app.route('/abortar')
def login():
    abort(404)

@app.route('/objetoresposta')
def objetoResposta():
    resposta = make_response('<h1>This document carries a cookie!</h1>')
    resposta.set_cookie('resposta', '42')
    return resposta

if __name__ == "__main__":
    app.run(debug=True)
