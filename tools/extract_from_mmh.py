import json, sys
from pathlib import Path

gfile = Path('mmh/graphics.txt')
if not gfile.exists():
    print('graphics.txt not found'); exit(1)

dest = Path('data_hzw'); dest.mkdir(exist_ok=True)
chars = sys.argv[1:]
if not chars:
    print('Usage: python tools/extract_from_mmh.py <char1> <char2> ...'); exit()
count=0
with gfile.open(encoding='utf-8') as f:
    for line in f:
        obj=json.loads(line)
        c = obj['character']
        if c in chars:
            out={'strokes':obj['strokes'],'medians':obj['medians']}
            with (dest / f'{c}.json').open('w',encoding='utf-8') as w:
                json.dump(out,w,ensure_ascii=False)
            count+=1
            if count==len(chars):
                break
print('wrote',count,'chars to',dest) 