def get_direct_image_link(github_link: str) -> str:
    # Предполагаем, что пользователь вводит полную ссылку на файл
    # Пример: https://github.com/USERNAME/REPO/blob/BRANCH/PATH_TO_IMAGE

    # Извлекаем необходимые части из ссылки
    if "github.com" in github_link and "blob" in github_link:
        parts = github_link.split('/')
        username = parts[3]  # USERNAME
        repo = parts[4]      # REPO
        branch = parts[6]    # BRANCH
        path_to_file = '/'.join(parts[7:])  # PATH_TO_IMAGE
        direct_link = f"https://raw.githubusercontent.com/{username}/{repo}/{branch}/{path_to_file}"
        return direct_link
    else:
        return ""  # Возвращаем пустую строку или сообщение об ошибке
