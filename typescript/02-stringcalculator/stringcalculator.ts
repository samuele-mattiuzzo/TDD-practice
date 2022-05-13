
export function StringCalculator(input: string): number {
  if (input === "") return 0;

  // we need filter to remove empty values
  var splitted = input.split(/\n/),
      sum = 0;

  var delimiter = splitted[0].replace('//', ''),
      values = splitted[1].split(delimiter).filter(c => c);

    if (input.endsWith(delimiter)) {
      throw new Error("Error: the input can't end with a delimiter");
    }

  values.forEach(x => { sum += +x; });

  return sum;
}
