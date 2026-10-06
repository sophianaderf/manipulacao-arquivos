import csv

def criar_csv():
    with open("alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
         escritor = csv.writer(arquivo)

         escritor.writerow(["Nome", "Idade", "Curso"])

         escritor.writerow(["Sophia", "16", "Desenvolvimento de sistemas"])
         escritor.writerow(["Miguel", "16", "Eletroeletrônica"])
         escritor.writerow(["Sara", "13", "Nenhum"])
         escritor.writerow(["Amira", "39", "Pedgogia"])

#criar_csv()

def salvar_alunos():
     alunos = [
          ["Sophia", 16, "Desenvolvimento de sistemas" ],
          ["Sara", 13, "Nenhum" ],
          ["Amira", 39, "Pedgogia" ],
          ["Miguel", 16, "Eletroeletronica"],
          ["Mayara", 16, "Desenvolvimento de sistemas"],
          ["Laura", 16, "Desenvolvimento de sistemas"],
     ]

     with open("novos_alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
          escritor = csv.writer(arquivo)

          escritor.writerow(["Nome", "Idade", "Curso"])

          escritor.writerows(alunos)

#salvar_alunos()

def ler_csv():
    with open("novos_alunos.csv", "r", encoding="utf-8") as arquivo:
         leitor = csv.reader(arquivo)

         next(leitor)

         for linha in leitor:
              print(linha[0])

#ler_csv()

def exibir_alunos():
     with open("novos_alunos.csv", "r", encoding="utf-8") as arquivo:
          alunos = csv.DictReader(arquivo)

          for aluno in alunos:
               print(aluno["Nome"])

#exibir_alunos()




def cadastrar_aluno():
     with open("novos_alunos.csv", "a+", newline="", encoding="utf-8") as arquivo:
          arquivo.seek(0,2)
          nome = input("Digite o nome do aluno: ")
          idade = int(input("Digite a idade do aluno: "))
          curso = input("Digite o curso no qual o aluno está matriculado: ")

          escritor = csv.writer(arquivo)

          escritor.writerow([nome, idade, curso])

          # Move o cursor para o início do arquivo
          arquivo.seek(0)
          leitor = csv.reader(arquivo)

          for linha in leitor:
               print(linha)

#cadastrar_aluno()



def deletar_aluno():

     with open("novos_alunos.csv", "r", newline="", encoding="utf-8") as arquivo:
          leitor = csv.reader(arquivo)
          alunos = list(leitor)

     with open("novos_alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
          cabecalho = ["Nome", "Idade", "Curso"]
          escritor = csv.writer(arquivo, fieldnames=cabecalho)

          escritor.writeheader()

          aluno_apagar = input("Digite o nome que deseja excluir: ")

          for aluno in alunos:
               if aluno["Nome"] != aluno_apagar:
                    escritor.writerow(aluno)

deletar_aluno()