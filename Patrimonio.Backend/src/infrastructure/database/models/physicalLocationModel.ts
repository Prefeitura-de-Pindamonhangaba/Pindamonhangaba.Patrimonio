import { Table, Column, Model, DataType } from 'sequelize-typescript';

@Table({
  tableName: 'physicalLocations',
  timestamps: true,
})
export class PhysicalLocationModel extends Model {
  @Column({
    type: DataType.STRING,
    allowNull: false,
  })
  referencial!: string;

  @Column({
    type: DataType.STRING,
    allowNull: true,
  })
  refProprio!: string;

  @Column({
    type: DataType.STRING,
    allowNull: true,
  })
  refSubordinacao!: string;

  @Column({
    type: DataType.STRING,
    allowNull: true,
  })
  refSubordinacaoAdmMigra!: string;

  @Column({
    type: DataType.STRING,
    allowNull: true,
  })
  refResponsavel!: string;

  @Column({
    type: DataType.STRING,
    allowNull: true,
  })
  refTipoMigra!: string;

  @Column({
    type: DataType.STRING,
    allowNull: true,
  })
  sigla!: string;

  @Column({
    type: DataType.BOOLEAN,
    allowNull: true,
  })
  ativo!: boolean;

  @Column({
    type: DataType.TEXT,
    allowNull: true,
  })
  obs!: string;

  @Column({
    type: DataType.STRING,
    allowNull: true,
  })
  modulo!: string;

  @Column({
    type: DataType.INTEGER,
    allowNull: true,
  })
  nivel!: number;

  @Column({
    type: DataType.STRING,
    allowNull: true,
  })
  codigo!: string;

  @Column({
    type: DataType.STRING,
    allowNull: true,
  })
  descricao!: string;

  @Column({
    type: DataType.INTEGER,
    allowNull: true,
  })
  unidadeGestora!: number;

  @Column({
    type: DataType.STRING,
    allowNull: true,
  })
  refTipo!: string;

  @Column({
    type: DataType.STRING,
    allowNull: true,
  })
  refSubordinacaoAdm!: string;
}