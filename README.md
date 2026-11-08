MapReduce Python Simulator

Quickstart
- Create venv and install requirements if needed.
- Run a sample job after scaffolding is complete:
  - python -m src.cli.main run --workers 4 --input data/input --output data/output/wordcount --job student_jobs.word_count.mapper:WordCountMapper,student_jobs.word_count.reducer:WordCountReducer --reducers 4

#### Завдання 1: Підрахунок слів з очищенням від розділових знаків

```bash
python -m src.cli.main run --workers 4 --input data/input --output data/output/task1_clean_words --job src.student_jobs.clean_count.mapper:CleanWordCountMapper,src.student_jobs.clean_count.reducer:CleanWordCountReducer --reducers 4

```

#### Завдання 2: Підрахунок слів, довжина яких більша за 5 символів

```bash
python -m src.cli.main run --workers 4 --input data/input --output data/output/task2_long_words --job src.student_jobs.long_count.mapper:LongWordCountMapper,src.student_jobs.long_count.reducer:LongWordCountReducer --reducers 4

```

#### Завдання 3: Підрахунок голосних і приголосних (співвідношення)

```bash
python -m src.cli.main run --workers 4 --input data/input --output data/output/task3_vowels_consonants --job src.student_jobs.sounds_count.mapper:VowelsConsonantsMapper,src.student_jobs.sounds_count.reducer:VowelsConsonantsReducer --reducers 4

```