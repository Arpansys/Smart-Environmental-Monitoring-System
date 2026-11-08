import os
import time

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("Gemini API key not found in .env file")

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.1-flash-lite"


def ask_gemini(diagnostic_report):

    prompt = f"""
    You are an AI assistant supporting a four-agent
    embedded engineering team.

    Analyse the diagnostic report.

    Identify:
    1. The likely problem.
    2. Possible causes.
    3. Recommended corrective actions.
    4. How to verify the fix.

    Do not claim a physical repair succeeded
    without hardware verification.

    Diagnostic report:
    {diagnostic_report}

    Keep your answer concise and practical.
    """

    # Retry temporary server or quota errors
    for attempt in range(3):

        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )

            return response.text or "Gemini returned an empty response."

        except Exception as error:

            error_message = str(error)

            temporary_error = any(
                code in error_message.upper()
                for code in [
                    "503",
                    "UNAVAILABLE",
                    "429",
                    "RESOURCE_EXHAUSTED"
                ]
            )

            if temporary_error and attempt < 2:

                wait_time = 2 ** (attempt + 1)

                print(
                    f"Gemini is temporarily unavailable. "
                    f"Retrying in {wait_time} seconds..."
                )

                time.sleep(wait_time)

            else:
                return f"Gemini AI error: {error_message}"

    return "Gemini AI unavailable after three attempts."


if __name__ == "__main__":

    test_report = """
    Gas sensor reading: 2000
    Valid gas range: 0 to 1023
    Test result: FAIL
    """

    print("Gemini AI Assistant:")
    print(ask_gemini(test_report))