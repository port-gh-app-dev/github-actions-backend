/** @type {import('jest').Config} */
module.exports = {
  testEnvironment: "node",
  testMatch: ["**/__tests__/**/*.js", "**/?(*.)+(spec|test).js"],
  clearMocks: true,
  collectCoverageFrom: ["**/*.js", "!**/node_modules/**", "!**/coverage/**"],
};
