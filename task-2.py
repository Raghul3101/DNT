import cv2

input_video = cv2.VideoCapture("input_video.mp4")

width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(input_video.get(cv2.CAP_PROP_FPS))

output_width = width * 2
output_height = height * 2
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

output_video = cv2.VideoWriter("output_video.mp4", fourcc, fps, (output_width, output_height), isColor=True)

while True:
    ret, frame = input_video.read()
    if not ret:
        break

    upscaled_frame = cv2.resize(frame, (output_width, output_height), interpolation=cv2.INTER_CUBIC)

    output_video.write(upscaled_frame)

input_video.release()
output_video.release()

output_video = cv2.VideoCapture("output_video.mp4")
while True:
    ret, frame = output_video.read()
    if not ret:
        break
    cv2.imshow("Output Video", frame)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

output_video.release()
cv2.destroyAllWindows()
