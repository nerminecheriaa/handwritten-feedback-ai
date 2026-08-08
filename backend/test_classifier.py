from services.classifier import ClassificationService


def main():

    transcription = """
I Expect from this program to enlarge
my network, discover new things,
acquire more knowledge specially about
concepts like blockchain and quantum in
relation to AI. I'd like to hear
people speak (more conferences).
"""

    classifier = ClassificationService()

    result = classifier.classify(
        transcription
    )

    print("\n==============================")
    print("CLASSIFICATION")
    print("==============================\n")

    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()