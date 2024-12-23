from facer import facer
import numpy as np
import matplotlib.pyplot as plt

path_to_images = "./face-images"
images = facer.load_images(path_to_images)

# Detect landmarks for each face
landmarks, faces = facer.detect_face_landmarks(images)

# Use the detected landmarks to create an average face
average_face = facer.create_average_face(faces, landmarks, save_image=True)
print(type(average_face))
average_face = average_face[0]


if isinstance(average_face, np.ndarray):
    plt.imshow(average_face)
    plt.show()
else:
    print("The average face is not in a valid image format.")