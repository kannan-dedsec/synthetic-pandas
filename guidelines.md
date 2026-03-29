```markdown
# Pandas Project Coding Guidelines

## Code Style
- Adhere to [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code style.
- Use 4 spaces per indentation level; do not use tabs.
- Limit lines to 79 characters.
- Use blank lines to separate functions and classes, and larger blocks of code inside functions.

## Import Organization
- Group imports in the following order:
  1. Standard library imports
  2. Related third-party imports (e.g., `pandas`, `numpy`)
  3. Local application/library specific imports
- Each group should be separated by a blank line.
- Import only what you need; prefer specific imports over wildcard imports.
  
  ```python
  import os
  import sys
  
  import pandas as pd
  import numpy as np
  
  from mymodule import my_function
  ```

## Naming Conventions
- Use `snake_case` for variable and function names.
- Use `CamelCase` for class names.
- Constants should be written in `UPPER_SNAKE_CASE`.
- Use descriptive names that convey the purpose of the variable or function.
  
  ```python
  def calculate_mean(data_frame):
      pass
  
  class DataProcessor:
      pass
  ```

## Documentation
- Use docstrings to describe all public modules, classes, methods, and functions.
- Follow the [NumPy/SciPy documentation style](https://numpydoc.readthedocs.io/en/latest/format.html) for consistency.
  
  ```python
  def calculate_mean(data_frame: pd.DataFrame) -> float:
      """
      Calculate the mean of a specified DataFrame column.

      Parameters
      ----------
      data_frame : pd.DataFrame
          The DataFrame containing the data.

      Returns
      -------
      float
          The mean of the specified column.
      """
      return data_frame.mean()
  ```

## Common Pitfalls (Mutable Defaults)
- Avoid using mutable default arguments (e.g., lists or dictionaries) in function definitions.
- Instead, use `None` as a default and initialize inside the function.

  ```python
  def process_data(data=None):
      if data is None:
          data = []
      # Process data
  ```

## Additional Tips
- Use `pandas` built-in functions for efficiency and readability.
- Regularly run linters (e.g., `flake8`, `pylint`) to ensure code quality.
- Write unit tests for critical functions using `pytest` or `unittest`.
- Keep dependencies updated and document them in a `requirements.txt` file.

By following these guidelines, we can maintain a clean, efficient, and collaborative codebase for our pandas projects.
```