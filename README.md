Description: A comprehensive face recognition system using face_recognition and cv2 libraries. The system is capable of identifying and counting faces in a collection of photos, providing a summary of individual and co-appearances.

README:

# Face-Recognition-Photo-Analyzer

Face-Recognition-Photo-Analyzer is a python-based face recognition system. It uses face_recognition and cv2 libraries to identify and count faces in a collection of photos. The output is an insightful summary of how many times each person appeared and how many times each pair of individuals appeared together in the photos.

## Features

- Loads known faces and their corresponding names from a directory.
- Analyzes photos, recognizing and identifying faces based on the loaded known faces.
- Stores identified faces in a dictionary where photo names are keys and lists of identified names are values.
- Generates a summary of the photo data, including counts of individual appearances and co-appearances.

## Functions

- `load_known_faces`: Loads known faces and their corresponding names from a directory.
- `process_photos`: Analyzes photos in a specified directory, recognizing and identifying faces.
- `summarize_data`: Generates a summary of the photo data, which includes counts of individual appearances and co-appearances in the photos.
- `main`: Coordinates the entire process, from loading known faces, processing photos, to summarizing data.

## Results

The result is a detailed summary of how many photos each person appeared in, and how many photos each pair of individuals appeared in together. This is a handy tool for understanding the frequency of appearances in a photo collection, useful for data analysis in various contexts.

## Dependencies

This project utilizes the face_recognition and cv2 libraries. Ensure they are installed in your environment for successful execution.