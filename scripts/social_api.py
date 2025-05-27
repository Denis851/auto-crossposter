import os
import vk_api
from dotenv import load_dotenv

load_dotenv()
VK_TOKEN = os.getenv('VK_TOKEN')

def post_to_vk(text, group_id=None):
    """
    Публикация поста в VK.
    Если указан group_id — постит в группу, иначе — на личную страницу.
    """
    try:
        vk_session = vk_api.VkApi(token=VK_TOKEN)
        vk = vk_session.get_api()

        if group_id:
            # Постинг в группу от имени группы
            vk.wall.post(owner_id=-int(group_id), from_group=1, message=text)
        else:
            # Постинг на личную страницу
            vk.wall.post(message=text)

        print("Пост отправлен в VK!")
    except Exception as e:
        print("Ошибка при отправке в VK:", e)

