"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ItemRepository = void 0;
const itemModel_1 = require("../database/models/itemModel");
const itemEntity_1 = require("../../domain/entities/itemEntity");
class ItemRepository {
    async create(item) {
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
        const createdItem = await itemModel_1.ItemModel.create(plainItem);
        return this.mapModelToEntity(createdItem);
    }
    async findById(id) {
        const itemModel = await itemModel_1.ItemModel.findByPk(id);
        return itemModel ? this.mapModelToEntity(itemModel) : null;
    }
    mapModelToEntity(itemModel) {
        return new itemEntity_1.Item(itemModel.id, itemModel.assetCode, itemModel.description, itemModel.acquisitionDate, itemModel.acquisitionMethod, itemModel.supplier, itemModel.physicalLocation, itemModel.oldPhysicalLocation, itemModel.imageUrl, itemModel.status, itemModel.inventoried, itemModel.reference, itemModel.observation, itemModel.itemChanged, itemModel.createdAt, itemModel.updatedAt);
    }
}
exports.ItemRepository = ItemRepository;
