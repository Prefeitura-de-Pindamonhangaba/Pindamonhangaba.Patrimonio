"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ItemRepository = void 0;
const itemModel_1 = require("../database/models/itemModel");
const itemEntity_1 = require("../../domain/entities/itemEntity");
const physicalLocationEntity_1 = require("../../domain/entities/physicalLocationEntity");
class ItemRepository {
    async create(item) {
        const createdItem = await itemModel_1.ItemModel.create(item.toPlainObject());
        return this.mapModelToEntity(createdItem);
    }
    async findById(id) {
        const itemModel = await itemModel_1.ItemModel.findByPk(id);
        return itemModel ? this.mapModelToEntity(itemModel) : null;
    }
    mapModelToEntity(itemModel) {
        return new itemEntity_1.Item(itemModel.assetCode, itemModel.description, itemModel.acquisitionDate, itemModel.acquisitionMethod, itemModel.supplier, new physicalLocationEntity_1.PhysicalLocation(itemModel.physicalLocation.referencial, itemModel.physicalLocation.refProprio, itemModel.physicalLocation.refSubordinacao, itemModel.physicalLocation.refSubordinacaoAdmMigra, itemModel.physicalLocation.refResponsavel, itemModel.physicalLocation.refTipoMigra, itemModel.physicalLocation.sigla, itemModel.physicalLocation.ativo, itemModel.physicalLocation.obs, itemModel.physicalLocation.modulo, itemModel.physicalLocation.nivel, itemModel.physicalLocation.codigo, itemModel.physicalLocation.descricao, itemModel.physicalLocation.unidadeGestora, itemModel.physicalLocation.refTipo, itemModel.physicalLocation.refSubordinacaoAdm, itemModel.physicalLocation.createdAt, itemModel.physicalLocation.updatedAt), new physicalLocationEntity_1.PhysicalLocation(itemModel.oldPhysicalLocation.referencial, itemModel.oldPhysicalLocation.refProprio, itemModel.oldPhysicalLocation.refSubordinacao, itemModel.oldPhysicalLocation.refSubordinacaoAdmMigra, itemModel.oldPhysicalLocation.refResponsavel, itemModel.oldPhysicalLocation.refTipoMigra, itemModel.oldPhysicalLocation.sigla, itemModel.oldPhysicalLocation.ativo, itemModel.oldPhysicalLocation.obs, itemModel.oldPhysicalLocation.modulo, itemModel.oldPhysicalLocation.nivel, itemModel.oldPhysicalLocation.codigo, itemModel.oldPhysicalLocation.descricao, itemModel.oldPhysicalLocation.unidadeGestora, itemModel.oldPhysicalLocation.refTipo, itemModel.oldPhysicalLocation.refSubordinacaoAdm, itemModel.oldPhysicalLocation.createdAt, itemModel.oldPhysicalLocation.updatedAt), itemModel.imageUrl, itemModel.status, itemModel.inventoried, itemModel.reference, itemModel.observation, itemModel.createdAt, itemModel.updatedAt);
    }
}
exports.ItemRepository = ItemRepository;
