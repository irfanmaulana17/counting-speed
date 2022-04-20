import cv2 as cv


def rescale_frame(frame, scale):    # works for image, video, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('')  # integer to capture from webcam, path to capture video file
capture.set(3, 1440)

while True:
    isTrue, frame = capture.read()
    frame_resized = rescale_frame(frame, scale=.2)
    cv.imshow("video with set", frame)
    cv.imshow("Video Resized", frame_resized)
    if cv.waitKey(20) & 0xFF == ord("q"):       # press "q" key to exit loop
        break


capture.release()   # stop capturing the image/video
cv.destroyAllWindows()      # close windows