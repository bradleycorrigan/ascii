import cv2

CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def img_to_ascii(path, width=110):
    # load image in grayscale
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.equalizeHist(img) # Forces the image to use the full range of characters
    if img is None: return "image not found"

    # resize, and maintain aspect ratio
    #'chars are taller than they are wide, so scale height by .5
    h, w = img.shape
    aspect_ratio = h/w
    new_height = int(width*aspect_ratio*0.5)
    img = cv2.resize(img, (width, new_height))

    # map pixels to character
    ascii_str = ""
    for row in img:
        for pixel in row:
            # scale 0-255 down to len of char string
            index = int(pixel / 256 * len(CHARS))
            ascii_str += CHARS[index]
        ascii_str += "\n" 
    return ascii_str
    
    
print(img_to_ascii("image5.png"))