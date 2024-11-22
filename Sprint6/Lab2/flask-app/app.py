import io
from flask import Flask, Response
from cryptography.fernet import Fernet
from PIL import Image, ImageDraw

app = Flask(__name__)

@app.route('/')
def hello():
 secret_text = f"""
The secret code is:
{Fernet.generate_key().decode()}
-"""

 img = Image.new('RGB', (400, 400), color=(73, 109, 137))
 d = ImageDraw.Draw(img)
 d.text((10, 10), secret_text, fill=(255, 255, 0))
 img_byte_array = io.BytesIO()
 img.save(img_byte_array, format="PNG")
 img_byte_array = img_byte_array.getvalue()
 
 return Response(img_byte_array, content_type="image/png")