PROMPT = """
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
