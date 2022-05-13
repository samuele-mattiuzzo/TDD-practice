
export function StringCalculator(input: string): number {
  if (input === "") return 0;

  var values = input.split(','),
      sum = 0;

  for (var i = 0; i < values.length; i++) {
    sum += +values[i];
  }
  
  return sum;
}
