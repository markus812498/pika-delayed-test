FROM ruby:3-alpine
RUN apk add build-base
WORKDIR /usr/src/app
COPY . .
USER nobody:nogroup
CMD ["ruby", "app.rb"]
