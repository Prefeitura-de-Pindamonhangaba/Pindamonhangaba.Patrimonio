import dotenv from 'dotenv';

dotenv.config();

export default {
  db: {
    username: process.env.DB_USERNAME || '',
    password: process.env.DB_PASSWORD || '',
    database: process.env.DB_DATABASE || '',
    host: process.env.DB_HOST || '',
    dialect: process.env.DB_DIALECT || '',
  },
  server: {
    port: process.env.PORT || 3000
  },
};