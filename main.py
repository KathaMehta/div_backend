from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from openai import OpenAI
from dotenv import load_dotenv
import json 
import re
import time
import os
from fastapi.middleware.cors import CORSMiddleware

# Load .env variables
load_dotenv()
assistant_id = "asst_RhWhWWq7aN8OfQ8oP0cwAmcn"

app = FastAPI()
print("fastapi running")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPEN_AI_API"))

@app.post("/analyze-diversity/")
async def analyze(file: UploadFile = File(...)):
    # Read uploaded CSV file
    contents = await file.read()
    print("got it")

    # Upload file to OpenAI for code interpreter use
    uploaded_file = client.files.create(file=contents, purpose='assistants')
    thread = client.beta.threads.create()

    # Create Assistant
    client.beta.threads.messages.create(
    thread_id=thread.id,
    # assistant_id=assistant_id,
    role="user",
    content="Analyze this CSV file and summarize key trends.",
    attachments=[
        {
            "file_id": uploaded_file.id,
            "tools": [{"type": "code_interpreter"}]
        }
    ]
)
    run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant_id
)
    # Step 6: Get the response
    while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run_status.status in ["completed", "failed", "cancelled"]:
            break
        time.sleep(2)
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    final_message = messages.data[0].content[0].text.value if messages.data else "No response."
    
    print(final_message)
    
    if messages.data:
        # Extract content between triple backticks (```json ... ```)
        match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", final_message, re.DOTALL)

        if match:
            json_block = match.group(1)  # this is the content inside ```
            try:
                parsed_json = json.loads(json_block)
                print("✅ Parsed JSON:")
                final_message=json.dumps(parsed_json, indent=2)
            except json.JSONDecodeError as e:
                print("❌ Failed to parse JSON:", e)
        else:
            print("❌ No valid JSON block found between triple backticks.")
    return JSONResponse(content={
        "summary_and_visualization": final_message
    })
