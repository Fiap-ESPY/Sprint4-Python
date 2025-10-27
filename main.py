import os

from championship.championship import list_championships, add_championship, edit_championship, remove_championship, \
    register_for_championship
from login.login import login
from news.news import add_news, list_news, remove_news, edit_news
from utils.utils import save_data


# ---------- Menus ----------
def admin_menu():
    while True:
        print("===== MENU ADMIN =====")
        print("1. CRUD de Campeonatos")
        print("2. CRUD de Notícias")
        print("0. Sair")
        option = input("Escolha: ").strip()

        if option == "1":
            championship_menu()
        elif option == "2":
            news_menu()
        elif option == "0":
            break
        else:
            print("Opção inválida!\n")


def championship_menu():
    while True:
        print("===== CRUD CAMPEONATOS =====")
        print("1. Listar Campeonatos")
        print("2. Adicionar Campeonato")
        print("3. Editar Campeonato")
        print("4. Remover Campeonato")
        print("0. Voltar")
        option = input("Escolha: ").strip()

        if option == "1":
            list_championships("admin")
        elif option == "2":
            add_championship()
        elif option == "3":
            edit_championship()
        elif option == "4":
            remove_championship()
        elif option == "0":
            break
        else:
            print("Opção inválida!\n")


def news_menu():
    while True:
        print("===== CRUD NOTÍCIAS =====")
        print("1. Listar Notícias")
        print("2. Adicionar Notícia")
        print("3. Editar Notícia")
        print("4. Remover Notícia")
        print("0. Voltar")
        option = input("Escolha: ").strip()

        if option == "1":
            list_news()
        elif option == "2":
            add_news()
        elif option == "3":
            edit_news()
        elif option == "4":
            remove_news()
        elif option == "0":
            break
        else:
            print("Opção inválida!\n")


def organization_menu(user):
    while True:
        print("===== MENU ORGANIZAÇÃO =====")
        print("1. Listar Campeonatos")
        print("2. Inscrever-se em Campeonato")
        print("0. Sair")
        option = input("Escolha: ").strip()

        if option == "1":
            list_championships()
        elif option == "2":
            register_for_championship(user["username"])
        elif option == "0":
            break
        else:
            print("Opção inválida!\n")


def visitor_menu():
    while True:
        print("===== MENU VISITANTE =====")
        print("1. Listar Campeonatos")
        print("0. Sair")
        option = input("Escolha: ").strip()

        if option == "1":
            list_championships()
        elif option == "0":
            break
        else:
            print("Opção inválida!\n")


# ---------- Programa principal ----------
def main():
    while True:
        print("===== SISTEMA DE CAMPEONATOS =====")
        print("1. Login")
        print("2. Continuar como Visitante")
        print("0. Sair")
        option = input("Escolha: ").strip()

        if option == "1":
            user = login()
            if user:
                if user["role"] == "admin":
                    admin_menu()
                elif user["role"] == "organization":
                    organization_menu(user)
        elif option == "2":
            visitor_menu()
        elif option == "0":
            print("Saindo... 👋")
            break
        else:
            print("Opção inválida!\n")


if __name__ == "__main__":
    # Cria usuários padrão se não existirem
    if not os.path.exists("jsons/users.json"):
        default_users = [
            {"username": "admin", "password": "123", "role": "admin"},
            {"username": "org1", "password": "123", "role": "organization"},
        ]
        save_data("jsons/users.json", default_users)

    main()
