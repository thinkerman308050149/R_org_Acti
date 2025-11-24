# R_org_Acti - Activity Organizer

## Overview

R_org_Acti is a Python-based activity organizer project designed to handle time logic and activity orchestration. The core of the project is the `tiempo` class, which allows for robust manipulation of dates and times, including leap year calculations, day-of-week determination, and time travel (advancing or reversing time).

## Project Structure

*   `tiempo.py`: Contains the `tiempo` class, which encapsulates all date and time manipulation logic.
*   `orquestador.py`: Contains the `Orquestador` class, intended to manage and orchestrate activities (currently a skeleton).
*   `tests/`: Directory containing unit tests for the project.

## Installation

This project requires Python 3. To set it up:

1.  Clone the repository.
2.  Navigate to the project root.
3.  Ensure you have `pytest` installed for running tests:
    ```bash
    pip install pytest
    ```

## Usage

### Using the `tiempo` class

The `tiempo` class is the main component for handling time. You can initialize it with a specific date and time, and then manipulate it.

```python
from tiempo import tiempo

# Initialize with default values (Saturday, Jan 1, 2000, 00:00)
t = tiempo()
print(t)
# Output: Fecha:Sábado 01 de Enero del 2000 - Hora: 00:00

# Initialize with specific values
# Example: Monday, May 15, 2024, 12:30
t_custom = tiempo(minuto=30, hora=12, dia=1, fecha=15, mes=5, year=2024)
print(t_custom)
# Output: Fecha:Lunes 15 de Mayo del 2024 - Hora: 12:30

# Check for leap year
print(f"Is leap year? {t_custom.yearbisiesto()}")

# Advance time
t_custom.avancetime_hora() # Advance by 1 hour
print(t_custom)

# Using properties to advance time by multiple units
t_custom.avance_tempfecha = 5 # Advance by 5 days
print(t_custom)

# Move back in time
t_custom.back_timeyear = 1 # Go back 1 year
print(t_custom)
```

### Running Tests

To run the unit tests and ensure everything is working correctly:

```bash
python -m pytest
```

## Contributing

Contributions are welcome! Please ensure that you:
1.  Write tests for any new features or bug fixes.
2.  Add docstrings to all new functions and classes following the Google Style Python Docstrings convention.
