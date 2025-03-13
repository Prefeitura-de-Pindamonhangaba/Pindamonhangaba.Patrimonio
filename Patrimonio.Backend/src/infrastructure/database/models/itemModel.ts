import { Table, Column, Model, DataType } from 'sequelize-typescript';

@Table({
  tableName: 'items',
  timestamps: true,
})
export class ItemModel extends Model {
  @Column({
    type: DataType.STRING,
    allowNull: false,
    unique: true,
  })
  assetCode!: string;

  @Column({
    type: DataType.STRING,
    allowNull: false,
  })
  description!: string;

  @Column({
    type: DataType.DATE,
    allowNull: false,
  })
  acquisitionDate!: Date;

  @Column({
    type: DataType.STRING,
    allowNull: true,
  })
  acquisitionMethod!: string;

  @Column({
    type: DataType.STRING,
    allowNull: true,
  })
  supplier!: string;

  @Column({
    type: DataType.STRING,
    allowNull: false,
  })
  physicalLocation!: string;

  @Column({
    type: DataType.STRING,
    allowNull: true,
  })
  oldPhysicalLocation!: string;

  @Column({
    type: DataType.STRING,
    allowNull: true,
  })
  imageUrl!: string;

  @Column({
    type: DataType.STRING,
    allowNull: true,
  })
  status!: string;

  @Column({
    type: DataType.BOOLEAN,
    allowNull: false,
    defaultValue: false,
  })
  inventoried!: boolean;

  @Column({
    type: DataType.STRING,
    allowNull: true,
  })
  reference!: string;

  @Column({
    type: DataType.TEXT,
    allowNull: true,
  })
  observation!: string;

  @Column({
    type: DataType.BOOLEAN,
    allowNull: false,
    defaultValue: false,
  })
  itemChanged!: boolean;
}