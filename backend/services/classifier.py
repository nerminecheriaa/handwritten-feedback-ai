from google import genai
from google.genai import types

from config import GEMINI_API_KEY, GEMINI_MODEL
from models.expectation import ClassificationResult


class ClassificationService:

    def __init__(self):
        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def classify(self, transcription: str) -> ClassificationResult:

        if not transcription.strip():
            raise ValueError(
                "La transcription est vide."
            )

        prompt = f"""
You are analyzing a student's expectations for an internship
or academic program.

Your task is to extract the expectations explicitly expressed
in the student's text.

Rules:

1. Extract each distinct expectation.
2. Do not invent expectations.
3. Do not add information that is not present in the text.
4. Keep the original meaning.
5. Each expectation must have exactly one category.
6. If an expectation does not fit the predefined categories,
   use "Other".

Available categories:

- Learning
- Networking
- Career
- Technical Skills
- Events & Conferences
- Other

Student transcription:

---
{transcription}
---

Return only the structured result.
"""

        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ClassificationResult,
            ),
        )

        return ClassificationResult.model_validate_json(
            response.text
        )