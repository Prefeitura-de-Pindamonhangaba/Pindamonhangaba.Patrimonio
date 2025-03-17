import { Table, Column, Model, DataType, ForeignKey, BelongsTo } from 'sequelize-typescript';
import { PhysicalLocationModel } from './physicalLocationModel';

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

  @ForeignKey(() => PhysicalLocationModel)
  @Column({
    type: DataType.INTEGER,
    allowNull: false,
  })
  physicalLocationId!: number;

  @BelongsTo(() => PhysicalLocationModel)
  physicalLocation!: PhysicalLocationModel;

  @ForeignKey(() => PhysicalLocationModel)
  @Column({
    type: DataType.INTEGER,
    allowNull: true,
  })
  oldPhysicalLocationId!: number;

  @BelongsTo(() => PhysicalLocationModel)
  oldPhysicalLocation!: PhysicalLocationModel;

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