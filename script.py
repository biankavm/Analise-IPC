import os
import csv
    
def extrair_dados_alunos(diretorio_base):
    

        # Lista por compreensão para obter os diretórios de período letivo
        periodos = [os.path.join(diretorio_base, periodo_letivo) for periodo_letivo in os.listdir(diretorio_base)
                    if os.path.isdir(os.path.join(diretorio_base, periodo_letivo))
                    ]
        
        # Iteração sobre os diretórios de período letivo
        for caminho_periodo in periodos:
            
            arquivo_csv = os.path.basename(caminho_periodo) + ".csv"
            
            with open(arquivo_csv, 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(["ID do Aluno", "Período Letivo", "Turma", "Nome do Curso", "Nota Final", "Departamento"])
                
                
                turmas = [os.path.join(caminho_periodo, turma) for turma in os.listdir(caminho_periodo) 
                            if os.path.isdir(os.path.join(caminho_periodo, turma))
                            ]
                
                # Iteração sobre os diretórios de turma
                for caminho_turma in turmas:
                    curso = ""
                    caminho_users = os.path.join(caminho_turma, "users")
                    
                    # Verifica se o diretório "users" existe
                    if os.path.isdir(caminho_users):
                        usuarios = [os.path.join(caminho_users, usuario) for usuario in os.listdir(caminho_users)]
                        
                        
                        # Iteração sobre os diretórios de usuário
                        for caminho_usuario in usuarios:
                            caminho_grades = os.path.join(caminho_usuario, "grades")
                            
                            caminho_user_data = os.path.join(caminho_usuario, "user.data")
                            
                            # Verifica se o arquivo "user.data" existe
                            if os.path.exists(caminho_user_data):
                                with open(caminho_user_data, 'r', encoding='utf-8') as f:
                                    for linha in f:
                                        s = linha.strip().split(':')
                                        if len(s) > 1 and s[0].strip() == '---- course name':
                                            curso = s[1].strip()
                            
                            
                            lista_icomp = ["Sistemas", "Ciência", "Software"]
                            lista_ft = ["Engenharia"]
                            lista_ice = ["Matemática", "Física", "Estatística", "Geologia"]
                            
                            if any(item in curso for item in lista_icomp):
                                type_departamento = "ICOMP"
                            elif any(item in curso for item in lista_ft):
                                type_departamento = "FT"
                            elif any(item in curso for item in lista_ice):
                                type_departamento = "ICE"
                            else:
                                type_departamento = "EXTRA"
                                                                       
                            # Verifica se o diretório "grades" existe
                            if os.path.isdir(caminho_grades):
                                
                                final_grades_path = os.path.join(caminho_grades, "final_grade.data")
                            
                                if os.path.exists(final_grades_path):
                                    with open(final_grades_path, 'r') as f:
                                            nota_final = f.readline().strip()
                                            csv_writer.writerow([os.path.basename(caminho_usuario), 
                                                                    os.path.basename(caminho_periodo), 
                                                                    os.path.basename(caminho_turma), 
                                                                    curso, 
                                                                    nota_final, type_departamento])


diretorio_base = "./datasets"  # caminho com todos os datasets
arquivo_saida = "saida.csv"  # csv de saída

extrair_dados_alunos(diretorio_base)