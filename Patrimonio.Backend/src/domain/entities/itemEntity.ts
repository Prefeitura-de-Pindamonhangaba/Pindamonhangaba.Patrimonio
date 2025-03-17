import { PhysicalLocation } from "./physicalLocationEntity";

export class Item {
  constructor(
    public assetCode: string,
    public description: string,
    public acquisitionDate: Date,
    public acquisitionMethod: string,
    public supplier: string,
    public physicalLocation: PhysicalLocation,
    public oldPhysicalLocation: PhysicalLocation,
    public imageUrl: string,
    public status: string,
    public inventoried: boolean,
    public reference: string,
    public observation: string,
    public createdAt?: Date,
    public updatedAt?: Date
  ) {}

  public toPlainObject(): any {
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
