import { ItemModel } from '../database/models/itemModel';
import { Item } from '../../domain/entities/itemEntity';

export class ItemRepository {
  async create(item: Item): Promise<Item> {
    const plainItem = {
      assetCode: item.assetCode,
      description: item.description,
      acquisitionDate: item.acquisitionDate,
      acquisitionMethod: item.acquisitionMethod,
      supplier: item.supplier,
      physicalLocation: item.physicalLocation,
      oldPhysicalLocation: item.oldPhysicalLocation,
      imageUrl: item.imageUrl,
      status: item.status,
      inventoried: item.inventoried,
      reference: item.reference,
      observation: item.observation
    };
    const createdItem = await ItemModel.create(plainItem);
    return this.mapModelToEntity(createdItem);
  }

  async findById(id: number): Promise<Item | null> {
    const itemModel = await ItemModel.findByPk(id);
    return itemModel ? this.mapModelToEntity(itemModel) : null;
  }

  private mapModelToEntity(itemModel: ItemModel): Item {
    return new Item(
      itemModel.id,
      itemModel.assetCode,
      itemModel.description,
      itemModel.acquisitionDate,
      itemModel.acquisitionMethod,
      itemModel.supplier,
      itemModel.physicalLocation,
      itemModel.oldPhysicalLocation,
      itemModel.imageUrl,
      itemModel.status,
      itemModel.inventoried,
      itemModel.reference,
      itemModel.observation,
      itemModel.itemChanged,
      itemModel.createdAt,
      itemModel.updatedAt,
    );
  }
}