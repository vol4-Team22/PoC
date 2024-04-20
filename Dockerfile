FROM golang:1.22.2

WORKDIR /app

COPY ./backend /app

CMD ["go", "run", "main.go"]