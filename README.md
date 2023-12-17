# Markdown Terminal Renderer (mdtr)

Markdown Terminal Renderer (`mdtr`) is a Python script designed to render Markdown content within the terminal. It leverages the `rich` library to provide enhanced formatting and color options for displaying Markdown files directly in your command-line interface.

## Features

- **Markdown Rendering**: Display Markdown files in a formatted and readable manner directly in the terminal.
- **Color Control**: Toggle color output for customized viewing experiences.
- **Easy-to-Use**: Simple command-line interface for rendering Markdown content.

## Installation

### Prerequisites

- Python 3.x installed
- [rich](https://github.com/Textualize/rich) - a python library for rich text and formatting in the terminal

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/AndruJorj/mdtr.git
   ```

2. Navigate to the cloned directory:

   ```bash
   cd mdtr
   ```

3. Install dependencies:

Python package installer

   ```bash
   pip install rich
   ```

Ubuntu (22.04.3)

   ```bash
   apt install python3-rich
   ```

## Usage

### Rendering Markdown

To render a Markdown file in the terminal:

   ```bash
   python mdtr.py path/to/your/file.md
   ```

Replace `path/to/your/file.md` with the path to your Markdown file.

### Options

-  `--no-color`: Disable colored output in the terminal.
  
 ```bash
 python mdtr.py --no-color path/to/your/file.md
 ```
## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve `mdtr`.

## License

This project is licensed under the [MIT License](LICENSE).

