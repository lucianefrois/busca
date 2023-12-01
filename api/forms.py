from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class FormFuncionario(FlaskForm):
    nome_funcionario = StringField('Nome', validators=[DataRequired()])
    cpf_funcionario = StringField('CPF', validators=[DataRequired()])
    email_funcionario = StringField('E-mail', validators=[DataRequired(), Email()])
    
    #botao_submit_criarconta = SubmitField('Cadastrar Usuario')
class FormCliente(FlaskForm):
    id_cliente = StringField('ID do Cliente',validators=[DataRequired()]) 
    nome_cliente = StringField('Nome', validators=[DataRequired()])
    cpf_cliente = StringField('CPF', validators=[DataRequired()])
    email_cliente = StringField('E-mail', validators=[DataRequired(),Email()])
    data_ultima_iteracao = StringField('Data Última Iteração', validators=[DataRequired()])
    status_follow_up = StringField('Status Follow-up', validators=[DataRequired()])
    data_proximo_followup = StringField('Data Próximo Follow-up', validators=[DataRequired()])
    descricao_ultima_iteracao = StringField('Descrição Última Iteração', validators=[DataRequired()])

    submit = SubmitField('Adicionar Cliente')


class FormProduto(FlaskForm):
    id_produto = StringField('ID do Produto',validators=[DataRequired()])
    nome_produto = StringField('Nome do Produto',validators=[DataRequired()])
    preco_produto = StringField('Preco do Produto',validators=[DataRequired()])

    submit = SubmitField('Adicionar Produto')


class FormGalpao(FlaskForm):
    id_galpao = StringField('ID do galpão',validators=[DataRequired()])
    local_estoque = StringField('estoque do galpão',validators=[DataRequired()])

    submit = SubmitField('Adicionar Galpao')


class FormTarefa(FlaskForm):
    id_tarefa = StringField('ID da tarefa',validators=[DataRequired()])
    data_tarefa = StringField('data da tarefa',validators=[DataRequired()])
    nome_tarefa = StringField('nome da tarefa',validators=[DataRequired()])
    status_tarefa = StringField('status da tarefa',validators=[DataRequired()])

    submit = SubmitField('Adicionar Tarefa')

class FormEstoque(FlaskForm):
    id_estoque = StringField('ID do estoque',validators=[DataRequired()])
    id_produto = StringField('ID produto',validators=[DataRequired()])
    qtd_produto = StringField('qtd produto',validators=[DataRequired()])
    status_estoque = StringField('status do estoque',validators=[DataRequired()])
    id_galpao = StringField('ID do galpão',validators=[DataRequired()])

    submit = SubmitField('Adicionar Estoque')


class FormFuncionarioTarefa(FlaskForm):
    id_tarefa = StringField('ID da tarefa',validators=[DataRequired()])
    id_funcionario = StringField('ID funcionario',validators=[DataRequired()])

    submit = SubmitField('Adicionar funcionario tarefa')

class FormHistoricoCompra(FlaskForm):
    id_compra = StringField('ID da tarefa',validators=[DataRequired()])
    data_compra = StringField('Data compra',validators=[DataRequired()])
    id_cliente = StringField('ID do cliente',validators=[DataRequired()])
    id_produto = StringField('ID do produto',validators=[DataRequired()])

    submit = SubmitField('Adicionar historico de compra')


class FormRegistroInteracao(FlaskForm):
    id_interacao = StringField('ID interacao',validators=[DataRequired()])
    id_cliente = StringField('ID cliente',validators=[DataRequired()])
    id_funcionario = StringField('ID funcionario',validators=[DataRequired()])
    data_interacao = StringField('Data interacao',validators=[DataRequired()])
    tipo_interacao = StringField('Tipo interacao',validators=[DataRequired()])
    descricao_interacao = StringField('Descricao interacao',validators=[DataRequired()])
    registro_interacaocol = StringField('Registro interacao',validators=[DataRequired()])
    etapa_followup = StringField('Etapa followup',validators=[DataRequired()])
    status_followup = StringField('Status followup',validators=[DataRequired()])
    data_prox_followup = StringField('Data proximo followup',validators=[DataRequired()])

    submit = SubmitField('Adicionar historico de compra')