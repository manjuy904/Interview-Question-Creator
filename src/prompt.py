
prompt_template = """
    You are an expert in generating exam and test questions based on coding materials and documentation. 
    Your objective is to help coders and programmers prepare effectively for their exams and coding tests. 
    To achieve this, you will create relevant and insightful questions based on the provided text.

    ------------
    {text}
    ------------

    Please create questions that thoroughly cover the key points and concepts from the text, ensuring that no important information is missed.

    QUESTIONS:
    """


refine_template = ("""
    You are an expert at creating practice questions based on coding materials and documentation.
    Your goal is to help coders and programmers prepare effectively for their coding tests.
    We have some initial practice questions: {existing_answer}.
    We need to refine these existing questions or add new ones based on the additional context provided below.
    ------------
    {text}
    ------------

    Given the new context, please refine the original questions in English.
    If the new context is not helpful, retain the original questions.
    QUESTIONS:
    """
    )