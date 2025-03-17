import { Request, Response } from 'express';
import { CreateItemDTO } from '../../application/dtos/itemDTOs';
import { CreateItemUseCase } from '../../application/useCases/itemUseCases';

export async function createItem(req: Request<{}, {}, CreateItemDTO>, res: Response): Promise<void> {
  try {
    const novoItem = await CreateItemUseCase(req.body);
    res.status(201).json(novoItem);
  } catch (error) {
    res.status(400).json({ message: 'Erro ao criar item' });
  }
}
