# here is a code snippet that uses the `numpy` library to perform a simple matrix multiplication
import cv2 
import numpy as np
  
def applyGrayscale(image): 
    """Convert the image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def applySepia(image):
    """Apply a sepia filter to the image."""
    sepiaFilter = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    sepiaImage = cv2.transform(image, sepiaFilter)
    sepiaImage = np.clip(sepiaImage, 0, 255).astype('uint8')
    return sepiaImage

def applyBlur(image):
    """Apply a Gaussian blur to the image."""
    return cv2.GaussianBlur(image, (15, 15), 0)

def applyEdgeDetection(image):
    """Apply Canny edge detection."""
    return cv2.Canny(image, 100, 200)

def displayFilters(image):
    """Interactive menu to select and apply filters."""
    while True:
        print("\nChoose a filter:")
        print("1. Grayscale")
        print("2. Sepia")
        print("3. Blur")
        print("4. Edge Detection")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            result = applyGrayscale(image)
            cv2.imshow("Grayscale", result)
        elif choice == '2':
            result = applySepia(image)
            cv2.imshow("Sepia", result)
        elif choice == '3':
            result = applyBlur(image)
            cv2.imshow("Blur", result)
        elif choice == '4':
            result = applyEdgeDetection(image)
            cv2.imshow("Edge Detection", result)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
            continue

        # Save the result and display it
        saveChoice = input("Save this image? (y/n): ").lower()
        if saveChoice == 'y':
            fileName = input("Enter file name to save (with extension, e.g., output.jpg): ")
            if choice == '1':
                cv2.imwrite(fileName, result)  # Grayscale needs special handling
            else:
                cv2.imwrite(fileName, cv2.cvtColor(result, cv2.COLOR_GRAY2BGR))
            print(f"Image saved as {fileName}")

        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Main Program
if __name__ == "__main__":
    # Load an image
    filePath = input("Enter the path to the image file: ")
    image = cv2.imread(filePath)

    if image is None:
        print("Error: Could not load the image. Please check the file path.")
    else:
        cv2.imshow("Original Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        displayFilters(image)

       # we can also use a loop to load multiple images and apply filters if we need

