# Local AI Resume & Career Assistant

A complete AI-powered resume analysis and career guidance tool that runs **100% locally** using Ollama and open-source LLMs.

## Features

### 1. Resume Improvement
- Analyzes your resume for missing sections
- Identifies weak or generic content
- Suggests missing important skills
- Provides ATS (Applicant Tracking System) optimization tips

### 2. AI Job Prediction
- Extracts skills from your resume
- Matches skills against 30+ predefined job roles
- Provides top 3-5 suitable job recommendations
- Shows match percentages with justifications

### 3. Application-Based Resume Converter
- Tailors your resume for specific job applications
- Emphasizes relevant skills and keywords
- Maintains factual accuracy (no hallucinations)
- Generates ATS-friendly format

### 4. Career Roadmap Generator
- Creates structured learning paths (Beginner → Intermediate → Advanced)
- Lists required skills, tools, and technologies
- Suggests practical projects and certifications
- Provides realistic timelines

## Prerequisites

### 1. Python
- Python 3.8 or higher
- pip package manager

### 2. Ollama
You must have Ollama installed and running locally.

**Installation:**

- **macOS/Linux:**
  ```bash
  curl -fsSL https://ollama.ai/install.sh | sh
  ```

- **Windows:**
  Download from [https://ollama.ai/download](https://ollama.ai/download)

**Pull a model:**
```bash
ollama pull llama3.1
```

**Start Ollama server:**
```bash
ollama serve
```

## Installation

### 1. Clone or Download the Project
```bash
cd resume_ai
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv

# Activate on Linux/macOS
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### 1. Start Ollama Server
In a separate terminal:
```bash
ollama serve
```

### 2. Run the Application
```bash
python app.py
```

### 3. Open in Browser
The application will automatically open at:
```
http://localhost:7860
```

## Project Structure

```
resume_ai/
├── app.py                # Main Gradio UI application
├── llm.py                # Ollama HTTP API client
├── resume_parser.py      # PDF/DOCX parsing logic
├── skill_extractor.py    # Skill extraction and matching
├── job_roles.py          # Job role definitions (30+ roles)
├── prompts.py            # LLM prompt templates
├── utils.py              # Helper functions
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## How It Works

### Resume Parsing
- **PDF files:** Extracted using `pdfplumber`
- **DOCX files:** Extracted using `python-docx`
- Text validation ensures meaningful content

### LLM Integration
- Uses Ollama HTTP API (default: `http://localhost:11434`)
- Default model: `llama3.1` (easily configurable)
- All processing happens locally on your machine

### Skill Matching
- LLM extracts skills from resume text
- Skills are matched against 30+ predefined job roles
- Similarity scoring ranks suitable positions
- LLM refines rankings with justifications

### Prompt Engineering
- Explicit, structured prompts prevent hallucinations
- Instructions emphasize factual accuracy
- Output formats ensure consistent results

## Configuration

### Change LLM Model
Edit `app.py` line with `initialize_llm()`:
```python
initialize_llm(model="llama3.1")  # Change to any Ollama model
```

### Add More Job Roles
Edit `job_roles.py` and add entries to the `JOB_ROLES` dictionary:
```python
"Your Job Role": [
    "skill1", "skill2", "skill3", ...
]
```

### Adjust Token Limits
Edit `utils.py` to change text truncation limits:
```python
def truncate_text(text: str, max_length: int = 10000):
    # Adjust max_length as needed
```

## Troubleshooting

### "Cannot connect to Ollama"
- Ensure Ollama is running: `ollama serve`
- Check if Ollama is accessible: `curl http://localhost:11434/api/tags`
- Verify firewall settings

### "No text extracted from PDF"
- Check if PDF is password-protected
- Try converting to a different format
- Ensure PDF contains selectable text (not scanned images)

### "Request timeout"
- Use a smaller/faster model (e.g., `llama3.1:8b`)
- Reduce max_tokens in LLM calls
- Upgrade hardware or wait longer

### "Module not found"
- Activate virtual environment
- Reinstall dependencies: `pip install -r requirements.txt`

## Performance Tips

1. **Use smaller models for faster responses:**
   ```bash
   ollama pull llama3.1:8b
   ```

2. **Reduce token limits** in `app.py` for each LLM call

3. **Keep resumes concise** (1-2 pages recommended)

4. **Run on machines with at least 8GB RAM**

## Privacy & Security

- **100% Local:** No data leaves your machine
- **No Cloud APIs:** No API keys or subscriptions needed
- **No Database:** No persistent storage of your data
- **Open Source:** Full transparency in code

## Limitations

- Requires Ollama installation and setup
- Performance depends on local hardware
- LLM responses may vary between runs
- Limited to models available in Ollama

## Future Enhancements

Potential improvements:
- Support for more file formats (TXT, RTF)
- Resume export to PDF/DOCX
- Job description comparison
- Interview question generator
- Skill gap analysis
- Multi-language support

## License

This project is open source. Feel free to modify and extend it.

## Support

For issues or questions:
1. Check troubleshooting section above
2. Verify Ollama installation: `ollama --version`
3. Test with sample resume first
4. Check Ollama logs for errors

## Acknowledgments

- **Gradio:** For the excellent UI framework
- **Ollama:** For making local LLMs accessible
- **Open-source community:** For maintaining the dependencies

---

**Built with Python, Gradio, and Ollama**

Enjoy your local AI-powered career assistant!
