# Используем легковесный образ Node.js на базе Alpine
FROM node:18-alpine

# Устанавливаем рабочую директорию
WORKDIR /usr/src/app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем только production-зависимости
RUN npm install && npm cache clean --force

# Копируем все файлы проекта
COPY . .

# Запускаем миграции перед стартом приложения
CMD ["sh", "-c", "node bin/migrate.js up && node bin/start.js"]
