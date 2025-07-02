import { CharacterJson } from './typings/types';
import defaultCharDataLoader from './defaultCharDataLoader';

/**
 * Hybrid loader: attempt to load stroke data from the locally installed
 * `hanzi-writer-data` NPM package for offline performance. If the character
 * is not bundled locally (or the package is not present), fall back to the
 * original remote CDN loader.
 */
const hybridCharDataLoader = (
  char: string,
  onLoad: (data: CharacterJson) => void,
  onError: (error?: any, context?: any) => void,
) => {
  // try japanese dataset first (sharper computer-like strokes)
  import(`hanzi-writer-data-jp/${encodeURIComponent(char)}`)
    .catch(() => import(`hanzi-writer-data/${encodeURIComponent(char)}`))
    .then((mod) => {
      // The module can export the JSON either as default or as the module itself
      const data: CharacterJson = (mod as any).default || (mod as any);
      onLoad(data);
    })
    .catch(() => {
      // fallback to CDN
      defaultCharDataLoader(char, onLoad, onError);
    });
};

export default hybridCharDataLoader; 