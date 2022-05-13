
export function StringCalculator(input: string): number {
  if (input.endsWith(',') || input.endsWith('\n')) {
    throw new Error("Error: the input can't end with a delimiter");
  }

  if (input === "") return 0;

  // we need filter to remove empty values
  var splitted = input.split(/\n/),
      sum = 0,
      delimiter = '',
      values = [];

  delimiter = splitted[0].replace('//', '');
  values = splitted[1].split(delimiter).filter(c => c);

  for (var i = 0; i < values.length; i++) {
    sum += +values[i];
  }

  return sum;
}
