import cv2
import os


img = cv2.imread("nature.jpeg")  
if img is None:
    print("Error: Image not found!")
    exit()

height, width, _ = img.shape  

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")


d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}


max_chars = (height * width * 3) // 8  
if len(msg) > max_chars:
    print("Error: Message is too long for this image.")
    exit()


msg = f"{len(msg):08d}" + msg  


index = 0
for i in range(height):
    for j in range(width):
        for k in range(3):  
            if index < len(msg):
                img[i, j, k] = d[msg[index]]  
                index += 1

cv2.imwrite("encryptedImage.jpg", img)
print("Message encrypted successfully!")

os.system("start encryptedImage.jpg" if os.name == "nt" else "xdg-open encryptedImage.jpg")


message = ""
index = 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    msg_length = ""
    for i in range(8):  
        msg_length += c[img[i // width, i % width, 0]]
    
    msg_length = int(msg_length)  
    print(f"Detected message length: {msg_length}")

    for i in range(height):
        for j in range(width):
            for k in range(3):
                if index < msg_length:
                    message += c[img[i, j, k]]
                    index += 1

    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
