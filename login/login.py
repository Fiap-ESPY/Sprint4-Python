# ---------- Login ----------
from utils.utils import load_data


def login():
    users = load_data("jsons/users.json")
    username = input("Usuário: ").strip()
    password = input("Senha: ").strip()

    if len(users) == 0:
        print("❌ Nenhum usuário encontrado.\n")
        return None

    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"👋 Bem-vindo, {username} ({user['role']})!\n")
            return user

    print("❌ Usuário ou senha incorretos.\n")

    return None
