// src/infrastructure/database/models/locationResponsibleModel.ts
import { Table, Column, Model, DataType } from 'sequelize-typescript';

@Table({
  tableName: 'locationResponsibles',
  timestamps: true,
})
export class LocationResponsibleModel extends Model {
  @Column({
    type: DataType.STRING,
    allowNull: false,
  })
  reference!: string;

  @Column({
    type: DataType.STRING,
    allowNull: false,
  })
  name!: string;

  @Column({
    type: DataType.BOOLEAN,
    allowNull: true,
  })
  active!: boolean;

  @Column({
    type: DataType.TEXT,
    allowNull: true,
  })
  obs!: string;

  @Column({
    type: DataType.DATE,
    allowNull: true,
  })
  startDate!: Date;

  @Column({
    type: DataType.DATE,
    allowNull: true,
  })
  endDate!: Date;

  @Column({
    type: DataType.STRING,
    allowNull: true,
  })
  position!: string;

  @Column({
    type: DataType.INTEGER,
    allowNull: false,
  })
  employeeId!: number;

  @Column({
    type: DataType.INTEGER,
    allowNull: false,
  })
  managementUnitId!: number;
}