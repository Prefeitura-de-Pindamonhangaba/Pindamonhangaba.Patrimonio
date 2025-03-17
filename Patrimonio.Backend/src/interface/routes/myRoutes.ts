// interface/routes/myRoutes.ts

import express, { Router, Request, Response } from 'express';
import { createItem } from '../controllers/itemController';

const router: Router = express.Router();

router.post('/item', createItem);

// Adicione outras rotas aqui

export default router;