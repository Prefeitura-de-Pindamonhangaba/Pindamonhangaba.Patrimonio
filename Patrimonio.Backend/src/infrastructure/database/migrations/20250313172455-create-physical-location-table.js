'use strict';

module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.createTable('physicalLocations', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER,
      },
      referencial: {
        type: Sequelize.STRING,
        allowNull: false,
      },
      refProprio: {
        type: Sequelize.STRING,
        allowNull: true,
      },
      refSubordinacao: {
        type: Sequelize.STRING,
        allowNull: true,
      },
      refSubordinacaoAdmMigra: {
        type: Sequelize.STRING,
        allowNull: true,
      },
      refResponsavel: {
        type: Sequelize.STRING,
        allowNull: true,
      },
      refTipoMigra: {
        type: Sequelize.STRING,
        allowNull: true,
      },
      sigla: {
        type: Sequelize.STRING,
        allowNull: true,
      },
      ativo: {
        type: Sequelize.BOOLEAN,
        allowNull: true,
      },
      obs: {
        type: Sequelize.TEXT,
        allowNull: true,
      },
      modulo: {
        type: Sequelize.STRING,
        allowNull: true,
      },
      nivel: {
        type: Sequelize.INTEGER,
        allowNull: true,
      },
      codigo: {
        type: Sequelize.STRING,
        allowNull: true,
      },
      descricao: {
        type: Sequelize.STRING,
        allowNull: true,
      },
      unidadeGestora: {
        type: Sequelize.INTEGER,
        allowNull: true,
      },
      refTipo: {
        type: Sequelize.STRING,
        allowNull: true,
      },
      refSubordinacaoAdm: {
        type: Sequelize.STRING,
        allowNull: true,
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE,
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE,
      },
    });
  },

  async down(queryInterface, Sequelize) {
    await queryInterface.dropTable('physicalLocations');
  },
};