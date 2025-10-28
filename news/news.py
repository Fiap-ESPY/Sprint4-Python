# ---------- CRUD de Notícias ----------
from utils.utils import load_data, save_data


def list_news():
    news_list = load_data("jsons/news.json")
    if not news_list:
        print("Nenhuma notícia cadastrada.\n")
        return None

    for news_item in news_list:
        print(f"ID: {news_item['id']} | Título: {news_item['title']} | Texto: {news_item['text']}\n")

    return news_list

def add_news():
    title = input("Título da notícia: ").strip()
    text = input("Texto: ").strip()
    news_list = load_data("jsons/news.json")

    new_id = max([news_item["id"] for news_item in news_list], default=0) + 1
    news_list.append({"id": new_id, "title": title, "text": text})

    save_data("jsons/news.json", news_list)
    print("✅ Notícia adicionada!\n")

    updated_news_list = load_data("jsons/news.json")
    return updated_news_list


def edit_news():
    list_news()

    try:
        news_id = int(input("Digite o ID da notícia a editar: "))
        news_list = load_data("jsons/news.json")
        for news_item in news_list:
            if news_item["id"] == news_id:
                news_item["title"] = input("Novo título: ").strip()
                news_item["text"] = input("Novo texto: ").strip()

                save_data("jsons/news.json", news_list)
                print("✅ Notícia atualizada!\n")

                updated_news_list = load_data("jsons/news.json")
                return updated_news_list

        print("❌ ID não encontrado.\n")
    except ValueError:
        print("ID inválido.\n")


def remove_news():
    list_news()

    try:
        news_id = int(input("Digite o ID da notícia a excluir: "))
        news_list = load_data("jsons/news.json")
        news_list = [news_item for news_item in news_list if news_item["id"] != news_id]

        save_data("jsons/news.json", news_list)
        print("✅ Notícia removida.\n")

        updated_news_list = load_data("jsons/news.json")
        return updated_news_list
    except ValueError:
        print("ID inválido.\n")
