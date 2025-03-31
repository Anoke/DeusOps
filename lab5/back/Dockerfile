FROM eclipse-temurin:17-alpine

WORKDIR /app

# Копируем только бэкенд часть
COPY --from=app-source /repo/spring-backend /app

RUN apk add --no-cache maven && \
    mvn clean package && \
    apk del maven && \
    rm -rf /var/cache/apk/* /tmp/* /root/.m2

RUN addgroup -S appgroup && adduser -S appuser -G appgroup && \
    chown -R appuser:appgroup /app

USER appuser

CMD ["sh", "-c", "java -jar target/$(ls target/ | grep -E '.*\\.jar$')"]