
export function StringCalculator(input: string): number {
  if (input === "") return 0;

  if (input.length === 1) return +input;

  var values = input.split(',');
  return +values[0] + +values[1];
}
