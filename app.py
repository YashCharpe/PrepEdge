import re
from streamlit import streamlit as st
from langchain.chains import LLMChain
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from PyPDF2 import PdfReader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader
from services.scraper import url_scraper, pdf_scraper


def generateQuestions(resume_content, job_description, difficulty_level):
    template="""
        You are an expert technical interviewer with deep experience in assessing candidates for specialized technical roles.

        Using the information below, generate a set of exactly 10 highly relevant, clear, and technically focused interview questions for a candidate applying to this position. You are also provided with a difficulty level of interview, make sure to generate questions based on difficulty level.

        Inputs:
        Job Description:
        {job_description}

        Resume Content:
        {resume_content}

        Difficulty Level:
        {difficulty_level}

        Requirements for the Questions:

        Relevance: Base each question strictly on the skills, tools, technologies, and responsibilities mentioned in both the job description and the resume. Avoid introducing topics not covered in either.

        Coverage: Ensure the questions collectively test the candidate’s:

        Core technical skills mentioned in the job description

        Problem-solving and troubleshooting ability

        Understanding of relevant tools, frameworks, and methodologies

        Ability to work in a team, collaborate, and communicate effectively

        Clarity & Precision: Make each question concise, unambiguous, and answerable in a technical interview setting.

        Variety: Include a balanced mix of:

        Practical scenario-based questions

        Conceptual/theoretical knowledge checks

        Problem-solving and optimization challenges

        Questions to assess experience in past projects mentioned in the resume

        Format: Present the questions as a numbered list from 1 to 10. Do not provide answers.
    """
    promptTemplate = PromptTemplate(
        template=template,
        input_variables=["job_description", "resume_content","difficulty_level"]
    )

    llm = Ollama(model="llama3.2")
    chain = LLMChain(
        llm=llm,
        prompt=promptTemplate
    )
    res = chain.invoke({
        "job_description": job_description,
        "resume_content": resume_content,
        "difficulty_level": difficulty_level
    })
    return res.get("text")


if __name__ == "__main__":
    st.title("PrepEdge - Your Interview Buddy")

    st.markdown("This is a simple app to help you prepare for interviews by asking questions based on your resume and job description")

    job_posting_url = st.text_input("Enter your job posting URL here", key="job_posting_url")
    resume_file = st.file_uploader("Upload your resume here", type=["pdf"], key="resume_file")

    difficulty_level = st.selectbox("Select difficuly level",("Easy", "Medium", "Hard"), key="difficulty_level")

    if resume_file is not None and job_posting_url:
        
        if st.button("Submit"):
            status_placeholder = st.empty()
            status_placeholder.write("Processing your resume and job description...🔄")

            resume_content = pdf_scraper(resume_file)
            job_description = url_scraper(job_posting_url)

            status_placeholder.write("Generating interview questions...👀")
            result = generateQuestions(resume_content, job_description, difficulty_level)
            status_placeholder.empty()
            st.success("Interview questions generated successfully!✅")
            st.subheader("Generated Interview Questions:")
            st.write(result)
    else:
        st.warning("Please upload your resume and enter the job posting URL to generate interview questions.")

