'use strict';

module.exports = (sequelize, DataTypes) => {
  const PendingRequest = sequelize.define('PendingRequest', {
    sid: DataTypes.STRING,
    begin: DataTypes.DATE,
    end: DataTypes.DATE,
    reason: DataTypes.TEXT
  }, {});
  PendingRequest.associate = function(models) {
    // associations can be defined here
  };
  return PendingRequest;
};