export class Item {
  constructor(
    public id: number,
    public assetCode: string,
    public description: string,
    public acquisitionDate: Date,
    public acquisitionMethod: string,
    public supplier: string,
    public physicalLocation: string,
    public oldPhysicalLocation: string,
    public imageUrl: string,
    public status: string,
    public inventoried: boolean,
    public reference: string,
    public observation: string,
    public changed: boolean,
    public createdAt?: Date,
    public updatedAt?: Date
  ) {}
}
