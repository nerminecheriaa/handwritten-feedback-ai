from pathlib import Path
import json

from pipeline import StudentExpectationPipeline


class BatchProcessor:

    def __init__(self):
        self.pipeline = StudentExpectationPipeline()

    def process_folder(
        self,
        input_dir: str,
        output_dir: str
    ):

        input_path = Path(input_dir)
        output_path = Path(output_dir)

        output_path.mkdir(
            parents=True,
            exist_ok=True
        )

        image_extensions = {
            ".jpg",
            ".jpeg",
            ".png",
            ".webp"
        }

        images = [
            image
            for image in input_path.iterdir()
            if image.suffix.lower() in image_extensions
        ]

        images.sort()

        print(f"{len(images)} image(s) trouvée(s).")

        results = []

        for index, image_path in enumerate(images, start=1):

            print(
                f"\n[{index}/{len(images)}] "
                f"Traitement de {image_path.name}"
            )

            try:

                result = self.pipeline.process(
                    str(image_path)
                )

                output_data = {
                    "image": image_path.name,
                    "status": "success",
                    "transcription": result["transcription"],
                    "expectations": [
                        {
                            "category": expectation.category,
                            "sentiment": expectation.sentiment,
                            "text": expectation.text
                        }
                        for expectation in result["expectations"]
                    ]
                }

            except Exception as e:

                print(
                    f"Erreur avec {image_path.name}: {e}"
                )

                output_data = {
                    "image": image_path.name,
                    "status": "error",
                    "error": str(e)
                }

            json_filename = (
                image_path.stem + ".json"
            )

            json_path = (
                output_path / json_filename
            )

            with open(
                json_path,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    output_data,
                    file,
                    ensure_ascii=False,
                    indent=2
                )

            results.append(output_data)

        return results