'use strict';

module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.changeColumn('items', 'physicalLocationId', {
      type: Sequelize.INTEGER,
      allowNull: true, 
    });

    await queryInterface.changeColumn('items', 'oldPhysicalLocationId', {
      type: Sequelize.INTEGER,
      allowNull: true, 
    });

    await queryInterface.changeColumn('items', 'physicalLocationId', {
      type: Sequelize.INTEGER,
      references: {
        model: 'physicalLocations',
        key: 'id',
      },
      onUpdate: 'CASCADE',
      onDelete: 'CASCADE',
    });

    await queryInterface.changeColumn('items', 'oldPhysicalLocationId', {
      type: Sequelize.INTEGER,
      references: {
        model: 'physicalLocations',
        key: 'id',
      },
      onUpdate: 'CASCADE',
      onDelete: 'SET NULL',
    });
  },

  async down(queryInterface, Sequelize) {
    await queryInterface.changeColumn('items', 'physicalLocationId', {
      type: Sequelize.INTEGER,
    });

    await queryInterface.changeColumn('items', 'oldPhysicalLocationId', {
      type: Sequelize.INTEGER,
    });
  },
};