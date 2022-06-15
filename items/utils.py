import io
import base64
import qrcode

def generate_qr_code(data):
  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
  )
  qr.add_data(data)
  qr.make(fit=True)
  img = qr.make_image(fill_color="black", back_color="white")
  buffer = io.BytesIO()
  img_save = img.save(buffer)
  qr_code = 'data:image/png;base64,'+base64.b64encode(buffer.getvalue()).decode('utf-8')
  
  return qr_code