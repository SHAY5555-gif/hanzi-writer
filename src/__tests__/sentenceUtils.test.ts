import { extractChineseCharacters } from '../sentenceUtils';

describe('extractChineseCharacters', () => {
  it('extracts all Chinese characters in order', () => {
    const input = '我喜欢苹果';
    expect(extractChineseCharacters(input)).toEqual(['我', '喜', '欢', '苹', '果']);
  });

  it('ignores punctuation and spaces', () => {
    const input = '我 喜欢 苹果！';
    expect(extractChineseCharacters(input)).toEqual(['我', '喜', '欢', '苹', '果']);
  });

  it('returns an empty array when no Chinese characters are present', () => {
    expect(extractChineseCharacters('Hello world!')).toEqual([]);
  });
}); 