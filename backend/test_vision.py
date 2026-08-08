from pathlib import Path

from services.vision import VisionService


def main():

    base_dir = Path(__file__).resolve().parent

    image_path = base_dir / "uploads" / "test.jpg"

    vision_service = VisionService()

    text = vision_service.transcribe(
        str(image_path)
    )

    print("\n==============================")
    print("TRANSCRIPTION GEMINI")
    print("==============================\n")

    print(text)


if __name__ == "__main__":
    main()