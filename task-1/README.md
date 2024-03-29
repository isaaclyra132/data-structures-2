# Pesquisa de Palavras com Prefixo

Este é um aplicativo simples que permite ao usuário inserir um prefixo e encontrar palavras na árvore AVL que começam com esse prefixo. O aplicativo foi desenvolvido em Python utilizando a biblioteca Streamlit para criar a interface do usuário e a estrutura de dados de uma Árvore AVL para realizar a busca eficiente das palavras.

[Link de apresentação](https://www.loom.com/share/9ef123e57e7040f0a84f8a2893f26e39?sid=1c4d5ded-c9f5-4418-ab51-d986cb211eac) 

## Funcionalidades

- O usuário insere um prefixo em um campo de texto na interface.
- Ao clicar no botão "Pesquisar", o aplicativo exibe todas as palavras na árvore AVL que começam com o prefixo inserido.
- O corpus de texto exibido na interface é lido de um arquivo `1-memorias-postumas.txt`.
- O aplicativo também permite ao usuário visualizar o corpus de texto na interface.

## Como executar

Para executar o aplicativo, siga as etapas abaixo:

1. Certifique-se de ter o Python instalado em seu sistema. Se não tiver, você pode baixá-lo em [python.org](https://www.python.org/).

2. Instale as dependências executando o seguinte comando no terminal:

    ```
    pip install streamlit pandas nltk
    ```

3. Clone este repositório em sua máquina local:

    ```
    git clone https://github.com/isaaclyra132/data-structures-2.git
    ```

4. Navegue até o diretório do projeto:

    ```
    cd data-structures-2
    ```

5. Execute o aplicativo usando o Streamlit:

    ```
    streamlit run main.py
    ```

Isso iniciará um servidor local e abrirá automaticamente uma página da web no navegador com a interface do aplicativo.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (`issues`) ou enviar `pull requests` com melhorias e novos recursos.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.
