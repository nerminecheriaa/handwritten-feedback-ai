from services.ocr import OCRService


def main():

    # Création du service OCR
    ocr_service = OCRService()


    # Image de test
    image_path = "backend/uploads/test.jpg"


    # Extraction texte
    text = ocr_service.extract_text(
        image_path
    )


    print("\n===== TEXTE EXTRAIT =====\n")
    print(text)



if __name__ == "__main__":
    main()