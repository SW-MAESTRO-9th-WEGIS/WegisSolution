import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 30.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret==False:
        break;

    frame = cv2.flip(frame, 0)

    out.write(frame)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break;

cap.release()
out.release()
cv.destroyAllWindows()
