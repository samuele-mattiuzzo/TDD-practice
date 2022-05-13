/** @type {import('ts-jest/dist/types').InitialOptionsTsJest} */
import type { Config } from '@jest/types';

module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
};

const config: Config.InitialOptions = {
  verbose: true,
  transform: {
  '^.+\\.tsx?$': 'ts-test'
  },
};
export default config;
