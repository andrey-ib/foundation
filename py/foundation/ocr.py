""" OCR types wrappers. """

from dataclasses import dataclass
from typing import Optional, Tuple

from .geometry import BBox


@dataclass(frozen=True)
class CharConfidence:
  percentage: float
  unsure: Optional[bool]


@dataclass(frozen=True)
class WordConfidence:
  word_confidence: Optional[float]
  low_confidence: Optional[bool]
  char_confidences: Optional[Tuple[CharConfidence, ...]]


@dataclass(frozen=True)
class InputWord:
  bounding_box: BBox
  text: Optional[str]
  confidence: Optional[WordConfidence]

  char_width: Optional[float]
  rotation_angle: Optional[float]
