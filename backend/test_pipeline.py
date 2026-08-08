from pathlib import Path
import json

from pipeline import StudentExpectationPipeline


def main():

    base_dir = Path(__file__).resolve().parent

    image_path = base_dir / "uploads" / "test.jpg"
    output_path = base_dir / "outputs" / "test_result.json"

    pipeline = StudentExpectationPipeline()

    result = pipeline.process(
        str(image_path)
    )

    # Conversion des objets Pydantic en dictionnaire
    output_data = {
        "transcription": result["transcription"],
        "expectations": [
            {
                "category": expectation.category,
                "text": expectation.text
            }
            for expectation in result["expectations"]
        ]
    }

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            output_data,
            file,
            ensure_ascii=False,
            indent=2
        )

    print("\nRésultat sauvegardé dans :")
    print(output_path)


if __name__ == "__main__":
    main()