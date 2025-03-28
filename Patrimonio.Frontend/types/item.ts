import type { PhysicalLocation } from './physicalLocation';

export interface Item {
  id: number;
  assetCode: string;
  description: string;
  acquisitionDate: string | null;
  acquisitionMethod: string;
  supplier: string;
  physicalLocationId: number;
  oldPhysicalLocationId: number;
  imageUrl: string;
  status: string;
  inventoried: boolean;
  reference: string;
  observation: string;
  itemChanged: boolean;
  createdAt: string;
  updatedAt: string;
  physicalLocation: PhysicalLocation | null;
  oldPhysicalLocation: PhysicalLocation | null;
}