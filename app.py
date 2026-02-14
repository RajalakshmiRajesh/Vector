from flask import Flask, render_template, request
from groq import Groq
import os
from dotenv import load_dotenv

# 1. Load the API Key from a .env file (Partner's secure method)
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

app = Flask(__name__)

# 2. Initialize Groq Client (Your preferred library)
client = Groq(api_key=api_key)

def generate_roast(code):
    # Using your partner's unique "Conversation" prompt for better personality
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile", # Using the more powerful model from your code
        messages=[
            {
                "role": "system", 
                "content": "You are a witty senior developer who creates funny code roast conversations."
            },
            {
                "role": "user", 
                "content": f"""
                Roast this code as a VERY SHORT funny conversation.
                Rules:
                - Maximum 6 lines total.
                - Speakers: 13yr (overconfident), 29yr (sarcastic), 42yr (senior dev).
                - Keep it simple, witty, and clean.
                
                Code:
                {code}
                """
            }
        ],
        temperature=0.7, # Slightly higher for more creative "roasts"
        max_tokens=150
    )
    return completion.choices[0].message.content

@app.route("/", methods=["GET", "POST"])
def home():
    roast = ""
    user_code = ""
    if request.method == "POST":
        user_code = request.form["code"]
        if user_code.strip(): # Only roast if there is actual text
            roast = generate_roast(user_code)
    return render_template("index.html", roast=roast, code=user_code)

if __name__ == "__main__":
    app.run(debug=True)