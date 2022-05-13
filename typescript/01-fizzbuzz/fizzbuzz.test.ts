import { FizzBuzz } from './fizzbuzz';

describe('test FizzBuzz implementation', () => {
  it('should return a valid number', () => {
    expect(FizzBuzz(1)).toEqual("1");
  })

  it('should return Fizz for multiples of 3', () => {
    expect(FizzBuzz(3)).toEqual("Fizz");
  })

  it('should return Buzz for multiples of 5', () => {
    expect(FizzBuzz(5)).toEqual("Buzz");
  })

  it('should return FizzBuzz for multiples of 3 and 5', () => {
    expect(FizzBuzz(15)).toEqual("FizzBuzz");
  })
})
