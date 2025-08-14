# PrepEdge - Your Interview Buddy

PrepEdge is an AI-powered interview preparation tool that generates highly relevant, technically focused interview questions tailored to your resume and a specific job description. By leveraging advanced language models and document processing, PrepEdge helps you practice for interviews with questions that match your skills, experience, and the requirements of your target job.

## Features

- **Job-Aware Question Generation:** Enter a job posting URL and upload your resume (PDF). PrepEdge analyzes both to generate 10 custom interview questions.
- **Difficulty Selection:** Choose the difficulty level (Easy, Medium, Hard) to match your preparation needs.
- **Smart Content Extraction:** Uses robust PDF and web scraping to extract relevant information from resumes and job postings.
- **Cleaned & Processed Data:** Automatically cleans and processes extracted text for optimal question generation.
- **Modern UI:** Built with Streamlit for a simple, interactive web experience.

## How It Works

1. **Input:**  
   - Enter the URL of a job posting.
   - Upload your resume as a PDF.
   - Select the desired difficulty level.

2. **Processing:**  
   - The app scrapes and cleans the job description and resume content.
   - Feeds the information into a prompt template for the LLM (Ollama with Llama 3.2).

3. **Output:**  
   - Generates a numbered list of 10 interview questions tailored to your profile and the job.

## Tech Stack

- **Python**
- **Streamlit** (UI)
- **LangChain** (Prompting, LLM orchestration)
- **Ollama** (LLM backend, e.g., Llama 3.2)
- **PyPDF2** (PDF parsing)
- **langchain_community.document_loaders** (Web & PDF loaders)

## Setup & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/PrepEdge.git
   cd PrepEdge
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

4. **Open in your browser:**  
   Go to `http://localhost:8501`

## File Structure

```
PrepEdge/
├── app.py                # Main Streamlit app
├── services/
│   ├── scraper.py        # Functions for scraping and cleaning data
│   └── preprocess.py     # (Optional) Text cleaning utilities
├── assets/               # Sample resumes or other assets
├── notebooks/            # Jupyter notebooks for prototyping
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Example

1. Enter a job posting URL (e.g., from LinkedIn or company careers page).
2. Upload your resume PDF.
3. Select "Medium" difficulty.
4. Click "Submit" to receive 10 tailored interview questions.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

MIT License

---

*PrepEdge helps you practice smarter, not harder. Good luck with your interviews!*