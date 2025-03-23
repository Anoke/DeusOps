FROM node:18-alpine AS builder

WORKDIR /usr/src/app

COPY ./express-postgres-starterpackage*.json ./
RUN npm install && npm cache clean --force

COPY . .

FROM node:18-alpine
WORKDIR /usr/src/app

COPY --from=builder /usr/src/app .

CMD ["sh", "-c", "node bin/migrate.js up && node bin/start.js"]
