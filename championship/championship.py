# ---------- CRUD de Campeonatos ----------
from utils.utils import load_data, save_data


def list_championships(role="visitor"):
    championships = load_data("jsons/championships.json")
    registrations = load_data("jsons/registrations.json")
    if not championships:
        print("Nenhum campeonato cadastrado.\n")
        return None

    for championship in championships:
        print(f"ID: {championship['id']} | Nome: {championship['name']} | Descrição: {championship['description']}")

        # Mostra organizações inscritas se o usuário for admin
        if role == "admin":
            orgs = [r["username"] for r in registrations if r["championship_id"] == championship["id"]]
            if orgs:
                print("   Organizações inscritas:")
                for org in orgs:
                    print(f"     - {org}")
            else:
                print("   Nenhuma organização inscrita.")
        print()  # linha em branco

    return championships


def add_championship():
    try:
        name = input("Nome do campeonato: ").strip()
        description = input("Descrição: ").strip()

        championships = load_data("jsons/championships.json")

        new_id = max([c["id"] for c in championships], default=0) + 1
        championships.append({"id": new_id, "name": name, "description": description})

        save_data("jsons/championships.json", championships)
        print("✅ Campeonato adicionado com sucesso!\n")

        updated_championships = load_data("jsons/championships.json")
        return updated_championships
    except Exception as error:
        print(f"Erro: {error}")


def edit_championship():
    list_championships("admin")
    try:
        championship_id = int(input("Digite o ID do campeonato que deseja editar: "))
        championships = load_data("jsons/championships.json")

        for championship in championships:
            if championship["id"] == championship_id:
                print("\nO que deseja editar?")
                print("1. Nome")
                print("2. Descrição")
                print("3. Ambos")
                option = input("Escolha: ").strip()

                if option == "1":
                    championship["name"] = input("Novo nome: ").strip()
                elif option == "2":
                    championship["description"] = input("Nova descrição: ").strip()
                elif option == "3":
                    championship["name"] = input("Novo nome: ").strip()
                    championship["description"] = input("Nova descrição: ").strip()
                else:
                    print("Opção inválida.\n")
                    return None

                save_data("jsons/championships.json", championships)
                print("✅ Campeonato atualizado!\n")

                updated_championships = load_data("jsons/championships.json")
                return updated_championships

        print("❌ ID não encontrado.\n")
    except ValueError:
        print("ID inválido.\n")


def remove_championship():
    list_championships("admin")

    try:
        championship_id = int(input("Digite o ID do campeonato a excluir: "))
        championships = load_data("jsons/championships.json")

        championships = [championship for championship in championships if championship["id"] != championship_id]

        save_data("jsons/championships.json", championships)
        print("✅ Campeonato removido.\n")

        updated_championships = load_data("jsons/championships.json")
        return updated_championships
    except ValueError:
        print("ID inválido.\n")


# ---------- Inscrição ----------
def register_for_championship(username):
    list_championships()
    try:
        championship_id = int(input("Digite o ID do campeonato para se inscrever: "))
        registrations = load_data("jsons/registrations.json")
        already_registered = any(
            registration["username"] == username and registration["championship_id"] == championship_id
            for registration in registrations
        )

        if already_registered:
            print("⚠️ Já inscrito nesse campeonato!\n")
            return registrations

        registrations.append({"username": username, "championship_id": championship_id})

        save_data("jsons/registrations.json", registrations)
        print("✅ Inscrição realizada!\n")

        updated_registrations = load_data("jsons/registrations.json")
        return updated_registrations
    except ValueError:
        print("ID inválido.\n")