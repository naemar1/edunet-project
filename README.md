Secure Data Hiding in Image Using Steganography


Project Description
This project implements image steganography, a technique used to securely hide secret data within digital images. It utilizes Least Significant Bit (LSB) substitution, along with optional encryption, to ensure data confidentiality and undetectability. The system is designed to protect sensitive information from unauthorized access while maintaining image quality.


Features
Secure data embedding into images using LSB steganography.
Encryption support for enhanced security.
Image integrity maintained, ensuring minimal visual distortion.
User-friendly interface for encoding and decoding messages.
Python-based implementation using OpenCV and PIL for image processing.


Technologies Used
Programming Language: Python
Libraries: OpenCV, NumPy, Cryptography
Steganography Techniques: Least Significant Bit (LSB), Discrete Cosine Transform (DCT), Discrete Wavelet Transform (DWT)


Usage
Encoding (Hiding Data in Image)

Select an image and enter the secret message.
The program embeds the message within the image using steganography.
The output is a stego-image containing hidden data.
Decoding (Extracting Hidden Data)

Load the stego-image into the program.
The hidden message is extracted and displayed.


Security Considerations
Encrypt sensitive data before embedding it in an image.
Use high-resolution images to minimize distortions.
Avoid using the same image for multiple secret messages to prevent detection.


Contributors
Naema Mohamed Rafiq (GitHub Profile)
