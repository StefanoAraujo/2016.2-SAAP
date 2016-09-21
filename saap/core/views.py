from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.template import RequestContext
from django.utils.translation import ugettext
from core.models import Contato

def checar_vazio(campos):
    nao_vazio = True
    for campo in campos:
        if campo == "":
            nao_vazio = False
    return nao_vazio

class CadastroView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        response = render(request, 'cadastro_contato.html')
        return response

    def post (self,request):

        nome = ""
        data_de_nascimento = ""
        sexo = ""
        telefone = ""
        celular = ""
        fax = ""
        cpf = ""
        rg= ""
        endereco = ""
        cidade = ""
        cep = ""
        estado = ""
        email = ""
        grupo = ""
        titulo = ""
        titulo_de_eleitor = ""
        zona = ""
        secao = ""
        profissao = ""
        cargo = ""
        empresa = ""
        dependente_nome = ""
        dependente_aniversario = ""
        dependente_parentesco = ""
        dependente_partido = ""
        dependente_data_filiacao = ""

        campos = [request.POST['nome'],request.POST['data_de_nascimento'],\
            request.POST['sexo'],request.POST['telefone'], request.POST['celular'],\
            request.POST['fax'], request.POST['cpf'], request.POST['rg'], request.POST['endereco'],\
            request.POST['cidade'], request.POST['cep'], request.POST['estado'], request.POST['email'],\
            request.POST['grupo'], request.POST['titulo'], request.POST['titulo_de_eleitor'], \
            request.POST['zona'],request.POST['secao'], request.POST['profissao'], \
            request.POST['cargo'], request.POST['empresa'],request.POST['dependente_nome'],\
            request.POST['dependente_aniversario'], request.POST['dependente_parentesco'],\
            request.POST['dependente_partido'],request.POST['dependente_data_filiacao']]

        if checar_vazio(campos) :

            nome = request.POST['nome']
            data_de_nascimento = request.POST['data_de_nascimento']
            sexo = request.POST['sexo']
            telefone = request.POST['telefone']
            celular = request.POST['celular']
            fax = request.POST['fax']
            cpf = request.POST['cpf']
            rg= request.POST['rg']
            endereco = request.POST['endereco']
            cidade = request.POST['cidade']
            cep = request.POST['cep']
            estado = request.POST['estado']
            email = request.POST['email']
            grupo = request.POST['grupo']
            titulo = request.POST['titulo']
            titulo_de_eleitor = request.POST['titulo_de_eleitor']
            zona = request.POST['zona']
            secao = request.POST['secao']
            profissao = request.POST['profissao']
            cargo = request.POST['cargo']
            empresa = request.POST['empresa']
            dependente_nome = request.POST['dependente_nome']
            dependente_aniversario = request.POST['dependente_aniversario']
            dependente_parentesco = request.POST['dependente_parentesco']
            dependente_partido = request.POST['dependente_partido']
            dependente_data_filiacao = request.POST['dependente_data_filiacao']

            contato = Contato()
            contato.nome = nome
            contato.data_de_nascimento = data_de_nascimento
            contato.sexo = sexo
            contato.telefone = telefone
            contato.celular = celular
            contato.fax = fax
            contato.cpf = cpf
            contato.rg= rg
            contato.endereco = endereco
            contato.cidade = cidade
            contato.cep = cep
            contato.estado = estado
            contato.email = email
            contato.grupo = grupo
            contato.titulo = titulo
            contato.titulo_de_eleitor = titulo_de_eleitor
            contato.zona = zona
            contato.secao = secao
            contato.profissao = profissao
            contato.cargo = cargo
            contato.empresa = empresa
            contato.dependente_nome = dependente_nome
            contato.dependente_aniversario = dependente_aniversario
            contato.dependente_parentesco = dependente_parentesco
            contato.dependente_partido = dependente_partido
            contato.dependente_data_filiacao = dependente_data_filiacao
            contato.save()
            contatos = Contato.objects.all()
            lista_contatos = list(contatos)
            response = render(request,'contato.html',locals())
        else:
            messages.error(request,'Preencha todos os campos!')
            response = render(request,'contato.html')

        return response

class DeletarContatoView(View):
    http_method_names = [u'get',u'post']

    def get (self, request):
        response = render(request, 'exclui_contato.html')
        return response

    def post(self, request):
        busca_email = request.POST['busca_email']
        c = Contato.objects.get(email = busca_email)
        c.delete()
        response = render(request,'cadastro_contato.html')
        return response

class AtualizaContato(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        response = render(request, 'atualiza_contato.html')
        return response

    def post(self, request):

        campos = [request.POST['nome'],request.POST['data_de_nascimento'],\
            request.POST['sexo'],request.POST['telefone'], request.POST['celular'],\
            request.POST['fax'], request.POST['cpf'], request.POST['rg'], request.POST['endereco'],\
            request.POST['cidade'], request.POST['cep'], request.POST['estado'], request.POST['email'],\
            request.POST['grupo'], request.POST['titulo'], request.POST['titulo_de_eleitor'], \
            request.POST['zona'],request.POST['secao'], request.POST['profissao'], \
            request.POST['cargo'], request.POST['empresa'],request.POST['dependente_nome'],\
            request.POST['dependente_aniversario'], request.POST['dependente_parentesco'],\
            request.POST['dependente_partido'],request.POST['dependente_data_filiacao']]

        if checar_vazio(campos) :

            nome = request.POST['nome']
            data_de_nascimento = request.POST['data_de_nascimento']
            sexo = request.POST['sexo']
            telefone = request.POST['telefone']
            celular = request.POST['celular']
            fax = request.POST['fax']
            cpf = request.POST['cpf']
            rg= request.POST['rg']
            endereco = request.POST['endereco']
            cidade = request.POST['cidade']
            cep = request.POST['cep']
            estado = request.POST['estado']
            email = request.POST['email']
            grupo = request.POST['grupo']
            titulo = request.POST['titulo']
            titulo_de_eleitor = request.POST['titulo_de_eleitor']
            zona = request.POST['zona']
            secao = request.POST['secao']
            profissao = request.POST['profissao']
            cargo = request.POST['cargo']
            empresa = request.POST['empresa']
            dependente_nome = request.POST['dependente_nome']
            dependente_aniversario = request.POST['dependente_aniversario']
            dependente_parentesco = request.POST['dependente_parentesco']
            dependente_partido = request.POST['dependente_partido']
            dependente_data_filiacao = request.POST['dependente_data_filiacao']

            busca_email = request.POST['busca_email']
            contato = Contato.objects.get(email = busca_email)
            contato.nome = nome
            contato.data_de_nascimento = data_de_nascimento
            contato.sexo = sexo
            contato.telefone = telefone
            contato.celular = celular
            contato.fax = fax
            contato.cpf = cpf
            contato.rg= rg
            contato.endereco = endereco
            contato.cidade = cidade
            contato.cep = cep
            contato.estado = estado
            contato.email = email
            contato.grupo = grupo
            contato.titulo = titulo
            contato.titulo_de_eleitor = titulo_de_eleitor
            contato.zona = zona
            contato.secao = secao
            contato.profissao = profissao
            contato.cargo = cargo
            contato.empresa = empresa
            contato.dependente_nome = dependente_nome
            contato.dependente_aniversario = dependente_aniversario
            contato.dependente_parentesco = dependente_parentesco
            contato.dependente_partido = dependente_partido
            contato.dependente_data_filiacao = dependente_data_filiacao
            contato.save()
            contatos = Contato.objects.all()
            lista_contatos = list(contatos)
            response = render(request,'contato.html',locals())
        else:
            messages.error(request,'Preencha todos os campos!')
            response = render(request,'atualiza_contato.html')

        return response

class ContatoView(View):
    http_method_names = [u'get', u'post']

    def get (self, request):
        contatos = Contato.objects.all()
        lista_contatos = list(contatos)
        return render(request,'contato.html',locals())
