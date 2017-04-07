FROM golang:1.8

ADD . /zipper
WORKDIR /zipper

ENV GOBIN=/go/bin
ENV PORT=8000

RUN go get

EXPOSE 8000
CMD go run main.go 
