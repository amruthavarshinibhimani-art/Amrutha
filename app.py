
from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv
import os
import time

from database import create_database, save_event

load_dotenv()

app = Flask(__name__)
create_database()

# Gemini API configuration
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate_plan():

    event_name = request.form.get("event_name")
    event_type = request.form.get("event_type")
    event_date = request.form.get("event_date")
    guests = request.form.get("guests")
    budget = request.form.get("budget")
    venue = request.form.get("venue")
    preferences = request.form.get("preferences")
    save_event(
    event_name,
    event_type,
    event_date,
    guests,
    budget,
    venue,
    preferences
)

    prompt = f"""
You are an AI Event Planner.

Create a practical and personalized event plan using the following details:

Event Name: {event_name}
Event Type: {event_type}
Event Date: {event_date}
Number of Guests: {guests}
Budget: ₹{budget}
Venue: {venue}
User Preferences: {preferences}

Generate the following:

1. Event Overview
2. Event Schedule
3. Decoration Ideas
4. Food and Menu Suggestions
5. Activities and Entertainment
6. Budget Allocation
7. Important Event Checklist

Make the plan clear, practical and suitable for the given budget
and number of guests.
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        plan = response.text

    except Exception as e:

        plan = f"Error generating AI plan: {str(e)}"

    return render_template(
        "result.html",
        plan=plan,
        event_name=event_name
    )


if __name__ == "__main__":
    app.run(debug=True)