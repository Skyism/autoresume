from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel
import os
import json




class Agent:
    def __init__(self):
        load_dotenv()
        self.model_name = os.getenv("GEMINI_MODEL")
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=self.api_key)

        prompt = open("prompt.txt", "r").read()

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
        )
        print(response.text)

    class Response(BaseModel):
        latex_code: str
        analysis_summary: str
        match_score: float
        company_name: str

    def format_prompt(self) -> str:
        resume_latex_code = open("resume.tex", "r").read()
        job_description = open("jobdesc.txt", "r").read()
        return f"""
        Please optimize the following resume for the following job posting url:
        Resume: {resume_latex_code}
        Job Description: {job_description}

        Please provide the answer in json format.
        """

    def generate_response(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": self.Response,
            },
        )
        return response.text
    
    def save_response(self, response):
        res = json.loads(response);
        company_name = res["company_name"]
        os.makedirs(f"results/{company_name}", exist_ok=True)
        with open(f"results/{company_name}/latex_code.tex", "w") as f:
            f.write(res["latex_code"])
        with open(f"results/{company_name}/analysis_summary.txt", "w") as f:
            f.write(res["analysis_summary"])
            f.write(f"\n\n\nMatch Score: {res['match_score']}")

    