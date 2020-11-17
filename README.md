# winx_solution

Uma solução aberta para outros vendedores colocarem seus produtos a venda
em nossa plataforma.

Discutindo os requisitos para o MVP, o pessoal de produto considerou:

Requisitos Obrigatórios:

- O desenvolvimento deve ser via API REST (sugestão de frameworks: Django, Flask, aiohttp);
- A representação dos dados (cadastrar/visualizar produto) o formato de dados é preferencialmente JSON
- Na solução, deve ser possível:
    - Cadastrar um produto;
    - Atualizar um produto;
    - Consultar um produto;
    - Inativar um produto (observação: não é necessário apagar produto e sim inativar);

- Um produto deve ter os seguintes campos:
    - Título;
    - Preço;
    - Código do produto;
    - Identificador do vendedor (seller);
    - Quantidade em estoque;

Requisitos não obrigatórios:

- Criação de testes unitários para a solução;
- Implementação de Continuous Integration (Sugestão se for fazer, utilizem o github =) );
- Versionamento do código (git);
- Autenticação na API por seller (cada seller teria uma "chave" de acesso)
