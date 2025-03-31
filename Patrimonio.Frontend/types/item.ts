import type { PhysicalLocation } from './physicalLocation';

export interface Item {
  id: number;
  assetCode: string;
  description: string;
  acquisitionDate: string | null;
  acquisitionMethod: string | null;
  supplier: string | null;
  physicalLocation: PhysicalLocation | null;
  oldPhysicalLocation: PhysicalLocation | null;
  imageUrl: string | null;
  status: string | null;
  inventoried: boolean;
  reference: string | null;
  observation: string | null;
  itemChanged: boolean;
  createdAt: string;
  updatedAt: string;
}