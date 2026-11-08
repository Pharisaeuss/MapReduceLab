import re
from src.core.job.mapper import Mapper


class VowelsConsonantsMapper(Mapper):
  def map(self, record, emit):
    # Підмножина голосних 
    vowels = set("aeiouyAEIOUYаеєиіїоуьюяАЕЄИІЇОУЬЮЯ")
    words = re.findall(r"\b\w+\b", str(record).lower())

    for word in words:
      length = len(word)
      v_count = sum(1 for char in word if char in vowels)
      c_count = sum(1 for char in word if char.isalpha() and char not in vowels)

      emit(length, [v_count, c_count])