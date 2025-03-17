import { ItemModel } from '../database/models/itemModel';
import { Item } from '../../domain/entities/itemEntity';
import { CreatedAt } from 'sequelize-typescript';
import { PhysicalLocationRepository } from './physicalLocationRepository';
import { PhysicalLocation } from '../../domain/entities/physicalLocationEntity';

export class ItemRepository {
  async create(item: Item): Promise<Item> {
    const createdItem = await ItemModel.create(item.toPlainObject());
    return this.mapModelToEntity(createdItem);
  }

  async findById(id: number): Promise<Item | null> {
    const itemModel = await ItemModel.findByPk(id);
    return itemModel ? this.mapModelToEntity(itemModel) : null;
  }

  private mapModelToEntity(itemModel: ItemModel): Item {
    return new Item(
      itemModel.assetCode,
      itemModel.description,
      itemModel.acquisitionDate,
      itemModel.acquisitionMethod,
      itemModel.supplier,
      new PhysicalLocation(
            itemModel.physicalLocation.referencial,
            itemModel.physicalLocation.refProprio,
            itemModel.physicalLocation.refSubordinacao,
            itemModel.physicalLocation.refSubordinacaoAdmMigra,
            itemModel.physicalLocation.refResponsavel,
            itemModel.physicalLocation.refTipoMigra,
            itemModel.physicalLocation.sigla,
            itemModel.physicalLocation.ativo,
            itemModel.physicalLocation.obs,
            itemModel.physicalLocation.modulo,
            itemModel.physicalLocation.nivel,
            itemModel.physicalLocation.codigo,
            itemModel.physicalLocation.descricao,
            itemModel.physicalLocation.unidadeGestora,
            itemModel.physicalLocation.refTipo,
            itemModel.physicalLocation.refSubordinacaoAdm,
            itemModel.physicalLocation.createdAt,
            itemModel.physicalLocation.updatedAt,
          ),
      itemModel.imageUrl,
      itemModel.status,
      itemModel.inventoried,
      itemModel.reference,
      itemModel.observation,
      new PhysicalLocation(
        itemModel.oldPhysicalLocation.referencial,
        itemModel.oldPhysicalLocation.refProprio,
        itemModel.oldPhysicalLocation.refSubordinacao,
        itemModel.oldPhysicalLocation.refSubordinacaoAdmMigra,
        itemModel.oldPhysicalLocation.refResponsavel,
        itemModel.oldPhysicalLocation.refTipoMigra,
        itemModel.oldPhysicalLocation.sigla,
        itemModel.oldPhysicalLocation.ativo,
        itemModel.oldPhysicalLocation.obs,
        itemModel.oldPhysicalLocation.modulo,
        itemModel.oldPhysicalLocation.nivel,
        itemModel.oldPhysicalLocation.codigo,
        itemModel.oldPhysicalLocation.descricao,
        itemModel.oldPhysicalLocation.unidadeGestora,
        itemModel.oldPhysicalLocation.refTipo,
        itemModel.oldPhysicalLocation.refSubordinacaoAdm,
        itemModel.oldPhysicalLocation.createdAt,
        itemModel.oldPhysicalLocation.updatedAt,
      ),
      itemModel.createdAt,
      itemModel.updatedAt
    );
  }
}