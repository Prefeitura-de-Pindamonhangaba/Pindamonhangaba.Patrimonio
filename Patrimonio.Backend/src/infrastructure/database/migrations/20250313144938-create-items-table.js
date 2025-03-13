'use strict';

module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.createTable('items', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER,
      },
      code: {
        type: Sequelize.STRING,
        allowNull: false,
        unique: true,
      },
      assetCode: {
        type: Sequelize.STRING,
        allowNull: false,
        unique: true,
      },
      description: {
        type: Sequelize.STRING,
        allowNull: false,
      },
      acquisitionDate: {
        type: Sequelize.DATE,
        allowNull: false,
      },
      acquisitionMethod: {
        type: Sequelize.STRING,
        allowNull: true,
      },
      supplier: {
        type: Sequelize.STRING,
        allowNull: true,
      },
      physicalLocation: {
        type: Sequelize.STRING,
        allowNull: false,
      },
      oldPhysicalLocation: {
        type: Sequelize.STRING,
        allowNull: true,
      },
      imageUrl: {
        type: Sequelize.STRING,
        allowNull: true,
      },
      status: {
        type: Sequelize.STRING,
        allowNull: true,
      },
      inventoried: {
        type: Sequelize.BOOLEAN,
        allowNull: false,
        defaultValue: false,
      },
      reference: {
        type: Sequelize.STRING,
        allowNull: true,
      },
      observation: {
        type: Sequelize.TEXT,
        allowNull: true,
      },
      itemChanged: {
        type: Sequelize.BOOLEAN,
        allowNull: false,
        defaultValue: false,
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
    await queryInterface.dropTable('items');
  },
};