import re
from src.core.job.mapper import Mapper


class LongWordCountMapper(Mapper):
  def map(self, record, emit):
    words = re.findall(r"\b\w+\b", str(record).lower())
    for word in words:
      if len(word) > 5:
        emit(word, 1)