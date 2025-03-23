FROM node:18-alpine AS system_stage

# Устанавливаем рабочую директорию
WORKDIR /usr/src/app

# Копируем только package.json для установки зависимостей
COPY ./package*.json ./

# Устанавливаем зависимости (не устанавливаем дополнительные пакеты)
RUN npm install && npm cache clean --force
