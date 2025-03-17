import { CreateItemDTO } from "../dtos/itemDTOs";
import { ItemRepository } from "../../infrastructure/repositories/itemRepository";
import { Item } from "../../domain/entities/itemEntity";
import { PhysicalLocationRepository } from "../../infrastructure/repositories/physicalLocationRepository";

export async function CreateItemUseCase(newItem: CreateItemDTO) {
  let itemRepository = new ItemRepository();
  let physicalLocationRepository = new PhysicalLocationRepository();

  if (!newItem.physicalLocationId) {
    throw new Error("O ID da localização física é obrigatório.");
  }
  const physicalLocation = await physicalLocationRepository.findById(
    newItem.physicalLocationId
  );
  if (!physicalLocation) {
    throw new Error(
      `Localização física com ID ${newItem.physicalLocationId} não encontrada.`
    );
  }

  let newItemEntity = new Item(
    newItem.assetCode,
    newItem.description,
    newItem.acquisitionDate,
    newItem.acquisitionMethod,
    newItem.supplier,
    physicalLocation,
    newItem.imageUrl,
    newItem.status,
    newItem.inventoried,
    newItem.reference,
    newItem.observation,
    await physicalLocationRepository.findById(newItem.oldPhysicalLocationId)
  );

  itemRepository.create(newItemEntity);
}
