# Virtual Env

``
pip isntall virtual env
``

### caso precise atualziar a versão do PIP utilize:
``
python.exe -m pip install --upgrade pip
``

## Criando ambientes Virtuais

### no PROMPT vamos criar um novo ambientre virtual utilziando o virtual ENV:

``
mkdir virtualenv
``

``
cd virtualenv
``

nome da pasta:

``
virtualenv venv
``

para ativar o ambiente virtual que voce acabou de criar utilizando o virtual env volte a pasta raiz criada e digite:

``
venv\Scripts\activate
``

Obs: vale lembrar que no linux voce ira utilizar o comando SOURCE

após feito isso voce estara apto a instalr pacotes e ter a segurança de estar em um ambiente isolado

CERTO MAS COMO FAZ PRA DESATIVAR ESSE AMBIENTE VIRTUAL?? BOM É SIMPLES:

``
\venv\Scripts\deactivate
``
com isso seu ambiente virtual sera desativado.

## Criando um ambiente virtual com uma versão especifica do Python


1 - retorne a sua pasta raiz para criar uma nova com a versão especifica do python e utilize
``
mkdir segundo_ambiente
``

2 - para cria com uma versão especifica primeiro voce precisa saber onde está o executavel do python
``
virtualenv venv --python='C:\Users\[username]\AppData\Local\Programs\Python\Python312\python.exe'
``

## Não sabe acahr o caminho ?? aqui um comandinho basico que voce ira executar, basta clicar em 'WIN' (folinha do windows)
## E procurar o python abra o cmd dele e utilize:
``
import os 
``

``
import sys
``

``
os.path.dirname(sys.executable)
``

Só não se esqueça de tirar as duplas barras antes de executar o comando e adicioanr o ``python.exe`` no final do comando

### Feito isso o ambiente estará criado com a versão do pytrhon de sua escolha.