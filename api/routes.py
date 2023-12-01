from api.app import app, db
from flask import render_template, request, redirect, url_for
from api.forms import FormFuncionario, FormCliente, FormProduto, FormGalpao, FormTarefa, FormEstoque, FormFuncionarioTarefa, FormHistoricoCompra, FormRegistroInteracao
from api.models import Funcionario, Cliente, Produto, Galpao, Tarefa, Estoque, Funcionario_tarefa, Historico_compra, Registro_interacao

# Cria as tabelas
with app.app_context():
    db.create_all()

# Restante do seu código
@app.route('/')
def index():
    registro_interacao = Registro_interacao.query.all()
    historico_compra = Historico_compra.query.all()
    funcionario_tarefa = Funcionario_tarefa.query.all()
    estoque = Estoque.query.all()
    tarefa = Tarefa.query.all()
    galpao = Galpao.query.all()
    produto = Produto.query.all()
    cliente = Cliente.query.all()
    funcionario = Funcionario.query.all()
    return render_template('index.html', funcionario=funcionario, cliente=cliente,produto=produto, galpao=galpao, tarefa=tarefa, estoque=estoque, funcionario_tarefa=funcionario_tarefa, historico_compra=historico_compra, registro_interacao=registro_interacao) 

@app.route('/adicionar_funcionario', methods=['POST', 'GET'])
def adicionar_funcionario():
    formFuncionario = FormFuncionario()
    if request.method == 'POST':
        if formFuncionario.validate_on_submit():
            nome_funcionario = formFuncionario.nome_funcionario.data
            cpf_funcionario = formFuncionario.cpf_funcionario.data
            email_funcionario = formFuncionario.email_funcionario.data

            funcionario = Funcionario(nome_funcionario, cpf_funcionario, email_funcionario)
            db.session.add(funcionario)
            db.session.commit()

            return redirect(url_for('index'))

    return render_template('funcionario.html', form=formFuncionario)

@app.route('/adicionar_cliente', methods=['POST', 'GET'])
def adicionar_cliente():
    formCliente = FormCliente()
    if request.method == 'POST':
        if  formCliente.validate_on_submit():
             nome_cliente = formCliente.nome_cliente.data
             cpf_cliente = formCliente.cpf_cliente.data
             email_cliente = formCliente.email_cliente.data
             data_ultima_iteracao = formCliente.data_ultima_iteracao.data
             status_follow_up = formCliente.status_follow_up.data
             data_proximo_followup = formCliente.data_proximo_followup.data
             descricao_ultima_iteracao = formCliente.descricao_ultima_iteracao.data

             cliente = Cliente(nome_cliente, cpf_cliente,email_cliente,data_ultima_iteracao,status_follow_up,data_proximo_followup,descricao_ultima_iteracao)
             db.session.add(cliente)
             db.session.commit()

             return redirect(url_for('index'))
        
    return render_template('cliente.html', form=formCliente) 


@app.route('/adicionar_produto', methods=['POST', 'GET'])
def adicionar_produto():
    formProduto = FormProduto()
    if request.method == 'POST':
        if formProduto.validate_on_submit():
            id_produto = formProduto.id_produto.data
            nome_produto = formProduto.nome_produto.data
            preco_produto = formProduto.preco_produto.data

            produto = Produto(id_produto, nome_produto, preco_produto)
            db.session.add(produto)
            db.session.commit()

            return redirect(url_for('index'))

    return render_template('produto.html', form=formProduto)

@app.route('/adicionar_galpao', methods=['POST', 'GET'])
def adicionar_galpao():
    formGalpao= FormGalpao()
    if request.method == 'POST':
        if formGalpao.validate_on_submit():
            id_galpao = formGalpao.id_galpao.data
            local_estoque = formGalpao.local_estoque.data

            galpao = Galpao(id_galpao, local_estoque)
            db.session.add(galpao)
            db.session.commit()

            return redirect(url_for('index'))

    return render_template('galpao.html', form=formGalpao)


@app.route('/adicionar_tarefa', methods=['POST', 'GET'])
def adicionar_tarefa():
    formTarefa= FormTarefa()
    if request.method == 'POST':
        if formTarefa.validate_on_submit():
            id_tarefa = formTarefa.id_tarefa.data
            data_tarefa = formTarefa.data_tarefa.data
            nome_tarefa = formTarefa.nome_tarefa.data
            status_tarefa = formTarefa.status_tarefa.data

            tarefa = Tarefa(id_tarefa, data_tarefa, nome_tarefa, status_tarefa )
            db.session.add(tarefa)
            db.session.commit()

            return redirect(url_for('index'))

    return render_template('tarefa.html', form=formTarefa)



@app.route('/adicionar_estoque', methods=['POST', 'GET'])
def adicionar_estoque():
    formEstoque = FormEstoque()
    if request.method == 'POST':
        if formEstoque.validate_on_submit():
            id_estoque = formEstoque.id_estoque.data
            id_produto = formEstoque.id_produto.data
            qtd_produto = formEstoque.qtd_produto.data
            status_estoque = formEstoque.status_estoque.data
            id_galpao = formEstoque.id_galpao.data

            estoque = Estoque(id_estoque, id_produto, qtd_produto, status_estoque, id_galpao)
            db.session.add(estoque)
            db.session.commit()

            return redirect(url_for('index'))

    return render_template('estoque.html', form=formEstoque)


@app.route('/adicionar_funcionario_tarefa', methods=['POST', 'GET'])
def adicionar_funcionario_tarefa():
    formFuncionarioTarefa = FormFuncionarioTarefa()
    if request.method == 'POST':
        if formFuncionarioTarefa.validate_on_submit():
            id_tarefa = formFuncionarioTarefa.id_tarefa.data
            id_funcionario = formFuncionarioTarefa.id_funcionario.data
          

            funcionario_tarefa = Funcionario_tarefa(id_tarefa, id_funcionario)
            db.session.add(funcionario_tarefa)
            db.session.commit()

            return redirect(url_for('index'))

    return render_template('funcionario_tarefa.html', form=formFuncionarioTarefa)
            

@app.route('/historico_compra', methods=['POST', 'GET'])
def historico_compra():
    formHistoricoCompra = FormHistoricoCompra()
    if request.method == 'POST':
        if formHistoricoCompra.validate_on_submit():
            id_compra = formHistoricoCompra.id_compra.data
            data_compra = formHistoricoCompra.data_compra.data
            id_cliente = formHistoricoCompra.id_cliente.data
            id_produto = formHistoricoCompra.id_produto.data
          

            historico_compra = Historico_compra(id_compra, data_compra,id_cliente, id_produto)
            db.session.add(historico_compra)
            db.session.commit()

            return redirect(url_for('index'))

    return render_template('historico_compra.html', form=formHistoricoCompra)



@app.route('/registro_interacao', methods=['POST', 'GET'])
def registro_interacao():
    formRegistroInteracao = FormRegistroInteracao()
    if request.method == 'POST':
        if formRegistroInteracao.validate_on_submit():
            id_interacao = formRegistroInteracao.id_interacao.data
            id_cliente = formRegistroInteracao.id_cliente.data
            id_funcionario = formRegistroInteracao.id_funcionario.data
            data_interacao = formRegistroInteracao.data_interacao.data
            tipo_interacao = formRegistroInteracao.tipo_interacao.data
            descricao_interacao = formRegistroInteracao.descricao_interacao.data
            registro_interacaocol = formRegistroInteracao.registro_interacaocol.data
            etapa_followup = formRegistroInteracao.etapa_followup.data
            status_followup = formRegistroInteracao.id_cliente.data
            data_prox_followup = formRegistroInteracao.data_prox_followup.data
            

            registro_interacao = Registro_interacao(id_interacao, id_cliente, id_funcionario,data_interacao,tipo_interacao, descricao_interacao,registro_interacaocol, etapa_followup,status_followup, data_prox_followup )
            db.session.add(registro_interacao)
            db.session.commit()

            return redirect(url_for('index'))

    return render_template('registro_interacao.html', form=formRegistroInteracao)








if __name__ == '__main__':
    app.run(debug=True)