
export function StringCalculator(input: string): number {
  if (input === "") return 0;

  if (input.length === 1) return +input;

  var values = input.split(',');
  var sum = 0;
  for (var i = 0; i < values.length; i++) {
    sum += +values[i];
  }
  return sum;
}
