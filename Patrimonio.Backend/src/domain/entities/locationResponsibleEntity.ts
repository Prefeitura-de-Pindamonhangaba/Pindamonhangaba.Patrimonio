export class LocationResponsible {
  constructor(
    public reference: string,
    public name: string,
    public active: boolean,
    public obs: string,
    public startDate: Date,
    public endDate: Date,
    public position: string,
    public employeeId: number,
    public managementUnitId: number,
    public createdAt: Date,
    public updatedAt: Date,
  ) {}

  toPlainObject(): any {
    return {
      reference: this.reference,
      name: this.name,
      active: this.active,
      obs: this.obs,
      startDate: this.startDate,
      endDate: this.endDate,
      position: this.position,
      employeeId: this.employeeId,
      managementUnitId: this.managementUnitId,
      createdAt: this.createdAt,
      updatedAt: this.updatedAt,
    };
  }
}