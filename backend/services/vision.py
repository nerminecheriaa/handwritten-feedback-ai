from pathlib import Path

from google import genai

from config import GEMINI_API_KEY, GEMINI_MODEL


class VisionService:
    """
    Service responsable de l'analyse d'une image
    manuscrite avec Gemini Vision.
    """

    def __init__(self):
        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def transcribe(self, image_path: str) -> str:
        """
        Transcrit fidèlement le texte manuscrit
        présent dans une image.

        Args:
            image_path: chemin vers l'image.

        Returns:
            Texte transcrit par Gemini.
        """

        image = Path(image_path)

        if not image.exists():
            raise FileNotFoundError(
                f"Image introuvable : {image}"
            )

        with open(image, "rb") as f:
            image_bytes = f.read()

        prompt = """
You are a handwriting transcription system.

Transcribe the handwritten text in the image as accurately
and faithfully as possible.

Rules:
- Do not summarize.
- Do not interpret.
- Do not invent missing words.
- Preserve the original wording.
- Preserve the approximate line structure.
- If a word is genuinely unreadable, write [unclear].
- Do not add explanations.
- Return only the transcription.
"""

        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=[
                {
                    "parts": [
                        {
                            "text": prompt
                        },
                        {
                            "inline_data": {
                                "mime_type": "image/jpeg",
                                "data": image_bytes,
                            }
                        },
                    ]
                }
            ],
        )

        return response.text.strip()