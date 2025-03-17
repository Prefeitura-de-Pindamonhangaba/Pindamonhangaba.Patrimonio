import { PhysicalLocation } from "../../domain/entities/physicalLocationEntity";
import { PhysicalLocationModel } from "../database/models/physicalLocationModel";

export class PhysicalLocationRepository {
  async create(physicalLocation: PhysicalLocation): Promise<PhysicalLocation> {
    const createdPhysicalLocation = await PhysicalLocationModel.create(physicalLocation.toPlainObject());
    return this.mapModelToEntity(createdPhysicalLocation);
  }

  async findById(id: number): Promise<PhysicalLocation | null> {
    const physicalLocationModel = await PhysicalLocationModel.findByPk(id);
    return physicalLocationModel ? this.mapModelToEntity(physicalLocationModel) : null;
  }

  private mapModelToEntity(physicalLocationModel: PhysicalLocationModel): PhysicalLocation {
    return new PhysicalLocation(
      physicalLocationModel.referencial,
      physicalLocationModel.refProprio,
      physicalLocationModel.refSubordinacao,
      physicalLocationModel.refSubordinacaoAdmMigra,
      physicalLocationModel.refResponsavel,
      physicalLocationModel.refTipoMigra,
      physicalLocationModel.sigla,
      physicalLocationModel.ativo,
      physicalLocationModel.obs,
      physicalLocationModel.modulo,
      physicalLocationModel.nivel,
      physicalLocationModel.codigo,
      physicalLocationModel.descricao,
      physicalLocationModel.unidadeGestora,
      physicalLocationModel.refTipo,
      physicalLocationModel.refSubordinacaoAdm,
      physicalLocationModel.createdAt,
      physicalLocationModel.updatedAt,
    );
  }
}