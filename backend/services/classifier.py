from google import genai
from google.genai import types

from config import GEMINI_API_KEY, GEMINI_MODEL
from models.expectation import ClassificationResult


class ClassificationService:

    def __init__(self):
        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def classify(
        self,
        transcription: str
    ) -> ClassificationResult:

        if not transcription.strip():
            raise ValueError(
                "La transcription est vide."
            )

        prompt = f"""
You are analyzing a student's expectations for an
internship or academic program.

Your task is to extract the expectations explicitly
expressed in the student's text.

For each expectation, determine:

1. Its category.
2. Whether it is positive or negative.
3. The expectation itself.

Categories:

- Learning
- Networking
- Career
- Technical Skills
- Events & Conferences
- Other

Sentiment rules:

- positive: the student wants, expects, would like,
  hopes to gain, discover, learn, meet, participate,
  improve, etc.

- negative: the student explicitly expresses something
  they do not want, dislike, reject, or want to avoid.

Important rules:

1. Extract only expectations explicitly expressed.
2. Do not invent expectations.
3. Preserve the original meaning.
4. Split distinct expectations when necessary.
5. Assign exactly one category to each expectation.
6. Assign either positive or negative.
7. Do not consider the student's writing style as sentiment.
8. If the expectation does not fit another category,
   use Other.

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