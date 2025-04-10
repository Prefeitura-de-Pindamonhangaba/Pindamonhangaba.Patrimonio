export interface PhysicalLocation {
  id: number;
  acronym: string;
  active: boolean;
  observation: string | null;
  module: string;
  level: number;
  code: string;
  description: string;
  managementUnit: string;
  createdAt: string;
  updatedAt: string;
} 