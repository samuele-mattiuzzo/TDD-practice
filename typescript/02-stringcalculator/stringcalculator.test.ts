import { StringCalculator } from './stringcalculator';

describe('test StringCalculator implementation', () => {
  it('should return a 0 if the input is an empty string', () => {
    expect(StringCalculator("")).toEqual(0);
  })

  it('should return the number if the input contains 1 number', () => {
    expect(StringCalculator("1")).toEqual(1);
  })

  it('should return the sum of number in comma-separated input', () => {
    expect(StringCalculator("1,2")).toEqual(3);
  })
})
