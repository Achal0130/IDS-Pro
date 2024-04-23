import cv2
import os

# Function to create dataset
def create_dataset(output_dir, num_images_per_person=10, num_persons=3):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Initialize webcam
    cap = cv2.VideoCapture(0)

    # Loop through each person
    for person_id in range(1, num_persons + 1):
        person_name = f"Person_{person_id}"
        person_dir = os.path.join(output_dir, person_name)

        # Create a directory for the person if it doesn't exist
        if not os.path.exists(person_dir):
            os.makedirs(person_dir)

        print(f"Capturing images for {person_name}...")

        # Capture images
        images_captured = 0
        while images_captured < num_images_per_person:
            # Read frame from webcam
            ret, frame = cap.read()

            # Save image
            image_path = os.path.join(person_dir, f"{person_name}_{images_captured + 1}.jpg")
            cv2.imwrite(image_path, frame)

            print(f"Image {images_captured + 1}/{num_images_per_person} captured")

            images_captured += 1

            # Wait for 1 second before capturing next image
            cv2.waitKey(2000)

            # Display captured image (optional)
            cv2.imshow("Captured Image", frame)
            cv2.waitKey(1000)  # Adjust the delay as needed (milliseconds)

    # Release the webcam and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Main function
def main():
    output_dir = "dataset"
    num_images_per_person = 5  # Adjust the number of images per person as needed
    num_persons = 2  # Adjust the number of persons as needed
    create_dataset(output_dir, num_images_per_person, num_persons)

if __name__ == "__main__":
    main()
