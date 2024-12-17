import os
import cv2
import face_recognition
from collections import defaultdict

def load_known_faces(known_faces_dir):
    """Load known faces and names from a directory."""
    known_faces = []
    known_names = []

    for name in os.listdir(known_faces_dir):
        person_dir = os.path.join(known_faces_dir, name)
        if os.path.isdir(person_dir):
            for image_name in os.listdir(person_dir):
                image_path = os.path.join(person_dir, image_name)
                image = face_recognition.load_image_file(image_path)
                encodings = face_recognition.face_encodings(image)
                if encodings:
                    known_faces.append(encodings[0])
                    known_names.append(name)

    return known_faces, known_names

def process_photos(photos_dir, known_faces, known_names):
    """Analyze photos to count faces and identify individuals."""
    photo_data = defaultdict(list)

    for photo_name in os.listdir(photos_dir):
        photo_path = os.path.join(photos_dir, photo_name)
        if os.path.isfile(photo_path):
            image = face_recognition.load_image_file(photo_path)
            face_locations = face_recognition.face_locations(image)
            face_encodings = face_recognition.face_encodings(image, face_locations)

            identified_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_faces, face_encoding)
                face_distances = face_recognition.face_distance(known_faces, face_encoding)
                best_match_index = face_distances.argmin() if matches else None

                if best_match_index is not None and matches[best_match_index]:
                    identified_names.append(known_names[best_match_index])
                else:
                    identified_names.append("Unknown")

            photo_data[photo_name] = identified_names

    return photo_data

def summarize_data(photo_data):
    """Summarize photo data with counts of individuals and co-appearances."""
    individual_counts = defaultdict(int)
    co_appearances = defaultdict(int)

    for photo, names in photo_data.items():
        unique_names = set(names)
        for name in unique_names:
            individual_counts[name] += 1
        if len(unique_names) > 1:
            co_appearances[tuple(sorted(unique_names))] += 1

    return individual_counts, co_appearances

def main():
    known_faces_dir = "known_faces"  # Directory with subdirectories named after people containing their photos
    photos_dir = "photos"  # Directory with photos to analyze

    print("Loading known faces...")
    known_faces, known_names = load_known_faces(known_faces_dir)

    print("Processing photos...")
    photo_data = process_photos(photos_dir, known_faces, known_names)

    print("Summarizing data...")
    individual_counts, co_appearances = summarize_data(photo_data)

    print("\nSummary of Photos:")
    for name, count in individual_counts.items():
        print(f"{name}: {count} photos")

    print("\nCo-Appearances:")
    for pair, count in co_appearances.items():
        print(f"{' & '.join(pair)}: {count} photos")

if __name__ == "__main__":
    main()
