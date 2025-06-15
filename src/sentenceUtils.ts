export function extractChineseCharacters(sentence: string): string[] {
  // Match Chinese characters in the basic multilingual plane (4E00–9FFF)
  // This covers most common simplified and traditional Han characters.
  // Returns an array of each character in order of appearance, excluding any non-Chinese symbols.
  const matches = sentence.match(/[\u4E00-\u9FFF]/g);
  return matches ? matches : [];
} 