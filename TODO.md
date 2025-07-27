## Próximas Implementações

- [x] Criar a função de validação
- [x] Fazer o tratamento de erros
    - [x] Valor: não aceitar um valor vazio
    - [x] Caso o usuário não informar nada em categoria, será adicionado um texto genérico padrão
    - [x] Caso o usuário não informar nada em descrição, será adicionado um texto genérico padrão
    - [x] Caso o usuário não informar data, será adicionada a data atual

- [x] Implementação de banco de dados
    - [x] Será criada toda a lógica para o armazenamento dos dados dos gastos informados pelo usuário.
    - [x] Ainda não sei qual tecnologia usar, mas tenho em mente sqlite3.
    - [ ] Fazer a implementação de With no codigo, o mesmo deixa o codigo mais seguro. // REFATORAR O CODIGO NA PARTE DO BANCO DE DADOS. 
    - [ ] Criar e implementar a função de editar gastos já criados.
    - [ ] Analisar se vale a pena mudar a forma da exibição dos gastos, para, Nome do gasto, valor, categoria e descrição.  

# Preparação para a Parte Visual

- [ ] Fazer a preparação de todo o código para receber a parte visual.

    - # O QUE SERÁ FEITO?

        - [ ] Retirar todo e qualquer `print()` que exista no código. alterar por `Return`

        - [ ] Mudar a lógica para uma lógica segmentada em rotas.
 

- [ ] Implementação da parte visual
    - [ ] A ideia primária é criar uma interface de linha de comando.
    - [ ] Depois, estudar sobre interfaces para criar uma interface para o nosso programa.

- [ ] Pontos incertos
    - [ ] Ainda não sei se devo criar um programa nativo para Windows ou se devo criar um programa web.

- [ ] Documentação
    - [ ] Preciso criar a documentação do projeto, ainda não fiz isso.



## Observação 
    - Eu acredito que, seja melhor eu ja tirar a parte de CLI e ja deixar pronto para receber uma interface grafica. 
    - No caso, eu ja vou deixar o programa retornar erros, sem o print.