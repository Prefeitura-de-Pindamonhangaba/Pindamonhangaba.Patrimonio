"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Item = void 0;
class Item {
    constructor(assetCode, description, acquisitionDate, acquisitionMethod, supplier, physicalLocation, imageUrl, status, inventoried, reference, observation, oldPhysicalLocation, createdAt, updatedAt) {
        this.assetCode = assetCode;
        this.description = description;
        this.acquisitionDate = acquisitionDate;
        this.acquisitionMethod = acquisitionMethod;
        this.supplier = supplier;
        this.physicalLocation = physicalLocation;
        this.imageUrl = imageUrl;
        this.status = status;
        this.inventoried = inventoried;
        this.reference = reference;
        this.observation = observation;
        this.oldPhysicalLocation = oldPhysicalLocation;
        this.createdAt = createdAt;
        this.updatedAt = updatedAt;
    }
    toPlainObject() {
        return {
            assetCode: this.assetCode,
            description: this.description,
            acquisitionDate: this.acquisitionDate,
            acquisitionMethod: this.acquisitionMethod,
            supplier: this.supplier,
            physicalLocation: this.physicalLocation,
            oldPhysicalLocation: this.oldPhysicalLocation,
            imageUrl: this.imageUrl,
            status: this.status,
            inventoried: this.inventoried,
            reference: this.reference,
            observation: this.observation,
            createdAt: this.createdAt,
            updatedAt: this.updatedAt,
        };
    }
}
exports.Item = Item;
