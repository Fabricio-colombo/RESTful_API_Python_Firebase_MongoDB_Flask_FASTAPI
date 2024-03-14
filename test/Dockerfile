FROM node

WORKDIR /user-app

COPY package*.json /user-app/

RUN npm install

COPY . /user-app/

EXPOSE 3000

CMD ["npm", "start"]