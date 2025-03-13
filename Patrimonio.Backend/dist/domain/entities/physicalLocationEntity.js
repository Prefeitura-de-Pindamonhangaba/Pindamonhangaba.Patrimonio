"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.PhysicalLocation = void 0;
// src/domain/entities/physicalLocation.ts
class PhysicalLocation {
    constructor(referencial, refProprio, refSubordinacao, refSubordinacaoAdmMigra, refResponsavel, refTipoMigra, sigla, ativo, obs, modulo, nivel, codigo, descricao, unidadeGestora, refTipo, refSubordinacaoAdm, createdAt, updatedAt) {
        this.referencial = referencial;
        this.refProprio = refProprio;
        this.refSubordinacao = refSubordinacao;
        this.refSubordinacaoAdmMigra = refSubordinacaoAdmMigra;
        this.refResponsavel = refResponsavel;
        this.refTipoMigra = refTipoMigra;
        this.sigla = sigla;
        this.ativo = ativo;
        this.obs = obs;
        this.modulo = modulo;
        this.nivel = nivel;
        this.codigo = codigo;
        this.descricao = descricao;
        this.unidadeGestora = unidadeGestora;
        this.refTipo = refTipo;
        this.refSubordinacaoAdm = refSubordinacaoAdm;
        this.createdAt = createdAt;
        this.updatedAt = updatedAt;
    }
    toPlainObject() {
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
exports.PhysicalLocation = PhysicalLocation;
