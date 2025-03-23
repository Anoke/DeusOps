FROM system AS build

COPY . .

# тут если для проекта нужна сборка в стиле npm run build, то использовать
# RUN npm run build, но для текущего проекта сборка не нужна
