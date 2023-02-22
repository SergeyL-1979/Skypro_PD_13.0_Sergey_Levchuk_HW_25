# Этот файл для глобальных констант. Чтобы не хардкодить строки/числа в коде, выносите их сюда.
# например вместо C:\\Windows в коде, создайте константу WINDOWS_PATH здесь и присвойте ей значение

# Пример

# CONSTANT_NAME = "value"
# LOG_DIR = "logs"
# Добавляем константы в файл constants.py
from app.config import Config

JWT_SECRET = Config.SECRET_KEY
JWT_ALGORITHM = "HS256"

PWD_HASH_SALT = b'secret here'
PWD_HASH_ITERATIONS = 100_000
