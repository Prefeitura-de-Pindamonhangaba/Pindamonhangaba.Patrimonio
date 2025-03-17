import express from 'express';
import myRoutes from '../interface/routes/myRoutes'

const app = express();

app.use(express.json());

app.use('/api', myRoutes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Servidor rodando na porta ${PORT}`);
});