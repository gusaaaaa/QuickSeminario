# QuickSeminario

A repository meant to store slide notes for further reference.

# Licensing

- The slide notes in this repository are licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0) DEED](https://creativecommons.org/licenses/by/4.0/).
- The `show.py` script is open-source and can be used without any restrictions.

## Folder Structure

```plaintext
root/
 - slides/
   - modelos_de_proceso_y_jira_elves.txt
   - ...
  - show.py
```

## Using the Script

`show.py` is a script that reads slide notes from a text file and displays them as a slide show. 

### Instructions:

1. It is recommended to use a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    ```

2. Install the required dependencies:
    ```bash
    pip install pygame
    ```

3. To use the script, feed your notes to the script through stdin:
    ```bash
    python show.py < slides/seminario.txt
    ```
   OR
    ```bash
    cat slides/seminario.txt | python show.py
    ```

## Note

The script expects slide notes in a specific format:

- Top-level slides should start without leading spaces.
- Lines with leading spaces are considered continuations of the previous slide.
