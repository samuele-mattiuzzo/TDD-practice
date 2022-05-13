import { FizzBuzz } from './fizzbuzz';

describe('test FizzBuzz implementation', () => {
  it('should return a valid number', () => {
    expect(FizzBuzz(1)).toEqual("1");
  })

  it('should return Fizz for multiples of 3', () => {
    expect(FizzBuzz(3)).toEqual("Fizz");
  })
})
