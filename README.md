# Autores
André Luiz Morato Barreto, Lucas Gabriel Rios da Silva

# Study Track
Este é um projeto de aplicação para gestão de estudos utilizando Python. 
O sistema permite ao usuário adicionar diferentes Subjects (matérias), para os quais pode-se definir metas de notas, tempo de estudo
e conteúdos a serem visitados, havendo, ainda, opção de estipular datas para os objetivos. O progresso de tais metas pode ser acompanhado
por meio de sessões de estudo, que indicarão o tempo e assuntos estudados. É possível, também, controlar a frequência do estudante em cada
disciplina.

## Entidades
**Subject**: Disciplinas realizadas pelo estudante, as quais possuem nome, nota mínima de aprovação, conteúdos (SubjectContent), atividades (GradedAssignment) e frequência do aluno (Attendance);
**SubjectContent**: Conteúdos associados aos Subjects, os quais possuem nome e prioridade, sendo possível indicar se já foi ou não visitado pelo estudante;
**GradedAssignment**: Atividades relacionadas aos Subjects, tendo nome, data de entrega, nota máxima e a nota obtida pelo estudante;
**Attendance**: Frequência do estudante em determinado Subject, sendo composta pela carga horária da disciplina, as horas realizadas pelo aluno e o
percentual mínimo de assiduidade necessário.

## Tecnologias Utilizadas
O sistema foi implementado utilizando Python.

### PySide6
Para criação das interfaces, será utilizado PySide6, um wrapper multiplataforma de software livre da linguagem Python para a biblioteca Qt que 
permite a programação de GUIs.

### pytest
Para implementação e execução de testes de unidade e integração, foi utilizado o pytest.
