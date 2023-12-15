# Book Reader Project

## Overview

The purpose of the **book_reader** project is to assist a friend in recreating his late wife's voice to read children's books to their young child. The project is currently in its early stages, focusing on Optical Character Recognition (OCR) and subsequent vocal cloning. Please follow the instructions below to set up the project and contribute.

## Setup

This project requires the installation of [pytesseract](https://github.com/UB-Mannheim/tesseract/wiki) for OCR. Detailed instructions for Windows installation can be found [here](https://github.com/UB-Mannheim/tesseract/wiki).

## Project Phases

### 1. Text Extraction/Input

The initial phase involves processing text from photos or images of children's books. The extracted text is stored in directories and text files. Manual entry is supported in case of formatting conflicts during the OCR process.

- **Status:** Initial commit complete

### 2. Vocal Cloning

The second phase focuses on developing a vocal cloning system (or using a pre-built package), allowing for the recreation of any voice from training samples.

- **Status:** In Progress

### 3. Reading Aloud

The third phase aims to implement the functionality to read back books from the directory using the cloned voice.

- **Status:** Not Started

### 4. User-Generated Content

As a future enhancement, users will be able to create their own stories. Text input can be submitted to Text-to-Image models, resulting in personalized illustrated children's books.

- **Status:** Future

## Important Notes

- **OCR Testing:** The OCR process was tested on copyrighted material (e.g., "Where the Wild Things Are" by Maurice Sendak), which is excluded from the repository. Example images or text containing copyrighted material may be included pending further investigation. These are intended for illustrative purposes only and not for distribution.

- **Testing Materials:** Example images used for testing can be found [here](https://docs.google.com/viewer?a=v&pid=sites&srcid=YXBwcy53ZWxsZXNsZXkuazEyLm1hLnVzfGpoZW5nbGlzaHxneDo3OTk2MGM3YWJlM2Y2OWU2).

- **Vocal Cloning Warning:** Any vocal cloning should be approached with caution, responsibility, and adherence to applicable laws. Cloning and using people's voices without their consent is strictly prohibited.

## Contributing

Feel free to contribute to the development of this project. Follow the standard GitHub workflow by forking the repository, creating a branch for your changes, and submitting a pull request for review.

Thank you for your interest and support in the **book_reader** project!
