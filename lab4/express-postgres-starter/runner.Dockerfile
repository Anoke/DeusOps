FROM node:18-alpine

WORKDIR /usr/src/app

COPY --from=build /usr/src/app .

RUN npm cache clean --force

# Запуск приложения (миграции и затем стартап)
CMD ["sh", "-c", "node bin/migrate.js up && node bin/start.js"]
