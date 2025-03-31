FROM node:alpine

WORKDIR /app

# Копируем только фронтенд часть
COPY --from=app-source /repo/react-frontend /app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup && \
    chown -R appuser:appgroup /app

USER appuser

RUN npm ci && \
    npm cache clean --force

CMD ["npm", "start"]