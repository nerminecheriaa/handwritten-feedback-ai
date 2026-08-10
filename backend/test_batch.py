from pathlib import Path

from services.batch_processor import BatchProcessor


def main():

    base_dir = Path(__file__).resolve().parent

    input_dir = base_dir / "uploads"
    output_dir = base_dir / "outputs"

    processor = BatchProcessor()

    results = processor.process_folder(
        str(input_dir),
        str(output_dir)
    )

    print("\n==============================")
    print("BATCH TERMINÉ")
    print("==============================")

    success = sum(
        1
        for result in results
        if result["status"] == "success"
    )

    errors = sum(
        1
        for result in results
        if result["status"] == "error"
    )

    print(f"Images traitées : {len(results)}")
    print(f"Succès          : {success}")
    print(f"Erreurs         : {errors}")


if __name__ == "__main__":
    main()