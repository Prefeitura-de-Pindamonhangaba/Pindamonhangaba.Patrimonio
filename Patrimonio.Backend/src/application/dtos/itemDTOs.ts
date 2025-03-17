export type CreateItemDTO = {
  assetCode: string;
  description: string;
  acquisitionDate: Date;
  acquisitionMethod: string;
  supplier: string;
  physicalLocationId: number;
  oldPhysicalLocationId: number;
  imageUrl: string;
  status: string;
  inventoried: boolean;
  reference: string;
  observation: string;
};
