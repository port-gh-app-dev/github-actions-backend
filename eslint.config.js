/** @type {import('eslint').Linter.Config[]} */
module.exports = [
  {
    ignores: ["node_modules/**", ".github/workflows/**"],
  },
  {
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
    },
    rules: {
      "no-eval": "error",
      "no-implied-eval": "error",
      "no-new-func": "error",
    },
  },
];
