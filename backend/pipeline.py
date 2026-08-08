from services.vision import VisionService
from services.classifier import ClassificationService


class StudentExpectationPipeline:

    def __init__(self):
        self.vision_service = VisionService()
        self.classifier_service = ClassificationService()

    def process(self, image_path: str):

        # Étape 1 : transcription
        transcription = self.vision_service.transcribe(
            image_path
        )

        # Étape 2 : classification
        classification = self.classifier_service.classify(
            transcription
        )

        return {
            "transcription": transcription,
            "expectations": classification.expectations
        }