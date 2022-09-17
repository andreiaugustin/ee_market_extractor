import cv2
import pytesseract

def getTextFromImage(pNPArray):
    gray = cv2.cvtColor(pNPArray, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    copy = pNPArray.copy()
    text = ''
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        rect = cv2.rectangle(copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cropped = copy[y:y + h, x:x + w]
        text += str(pytesseract.image_to_string(cropped))
    return text