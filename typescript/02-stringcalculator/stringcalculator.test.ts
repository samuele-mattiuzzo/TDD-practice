import { StringCalculator } from './stringcalculator';

describe('test StringCalculator implementation', () => {
  it('should return a 0 if the input is an empty string', () => {
    expect(StringCalculator("")).toEqual(0);
  })

  it('should return the number if the input contains 1 number', () => {
    expect(StringCalculator("1")).toEqual(1);
  })

  it('should return the sum of 2 numbers in comma-separated input', () => {
    expect(StringCalculator("1,2")).toEqual(3);
  })

  it('should return the sum of all numbers in comma-separated input', () => {
    expect(StringCalculator("1,2,3")).toEqual(6);
  })

  it('should return the sum of all numbers with mixed delimiters in input', () => {
    expect(StringCalculator("1,2\n3")).toEqual(6);
  })
})
