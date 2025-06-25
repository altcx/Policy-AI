declare module 'diff' {
  export function diffLines(oldStr: string, newStr: string): any;
  export function createTwoFilesPatch(fileName: string, oldFileName: string, oldStr: string, newStr: string): any;
}
