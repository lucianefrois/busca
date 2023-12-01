from sqlalchemy import ForeignKey
from sqlalchemy import PrimaryKeyConstraint
from api.app import db

class Funcionario(db.Model):

    __tablename__ = 'funcionario'

    id_funcionario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_funcionario = db.Column(db.String(30))
    cpf_funcionario = db.Column(db.String(15), unique=True)
    email_funcionario = db.Column(db.String(30), unique=True)

    def __init__ (self, nome_funcionario, cpf_funcionario, email_funcionario ):
        self.nome_funcionario = nome_funcionario
        self.cpf_funcionario = cpf_funcionario
        self.email_funcionario = email_funcionario

    def __repr__(self):
        return '<Funcionario %r>' % self.nome_funcionario

class Cliente(db.Model):
    __tablename__ = 'cliente'

    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_cliente = db.Column(db.String(30))
    cpf_cliente = db.Column(db.String(30))
    email_cliente = db.Column(db.String(30))
    data_ultima_iteracao = db.Column(db.String(30))
    status_follow_up = db.Column(db.String(30))
    data_proximo_followup = db.Column(db.String(30)) 
    descricao_ultima_iteracao = db.Column(db.String(30))

    def __init__ (self, nome_cliente, cpf_cliente,email_cliente,data_ultima_iteracao,status_follow_up,data_proximo_followup,descricao_ultima_iteracao):

        self.nome_cliente = nome_cliente
        self.cpf_cliente = cpf_cliente
        self.email_cliente = email_cliente
        self.data_ultima_iteracao = data_ultima_iteracao
        self.status_follow_up = status_follow_up
        self.data_proximo_followup = data_proximo_followup
        self.descricao_ultima_iteracao = descricao_ultima_iteracao
    
    def __repr__(self):
        return '<Cliente %r>' % self.nome_cliente

class Produto(db.Model):
    __tablename__ = 'produto'

    id_produto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_produto = db.Column(db.String(30))
    preco_produto = db.Column(db.Integer)


    def __init__ (self,id_produto, nome_produto, preco_produto):

        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto

    
    def __repr__(self):
        return '<Produto %r>' % self.nome_produto

class Galpao(db.Model):
    __tablename__ = 'galpao'

    id_galpao = db.Column(db.Integer, primary_key=True, autoincrement=True)
    local_estoque = db.Column(db.Integer)
   


    def __init__ (self,id_galpao, local_estoque):

        self.id_galpao = id_galpao
        self.local_estoque = local_estoque

    
    def __repr__(self):
        return '<Galpao %r>' % self.nome_galpao



class Tarefa(db.Model):
    __tablename__ = 'tarefa'

    id_tarefa = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_tarefa = db.Column(db.String(30))
    nome_tarefa = db.Column(db.String(30))
    status_tarefa = db.Column(db.String(30))

    def __init__ (self,id_tarefa, data_tarefa, nome_tarefa, status_tarefa ):

        self.id_tarefa = id_tarefa
        self.data_tarefa = data_tarefa
        self.nome_tarefa = nome_tarefa
        self.status_tarefa = status_tarefa

    
    def __repr__(self):
        return '<Tarefa %r>' % self.nome_tarefa


class Estoque(db.Model):
    __tablename__ = 'estoque'

    id_estoque = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_produto = db.Column(db.Integer, ForeignKey('produto.id_produto'))
    qtd_produto = db.Column(db.Integer)
    status_estoque = db.Column(db.String(30))
    id_galpao = db.Column(db.Integer, ForeignKey('galpao.id_galpao'))

    def __init__ (self,id_estoque, id_produto, qtd_produto, status_estoque, id_galpao ):

        self.id_estoque = id_estoque
        self.id_produto = id_produto
        self.qtd_produto = qtd_produto
        self.status_estoque = status_estoque
        self.id_galpao = id_galpao

    
    def __repr__(self):
        return '<Estoque %r>' % self.nome_estoque


class Funcionario_tarefa(db.Model):
    __tablename__ = 'funcionario_tarefa'

    id_tarefa = db.Column(db.Integer, ForeignKey('tarefa.id_tarefa'),primary_key=True)
    id_funcionario = db.Column(db.Integer, ForeignKey('funcionario.id_funcionario'),primary_key=True)

    def __init__ (self,id_tarefa, id_funcionario):

        self.id_tarefa = id_tarefa
        self.id_funcionario = id_funcionario
    
    def __repr__(self):
        return '<Funcionario_tarefa %r>' % self.nome_Funcionario_tarefa


class Historico_compra(db.Model):
    __tablename__ = 'historico_compra'

    id_compra = db.Column(db.Integer,primary_key=True)
    data_compra = db.Column(db.String(30))
    id_cliente = db.Column(db.Integer,ForeignKey('cliente.id_cliente'))
    id_produto = db.Column(db.Integer,ForeignKey('produto.id_produto'))

    def __init__ (self,id_compra, data_compra, id_cliente,id_produto ):

        self.id_compra = id_compra
        self.data_compra = data_compra
        self.id_cliente = id_cliente
        self.id_produto = id_produto
    
    def __repr__(self):
        return '<Historico_compra %r>' % self.nome_Historico_compra
    

class Registro_interacao(db.Model):
    __tablename__ = 'registro_interacao'

    id_interacao = db.Column(db.Integer,primary_key=True)
    id_cliente = db.Column(db.Integer,ForeignKey('cliente.id_cliente'))
    id_funcionario = db.Column(db.Integer, ForeignKey('funcionario.id_funcionario'))
    data_interacao = db.Column(db.String(30))
    tipo_interacao = db.Column(db.String(30))
    descricao_interacao = db.Column(db.String(30))
    registro_interacaocol = db.Column(db.String(30))
    etapa_followup = db.Column(db.String(30))
    status_followup = db.Column(db.String(30))
    data_prox_followup = db.Column(db.String(30))

    def __init__ (self,id_interacao, id_cliente, id_funcionario,data_interacao,tipo_interacao, descricao_interacao, registro_interacaocol,etapa_followup, status_followup, data_prox_followup  ):

        self.id_interacao = id_interacao
        self.id_cliente = id_cliente
        self.id_funcionario = id_funcionario 
        self.data_interacao = data_interacao
        self.tipo_interacao = tipo_interacao
        self.descricao_interacao = descricao_interacao
        self.registro_interacaocol = registro_interacaocol
        self.etapa_followup = etapa_followup
        self.status_followup = status_followup
        self.data_prox_followup = data_prox_followup
    
    def __repr__(self):
        return '<Registro_interacao %r>' % self.nome_Registro_interacao
