import cv2

img  = cv2.imread(r".\Images\SRA.png")

while True:
    cv2.imshow("SRA", img)

    # If We have waited at least 1 ms and we have pressed the Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()