
export function StringCalculator(input: string): number {
  if (input.endsWith(',') || input.endsWith('\n')) {
    throw new Error("Error: the input can't end with a delimiter");
  }

  if (input === "") return 0;

  // we need filter to remove empty values
  var values = input.split(/,|\n/).filter(c => c),
      sum = 0;

  for (var i = 0; i < values.length; i++) {
    sum += +values[i];
  }

  return sum;
}
