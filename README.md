#  Student Expectations AI

An AI-powered system for automatically analyzing handwritten student expectations.

The project uses a **Vision-Language Model (VLM)** to understand handwritten documents, transcribe their content, extract student expectations, and classify them by category and sentiment.

The system provides both:
- an **interactive interface** for analyzing a single document;
- a **batch processing pipeline** for analyzing multiple documents.

---

##  Features

### Handwritten Text Transcription

Uses **Gemini Vision** to process handwritten documents and convert their content into digital text.

The system is designed to handle handwritten text where traditional OCR approaches may struggle with handwriting quality.

### Expectation Extraction & Classification

The extracted text is automatically analyzed to identify individual expectations.

Each expectation is classified into one of the following categories:

- **Learning**
- **Networking**
- **Career**
- **Technical Skills**
- **Events & Conferences**
- **Other**

### Positive / Negative Classification

Each expectation is also classified according to its sentiment:

- **Positive** — what the student wants, expects, or would like to achieve.
- **Negative** — what the student explicitly does not want, dislikes, or wants to avoid.

### End-to-End Pipeline

The complete processing pipeline is:

```text
Handwritten Image
       │
       ▼
┌─────────────────┐
│  Gemini Vision  │
└────────┬────────┘
         │
         ▼
   Transcription
         │
         ▼
┌─────────────────┐
│   Classifier    │
└────────┬────────┘
         │
         ▼
Structured JSON