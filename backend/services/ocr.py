from pathlib import Path
from paddleocr import PaddleOCR


class OCRService:

    def __init__(self):
        self.ocr = PaddleOCR(
            use_angle_cls=True,
            lang="fr"
        )

    def extract_text(self, image_path: str) -> str:

        image = Path(image_path)

        if not image.exists():
            raise FileNotFoundError(f"Image introuvable : {image_path}")

        # API PaddleOCR 2.x
        result = self.ocr.ocr(str(image), cls=True)

        extracted_text = []

        for line in result:
            for word in line:
                extracted_text.append(word[1][0])

        return "\n".join(extracted_text)