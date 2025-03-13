"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Item = void 0;
class Item {
    constructor(id, assetCode, description, acquisitionDate, acquisitionMethod, supplier, physicalLocation, oldPhysicalLocation, imageUrl, status, inventoried, reference, observation, changed, createdAt, updatedAt) {
        this.id = id;
        this.assetCode = assetCode;
        this.description = description;
        this.acquisitionDate = acquisitionDate;
        this.acquisitionMethod = acquisitionMethod;
        this.supplier = supplier;
        this.physicalLocation = physicalLocation;
        this.oldPhysicalLocation = oldPhysicalLocation;
        this.imageUrl = imageUrl;
        this.status = status;
        this.inventoried = inventoried;
        this.reference = reference;
        this.observation = observation;
        this.changed = changed;
        this.createdAt = createdAt;
        this.updatedAt = updatedAt;
    }
}
exports.Item = Item;
