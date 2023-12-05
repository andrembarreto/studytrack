# Autores
André Luiz Morato Barreto, Lucas Gabriel Rios da Silva

# Study Track
Este é um projeto de aplicação para gestão de estudos utilizando Python. 
O sistema permite ao usuário adicionar diferentes Subjects (matérias), para os quais pode-se definir metas de notas, tempo de estudo
e conteúdos a serem visitados, havendo, ainda, opção de estipular datas para os objetivos. O progresso de tais metas pode ser acompanhado
por meio de sessões de estudo, que indicarão o tempo e assuntos estudados. É possível, também, controlar a frequência do estudante em cada
disciplina.

## Entidades
- **Subject**: Disciplinas realizadas pelo estudante, as quais possuem nome, nota mínima de aprovação, conteúdos (SubjectContent), atividades (GradedAssignment) e frequência do aluno (Attendance);
- **SubjectContent**: Conteúdos associados aos Subjects, os quais possuem nome e prioridade, sendo possível indicar se já foi ou não visitado pelo estudante;
- **GradedAssignment**: Atividades relacionadas aos Subjects, tendo nome, data de entrega, nota máxima e a nota obtida pelo estudante;
- **Attendance**: Frequência do estudante em determinado Subject, sendo composta pela carga horária da disciplina, as horas realizadas pelo aluno e o
percentual mínimo de assiduidade necessário.

## Instruções de execução
A interação com a aplicação é realizada via linha de comando. Para executar o sistema, deve-se utilizar o comando `python main.py`. Então, serão exibidas as opções disponibilizadas para:
1. Listar subjects
2. Adicionar subject
3. Remover subject
4. Filtrar subjects
5. Calcular média geral das disciplinas
6. Calcular quantidade atual de créditos
7. Verificar status da graduação
8. Atualizar frequência em subject

## Tecnologias Utilizadas
O sistema foi implementado utilizando Python.

### pytest
Para implementação e execução de testes de unidade e integração, foi utilizado o pytest.
