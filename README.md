# ppt_writer

AI-powered PPT generator that collects information from websites and documents, then generates structured PowerPoint presentations.

## Features

- 🌐 Web content scraping and research
- 📄 Document input support (PDF, Word, Markdown)
- 🎨 Multiple template themes
- 📊 Structured slide generation
- 💾 Export to PPTX/PDF

## Quick Start

### Prerequisites

- Python 3.10+
- Docker (optional)

### Installation

```bash
git clone https://github.com/harryxh/ppt_writer.git
cd ppt_writer
pip install -r requirements.txt
```

### Usage

```bash
python main.py --topic "Your presentation topic" --slides 10
```

## Project Structure

```
ppt_writer/
├── src/
│   ├── scraper/       # Web scraping modules
│   ├── generator/     # PPT generation logic
│   ├── templates/     # Presentation templates
│   └── utils/         # Utility functions
├── tests/
├── requirements.txt
└── README.md
```

## License

MIT
