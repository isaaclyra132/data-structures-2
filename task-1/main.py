import streamlit as st
import pandas as pd
from nltk.tokenize import word_tokenize
from avl import AVLTree

def read_corpus_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def process_corpus(corpus):
    tree = AVLTree()
    for word in corpus:
        tree.insert(word)
    return tree

def main():
    # text = "O rato roeu a roupa do rei de roma"
    text = read_corpus_from_file("1-memorias-postumas.txt")

    tokens = word_tokenize(text.lower())
    corpus = [word for word in tokens if word.isalnum()]
    avl_tree = process_corpus(corpus)

    print("Palavras únicas ordenadas:")
    avl_tree.inorder_traversal()

    st.title("Pesquisa de Palavras com Prefixo")
    st.write("Corpus de Texto:")
    st.markdown(f"<p style='color: aquamarine'>{text}</p>", unsafe_allow_html=True)

    st.write("Insira um prefixo no campo abaixo e clique em 'Pesquisar' para encontrar palavras com esse prefixo.")

    # Campo de texto para inserir o prefixo
    prefix = st.text_input("Prefixo:")
    if st.button("Pesquisar"):
        words = avl_tree.words_with_prefix(prefix.lower())
        if words:
            # Exibir os resultados em uma tabela
            df = pd.DataFrame({"Palavras com prefixo": words})
            st.table(df)
        else:
            st.write(f"Nenhuma palavra encontrada com o prefixo '{prefix}'.")

if __name__ == "__main__":
    main()