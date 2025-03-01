Image Steganography Application
A modern GUI application for hiding secret messages within images using steganography techniques. Built with Python and Tkinter.

Check out project Screenshots here

Features
🖼️ Supports multiple image formats (PNG, JPG, BMP)
📝 Input text directly or from files
🔐 Password protection for secure encoding/decoding
🎨 Modern dark-themed GUI interface
📊 Real-time status updates
⚡ Fast encoding and decoding
💾 Save encoded images in high-quality PNG format
Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/YOGESHWAR-PRABHU/Image-Steganography-Application.git
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Usage
Run the application:

bash
Copy
Edit
python steganography_app.py
To encode a message:

Click "Select Image" to choose your carrier image
Enter your secret message or use "Load from File"
Enter a password for security
Click "Encode Message"
Choose where to save the encoded image
To decode a message:

Select the encoded image
Enter the password used during encoding
Click "Decode Message"
The hidden message will be revealed
Technical Details
The application uses:

LSB (Least Significant Bit) steganography
Password-based message protection
Custom pixel manipulation using OpenCV
Message length preservation in image metadata
Requirements
Python 3.8+
OpenCV (opencv-python)
Pillow
NumPy
Tkinter (included with Python)
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the OpenCV team for their amazing image processing library
Inspired by various steganography techniques and implementations
Security Note
This implementation is for educational purposes. For sensitive data, please use established encryption standards. This project was developed with GPT assistance but customized for personal learning and improvement.

Author
Yogeshwar Prabhu

Support
If you found this project helpful, please give it a ⭐️!
