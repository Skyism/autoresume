# autoresume
automatically updates resume based on job keywords


it is tailored to my resume format which is latex.
uses google gemini and pylatex

instructions:

1. create virtual env
2. pip install -r requirements.txt
3. your resume in resume.tex
4. job description in jobdesc.txt
5. change scraper file in latex to match your resume format, the regex
6. input model and api key in .env
7. python3 main.py 
