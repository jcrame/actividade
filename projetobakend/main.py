from fastAPI import fastAPI

app = fastAPI()

@app.get("/cliente")
def cliente_rota():
    return {"id_cliente" : "1",
            "nome" : "juan",
            "cpf" : "12345678910",
            "data_nascimento" : "22-09-2003",
            "telefone" : "4999999999",
            "email" : "juan@gmail.com",
            "data_cadastro" : "10-06-2026"}

@app.get("/treinador")
def treinador_rota():
    return {"id_treinador" : "1",
            "nome" : "juakin",
            "cref" : "12345-G/CE",
            "especialidade" : "musculação",
            "telefone" : "4922222222",}

@app.get("/aula")
def aula_rota():
    return {"id_aula" : "1",
            "id_treinador" : "1",
            "modalidade" : "musculação",
            "dia_semana" : "segunda_sabado",
            "hora_inicio" : "07:00 AM",
            "capacidade": "1000"}

@app.get("/rotina")
def rotina_rota():
    return {"id_rotina" : "1",
            "id_cliente" : "1",
            "id_treinador" : "1",
            "data_criacao" : "22-09-2025",
            "objetivo" : "musculação"}

@app.get("/exercicio")
def exercicio_rota():
    return {"id_exercicio": "1",
            "nome_exercicio" : "novato",
            "grupo_muscular" : "biceps"}

@app.get("/equipamento")
def equipamento_rota():
    return {"id_equipamento" : "1",
            "nome" : "lalala",
            "categoria" : "braços",
            "data_equisicao" : "30-02-2020",
            "status" : "optimo"}

@app.get("/membresia")
def membresia_rota():
    return {"id_plano" : "1",
            "nome_plano" : "prata",
            "duracao_meses" : "1 mes",
            "valor" : "80,00"}

@app.get("/registro_acesso")
def registro_acesso_rota():
    return{"id_acesso" : "1",
           "id_cliente" : "1",
           "data_hora_entrada" : "07:00 AM", 
           "data_hora_saida" : "11:00 PM",
           "autorizacao" : "2209"}

@app.get("/manutencao")
def manutencao_rota():
    return{"id_manutencao" : "1",
           "id_equipamento":}
    