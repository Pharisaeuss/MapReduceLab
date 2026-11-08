from src.core.job.reducer import Reducer


class VowelsConsonantsReducer(Reducer):
  def reduce(self, key, values, emit):
    total_words = len(values)
    if total_words == 0:
      return

    total_vowels = sum(v for v, c in values)
    total_consonants = sum(c for v, c in values)

    total_letters = total_vowels + total_consonants
    if total_letters > 0:
      vowels_pct = (total_vowels / total_letters) * 100
      consonants_pct = (total_consonants / total_letters) * 100
    else:
      vowels_pct = 0.0
      consonants_pct = 0.0

    result_description = (
        f"{vowels_pct:.1f}% голосних, {consonants_pct:.1f}% приголосних "
    )
    emit(key, result_description)