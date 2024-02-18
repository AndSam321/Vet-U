import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Could not open camera")
    exit()

# Read the first frame
ret, frame = cap.read()

# Display the frame
cv2.imshow('frame', frame)

# Press any key to exit
cv2.waitKey(0)

# Release the camera
cap.release()

# Close all windows
cv2.destroyAllWindows()