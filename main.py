

from dotenv import load_dotenv
load_dotenv()

from utils.textTopdf import text_to_pdf
from graph.workflow import app

query = "Why Is the Government of india Focusing on Aravalli Hills?"


result = app.invoke({
    "question": query
})

print(result["final_answer"])
text_to_pdf(result["final_answer"],"Research Article.pdf")


