# CTLBench: Evaluating Large Language Models on Natural Language Presentations of Computation Tree Logic

This repository contains two small Python utilities to **generate** and **clean** a synthetic question–answer dataset for benchmarking large language models (LLMs) on conceptual time‑tree reasoning.

- `generate_and_save_questions(...)` creates a JSON dataset by calling many themed question generators with a specified distribution.
- `clean_dataset.py` (name suggested) removes duplicates, strips placeholder explanations, shuffles the data, and assigns stable IDs.

> **At a glance**
> - Input: Python modules `question_type*.py` that each expose a generation function.
> - Output: JSON with fields `question`, `truth_value`, `QT1`, `QT2`, and—after cleaning—`id`.
> - Scale: Defaults to **2,500** examples (configurable).

---

## Table of Contents
- [Project structure](#project-structure)
- [Requirements](#requirements)
- [Quick start](#quick-start)
- [Configuration](#configuration)
- [Dataset schema](#dataset-schema)
- [How question generation works](#how-question-generation-works)
- [Cleaning pipeline](#cleaning-pipeline)
- [Reproducibility tips](#reproducibility-tips)
- [Troubleshooting](#troubleshooting)
- [Citation](#citation)
- [License](#license)

---

## Project structure

```
repo/
├─ Questions/                       # All question type modules live here
│  ├─ question_type91.py            # must define generate_question_type1() (example)
│  ├─ question_type92.py
│  ├─ ...
│  └─ question_type712.py
├─ generate_dataset.py              # main script (from your snippet)
├─ clean_dataset.py                 # cleaning script (from your snippet)
├─ generated_questions.json         # raw output (example name)
└─ cleaned_questions.json           # cleaned output (example name)
```

> **Windows path note**: the main script appends a path like `D:\uni\fifth semester\logic\CTL\faze2\githubcodes\Questions` to `sys.path`. Adjust this to your local `Questions` folder (or package it properly; see [Configuration](#configuration)).

---

## Requirements

- **Python**: 3.9+ (3.10/3.11 recommended)
- **Standard library only** for generation. The cleaning script uses `json`, `random`, `re`, and `collections.Counter` (all stdlib).
- Optional custom helpers (referenced in your code): `addid.py`, `identical_finder.py`, `deleteexplain.py`. If you don’t use them, you can remove those imports from `clean_dataset.py`.

Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

---

## Quick start

1. **Place your question modules** in `Questions/` and ensure their function names match what `generate_dataset.py` imports.
2. **Run generation**:
   ```bash
   python generate_dataset.py
   ```
   This writes `generated_questions.json` (or your chosen filename).
3. **Run cleaning**:
   ```bash
   python clean_dataset.py
   ```
   This writes `cleaned_questions.json` (or your chosen filename).

---

## Configuration

Inside `generate_dataset.py` (your main snippet):

- **Number of examples**: set
  ```python
  num_questions_to_generate = 2500
  ```
- **Output path**:
  ```python
  output_json_file = 'generated_questions.json'
  ```
- **Module search path**: update the `sys.path.append(r'.../Questions')` line to point to your `Questions` directory.
- **Distribution across types**: edit `functions_dict` to change *how many times* each generator function is called per cycle.

> The script loops over `functions_dict` repeatedly until it reaches `num_questions_to_generate`, so the relative counts act like **weights**.

---

## Dataset schema

Each generated record has the shape:

```json
{
  "question": "<natural language prompt>",
  "truth_value": true,
  "QT1": "<subtype or metadata>",
  "QT2": "<subtype or metadata>"
}
```

After cleaning, an integer `id` field is appended:

```json
{
  "id": 42,
  "question": "...",
  "truth_value": false,
  "QT1": "...",
  "QT2": "..."
}
```

> **Contract for generators**: each question module’s function must return a 4‑tuple:
> 
> ```python
> (question: str, truth_label: bool, QT1: str, QT2: str)
> ```

### Question type naming

Question generator modules follow the pattern **`question_type<FAMILY><VARIANT>.py`**.
- **FAMILY** = the high‑level question family (e.g., `9`).
- **VARIANT** = the specific interpretation/variant within that family (e.g., `2`).

**Example:** `question_type92` means “**type‑9 questions, second interpretation**.”
Other examples from this repo: `question_type710` → family 7, variant 10; `question_type33` → family 3, variant 3.

> Tip: If you want this to be captured in your JSON, add (optional) metadata when emitting examples—e.g., a `source_module` field or split fields `type_family` and `type_variant`.
>
> ```json
> {
>   "id": 123,
>   "question": "...",
>   "truth_value": true,
>   "QT1": "...",
>   "QT2": "...",
>   "source_module": "question_type92",
>   "type_family": 9,
>   "type_variant": 2
> }
> ```

---

## How question generation works

- The main script imports many modules (`question_type91`, `question_type92`, …, `question_type712`, etc.).
- A `functions_dict` maps **callables → repeat counts** (weights). Example excerpt:

```python
functions_dict = {
    q2.generate_question_type1: 7,
    q12.generate_space_mission_question_type: 8,
    q31.generate_question_type7: 6,
    # ...
}
```

- The loop attempts each function `repeat_count` times per pass, catching and counting exceptions so generation can continue even if some modules occasionally fail.
- Generation stops exactly at `num_questions_to_generate` and writes a pretty‑printed JSON file.

**Console output** includes the final sample count and how many errors (exceptions) occurred while calling generators.

---

## Cleaning pipeline

`clean_dataset.py` (from your snippet) performs the following steps:

1. **Load** `input_json_file` (e.g., `generated_questions3.json`).
2. **De‑duplicate** entries by exact text match of the `question` field (keeps first occurrence).
3. **Strip placeholder explanations** from the `question` text via regex:
   ```python
   re.sub(r'"explanation": <your step by step solution>,\s*', '', question)
   ```
   Adjust the pattern if your data uses a different format.
4. **Shuffle** the dataset for randomness.
5. **Assign `id`** as the array index (stable after the shuffle).
6. **Write** to `output_json_file` (e.g., `cleaned_questions3.json`).

> You can safely remove the imports `addid`, `identical_finder`, `deleteexplain` if not used.

---

## Reproducibility tips

- Add a global seed at the top of your main and cleaning scripts:
  ```python
  import random
  random.seed(1337)
  ```
- If your question modules use NumPy or other RNGs, seed them too.
---

## Troubleshooting

- **ModuleNotFoundError** for `question_type…` files
  - Ensure `Questions/` is on `sys.path` *or* install it as a package.
  - Verify the filename and the imported symbol match exactly.
- **Regex didn’t remove explanations**
  - Inspect the raw `question` text and tweak the `deletexp` regex accordingly.
- **Many “error occurred while processing …” messages**
  - Catch and log details inside each generator to diagnose, or temporarily reduce that generator’s weight in `functions_dict`.
- **Duplicates not removed**
  - De‑duplication is a strict string match on `question`. Normalize whitespace or case if needed.

---

## Citation

If you use this dataset or code in academic work, please cite:

```bibtex
@software{time_tree_benchmark_generator,
  title        = {CTLBench: Evaluating Large Language Models on
 Natural Language Presentations of Computation Tree
 Logic},
  author       = {<->},
  year         = {-},
  url          = {-}
}
```

---

## License

MIT License

Copyright (c) 2025 Parham

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
