export type Item = {
  acquisitionDate: string;
  acquisitionMethod: string;
  assetCode: string;
  createdAt: string;
  description: string;
  id: number;
  imageUrl: string | null;
  inventoried: boolean;
  itemChanged: boolean;
  observation: string | null;
  oldPhysicalLocationId: number | null;
  physicalLocationId: number;
  reference: string;
  status: string;
  supplier: string;
  updatedAt: string;
}