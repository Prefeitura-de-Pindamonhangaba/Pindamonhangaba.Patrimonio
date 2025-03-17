// src/domain/entities/physicalLocation.ts
export class PhysicalLocation {
  constructor(
    public referencial: string,
    public refProprio: string,
    public refSubordinacao: string,
    public refSubordinacaoAdmMigra: string,
    public refResponsavel: string,
    public refTipoMigra: string,
    public sigla: string,
    public ativo: boolean,
    public obs: string,
    public modulo: string,
    public nivel: number,
    public codigo: string,
    public descricao: string,
    public unidadeGestora: number,
    public refTipo: string,
    public refSubordinacaoAdm: string,
    public createdAt: Date,
    public updatedAt: Date,
  ) {}

  public toPlainObject(): any {
    return {
      referencial: this.referencial,
      refProprio: this.refProprio,
      refSubordinacao: this.refSubordinacao,
      refSubordinacaoAdmMigra: this.refSubordinacaoAdmMigra,
      refResponsavel: this.refResponsavel,
      refTipoMigra: this.refTipoMigra,
      sigla: this.sigla,
      ativo: this.ativo,
      obs: this.obs,
      modulo: this.modulo,
      nivel: this.nivel,
      codigo: this.codigo,
      descricao: this.descricao,
      unidadeGestora: this.unidadeGestora,
      refTipo: this.refTipo,
      refSubordinacaoAdm: this.refSubordinacaoAdm,
      createdAt: this.createdAt,
      updatedAt: this.updatedAt,
    };
  }
}