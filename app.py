import re
from streamlit import streamlit as st
from langchain.chains import LLMChain
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from PyPDF2 import PdfReader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader
from services.scraper import url_scraper, pdf_scraper
from prompt.questions import PROMPT as QUESTIONS_PROMPT
from prompt.score import PROMPT as SCORE_PROMPT

def generateQuestions(resume_content, job_description, difficulty_level):
    template = QUESTIONS_PROMPT
    promptTemplate = PromptTemplate(
        template=template,
        input_variables=["job_description", "resume_content", "difficulty_level"],
    )

    llm = Ollama(model="llama3.2")
    chain = LLMChain(llm=llm, prompt=promptTemplate)
    res = chain.invoke(
        {
            "job_description": job_description,
            "resume_content": resume_content,
            "difficulty_level": difficulty_level,
        }
    )
    return res.get("text")

def calculateATSScore(resume_content, job_description):
    template = SCORE_PROMPT
    promptTemplate = PromptTemplate(
        template=template,
        input_variables=["job_description", "resume_content"],
    )
    
    llm = Ollama(model="llama3.2")
    chain = LLMChain(llm=llm, prompt=promptTemplate)
    res = chain.invoke(
        {
            "job_description": job_description,
            "resume_content": resume_content,
        }
    )
    return res.get("text")


if __name__ == "__main__":
    st.title("PrepEdge - Your Interview Buddy")

    st.markdown(
        "This is a simple app to help you prepare for interviews by asking questions based on your resume and job description"
    )

    job_posting_url = st.text_input(
        "Enter your job posting URL here", key="job_posting_url"
    )
    resume_file = st.file_uploader(
        "Upload your resume here", type=["pdf"], key="resume_file"
    )

    difficulty_level = st.selectbox(
        "Select difficuly level", ("Easy", "Medium", "Hard"), key="difficulty_level"
    )

    if resume_file is not None and job_posting_url:

        col1, col2, col3 = st.columns(3)
        
        interview_question_result = None
        ats_score_result = None
        status_placeholder = st.empty()

        with col1:
            if st.button("Generate Interview Questions"):
                status_placeholder.write(
                    "Processing your resume and job description...🔄"
                )

                resume_content = pdf_scraper(resume_file)
                job_description = url_scraper(job_posting_url)

                status_placeholder.write("Generating interview questions...👀")
                interview_question_result = generateQuestions(
                    resume_content, job_description, difficulty_level
                )
                status_placeholder.empty()
                
        with col2:
            if st.button("Calculate ATS Score"):
                status_placeholder.write(
                    "Processing your resume and job description...🔄"
                )
                
                resume_content = pdf_scraper(resume_file)
                job_description = url_scraper(job_posting_url)
                
                status_placeholder.write("Calculating ATS score...👀")
                
                ats_score_result = calculateATSScore(resume_content, job_description)
                status_placeholder.empty()
        if interview_question_result:
            st.success("Interview questions generated successfully!✅")
            st.subheader("Generated Interview Questions:")
            st.write(interview_question_result)
        if ats_score_result:
            st.success("ATS score calculated successfully!✅")
            st.subheader("ATS Match Score:")
            st.write(ats_score_result)
        if not interview_question_result and not ats_score_result:
            st.warning(
                "Please generate interview questions or calculate ATS score to see the results."
            )
    else:
        st.warning(
            "Please upload your resume and enter the job posting URL to generate interview questions."
        )
