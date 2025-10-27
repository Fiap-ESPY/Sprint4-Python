# ⚽ Passa Bola - Challenger Sprint 4

Este repositório contém o script principal (`main.py`) que simula a lógica de back-end do projeto "Passa Bola". Este script foi desenvolvido como parte do **Challenger da Sprint 4**.

O sistema gerencia o acesso por diferentes níveis de permissão (Admin, Organização, Visitante) e controla as operações de gerenciamento de campeonatos e notícias, utilizando arquivos JSON locais para simular a persistência de dados.

## ✨ Funcionalidades

O sistema é baseado em menus e controlado por tipos de usuário:

### 1. Sistema de Autenticação
* Tela de login principal.
* Criação automática de usuários padrão (`admin`, `org1`) se o arquivo `jsons/users.json` não for encontrado.
* Navegação como "Visitante" sem necessidade de login.

### 2. Perfil: Administrador (`admin`)
O administrador tem controle total sobre o sistema.
* **Gerenciar Campeonatos:**
    * Listar todos os campeonatos.
    * Adicionar novos campeonatos.
    * Editar informações de campeonatos existentes.
    * Remover campeonatos.
* **Gerenciar Notícias:**
    * Listar todas as notícias.
    * Adicionar novas notícias.
    * Editar notícias existentes.
    * Remover notícias.

### 3. Perfil: Organização (`organization`)
Organizações podem interagir com os campeonatos.
* Listar todos os campeonatos disponíveis.
* Inscrever-se em um campeonato.

### 4. Perfil: Visitante
Visitantes têm acesso limitado de apenas visualização.
* Listar todos os campeonatos disponíveis.

## 🚀 Como Executar

1.  Certifique-se de ter o [Python 3](https://www.python.org/downloads/) instalado.
2.  Clone este repositório (ou baixe os arquivos).
3.  Execute o script principal através do seu terminal:

    ```bash
    python main.py
    ```

## 🔑 Acesso ao Sistema

Ao executar o programa pela primeira vez, os seguintes usuários padrão serão criados no arquivo `jsons/users.json`:

* **Admin:**
    * **Usuário:** `admin`
    * **Senha:** `123`
* **Organização:**
    * **Usuário:** `org1`
    * **Senha:** `123`

## 👨‍💻 Autores  

- Beatriz Cortez - RM561431
 
- Bruno Alves - RM563986
 
- Gabriel Augusto - RM564126
 
- Gustavo Moura - RM566190
 
- Pedro Henrique - RM563281
