
export function StringCalculator(input: string): number {
  if (input === "") return 0;

  // we need filter to remove empty values
  var values = input.split(/,|\n/).filter(c => c),
      sum = 0;

  for (var i = 0; i < values.length; i++) {
    sum += +values[i];
  }

  return sum;
}
