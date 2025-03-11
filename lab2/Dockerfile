FROM node:18-alpine

WORKDIR /usr/src/app

COPY ./express-postgres-starter/package*.json ./

RUN npm install && npm cache clean --force

COPY ./express-postgres-starter .

# Запускаем миграции перед стартом приложения
CMD ["sh", "-c", "node bin/migrate.js up && node bin/start.js"]
