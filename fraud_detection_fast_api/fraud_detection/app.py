from fastapi import FastAPI, HTTPException, Body
import pandas as pd
import io
import anthropic
import os
from pydantic import BaseModel
from dotenv import load_dotenv

#Load Environement Variabled from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Fraud Detection API",
    description="An API to analyze transaction data and identify potential fraudulent transactions.",
    version="1.0.0",
    servers=[
        {
            "url": "https://handbags-formal-stockings-butterfly.trycloudflare.com",
            "description": "Development Server"
        }
    ]
)

# Set up Anthropic API client
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise Exception("Anthropic Api Key is not set")

client = anthropic.Client(api_key=api_key)

@app.get("/test", operation_id="test" , summary="Test API Connectivity", description="A simple endpoint to test if the API is running correctly. Returns 'Hello, World!'.")
async def test_api():
    return {"message": "Hello, World!"}

class TransactionDataRequest(BaseModel):
    data:str

@app.post("/analyze-transactions-text", operation_id="analyze-transactions-text" ,summary="Analyze Transactions from Text", description="Submit transaction data in CSV text format. The API will analyze the transactions and identify any that may be fraudulent.")
async def analyze_transactions_from_text(request: TransactionDataRequest):
    try:
        # Convert the input text to a pandas DataFrame
        df = pd.read_csv(io.StringIO(request.data))
        
        # Convert DataFrame to string
        transaction_text = df.to_string(index=False)

        # Prepare the prompt for the Anthropic API
        prompt = f"\n\nHuman: Analyze the following transactions and identify any that may be fraudulent:\n{transaction_text}\n\nAssistant:"

        # Call the Anthropic API
        response = client.completions.create(
            model="claude-v1",
            prompt=prompt,
            max_tokens_to_sample=500
        )
        predictions = response.completion
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=400, detail="The provided data is empty or invalid.")
    except anthropic.AuthenticationError as e:
        raise HTTPException(status_code=401, detail="Anthropic API key is invalid or expired.")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error occurred while processing the request.")

    # Return the predictions
    return {"predictions": predictions}
