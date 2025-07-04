import { HanziWriterOptions } from './typings/types';
import hybridCharDataLoader from './charDataHybridLoader';

const defaultOptions: HanziWriterOptions = {
  charDataLoader: hybridCharDataLoader,
  onLoadCharDataError: null,
  onLoadCharDataSuccess: null,
  showOutline: true,
  showCharacter: true,
  renderer: 'svg',

  // positioning options

  width: 0,
  height: 0,
  padding: 20,

  // animation options

  strokeAnimationSpeed: 0.5,
  strokeFadeDuration: 600,
  strokeHighlightDuration: 300,
  strokeHighlightSpeed: 1,
  delayBetweenStrokes: 1200,
  delayBetweenLoops: 2500,

  // colors

  strokeColor: '#555',
  radicalColor: null,
  highlightColor: '#AAF',
  outlineColor: '#DDD',
  drawingColor: '#333',

  // quiz options

  leniency: 1,
  showHintAfterMisses: 3,
  highlightOnComplete: true,
  highlightCompleteColor: null,
  markStrokeCorrectAfterMisses: false,
  acceptBackwardsStrokes: false,
  quizStartStrokeNum: 0,
  averageDistanceThreshold: 350,

  // undocumented obscure options

  drawingFadeDuration: 300,
  drawingWidth: 4,
  strokeWidth: 2,
  outlineWidth: 2,
  rendererOverride: {},
};

export default defaultOptions;
