# SteganoCrypt: Secure Image Steganography Tool

Easily **hide and retrieve secret messages** within images using this **user-friendly steganography tool**. This Python-based application, powered by Tkinter, provides a **secure and efficient** way to conceal text within images while keeping their appearance unchanged.

✨ **View project screenshots** [here](outputs).

## **Key Features**

- 🏞️ **Supports PNG, JPG, and BMP formats** for broad compatibility.  
- ✏️ **Enter text manually** or 📄 **load from a file** for convenience.  
- 🔑 **Secure encoding & decoding** with password protection.  
- 🎨 **Dark-themed modern UI** for an enhanced visual experience.  
- 📟 **Real-time status updates** to track encoding & decoding progress.  
- ⚡ **Optimized performance** for lightning-fast message processing.  
- 🖼️ **Preserves image quality** while embedding secret messages.  

## **Installation**

1. Clone the repository:
```bash
git clone https://github.com/YOGESHWAR-PRABHU/Image-Steganography-Application.git
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## **Usage**

1. Run the application:
```bash
python steganography_app.py
```

2. To encode a message:
   - Click "Select Image" to choose your carrier image
   - Enter your secret message or use "Load from File" to load from a text file
   - Enter a password for security
   - Click "Encode Message"
   - Choose where to save the encoded image

3. To decode a message:
   - Select the encoded image
   - Enter the password used during encoding
   - Click "Decode Message"
   - The hidden message will appear in the output section

## **Technical Details**

The application uses the following techniques:
- LSB (Least Significant Bit) steganography
- Password-based message protection
- Custom pixel manipulation using OpenCV
- Message length preservation in image metadata

## **Requirements**

- Python 3.8+
- OpenCV (opencv-python)
- Pillow
- NumPy
- Tkinter (included with Python)

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## **Acknowledgments**

- Thanks to the OpenCV team for their amazing image processing library
- Inspired by various steganography techniques and implementations

## **Security Note**

This implementation is for educational purposes. For sensitive data, please use established encryption standards.

## **Author**

[Yogeshwar Prabhu](https://github.com/YOGESHWAR-PRABHU)

## **Support**

If you found this project helpful, please give it a ⭐️!
