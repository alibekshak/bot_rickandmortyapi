import requests


def get_character(id):
    url = f'https://rickandmortyapi.com/api/{id}'
    response = requests.get(url)
    data = response.json()
    return data


def character_id (id):
    try:
        data = get_character(f"character/{id}")
        text = f"""
Изображение персонажа: {data['image']}
Идентификатор персонажа: {data['id']}
Имя персонажа: {data['name']}
Статус персонажа: {data['status']}
Вид персонажа: {data['species']}
Тип или подвид персонажа: {data['type']}
Пол персонажа: {data['gender']}
Происхождение: {data['origin']['name']}
Местоположение: {data['location']['name']}
{character_episodes(id)}
        """
        return text

    except Exception:
        return "Персонажа с таким айди не существует"


def character_episodes(id):
    get_episodes = get_character(f"character/{id}")
    for i in get_episodes.keys():
        if i == "episode":
            episodes_information = f"""
В каких эпизодах был: {get_episodes["episode"]}
            """
    return episodes_information


def episodes(id):
    get_id = get_character(f"character/{id}")
    for i in get_id.keys():
        if i == 'episode':
            episode_url = get_id["url"]
            episode_id = episode_url.split('/')[-1]
            get_id_episodes = get_character(f"episode/{episode_id}")
            episodes_name =get_id_episodes["name"]
            episodes_air_date = get_id_episodes["air_date"]
            episodes = get_id_episodes["episode"]
            episodes_created = get_id_episodes["created"]
            episodes_information = f"""
Название эпизода: {episodes_name}
Дата выхода: {episodes_air_date}
Эпизод: {episodes}
Дата создания: {episodes_created}
            """
            return episodes_information

