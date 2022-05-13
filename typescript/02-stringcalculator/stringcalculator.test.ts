import { StringCalculator } from './stringcalculator';

describe('test StringCalculator implementation', () => {
  it('should return a 0 if the input is an empty string', () => {
    expect(StringCalculator("")).toEqual(0);
  })

  it('should return the number if the input contains 1 number', () => {
    expect(StringCalculator("//,\n1")).toEqual(1);
  })

  it('should return the sum of 2 numbers in comma-separated input', () => {
    expect(StringCalculator("//,\n1,2")).toEqual(3);
  })

  it('should return the sum of all numbers in comma-separated input', () => {
    expect(StringCalculator("//,\n1,2,3")).toEqual(6);
  })

  it('should return an error if the input ends with a delimiter', () => {
    expect(() => StringCalculator("//;\n1;2;3;")).toThrow("Error: the input can't end with a delimiter");
  })

  it('should return the sum of all numbers with an arbitrary delimiter in input', () => {
    expect(StringCalculator("//;\n1;3")).toEqual(4);;
  })
})
