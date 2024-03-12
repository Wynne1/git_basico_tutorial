

#-------------------------------------------------- PRIMEIRO PASSO ------------------------------------------------------------------

"""PRIMEIRO USA O COMANDO: git init /que cria um novo repositório do Git. Pode inicializar um repositório vazio
ou converter um projeto existente e não versionado em um repositório Git"""

"""git status é um relatório que diz quais arquivos ja foram adicionados, e quais não foram

"""

# Para adicionar um arquivo ao controle de versão basta o usar o comando: git add "nomedoarquivo.txt"

"""Porém para adicionar vários arquivos não é interessante utilizar esse comando e sim o comando: git add .  

"""

"""O Comando : git commit -m "commit inicial" serve para fazer os comentários sobre o que foi feito na versão     
   """

# Para enviar o projeto para a nuvem, no caso o github, é necessário fazer um novo repositório no github e copiar o seu link"
"""
 Dentro do GIT, utiliza o comando git remote add origin junto ao seu link criado do repositório do github,
  que nada mais é que adicionar o local onde está seu repositório do github,
  então: git remote add origin link
    
      """
# Agora é necessário usar o push para fazer o envio dos seus arquivos usando o comando : git push. Que a princípio não irá funcionar
# porque a branch que o código deseja ser enviado não foi definida. Então ao executar o git push, o próprio git vai enviar um código
# git push --set-upstream origin master , que servirá para fazer o login do seu github. Feito isso, o push será feito e 
# seus arquivos serão enviadosda máquina local para a nuvem.

"""
Para fazer novas atualizações no código/arquivo desejado, basta adicionar uma nova atualização dentro dele mesmo, e ir ao git e
usar o comando git commit -m "nome_da_atualização". Ao fazer isso , basta dá um git push e seu arquivo será atualizado no github.

"""

# Para ver o histórico de commits utilizados, usa o comando : git reflog
#sendo o primeiro da lista a última atualização feita(o que está no HEAD)

# Junto a isso , para voltar a um commit anterior basta acessar o reflog e pegar o ID do commit desejado. E entao utilizar
#o comando git reset --hard 9485bb1 (nesse caso esse número é ilustrativo para o ID)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



#----------------------------------------------------BRANCH---------------------------------------------------------------------------


"""
BRANCH nada mais é que caminhos diferentes que podem ser seguidos para realizar um projeto.
  O ideal é ter uma branch "master" que vai ser a branch principal do sistema e deixá-la estável, apenas códigos que funcionam nela,
  e uma ou mais branches para o desenvolvimento. 
  Ou seja o desenvolvimento é feito numa branch chamada staging(ou qualquer outro nome), e assim que estiver pronto manda para a "master"

"""

# Para mudar a branch é necessário usar o comando: git checkout nome_da_branch

"""
Qualquer alteração feita a partir desse momento será feita na nova branch
Alterando qualquer arquivo, é obrigatório adicioná-lo ao git add . 
E fazer o commit evidenciando as alterações feitas :  git commit -m "alteração_feita"
E então fazer o push
No github será mostrado todas as suas branches. No branch staging será mostrado o histórico de commits, inclusive o novo feito, 
porém na branch master , as alterações ainda não estarão lá

"""

# Para fazer a união(merge) das branches 
"""
Agora é necessário fazer a junção da branch de teste com a master. 
É indispensável entrar na branch master , com o comando git checkout master 
Antes de fazer o merge, é preciso puxar as atualizações que estão no servidor para a máquina, para garantir que os códigos estejam
 na versão mais atuais possíveis. Rodando o comando : git pull

Assim que faz o git pull, faz-se: o git merge 
Exemplo: Se você está usando uma branch teste chamada staging e quer colocar as atualizações na branch principal, 
 então seleciona o branch master, faz o git pull, e então roda o comando : git merge staging

E por fim faz o git push
"""

#----------------------------------------------TRABALHO EM EQUIPE-----------------------------------------------------------------

#Caso seja necessário a criação de uma nova tarefa/funcionalidade no código(em equipe), como por exemplo criar um sistema de login

"""
Cria uma nova branch baseada no branch principal(master) ; git checkout -b nome_da_nova_funcionalidade

lembrando que isso é para trabalho em equipe, se é um projeto solo o certo é prosseguir com 2 branches. A principal e a teste

"""
#-------------------------------------Todo esse processo serve para a branch principal não ser quebrada-----------------------------


# Para não enviar certos arquivos para o controle de versão:

"""
É necessário utilizar a função de ignorar arquivos, com o comando : touch .gitignore
Vai ser criado um arquivo .gitignore em sua pasta do local projeto, dentro do arquivo .gitignore coloca-se o caminho do
 arquivo que almeja esconder

"""